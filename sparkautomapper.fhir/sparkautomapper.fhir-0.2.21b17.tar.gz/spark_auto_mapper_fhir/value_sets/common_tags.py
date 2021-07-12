from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class CommonTagsCode(GenericTypeCode):
    """
    CommonTags
    From: http://terminology.hl7.org/CodeSystem/common-tags in valuesets.xml
        Common Tag Codes defined by FHIR project
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/common-tags
    """
    codeset: FhirUri = "http://terminology.hl7.org/CodeSystem/common-tags"


class CommonTagsCodeValues:
    """
    This request is intended to be acted upon, not merely stored
    From: http://terminology.hl7.org/CodeSystem/common-tags in valuesets.xml
    """

    Actionable = CommonTagsCode("actionable")
