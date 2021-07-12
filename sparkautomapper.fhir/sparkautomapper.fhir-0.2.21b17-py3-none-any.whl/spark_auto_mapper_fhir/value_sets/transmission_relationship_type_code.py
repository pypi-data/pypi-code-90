from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class TransmissionRelationshipTypeCode(GenericTypeCode):
    """
    v3.TransmissionRelationshipTypeCode
    From: http://terminology.hl7.org/ValueSet/v3-TransmissionRelationshipTypeCode in v3-codesystems.xml
          Description:
    A code specifying the meaning and purpose of every TransmissionRelationship
    instance. Each of its values implies specific constraints to what kinds of
    Transmission objects can be related and in which way.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/v3-TransmissionRelationshipTypeCode
    """
    codeset: FhirUri = (
        "http://terminology.hl7.org/CodeSystem/v3-TransmissionRelationshipTypeCode"
    )


class TransmissionRelationshipTypeCodeValues:
    """
    Description:A transmission relationship indicating that the source
    transmission follows the target transmission.
    From: http://terminology.hl7.org/CodeSystem/v3-TransmissionRelationshipTypeCode in v3-codesystems.xml
    """

    Sequence = TransmissionRelationshipTypeCode("SEQL")
