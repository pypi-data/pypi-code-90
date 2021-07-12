from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ICD_10CodesCode(GenericTypeCode):
    """
    ICD-10Codes
    From: http://hl7.org/fhir/ValueSet/icd-10 in valuesets.xml
        This value set includes sample ICD-10 codes.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/sid/icd-10
    """
    codeset: FhirUri = "http://hl7.org/fhir/sid/icd-10"


class ICD_10CodesCodeValues:
    """
    From: http://hl7.org/fhir/ValueSet/icd-10 in valuesets.xml
    """

    DIAG_1 = ICD_10CodesCode("123456")
    """
    From: http://hl7.org/fhir/ValueSet/icd-10 in valuesets.xml
    """
    DIAG_1a = ICD_10CodesCode("123457")
    """
    From: http://hl7.org/fhir/ValueSet/icd-10 in valuesets.xml
    """
    DIAG_2 = ICD_10CodesCode("987654")
    """
    From: http://hl7.org/fhir/ValueSet/icd-10 in valuesets.xml
    """
    DIAG_3 = ICD_10CodesCode("123987")
    """
    From: http://hl7.org/fhir/ValueSet/icd-10 in valuesets.xml
    """
    DIAG_4 = ICD_10CodesCode("112233")
    """
    From: http://hl7.org/fhir/ValueSet/icd-10 in valuesets.xml
    """
    DIAG_5 = ICD_10CodesCode("997755")
    """
    From: http://hl7.org/fhir/ValueSet/icd-10 in valuesets.xml
    """
    DIAG_6 = ICD_10CodesCode("321789")
