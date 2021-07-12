from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ActStatus(GenericTypeCode):
    """
    v3.ActStatus
    From: http://terminology.hl7.org/ValueSet/v3-ActStatus in v3-codesystems.xml
         Codes representing the defined possible states of an Act, as defined by the
    Act class state machine.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/v3-ActStatus
    """
    codeset: FhirUri = "http://terminology.hl7.org/CodeSystem/v3-ActStatus"


class ActStatusValues:
    """
    Encompasses the expected states of an Act, but excludes "nullified" and
    "obsolete" which represent unusual terminal states for the life-cycle.
    From: http://terminology.hl7.org/CodeSystem/v3-ActStatus in v3-codesystems.xml
    """

    Normal = ActStatus("normal")
    """
    This Act instance was created in error and has been 'removed' and is treated
    as though it never existed.  A record is retained for audit purposes only.
    From: http://terminology.hl7.org/CodeSystem/v3-ActStatus in v3-codesystems.xml
    """
    Nullified = ActStatus("nullified")
    """
    This Act instance has been replaced by a new instance.
    From: http://terminology.hl7.org/CodeSystem/v3-ActStatus in v3-codesystems.xml
    """
    Obsolete = ActStatus("obsolete")
