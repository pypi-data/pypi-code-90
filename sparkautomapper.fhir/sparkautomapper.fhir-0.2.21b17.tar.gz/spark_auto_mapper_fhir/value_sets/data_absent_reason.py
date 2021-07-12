from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class DataAbsentReasonCode(GenericTypeCode):
    """
    DataAbsentReason
    From: http://terminology.hl7.org/CodeSystem/data-absent-reason in valuesets.xml
        Used to specify why the normally expected content of the data element is
    missing.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/data-absent-reason
    """
    codeset: FhirUri = "http://terminology.hl7.org/CodeSystem/data-absent-reason"


class DataAbsentReasonCodeValues:
    """
    The value is expected to exist but is not known.
    From: http://terminology.hl7.org/CodeSystem/data-absent-reason in valuesets.xml
    """

    Unknown = DataAbsentReasonCode("unknown")
    """
    The information is not available due to security, privacy or related reasons.
    From: http://terminology.hl7.org/CodeSystem/data-absent-reason in valuesets.xml
    """
    Masked = DataAbsentReasonCode("masked")
    """
    There is no proper value for this element (e.g. last menstrual period for a
    male).
    From: http://terminology.hl7.org/CodeSystem/data-absent-reason in valuesets.xml
    """
    NotApplicable = DataAbsentReasonCode("not-applicable")
    """
    The source system wasn't capable of supporting this element.
    From: http://terminology.hl7.org/CodeSystem/data-absent-reason in valuesets.xml
    """
    Unsupported = DataAbsentReasonCode("unsupported")
    """
    The content of the data is represented in the resource narrative.
    From: http://terminology.hl7.org/CodeSystem/data-absent-reason in valuesets.xml
    """
    AsText = DataAbsentReasonCode("as-text")
    """
    Some system or workflow process error means that the information is not
    available.
    From: http://terminology.hl7.org/CodeSystem/data-absent-reason in valuesets.xml
    """
    Error = DataAbsentReasonCode("error")
    """
    The value is not available because the observation procedure (test, etc.) was
    not performed.
    From: http://terminology.hl7.org/CodeSystem/data-absent-reason in valuesets.xml
    """
    NotPerformed = DataAbsentReasonCode("not-performed")
    """
    The value is not permitted in this context (e.g. due to profiles, or the base
    data types).
    From: http://terminology.hl7.org/CodeSystem/data-absent-reason in valuesets.xml
    """
    NotPermitted = DataAbsentReasonCode("not-permitted")
