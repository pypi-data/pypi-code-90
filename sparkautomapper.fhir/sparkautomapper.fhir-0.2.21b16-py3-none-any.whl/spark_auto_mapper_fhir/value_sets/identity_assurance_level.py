from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class IdentityAssuranceLevelCode(GenericTypeCode):
    """
    IdentityAssuranceLevel
    From: http://hl7.org/fhir/identity-assuranceLevel in valuesets.xml
        The level of confidence that this link represents the same actual person,
    based on NIST Authentication Levels.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/identity-assuranceLevel
    """
    codeset: FhirUri = "http://hl7.org/fhir/identity-assuranceLevel"


class IdentityAssuranceLevelCodeValues:
    """
    Little or no confidence in the asserted identity's accuracy.
    From: http://hl7.org/fhir/identity-assuranceLevel in valuesets.xml
    """

    Level1 = IdentityAssuranceLevelCode("level1")
    """
    Some confidence in the asserted identity's accuracy.
    From: http://hl7.org/fhir/identity-assuranceLevel in valuesets.xml
    """
    Level2 = IdentityAssuranceLevelCode("level2")
    """
    High confidence in the asserted identity's accuracy.
    From: http://hl7.org/fhir/identity-assuranceLevel in valuesets.xml
    """
    Level3 = IdentityAssuranceLevelCode("level3")
    """
    Very high confidence in the asserted identity's accuracy.
    From: http://hl7.org/fhir/identity-assuranceLevel in valuesets.xml
    """
    Level4 = IdentityAssuranceLevelCode("level4")
