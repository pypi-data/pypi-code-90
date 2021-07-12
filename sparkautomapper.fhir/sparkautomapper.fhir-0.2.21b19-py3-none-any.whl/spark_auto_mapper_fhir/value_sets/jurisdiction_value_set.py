from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class JurisdictionValueSetCode(GenericTypeCode):
    """
    Jurisdiction ValueSet
    From: http://hl7.org/fhir/ValueSet/jurisdiction in valuesets.xml
        This value set defines a base set of codes for country, country subdivision
    and region    for indicating where a resource is intended to be used.

       Note: The codes for countries and country subdivisions are taken from
    [ISO 3166](https://www.iso.org/iso-3166-country-codes.html)    while the codes
    for "supra-national" regions are from    [UN Standard country or area codes
    for statistical use (M49)](http://unstats.un.org/unsd/methods/m49/m49.htm).
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://unstats.un.org/unsd/methods/m49/m49.htm
    """
    codeset_m49_htm: FhirUri = "http://unstats.un.org/unsd/methods/m49/m49.htm"
    """
    urn:iso:std:iso:3166:-2
    """
    codeset_urn_iso_std_iso_3166__2: FhirUri = "urn:iso:std:iso:3166:-2"
    """
    urn:iso:std:iso:3166
    """
    codeset_urn_iso_std_iso_3166: FhirUri = "urn:iso:std:iso:3166"
