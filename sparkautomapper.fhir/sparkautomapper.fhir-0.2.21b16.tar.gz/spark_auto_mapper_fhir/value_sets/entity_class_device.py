from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class EntityClassDevice(GenericTypeCode):
    """
    v3.EntityClassDevice
    From: http://terminology.hl7.org/ValueSet/v3-EntityClassDevice in v3-codesystems.xml
         A subtype of ManufacturedMaterial used in an activity, without being
    substantially changed through that activity.  The kind of device is identified
    by the code attribute inherited from Entity.  Usage:
    This includes durable (reusable) medical equipment as well as disposable
    equipment.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/v3-EntityClass
    """
    codeset: FhirUri = "http://terminology.hl7.org/CodeSystem/v3-EntityClass"


class EntityClassDeviceValues:
    """
    Corresponds to the Entity class
    From: http://terminology.hl7.org/CodeSystem/v3-EntityClass in v3-codesystems.xml
    """

    Entity = EntityClassDevice("ENT")
