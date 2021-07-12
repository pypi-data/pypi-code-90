from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ConsentContentClassCode(GenericTypeCode):
    """
    ConsentContentClass
    From: http://hl7.org/fhir/ValueSet/consent-content-class in valuesets.xml
        This value set includes the FHIR resource types, along with some other
    important content class codes
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    urn:ietf:rfc:3986
    """
    codeset_urn_ietf_rfc_3986: FhirUri = "urn:ietf:rfc:3986"
    """
    urn:ietf:bcp:13
    """
    codeset_urn_ietf_bcp_13: FhirUri = "urn:ietf:bcp:13"
    """
    http://hl7.org/fhir/resource-types
    """
    codeset_resource_types: FhirUri = "http://hl7.org/fhir/resource-types"


class ConsentContentClassCodeValues:
    """
    From: http://hl7.org/fhir/ValueSet/consent-content-class in valuesets.xml
    """

    LipidLabReport = ConsentContentClassCode(
        "http://hl7.org/fhir/StructureDefinition/lipidprofile"
    )
    """
    From: http://hl7.org/fhir/ValueSet/consent-content-class in valuesets.xml
    """
    CDADocuments = ConsentContentClassCode("application/hl7-cda+xml")
