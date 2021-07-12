from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class V2_0793(GenericTypeCode):
    """
    v2.0793
    From: http://terminology.hl7.org/ValueSet/v2-0793 in v2-tables.xml
        FHIR Value set/code system definition for HL7 v2 table 0793 ( Ruling Act)
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/ValueSet/v2-0793
    """
    codeset: FhirUri = "http://terminology.hl7.org/ValueSet/v2-0793"
