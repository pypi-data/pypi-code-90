from typing import Union, List, Optional

from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    ArrayType,
    BooleanType,
    DataType,
)


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class ConditionSchema:
    """
    A clinical condition, problem, diagnosis, or other event, situation, issue, or
    clinical concept that has risen to a level of concern.
    """

    # noinspection PyDefaultArgument
    @staticmethod
    def get_schema(
        max_nesting_depth: Optional[int] = 6,
        nesting_depth: int = 0,
        nesting_list: List[str] = [],
        max_recursion_limit: Optional[int] = 2,
        include_extension: Optional[bool] = False,
        extension_fields: Optional[List[str]] = [
            "valueBoolean",
            "valueCode",
            "valueDate",
            "valueDateTime",
            "valueDecimal",
            "valueId",
            "valueInteger",
            "valuePositiveInt",
            "valueString",
            "valueTime",
            "valueUnsignedInt",
            "valueUri",
            "valueUrl",
        ],
        extension_depth: int = 0,
        max_extension_depth: Optional[int] = 2,
    ) -> Union[StructType, DataType]:
        """
        A clinical condition, problem, diagnosis, or other event, situation, issue, or
        clinical concept that has risen to a level of concern.


        id: The logical id of the resource, as used in the URL for the resource. Once
            assigned, this value never changes.

        extension: May be used to represent additional information that is not part of the basic
            definition of the resource. In order to make the use of extensions safe and
            manageable, there is a strict set of governance  applied to the definition and
            use of extensions. Though any implementer is allowed to define an extension,
            there is a set of requirements that SHALL be met as part of the definition of
            the extension.

        meta: The metadata about the resource. This is content that is maintained by the
            infrastructure. Changes to the content may not always be associated with
            version changes to the resource.

        implicitRules: A reference to a set of rules that were followed when the resource was
            constructed, and which must be understood when processing the content.

        language: The base language in which the resource is written.

        text: A human-readable narrative that contains a summary of the resource, and may be
            used to represent the content of the resource to a human. The narrative need
            not encode all the structured data, but is required to contain sufficient
            detail to make it "clinically safe" for a human to just read the narrative.
            Resource definitions may define what content should be represented in the
            narrative to ensure clinical safety.

        contained: These resources do not have an independent existence apart from the resource
            that contains them - they cannot be identified independently, and nor can they
            have their own independent transaction scope.

        resourceType: This is a Condition resource

        identifier: This records identifiers associated with this condition that are defined by
            business processes and/or used to refer to it when a direct URL reference to
            the resource itself is not appropriate (e.g. in CDA documents, or in written /
            printed documentation).

        clinicalStatus: The clinical status of the condition.

        verificationStatus: The verification status to support the clinical status of the condition.

        category: A category assigned to the condition.

        severity: A subjective assessment of the severity of the condition as evaluated by the
            clinician.

        code: Identification of the condition, problem or diagnosis.

        bodySite: The anatomical location where this condition manifests itself.

        subject: Indicates the patient or group who the condition record is associated with.

        context: Encounter during which the condition was first asserted.

        onsetDateTime: Estimated or actual date or date-time  the condition began, in the opinion of
            the clinician.

        onsetAge: Estimated or actual date or date-time  the condition began, in the opinion of
            the clinician.

        onsetPeriod: Estimated or actual date or date-time  the condition began, in the opinion of
            the clinician.

        onsetRange: Estimated or actual date or date-time  the condition began, in the opinion of
            the clinician.

        onsetString: Estimated or actual date or date-time  the condition began, in the opinion of
            the clinician.

        abatementDateTime: The date or estimated date that the condition resolved or went into remission.
            This is called "abatement" because of the many overloaded connotations
            associated with "remission" or "resolution" - Conditions are never really
            resolved, but they can abate.

        abatementAge: The date or estimated date that the condition resolved or went into remission.
            This is called "abatement" because of the many overloaded connotations
            associated with "remission" or "resolution" - Conditions are never really
            resolved, but they can abate.

        abatementBoolean: The date or estimated date that the condition resolved or went into remission.
            This is called "abatement" because of the many overloaded connotations
            associated with "remission" or "resolution" - Conditions are never really
            resolved, but they can abate.

        abatementPeriod: The date or estimated date that the condition resolved or went into remission.
            This is called "abatement" because of the many overloaded connotations
            associated with "remission" or "resolution" - Conditions are never really
            resolved, but they can abate.

        abatementRange: The date or estimated date that the condition resolved or went into remission.
            This is called "abatement" because of the many overloaded connotations
            associated with "remission" or "resolution" - Conditions are never really
            resolved, but they can abate.

        abatementString: The date or estimated date that the condition resolved or went into remission.
            This is called "abatement" because of the many overloaded connotations
            associated with "remission" or "resolution" - Conditions are never really
            resolved, but they can abate.

        assertedDate: The date on which the existance of the Condition was first asserted or
            acknowledged.

        asserter: Individual who is making the condition statement.

        stage: Clinical stage or grade of a condition. May include formal severity
            assessments.

        evidence: Supporting Evidence / manifestations that are the basis on which this
            condition is suspected or confirmed.

        note: Additional information about the Condition. This is a general notes/comments
            entry  for description of the Condition, its diagnosis and prognosis.

        """
        from spark_fhir_schemas.stu3.complex_types.extension import ExtensionSchema
        from spark_fhir_schemas.stu3.complex_types.meta import MetaSchema
        from spark_fhir_schemas.stu3.complex_types.narrative import NarrativeSchema
        from spark_fhir_schemas.stu3.simple_types.resourcelist import ResourceListSchema
        from spark_fhir_schemas.stu3.complex_types.identifier import IdentifierSchema
        from spark_fhir_schemas.stu3.complex_types.codeableconcept import (
            CodeableConceptSchema,
        )
        from spark_fhir_schemas.stu3.complex_types.reference import ReferenceSchema
        from spark_fhir_schemas.stu3.complex_types.age import AgeSchema
        from spark_fhir_schemas.stu3.complex_types.period import PeriodSchema
        from spark_fhir_schemas.stu3.complex_types.range import RangeSchema
        from spark_fhir_schemas.stu3.complex_types.condition_stage import (
            Condition_StageSchema,
        )
        from spark_fhir_schemas.stu3.complex_types.condition_evidence import (
            Condition_EvidenceSchema,
        )
        from spark_fhir_schemas.stu3.complex_types.annotation import AnnotationSchema

        if (
            max_recursion_limit
            and nesting_list.count("Condition") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Condition"]
        schema = StructType(
            [
                # The logical id of the resource, as used in the URL for the resource. Once
                # assigned, this value never changes.
                StructField("id", StringType(), True),
                # May be used to represent additional information that is not part of the basic
                # definition of the resource. In order to make the use of extensions safe and
                # manageable, there is a strict set of governance  applied to the definition and
                # use of extensions. Though any implementer is allowed to define an extension,
                # there is a set of requirements that SHALL be met as part of the definition of
                # the extension.
                StructField(
                    "extension",
                    ArrayType(
                        ExtensionSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                            extension_fields=extension_fields,
                            extension_depth=extension_depth,
                            max_extension_depth=max_extension_depth,
                        )
                    ),
                    True,
                ),
                # The metadata about the resource. This is content that is maintained by the
                # infrastructure. Changes to the content may not always be associated with
                # version changes to the resource.
                StructField(
                    "meta",
                    MetaSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                    ),
                    True,
                ),
                # A reference to a set of rules that were followed when the resource was
                # constructed, and which must be understood when processing the content.
                StructField("implicitRules", StringType(), True),
                # The base language in which the resource is written.
                StructField("language", StringType(), True),
                # A human-readable narrative that contains a summary of the resource, and may be
                # used to represent the content of the resource to a human. The narrative need
                # not encode all the structured data, but is required to contain sufficient
                # detail to make it "clinically safe" for a human to just read the narrative.
                # Resource definitions may define what content should be represented in the
                # narrative to ensure clinical safety.
                StructField(
                    "text",
                    NarrativeSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                    ),
                    True,
                ),
                # These resources do not have an independent existence apart from the resource
                # that contains them - they cannot be identified independently, and nor can they
                # have their own independent transaction scope.
                StructField(
                    "contained",
                    ArrayType(
                        ResourceListSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                            extension_fields=extension_fields,
                            extension_depth=extension_depth,
                            max_extension_depth=max_extension_depth,
                        )
                    ),
                    True,
                ),
                # This is a Condition resource
                StructField("resourceType", StringType(), True),
                # This records identifiers associated with this condition that are defined by
                # business processes and/or used to refer to it when a direct URL reference to
                # the resource itself is not appropriate (e.g. in CDA documents, or in written /
                # printed documentation).
                StructField(
                    "identifier",
                    ArrayType(
                        IdentifierSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                            extension_fields=extension_fields,
                            extension_depth=extension_depth,
                            max_extension_depth=max_extension_depth,
                        )
                    ),
                    True,
                ),
                # The clinical status of the condition.
                StructField("clinicalStatus", StringType(), True),
                # The verification status to support the clinical status of the condition.
                StructField("verificationStatus", StringType(), True),
                # A category assigned to the condition.
                StructField(
                    "category",
                    ArrayType(
                        CodeableConceptSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                            extension_fields=extension_fields,
                            extension_depth=extension_depth,
                            max_extension_depth=max_extension_depth,
                        )
                    ),
                    True,
                ),
                # A subjective assessment of the severity of the condition as evaluated by the
                # clinician.
                StructField(
                    "severity",
                    CodeableConceptSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                    ),
                    True,
                ),
                # Identification of the condition, problem or diagnosis.
                StructField(
                    "code",
                    CodeableConceptSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                    ),
                    True,
                ),
                # The anatomical location where this condition manifests itself.
                StructField(
                    "bodySite",
                    ArrayType(
                        CodeableConceptSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                            extension_fields=extension_fields,
                            extension_depth=extension_depth,
                            max_extension_depth=max_extension_depth,
                        )
                    ),
                    True,
                ),
                # Indicates the patient or group who the condition record is associated with.
                StructField(
                    "subject",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                    ),
                    True,
                ),
                # Encounter during which the condition was first asserted.
                StructField(
                    "context",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                    ),
                    True,
                ),
                # Estimated or actual date or date-time  the condition began, in the opinion of
                # the clinician.
                StructField("onsetDateTime", StringType(), True),
                # Estimated or actual date or date-time  the condition began, in the opinion of
                # the clinician.
                StructField(
                    "onsetAge",
                    AgeSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                    ),
                    True,
                ),
                # Estimated or actual date or date-time  the condition began, in the opinion of
                # the clinician.
                StructField(
                    "onsetPeriod",
                    PeriodSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                    ),
                    True,
                ),
                # Estimated or actual date or date-time  the condition began, in the opinion of
                # the clinician.
                StructField(
                    "onsetRange",
                    RangeSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                    ),
                    True,
                ),
                # Estimated or actual date or date-time  the condition began, in the opinion of
                # the clinician.
                StructField("onsetString", StringType(), True),
                # The date or estimated date that the condition resolved or went into remission.
                # This is called "abatement" because of the many overloaded connotations
                # associated with "remission" or "resolution" - Conditions are never really
                # resolved, but they can abate.
                StructField("abatementDateTime", StringType(), True),
                # The date or estimated date that the condition resolved or went into remission.
                # This is called "abatement" because of the many overloaded connotations
                # associated with "remission" or "resolution" - Conditions are never really
                # resolved, but they can abate.
                StructField(
                    "abatementAge",
                    AgeSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                    ),
                    True,
                ),
                # The date or estimated date that the condition resolved or went into remission.
                # This is called "abatement" because of the many overloaded connotations
                # associated with "remission" or "resolution" - Conditions are never really
                # resolved, but they can abate.
                StructField("abatementBoolean", BooleanType(), True),
                # The date or estimated date that the condition resolved or went into remission.
                # This is called "abatement" because of the many overloaded connotations
                # associated with "remission" or "resolution" - Conditions are never really
                # resolved, but they can abate.
                StructField(
                    "abatementPeriod",
                    PeriodSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                    ),
                    True,
                ),
                # The date or estimated date that the condition resolved or went into remission.
                # This is called "abatement" because of the many overloaded connotations
                # associated with "remission" or "resolution" - Conditions are never really
                # resolved, but they can abate.
                StructField(
                    "abatementRange",
                    RangeSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                    ),
                    True,
                ),
                # The date or estimated date that the condition resolved or went into remission.
                # This is called "abatement" because of the many overloaded connotations
                # associated with "remission" or "resolution" - Conditions are never really
                # resolved, but they can abate.
                StructField("abatementString", StringType(), True),
                # The date on which the existance of the Condition was first asserted or
                # acknowledged.
                StructField("assertedDate", StringType(), True),
                # Individual who is making the condition statement.
                StructField(
                    "asserter",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                    ),
                    True,
                ),
                # Clinical stage or grade of a condition. May include formal severity
                # assessments.
                StructField(
                    "stage",
                    Condition_StageSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                    ),
                    True,
                ),
                # Supporting Evidence / manifestations that are the basis on which this
                # condition is suspected or confirmed.
                StructField(
                    "evidence",
                    ArrayType(
                        Condition_EvidenceSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                            extension_fields=extension_fields,
                            extension_depth=extension_depth,
                            max_extension_depth=max_extension_depth,
                        )
                    ),
                    True,
                ),
                # Additional information about the Condition. This is a general notes/comments
                # entry  for description of the Condition, its diagnosis and prognosis.
                StructField(
                    "note",
                    ArrayType(
                        AnnotationSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                            extension_fields=extension_fields,
                            extension_depth=extension_depth,
                            max_extension_depth=max_extension_depth,
                        )
                    ),
                    True,
                ),
            ]
        )
        if not include_extension:
            schema.fields = [
                c
                if c.name != "extension"
                else StructField("extension", StringType(), True)
                for c in schema.fields
            ]

        return schema
