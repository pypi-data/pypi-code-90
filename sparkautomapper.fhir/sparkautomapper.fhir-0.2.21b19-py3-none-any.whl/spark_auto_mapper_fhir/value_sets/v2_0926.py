from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class V2_0926(GenericTypeCode):
    """
    v2.0926
    From: http://terminology.hl7.org/ValueSet/v2-0926 in v2-tables.xml
        FHIR Value set/code system definition for HL7 v2 table 0926 ( Phlebotomy
    Status)
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/ValueSet/v2-0926
    """
    codeset: FhirUri = "http://terminology.hl7.org/ValueSet/v2-0926"
