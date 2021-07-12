from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class Yes_or_No_or_Don_tKnowCode(GenericTypeCode):
    """
    Yes/No/Don't Know
    From: http://hl7.org/fhir/ValueSet/yesnodontknow in valuesets.xml
        For Capturing simple yes-no-don't know answers
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/ValueSet/v2-0136
    """
    codeset_v2_0136: FhirUri = "http://terminology.hl7.org/ValueSet/v2-0136"
    """
    http://terminology.hl7.org/CodeSystem/data-absent-reason
    """
    codeset_data_absent_reason: FhirUri = (
        "http://terminology.hl7.org/CodeSystem/data-absent-reason"
    )


class Yes_or_No_or_Don_tKnowCodeValues:
    """
    From: http://hl7.org/fhir/ValueSet/yesnodontknow in valuesets.xml
    """

    Don_tKnow = Yes_or_No_or_Don_tKnowCode("asked-unknown")
