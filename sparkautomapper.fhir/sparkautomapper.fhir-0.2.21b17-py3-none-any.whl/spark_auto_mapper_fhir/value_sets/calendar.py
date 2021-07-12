from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class Calendar(GenericTypeCode):
    """
    v3.Calendar
    From: http://terminology.hl7.org/ValueSet/v3-Calendar in v3-codesystems.xml
        **** MISSING DEFINITIONS ****
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/v3-Calendar
    """
    codeset: FhirUri = "http://terminology.hl7.org/CodeSystem/v3-Calendar"


class CalendarValues:
    """
    The Gregorian calendar is the calendar in effect in most countries of
    Christian influence since approximately 1582. This calendar superceded the
    Julian calendar.
    From: http://terminology.hl7.org/CodeSystem/v3-Calendar in v3-codesystems.xml
    """

    Gregorian = Calendar("GREG")
