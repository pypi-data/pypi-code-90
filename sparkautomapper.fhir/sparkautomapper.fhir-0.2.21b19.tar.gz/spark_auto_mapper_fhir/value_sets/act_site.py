from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ActSite(GenericTypeCode):
    """
    v3.ActSite
    From: http://terminology.hl7.org/ValueSet/v3-ActSite in v3-codesystems.xml
         An anatomical location on an organism which can be the focus of an act.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/v3-ActSite
    """
    codeset: FhirUri = "http://terminology.hl7.org/CodeSystem/v3-ActSite"


class ActSiteValues:
    """
    An anatomical location on a human which can be the focus of an act.
    From: http://terminology.hl7.org/CodeSystem/v3-ActSite in v3-codesystems.xml
    """

    HumanActSite = ActSite("_HumanActSite")
