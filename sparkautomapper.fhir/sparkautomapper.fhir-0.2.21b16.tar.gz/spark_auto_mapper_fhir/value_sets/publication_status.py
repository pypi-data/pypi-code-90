from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class PublicationStatusCode(GenericTypeCode):
    """
    PublicationStatus
    From: http://hl7.org/fhir/publication-status in valuesets.xml
        The lifecycle status of an artifact.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/publication-status
    """
    codeset: FhirUri = "http://hl7.org/fhir/publication-status"


class PublicationStatusCodeValues:
    """
    This resource is still under development and is not yet considered to be ready
    for normal use.
    From: http://hl7.org/fhir/publication-status in valuesets.xml
    """

    Draft = PublicationStatusCode("draft")
    """
    This resource is ready for normal use.
    From: http://hl7.org/fhir/publication-status in valuesets.xml
    """
    Active = PublicationStatusCode("active")
    """
    This resource has been withdrawn or superseded and should no longer be used.
    From: http://hl7.org/fhir/publication-status in valuesets.xml
    """
    Retired = PublicationStatusCode("retired")
    """
    The authoring system does not know which of the status values currently
    applies for this resource.  Note: This concept is not to be used for "other" -
    one of the listed statuses is presumed to apply, it's just not known which
    one.
    From: http://hl7.org/fhir/publication-status in valuesets.xml
    """
    Unknown = PublicationStatusCode("unknown")
