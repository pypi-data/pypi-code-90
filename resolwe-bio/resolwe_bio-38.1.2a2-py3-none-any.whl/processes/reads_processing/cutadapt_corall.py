"""Pre-process reads obtained using CORALL Total RNA-Seq Library Prep Kit."""
import os

from plumbum import TEE

from resolwe.process import (
    Cmd,
    DataField,
    FileField,
    FileHtmlField,
    GroupField,
    IntegerField,
    ListField,
    Process,
    SchedulingClass,
)


class CutadaptCorallSingle(Process):
    """Pre-process reads obtained using CORALL Total RNA-Seq Library Prep Kit.

    Trim UMI-tags from input reads and use Cutadapt to remove adapters and run QC filtering steps.
    """

    slug = "cutadapt-corall-single"
    name = "Cutadapt (Corall RNA-Seq, single-end)"
    process_type = "data:reads:fastq:single:cutadapt:"
    version = "1.2.1"
    category = "Other"
    scheduling_class = SchedulingClass.BATCH
    entity = {"type": "sample"}
    requirements = {
        "expression-engine": "jinja",
        "executor": {
            "docker": {"image": "public.ecr.aws/s4q6j6e8/resolwebio/rnaseq:5.9.0"},
        },
        "resources": {
            "cores": 10,
            "memory": 16384,
        },
    }
    data_name = '{{ reads|sample_name|default("?") }}'

    class Input:
        """Input fields."""

        reads = DataField("reads:fastq:single", label="Select sample(s)")

        class Options:
            """Options."""

            nextseq_trim = IntegerField(
                label="NextSeq/NovaSeq trim",
                description="NextSeq/NovaSeq-specific quality trimming. Trims also dark "
                "cycles appearing as high-quality G bases. This option is mutually "
                "exclusive with the use of standard quality-cutoff trimming and is "
                "suitable for the use with data generated by the recent Illumina "
                "machines that utilize two-color chemistry to encode the four bases.",
                default=10,
            )

            quality_cutoff = IntegerField(
                label="Quality cutoff",
                description="Trim low-quality bases from 3' end of each read before adapter "
                "removal. The use of this option will override the use of "
                "NextSeq/NovaSeq trim option.",
                required=False,
            )

            min_len = IntegerField(
                label="Minimum read length",
                default=20,
            )

            min_overlap = IntegerField(
                label="Mimimum overlap",
                description="Minimum overlap between adapter and read for an adapter to be found.",
                default=20,
            )

        options = GroupField(Options, label="Options")

    class Output:
        """Output fields."""

        fastq = ListField(FileField(), label="Reads file")
        report = FileField(label="Cutadapt report")
        fastqc_url = ListField(FileHtmlField(), label="Quality control with FastQC")
        fastqc_archive = ListField(FileField(), label="Download FastQC archive")

    def run(self, inputs, outputs):
        """Run analysis."""
        # Get input reads file name (for the first of the possible multiple lanes)
        reads_path = os.path.basename(inputs.reads.output.fastq[0].path)
        assert reads_path.endswith(".fastq.gz")
        name = reads_path[:-9]
        # Concatenate multi-lane read files
        (
            Cmd["cat"][[reads.path for reads in inputs.reads.output.fastq]]
            > "input_reads.fastq.gz"
        )()

        # Extract UMI sequences
        Cmd["extract_umi.sh"]([10, 13, "input_reads.fastq.gz"])

        # Prepare Cutadapt inputs
        if inputs.options.quality_cutoff is not None:
            read_trim_cutoff = "--quality-cutoff={}".format(
                inputs.options.quality_cutoff
            )
        else:
            read_trim_cutoff = "--nextseq-trim={}".format(inputs.options.nextseq_trim)

        rd1Adapter = "AGATCGGAAGAGCACACGTCTGAACTCCAGTCAC"

        first_pass_input = [
            "-m",
            inputs.options.min_len,
            "-O",
            inputs.options.min_overlap,
            "-a",
            "QUALITY=G{20}",
            "-j",
            self.requirements.resources.cores,
            "input_reads_umi.fastq.gz",
        ]

        second_pass_input = [
            "-m",
            inputs.options.min_len,
            read_trim_cutoff,
            "-a",
            rd1Adapter,
            "-j",
            self.requirements.resources.cores,
            "-",
        ]

        third_pass_input = [
            "-m",
            inputs.options.min_len,
            "-O",
            3,
            "-a",
            "r1polyA=A{18}",
            "-j",
            self.requirements.resources.cores,
            "-",
        ]

        fourth_pass_input = [
            "-m",
            inputs.options.min_len,
            "-O",
            inputs.options.min_overlap,
            "-g",
            rd1Adapter,
            "--discard-trimmed",
            "-j",
            self.requirements.resources.cores,
            "-o",
            "{}_trimmed.fastq.gz".format(name),
            "-",
        ]

        # Run Cutadapt, write analysis reports into a report file
        (
            Cmd["cutadapt"][first_pass_input]
            | Cmd["cutadapt"][second_pass_input]
            | Cmd["cutadapt"][third_pass_input]
            | Cmd["cutadapt"][fourth_pass_input]
            > "cutadapt_report.txt"
        )()

        # Prepare final FASTQC report
        fastqc_args = [
            "{}_trimmed.fastq.gz".format(name),
            "fastqc",
            "fastqc_archive",
            "fastqc_url",
            "--nogroup",
        ]
        return_code, _, _ = Cmd["fastqc.sh"][fastqc_args] & TEE(retcode=None)
        if return_code:
            self.error("Error while preparing FASTQC report.")

        # Save the outputs
        outputs.fastq = ["{}_trimmed.fastq.gz".format(name)]
        outputs.report = "cutadapt_report.txt"


class CutadaptCorallPaired(Process):
    """Pre-process reads obtained using CORALL Total RNA-Seq Library Prep Kit.

    Trim UMI-tags from input reads and use Cutadapt to remove adapters and run QC filtering steps.
    """

    slug = "cutadapt-corall-paired"
    name = "Cutadapt (Corall RNA-Seq, paired-end)"
    process_type = "data:reads:fastq:paired:cutadapt:"
    version = "1.1.2"
    category = "Other"
    scheduling_class = SchedulingClass.BATCH
    entity = {"type": "sample"}
    requirements = {
        "expression-engine": "jinja",
        "executor": {
            "docker": {"image": "public.ecr.aws/s4q6j6e8/resolwebio/rnaseq:5.9.0"},
        },
        "resources": {
            "cores": 10,
            "memory": 16384,
        },
    }
    data_name = '{{ reads|sample_name|default("?") }}'

    class Input:
        """Input fields."""

        reads = DataField("reads:fastq:paired", label="Select sample(s)")

        class Options:
            """Options."""

            nextseq_trim = IntegerField(
                label="NextSeq/NovaSeq trim",
                description="NextSeq/NovaSeq-specific quality trimming. Trims also dark "
                "cycles appearing as high-quality G bases. This option is mutually "
                "exclusive with the use of standard quality-cutoff trimming and is "
                "suitable for the use with data generated by the recent Illumina "
                "machines that utilize two-color chemistry to encode the four bases.",
                default=10,
            )

            quality_cutoff = IntegerField(
                label="Quality cutoff",
                description="Trim low-quality bases from 3' end of each read before adapter "
                "removal. The use of this option will override the use of "
                "NextSeq/NovaSeq trim option.",
                required=False,
            )

            min_len = IntegerField(
                label="Minimum read length",
                default=20,
            )

            min_overlap = IntegerField(
                label="Mimimum overlap",
                description="Minimum overlap between adapter and read for an adapter to be found.",
                default=20,
            )

        options = GroupField(Options, label="Options")

    class Output:
        """Output fields."""

        fastq = ListField(FileField(), label="Remaining mate1 reads")
        fastq2 = ListField(FileField(), label="Remaining mate2 reads")
        report = FileField(label="Cutadapt report")
        fastqc_url = ListField(
            FileHtmlField(), label="Mate1 quality control with FastQC"
        )
        fastqc_url2 = ListField(
            FileHtmlField(), label="Mate2 quality control with FastQC"
        )
        fastqc_archive = ListField(FileField(), label="Download mate1 FastQC archive")
        fastqc_archive2 = ListField(FileField(), label="Download mate2 FastQC archive")

    def run(self, inputs, outputs):
        """Run analysis."""
        # Get input reads file name (for the first of the possible multiple lanes)
        mate1_path = os.path.basename(inputs.reads.output.fastq[0].path)
        assert mate1_path.endswith(".fastq.gz")
        name_mate1 = mate1_path[:-9]
        mate2_path = os.path.basename(inputs.reads.output.fastq2[0].path)
        assert mate2_path.endswith(".fastq.gz")
        name_mate2 = mate2_path[:-9]

        # Concatenate multi-lane read files
        (
            Cmd["cat"][[reads.path for reads in inputs.reads.output.fastq]]
            > "input_reads_mate1.fastq.gz"
        )()
        (
            Cmd["cat"][[reads.path for reads in inputs.reads.output.fastq2]]
            > "input_reads_mate2.fastq.gz"
        )()

        # Extract UMI sequences
        Cmd["extract_umi.sh"](
            [10, 13, "input_reads_mate1.fastq.gz", "input_reads_mate2.fastq.gz"]
        )

        # Prepare Cutadapt inputs
        if inputs.options.quality_cutoff is not None:
            read_trim_cutoff = "--quality-cutoff={}".format(
                inputs.options.quality_cutoff
            )
        else:
            read_trim_cutoff = "--nextseq-trim={}".format(inputs.options.nextseq_trim)

        rd1Adapter = "AGATCGGAAGAGCACACGTCTGAACTCCAGTCAC"
        rd2Adapter = "AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT"

        first_pass_input = [
            "-m",
            inputs.options.min_len,
            "-O",
            inputs.options.min_overlap,
            "--interleaved",
            "-n",
            2,
            "-a",
            "QUALITY=G{20}",
            "-A",
            "QUALITY=G{20}",
            "-j",
            self.requirements.resources.cores,
            "input_reads_mate1_umi.fastq.gz",
            "input_reads_mate2_umi.fastq.gz",
        ]

        second_pass_input = [
            "-m",
            inputs.options.min_len,
            "--interleaved",
            "-n",
            3,
            read_trim_cutoff,
            "-a",
            rd1Adapter,
            "-A",
            rd2Adapter,
            "-G",
            "XT{18}",
            "-j",
            self.requirements.resources.cores,
            "-",
        ]

        third_pass_input = [
            "-m",
            inputs.options.min_len,
            "-O",
            3,
            "--interleaved",
            "-n",
            1,
            "-a",
            "r1polyA=A{18}",
            "-j",
            self.requirements.resources.cores,
            "-",
        ]

        fourth_pass_input = [
            "-m",
            inputs.options.min_len,
            "-O",
            inputs.options.min_overlap,
            "--interleaved",
            "-g",
            rd1Adapter,
            "-G",
            rd2Adapter,
            "--discard-trimmed",
            "-j",
            self.requirements.resources.cores,
            "-o",
            "{}_trimmed.fastq.gz".format(name_mate1),
            "-p",
            "{}_trimmed.fastq.gz".format(name_mate2),
            "-",
        ]

        # Run Cutadapt, write analysis reports into a report file
        (
            Cmd["cutadapt"][first_pass_input]
            | Cmd["cutadapt"][second_pass_input]
            | Cmd["cutadapt"][third_pass_input]
            | Cmd["cutadapt"][fourth_pass_input]
            > "cutadapt_report.txt"
        )()

        # Prepare final FASTQC report
        fastqc_args = [
            "{}_trimmed.fastq.gz".format(name_mate1),
            "fastqc",
            "fastqc_archive",
            "fastqc_url",
        ]
        return_code, _, _ = Cmd["fastqc.sh"][fastqc_args] & TEE(retcode=None)
        if return_code:
            self.error("Error while preparing FASTQC report.")

        fastqc_args = [
            "{}_trimmed.fastq.gz".format(name_mate2),
            "fastqc",
            "fastqc_archive2",
            "fastqc_url2",
        ]
        return_code, _, _ = Cmd["fastqc.sh"][fastqc_args] & TEE(retcode=None)
        if return_code:
            self.error("Error while preparing FASTQC report.")

        # Save the outputs
        outputs.fastq = ["{}_trimmed.fastq.gz".format(name_mate1)]
        outputs.fastq2 = ["{}_trimmed.fastq.gz".format(name_mate2)]
        outputs.report = "cutadapt_report.txt"
