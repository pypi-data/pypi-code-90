from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class MedicationAdministrationPerformerFunctionCodesCode(GenericTypeCode):
    """
    MedicationAdministration Performer Function Codes
    From: http://terminology.hl7.org/CodeSystem/med-admin-perform-function in valuesets.xml
        MedicationAdministration Performer Function Codes
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/med-admin-perform-function
    """
    codeset: FhirUri = (
        "http://terminology.hl7.org/CodeSystem/med-admin-perform-function"
    )


class MedicationAdministrationPerformerFunctionCodesCodeValues:
    """
    A person, non-person living subject, organization or device that who actually
    and principally carries out the action
    From: http://terminology.hl7.org/CodeSystem/med-admin-perform-function in valuesets.xml
    """

    Performer = MedicationAdministrationPerformerFunctionCodesCode("performer")
    """
    A person who verifies the correctness and appropriateness of the service
    (plan, order, event, etc.) and hence takes on accountability.
    From: http://terminology.hl7.org/CodeSystem/med-admin-perform-function in valuesets.xml
    """
    Verifier = MedicationAdministrationPerformerFunctionCodesCode("verifier")
    """
    A person witnessing the action happening without doing anything. A witness is
    not necessarily aware, much less approves of anything stated in the service
    event. Example for a witness is students watching an operation or an advanced
    directive witness.
    From: http://terminology.hl7.org/CodeSystem/med-admin-perform-function in valuesets.xml
    """
    Witness = MedicationAdministrationPerformerFunctionCodesCode("witness")
