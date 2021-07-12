from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class HumanNameAssemblyOrderCode(GenericTypeCode):
    """
    HumanNameAssemblyOrder
    From: http://terminology.hl7.org/CodeSystem/name-assembly-order in valuesets.xml
        A code that represents the preferred display order of the components of a
    human name.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/name-assembly-order
    """
    codeset: FhirUri = "http://terminology.hl7.org/CodeSystem/name-assembly-order"


class HumanNameAssemblyOrderCodeValues:
    """
    From: http://terminology.hl7.org/CodeSystem/name-assembly-order in valuesets.xml
    """

    OwnName = HumanNameAssemblyOrderCode("NL1")
    """
    From: http://terminology.hl7.org/CodeSystem/name-assembly-order in valuesets.xml
    """
    PartnerName = HumanNameAssemblyOrderCode("NL2")
    """
    From: http://terminology.hl7.org/CodeSystem/name-assembly-order in valuesets.xml
    """
    PartnerNameFollowedByMaidenName = HumanNameAssemblyOrderCode("NL3")
    """
    From: http://terminology.hl7.org/CodeSystem/name-assembly-order in valuesets.xml
    """
    OwnNameFollowedByPartnerName = HumanNameAssemblyOrderCode("NL4")
