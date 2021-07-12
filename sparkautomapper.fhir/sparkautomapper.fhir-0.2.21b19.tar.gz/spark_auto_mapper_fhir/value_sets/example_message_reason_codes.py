from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ExampleMessageReasonCodesCode(GenericTypeCode):
    """
    ExampleMessageReasonCodes
    From: http://terminology.hl7.org/CodeSystem/message-reasons-encounter in valuesets.xml
        Example Message Reasons. These are the set of codes that might be used an
    updating an encounter using admin-update.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/message-reasons-encounter
    """
    codeset: FhirUri = "http://terminology.hl7.org/CodeSystem/message-reasons-encounter"


class ExampleMessageReasonCodesCodeValues:
    """
    The patient has been admitted.
    From: http://terminology.hl7.org/CodeSystem/message-reasons-encounter in valuesets.xml
    """

    Admit = ExampleMessageReasonCodesCode("admit")
    """
    The patient has been discharged.
    From: http://terminology.hl7.org/CodeSystem/message-reasons-encounter in valuesets.xml
    """
    Discharge = ExampleMessageReasonCodesCode("discharge")
    """
    The patient has temporarily left the institution.
    From: http://terminology.hl7.org/CodeSystem/message-reasons-encounter in valuesets.xml
    """
    Absent = ExampleMessageReasonCodesCode("absent")
    """
    The patient has returned from a temporary absence.
    From: http://terminology.hl7.org/CodeSystem/message-reasons-encounter in valuesets.xml
    """
    Returned = ExampleMessageReasonCodesCode("return")
    """
    The patient has been moved to a new location.
    From: http://terminology.hl7.org/CodeSystem/message-reasons-encounter in valuesets.xml
    """
    Moved = ExampleMessageReasonCodesCode("moved")
    """
    Encounter details have been updated (e.g. to correct a coding error).
    From: http://terminology.hl7.org/CodeSystem/message-reasons-encounter in valuesets.xml
    """
    Edit = ExampleMessageReasonCodesCode("edit")
