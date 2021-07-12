from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class VisionBaseCode(GenericTypeCode):
    """
    VisionBase
    From: http://hl7.org/fhir/vision-base-codes in valuesets.xml
        A coded concept listing the base codes.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/vision-base-codes
    """
    codeset: FhirUri = "http://hl7.org/fhir/vision-base-codes"


class VisionBaseCodeValues:
    """
    top.
    From: http://hl7.org/fhir/vision-base-codes in valuesets.xml
    """

    Up = VisionBaseCode("up")
    """
    bottom.
    From: http://hl7.org/fhir/vision-base-codes in valuesets.xml
    """
    Down = VisionBaseCode("down")
    """
    inner edge.
    From: http://hl7.org/fhir/vision-base-codes in valuesets.xml
    """
    In = VisionBaseCode("in")
    """
    outer edge.
    From: http://hl7.org/fhir/vision-base-codes in valuesets.xml
    """
    Out = VisionBaseCode("out")
