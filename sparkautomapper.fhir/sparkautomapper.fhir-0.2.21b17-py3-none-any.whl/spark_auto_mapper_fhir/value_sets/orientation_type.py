from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class OrientationTypeCode(GenericTypeCode):
    """
    orientationType
    From: http://hl7.org/fhir/orientation-type in valuesets.xml
        Type for orientation.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/orientation-type
    """
    codeset: FhirUri = "http://hl7.org/fhir/orientation-type"


class OrientationTypeCodeValues:
    """
    Sense orientation of reference sequence.
    From: http://hl7.org/fhir/orientation-type in valuesets.xml
    """

    SenseOrientationOfReferenceSeq = OrientationTypeCode("sense")
    """
    Antisense orientation of reference sequence.
    From: http://hl7.org/fhir/orientation-type in valuesets.xml
    """
    AntisenseOrientationOfReferenceSeq = OrientationTypeCode("antisense")
