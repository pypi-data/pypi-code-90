from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class OralProsthoMaterialTypeCodesCode(GenericTypeCode):
    """
    OralProsthoMaterialTypeCodes
    From: http://hl7.org/fhir/ex-oralprostho in valuesets.xml
        This value set includes sample Oral Prosthodontic Material type codes.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/ex-oralprostho
    """
    codeset: FhirUri = "http://hl7.org/fhir/ex-oralprostho"


class OralProsthoMaterialTypeCodesCodeValues:
    """
    Fixed Bridge
    From: http://hl7.org/fhir/ex-oralprostho in valuesets.xml
    """

    FixedBridge = OralProsthoMaterialTypeCodesCode("1")
    """
    Maryland Bridge
    From: http://hl7.org/fhir/ex-oralprostho in valuesets.xml
    """
    MarylandBridge = OralProsthoMaterialTypeCodesCode("2")
    """
    Denture Acrylic
    From: http://hl7.org/fhir/ex-oralprostho in valuesets.xml
    """
    DentureAcrylic = OralProsthoMaterialTypeCodesCode("3")
    """
    Denture Chrome Cobalt
    From: http://hl7.org/fhir/ex-oralprostho in valuesets.xml
    """
    DentureChromeCobalt = OralProsthoMaterialTypeCodesCode("4")
