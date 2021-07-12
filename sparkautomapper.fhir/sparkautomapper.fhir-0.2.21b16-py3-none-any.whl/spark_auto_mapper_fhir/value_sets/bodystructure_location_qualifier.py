from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class BodystructureLocationQualifierCode(GenericTypeCode):
    """
    BodystructureLocationQualifier
    From: http://hl7.org/fhir/ValueSet/bodystructure-relative-location in valuesets.xml
        SNOMED-CT concepts modifying the anatomic location
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://snomed.info/sct
    """
    codeset: FhirUri = "http://snomed.info/sct"


class BodystructureLocationQualifierCodeValues:
    """
    From: http://hl7.org/fhir/ValueSet/bodystructure-relative-location in valuesets.xml
    """

    UnilateralLeft = BodystructureLocationQualifierCode("419161000")
    """
    From: http://hl7.org/fhir/ValueSet/bodystructure-relative-location in valuesets.xml
    """
    UnilateralRight = BodystructureLocationQualifierCode("419465000")
    """
    From: http://hl7.org/fhir/ValueSet/bodystructure-relative-location in valuesets.xml
    """
    Bilateral = BodystructureLocationQualifierCode("51440002")
    """
    From: http://hl7.org/fhir/ValueSet/bodystructure-relative-location in valuesets.xml
    """
    Upper = BodystructureLocationQualifierCode("261183002")
    """
    From: http://hl7.org/fhir/ValueSet/bodystructure-relative-location in valuesets.xml
    """
    Lower = BodystructureLocationQualifierCode("261122009")
    """
    From: http://hl7.org/fhir/ValueSet/bodystructure-relative-location in valuesets.xml
    """
    Medial = BodystructureLocationQualifierCode("255561001")
    """
    From: http://hl7.org/fhir/ValueSet/bodystructure-relative-location in valuesets.xml
    """
    Lateral = BodystructureLocationQualifierCode("49370004")
    """
    From: http://hl7.org/fhir/ValueSet/bodystructure-relative-location in valuesets.xml
    """
    Superior = BodystructureLocationQualifierCode("264217000")
    """
    From: http://hl7.org/fhir/ValueSet/bodystructure-relative-location in valuesets.xml
    """
    Inferior = BodystructureLocationQualifierCode("261089000")
    """
    From: http://hl7.org/fhir/ValueSet/bodystructure-relative-location in valuesets.xml
    """
    Posterior = BodystructureLocationQualifierCode("255551008")
    """
    From: http://hl7.org/fhir/ValueSet/bodystructure-relative-location in valuesets.xml
    """
    Below = BodystructureLocationQualifierCode("351726001")
    """
    From: http://hl7.org/fhir/ValueSet/bodystructure-relative-location in valuesets.xml
    """
    Above = BodystructureLocationQualifierCode("352730000")
