from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class StructureMapTransformCode(GenericTypeCode):
    """
    StructureMapTransform
    From: http://hl7.org/fhir/map-transform in valuesets.xml
        How data is copied/created.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/map-transform
    """
    codeset: FhirUri = "http://hl7.org/fhir/map-transform"


class StructureMapTransformCodeValues:
    """
    create(type : string) - type is passed through to the application on the
    standard API, and must be known by it.
    From: http://hl7.org/fhir/map-transform in valuesets.xml
    """

    Create = StructureMapTransformCode("create")
    """
    copy(source).
    From: http://hl7.org/fhir/map-transform in valuesets.xml
    """
    Copy = StructureMapTransformCode("copy")
    """
    truncate(source, length) - source must be stringy type.
    From: http://hl7.org/fhir/map-transform in valuesets.xml
    """
    Truncate = StructureMapTransformCode("truncate")
    """
    escape(source, fmt1, fmt2) - change source from one kind of escaping to
    another (plain, java, xml, json). note that this is for when the string itself
    is escaped.
    From: http://hl7.org/fhir/map-transform in valuesets.xml
    """
    Escape = StructureMapTransformCode("escape")
    """
    cast(source, type?) - case source from one type to another. target type can be
    left as implicit if there is one and only one target type known.
    From: http://hl7.org/fhir/map-transform in valuesets.xml
    """
    Cast = StructureMapTransformCode("cast")
    """
    append(source...) - source is element or string.
    From: http://hl7.org/fhir/map-transform in valuesets.xml
    """
    Append = StructureMapTransformCode("append")
    """
    translate(source, uri_of_map) - use the translate operation.
    From: http://hl7.org/fhir/map-transform in valuesets.xml
    """
    Translate = StructureMapTransformCode("translate")
    """
    reference(source : object) - return a string that references the provided tree
    properly.
    From: http://hl7.org/fhir/map-transform in valuesets.xml
    """
    Reference = StructureMapTransformCode("reference")
    """
    Perform a date operation. *Parameters to be documented*.
    From: http://hl7.org/fhir/map-transform in valuesets.xml
    """
    DateOp = StructureMapTransformCode("dateOp")
    """
    Generate a random UUID (in lowercase). No Parameters.
    From: http://hl7.org/fhir/map-transform in valuesets.xml
    """
    Uuid = StructureMapTransformCode("uuid")
    """
    Return the appropriate string to put in a reference that refers to the
    resource provided as a parameter.
    From: http://hl7.org/fhir/map-transform in valuesets.xml
    """
    Pointer = StructureMapTransformCode("pointer")
    """
    Execute the supplied FHIRPath expression and use the value returned by that.
    From: http://hl7.org/fhir/map-transform in valuesets.xml
    """
    Evaluate = StructureMapTransformCode("evaluate")
    """
    Create a CodeableConcept. Parameters = (text) or (system. Code[, display]).
    From: http://hl7.org/fhir/map-transform in valuesets.xml
    """
    Cc = StructureMapTransformCode("cc")
    """
    Create a Coding. Parameters = (system. Code[, display]).
    From: http://hl7.org/fhir/map-transform in valuesets.xml
    """
    C = StructureMapTransformCode("c")
    """
    Create a quantity. Parameters = (text) or (value, unit, [system, code]) where
    text is the natural representation e.g. [comparator]value[space]unit.
    From: http://hl7.org/fhir/map-transform in valuesets.xml
    """
    Qty = StructureMapTransformCode("qty")
    """
    Create an identifier. Parameters = (system, value[, type]) where type is a
    code from the identifier type value set.
    From: http://hl7.org/fhir/map-transform in valuesets.xml
    """
    Id = StructureMapTransformCode("id")
    """
    Create a contact details. Parameters = (value) or (system, value). If no
    system is provided, the system should be inferred from the content of the
    value.
    From: http://hl7.org/fhir/map-transform in valuesets.xml
    """
    Cp = StructureMapTransformCode("cp")
