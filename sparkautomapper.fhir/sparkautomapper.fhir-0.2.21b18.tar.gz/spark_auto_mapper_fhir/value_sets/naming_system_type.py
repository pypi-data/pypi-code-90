from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class NamingSystemTypeCode(GenericTypeCode):
    """
    NamingSystemType
    From: http://hl7.org/fhir/namingsystem-type in valuesets.xml
        Identifies the purpose of the naming system.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/namingsystem-type
    """
    codeset: FhirUri = "http://hl7.org/fhir/namingsystem-type"


class NamingSystemTypeCodeValues:
    """
    The naming system is used to define concepts and symbols to represent those
    concepts; e.g. UCUM, LOINC, NDC code, local lab codes, etc.
    From: http://hl7.org/fhir/namingsystem-type in valuesets.xml
    """

    CodeSystem = NamingSystemTypeCode("codesystem")
    """
    The naming system is used to manage identifiers (e.g. license numbers, order
    numbers, etc.).
    From: http://hl7.org/fhir/namingsystem-type in valuesets.xml
    """
    Identifier = NamingSystemTypeCode("identifier")
    """
    The naming system is used as the root for other identifiers and naming
    systems.
    From: http://hl7.org/fhir/namingsystem-type in valuesets.xml
    """
    Root = NamingSystemTypeCode("root")
