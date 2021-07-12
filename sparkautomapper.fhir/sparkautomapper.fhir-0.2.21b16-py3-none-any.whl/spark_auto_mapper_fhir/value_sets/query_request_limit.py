from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class QueryRequestLimit(GenericTypeCode):
    """
    v3.QueryRequestLimit
    From: http://terminology.hl7.org/ValueSet/v3-QueryRequestLimit in v3-codesystems.xml
          Definition:
    Defines the units associated with the magnitude of the maximum size limit of a
    query response that can be accepted by the requesting application.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/v3-QueryRequestLimit
    """
    codeset: FhirUri = "http://terminology.hl7.org/CodeSystem/v3-QueryRequestLimit"


class QueryRequestLimitValues:
    """
    Definition: The number of matching instances (number of focal classes). The
    document header class is the focal class of a document, a record would
    therefore be equal to a document.
    From: http://terminology.hl7.org/CodeSystem/v3-QueryRequestLimit in v3-codesystems.xml
    """

    QueryRequestLimit_ = QueryRequestLimit("_QueryRequestLimit")
