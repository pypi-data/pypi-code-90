from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class DietCodesCode(GenericTypeCode):
    """
    DietCodes
    From: http://hl7.org/fhir/ValueSet/diet-type in valuesets.xml
        Codes that can be used to indicate the type of food being ordered for a
    patient. This value set is provided as a suggestive example. It includes codes
    from [SNOMED CT](http://snomed.info/sct) where concept is-a 182922004 (Dietary
    regime (regime/therapy))
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://snomed.info/sct
    """
    codeset: FhirUri = "http://snomed.info/sct"
