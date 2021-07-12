from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ExampleProviderQualificationCodesCode(GenericTypeCode):
    """
    ExampleProviderQualificationCodes
    From: http://terminology.hl7.org/CodeSystem/ex-providerqualification in valuesets.xml
        This value set includes sample Provider Qualification codes.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/ex-providerqualification
    """
    codeset: FhirUri = "http://terminology.hl7.org/CodeSystem/ex-providerqualification"


class ExampleProviderQualificationCodesCodeValues:
    """
    Dentist General Practitioner (DDS, DDM).
    From: http://terminology.hl7.org/CodeSystem/ex-providerqualification in valuesets.xml
    """

    Dentist = ExampleProviderQualificationCodesCode("311405")
    """
    Ophthalmologist.
    From: http://terminology.hl7.org/CodeSystem/ex-providerqualification in valuesets.xml
    """
    Ophthalmologist = ExampleProviderQualificationCodesCode("604215")
    """
    Optometrist.
    From: http://terminology.hl7.org/CodeSystem/ex-providerqualification in valuesets.xml
    """
    Optometrist = ExampleProviderQualificationCodesCode("604210")
