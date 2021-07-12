from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class DocumentCompletion(GenericTypeCode):
    """
    v3.DocumentCompletion
    From: http://terminology.hl7.org/ValueSet/v3-DocumentCompletion in v3-codesystems.xml
         Identifies the current completion state of a clinical document.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/v3-DocumentCompletion
    """
    codeset: FhirUri = "http://terminology.hl7.org/CodeSystem/v3-DocumentCompletion"


class DocumentCompletionValues:
    """
    A completion status in which a document has been signed manually or
    electronically by one or more individuals who attest to its accuracy.  No
    explicit determination is made that the assigned individual has performed the
    authentication.  While the standard allows multiple instances of
    authentication, it would be typical to have a single instance of
    authentication, usually by the assigned individual.
    From: http://terminology.hl7.org/CodeSystem/v3-DocumentCompletion in v3-codesystems.xml
    """

    Authenticated = DocumentCompletion("AU")
    """
    A completion status in which information has been orally recorded but not yet
    transcribed.
    From: http://terminology.hl7.org/CodeSystem/v3-DocumentCompletion in v3-codesystems.xml
    """
    Dictated = DocumentCompletion("DI")
    """
    A completion status in which document content, other than dictation, has been
    received but has not been translated into the final electronic format.
    Examples include paper documents, whether hand-written or typewritten, and
    intermediate electronic forms, such as voice to text.
    From: http://terminology.hl7.org/CodeSystem/v3-DocumentCompletion in v3-codesystems.xml
    """
    Documented = DocumentCompletion("DO")
    """
    A completion status in which information is known to be missing from a
    transcribed document.
    From: http://terminology.hl7.org/CodeSystem/v3-DocumentCompletion in v3-codesystems.xml
    """
    Incomplete = DocumentCompletion("IN")
    """
    A workflow status where the material has been assigned to personnel to perform
    the task of transcription. The document remains in this state until the
    document is transcribed.
    From: http://terminology.hl7.org/CodeSystem/v3-DocumentCompletion in v3-codesystems.xml
    """
    InProgress = DocumentCompletion("IP")
    """
    A completion status in which a document has been signed manually or
    electronically by the individual who is legally responsible for that document.
    This is the most mature state in the workflow progression.
    From: http://terminology.hl7.org/CodeSystem/v3-DocumentCompletion in v3-codesystems.xml
    """
    LegallyAuthenticated = DocumentCompletion("LA")
    """
    A completion status in which a document was created in error or was placed in
    the wrong chart. The document is no longer available.
    From: http://terminology.hl7.org/CodeSystem/v3-DocumentCompletion in v3-codesystems.xml
    """
    NullifiedDocument = DocumentCompletion("NU")
    """
    A completion status in which a document is transcribed but not authenticated.
    From: http://terminology.hl7.org/CodeSystem/v3-DocumentCompletion in v3-codesystems.xml
    """
    Pre_authenticated = DocumentCompletion("PA")
    """
    A completion status where the document is complete and there is no expectation
    that the document will be signed.
    From: http://terminology.hl7.org/CodeSystem/v3-DocumentCompletion in v3-codesystems.xml
    """
    UnsignedCompletedDocument = DocumentCompletion("UC")
