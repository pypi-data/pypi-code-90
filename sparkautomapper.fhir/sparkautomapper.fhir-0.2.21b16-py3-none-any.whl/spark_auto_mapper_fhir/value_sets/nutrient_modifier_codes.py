from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class NutrientModifierCodesCode(GenericTypeCode):
    """
    NutrientModifierCodes
    From: http://hl7.org/fhir/ValueSet/nutrient-code in valuesets.xml
        NutrientModifier :  Codes for types of nutrients that are being modified such
    as carbohydrate or sodium.  This value set includes codes from [SNOMED
    CT](http://snomed.info/sct) where concept is-a 226355009
    (Nutrients(substance)), and the concepts for Sodium, Potassium and Fluid. This
    is provided as a suggestive example.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://snomed.info/sct
    """
    codeset: FhirUri = "http://snomed.info/sct"


class NutrientModifierCodesCodeValues:
    """
    From: http://hl7.org/fhir/ValueSet/nutrient-code in valuesets.xml
    """

    Fluid = NutrientModifierCodesCode("33463005")
    """
    From: http://hl7.org/fhir/ValueSet/nutrient-code in valuesets.xml
    """
    Sodium = NutrientModifierCodesCode("39972003")
    """
    From: http://hl7.org/fhir/ValueSet/nutrient-code in valuesets.xml
    """
    Potassium = NutrientModifierCodesCode("88480006")
