from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class EquipmentAlertLevel(GenericTypeCode):
    """
    v3.EquipmentAlertLevel
    From: http://terminology.hl7.org/ValueSet/v3-EquipmentAlertLevel in v3-codesystems.xml
        **** MISSING DEFINITIONS ****
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/v3-EquipmentAlertLevel
    """
    codeset: FhirUri = "http://terminology.hl7.org/CodeSystem/v3-EquipmentAlertLevel"


class EquipmentAlertLevelValues:
    """
    Shut Down, Fix Problem and Re-init
    From: http://terminology.hl7.org/CodeSystem/v3-EquipmentAlertLevel in v3-codesystems.xml
    """

    Critical = EquipmentAlertLevel("C")
    """
    No Corrective Action Needed
    From: http://terminology.hl7.org/CodeSystem/v3-EquipmentAlertLevel in v3-codesystems.xml
    """
    Normal = EquipmentAlertLevel("N")
    """
    Corrective Action Required
    From: http://terminology.hl7.org/CodeSystem/v3-EquipmentAlertLevel in v3-codesystems.xml
    """
    Serious = EquipmentAlertLevel("S")
    """
    Corrective Action Anticipated
    From: http://terminology.hl7.org/CodeSystem/v3-EquipmentAlertLevel in v3-codesystems.xml
    """
    Warning = EquipmentAlertLevel("W")
