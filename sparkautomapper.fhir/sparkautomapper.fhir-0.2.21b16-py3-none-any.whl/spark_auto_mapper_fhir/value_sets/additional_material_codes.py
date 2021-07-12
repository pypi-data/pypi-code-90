from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class AdditionalMaterialCodesCode(GenericTypeCode):
    """
    AdditionalMaterialCodes
    From: http://hl7.org/fhir/additionalmaterials in valuesets.xml
        This value set includes sample additional material type codes.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/additionalmaterials
    """
    codeset: FhirUri = "http://hl7.org/fhir/additionalmaterials"


class AdditionalMaterialCodesCodeValues:
    """
    XRay
    From: http://hl7.org/fhir/additionalmaterials in valuesets.xml
    """

    XRay = AdditionalMaterialCodesCode("xray")
    """
    Image
    From: http://hl7.org/fhir/additionalmaterials in valuesets.xml
    """
    Image = AdditionalMaterialCodesCode("image")
    """
    Email
    From: http://hl7.org/fhir/additionalmaterials in valuesets.xml
    """
    Email = AdditionalMaterialCodesCode("email")
    """
    Model
    From: http://hl7.org/fhir/additionalmaterials in valuesets.xml
    """
    Model = AdditionalMaterialCodesCode("model")
    """
    Document
    From: http://hl7.org/fhir/additionalmaterials in valuesets.xml
    """
    Document = AdditionalMaterialCodesCode("document")
    """
    Other
    From: http://hl7.org/fhir/additionalmaterials in valuesets.xml
    """
    Other = AdditionalMaterialCodesCode("other")
