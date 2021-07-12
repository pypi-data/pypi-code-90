from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class AllergyIntoleranceVerificationStatusCodesCode(GenericTypeCode):
    """
    AllergyIntoleranceVerificationStatusCodes
    From: http://terminology.hl7.org/CodeSystem/allergyintolerance-verification in valuesets.xml
        Preferred value set for AllergyIntolerance Verification Status.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/allergyintolerance-verification
    """
    codeset: FhirUri = (
        "http://terminology.hl7.org/CodeSystem/allergyintolerance-verification"
    )


class AllergyIntoleranceVerificationStatusCodesCodeValues:
    """
    A low level of certainty about the propensity for a reaction to the identified
    substance.
    From: http://terminology.hl7.org/CodeSystem/allergyintolerance-verification in valuesets.xml
    """

    Unconfirmed = AllergyIntoleranceVerificationStatusCodesCode("unconfirmed")
    """
    A high level of certainty about the propensity for a reaction to the
    identified substance, which may include clinical evidence by testing or
    rechallenge.
    From: http://terminology.hl7.org/CodeSystem/allergyintolerance-verification in valuesets.xml
    """
    Confirmed = AllergyIntoleranceVerificationStatusCodesCode("confirmed")
    """
    A propensity for a reaction to the identified substance has been disputed or
    disproven with a sufficient level of clinical certainty to justify
    invalidating the assertion. This might or might not include testing or
    rechallenge.
    From: http://terminology.hl7.org/CodeSystem/allergyintolerance-verification in valuesets.xml
    """
    Refuted = AllergyIntoleranceVerificationStatusCodesCode("refuted")
    """
    The statement was entered in error and is not valid.
    From: http://terminology.hl7.org/CodeSystem/allergyintolerance-verification in valuesets.xml
    """
    EnteredInError = AllergyIntoleranceVerificationStatusCodesCode("entered-in-error")
