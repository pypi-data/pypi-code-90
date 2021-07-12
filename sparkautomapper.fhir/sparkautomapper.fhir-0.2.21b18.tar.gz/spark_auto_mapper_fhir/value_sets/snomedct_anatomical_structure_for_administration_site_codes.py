from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class SNOMEDCTAnatomicalStructureForAdministrationSiteCodesCode(GenericTypeCode):
    """
    SNOMEDCTAnatomicalStructureForAdministrationSiteCodes
    From: http://hl7.org/fhir/ValueSet/approach-site-codes in valuesets.xml
        This value set includes Anatomical Structure codes from SNOMED CT - provided
    as an exemplar.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://snomed.info/sct
    """
    codeset: FhirUri = "http://snomed.info/sct"
