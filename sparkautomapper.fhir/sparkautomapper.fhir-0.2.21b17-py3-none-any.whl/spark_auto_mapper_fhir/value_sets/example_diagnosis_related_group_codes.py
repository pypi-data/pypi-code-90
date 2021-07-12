from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ExampleDiagnosisRelatedGroupCodesCode(GenericTypeCode):
    """
    ExampleDiagnosisRelatedGroupCodes
    From: http://terminology.hl7.org/CodeSystem/ex-diagnosisrelatedgroup in valuesets.xml
        This value set includes example Diagnosis Related Group codes.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/ex-diagnosisrelatedgroup
    """
    codeset: FhirUri = "http://terminology.hl7.org/CodeSystem/ex-diagnosisrelatedgroup"


class ExampleDiagnosisRelatedGroupCodesCodeValues:
    """
    Normal Vaginal Delivery.
    From: http://terminology.hl7.org/CodeSystem/ex-diagnosisrelatedgroup in valuesets.xml
    """

    NormalVaginalDelivery = ExampleDiagnosisRelatedGroupCodesCode("100")
    """
    Appendectomy without rupture or other complications.
    From: http://terminology.hl7.org/CodeSystem/ex-diagnosisrelatedgroup in valuesets.xml
    """
    Appendectomy_Uncomplicated = ExampleDiagnosisRelatedGroupCodesCode("101")
    """
    Emergency department treatment of a tooth abscess.
    From: http://terminology.hl7.org/CodeSystem/ex-diagnosisrelatedgroup in valuesets.xml
    """
    ToothAbscess = ExampleDiagnosisRelatedGroupCodesCode("300")
    """
    Head trauma - concussion.
    From: http://terminology.hl7.org/CodeSystem/ex-diagnosisrelatedgroup in valuesets.xml
    """
    HeadTrauma_Concussion = ExampleDiagnosisRelatedGroupCodesCode("400")
