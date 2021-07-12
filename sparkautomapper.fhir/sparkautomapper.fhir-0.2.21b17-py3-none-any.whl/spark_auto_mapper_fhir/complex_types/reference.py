from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.fhir_types.fhir_reference import FhirReference
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase

from spark_auto_mapper_fhir.base_types.fhir_complex_type_base import FhirComplexTypeBase

if TYPE_CHECKING:
    pass
    # id_ (string)
    # extension (Extension)
    # reference (string)
    # type_ (uri)
    # identifier (Identifier)
    from spark_auto_mapper_fhir.complex_types.identifier import Identifier

    # display (string)


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
from typing import TypeVar, Generic
from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase

_T = TypeVar("_T", bound=Union[FhirResourceBase])


class Reference(FhirComplexTypeBase, Generic[_T]):
    """
    Reference
    fhir-base.xsd
        A reference from one resource to another.
        If the element is present, it must have a value for at least one of the defined elements, an @id referenced from the Narrative, or extensions
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        reference: Optional[FhirReference] = None,
        type_: Optional[FhirUri] = None,
        identifier: Optional[Identifier] = None,
        display: Optional[FhirString] = None,
    ) -> None:
        """
            A reference from one resource to another.
            If the element is present, it must have a value for at least one of the
        defined elements, an @id referenced from the Narrative, or extensions

            :param id_: None
            :param extension: May be used to represent additional information that is not part of the basic
        definition of the element. To make the use of extensions safe and manageable,
        there is a strict set of governance  applied to the definition and use of
        extensions. Though any implementer can define an extension, there is a set of
        requirements that SHALL be met as part of the definition of the extension.
            :param reference: A reference to a location at which the other resource is found. The reference
        may be a relative reference, in which case it is relative to the service base
        URL, or an absolute URL that resolves to the location where the resource is
        found. The reference may be version specific or not. If the reference is not
        to a FHIR RESTful server, then it should be assumed to be version specific.
        Internal fragment references (start with '#') refer to contained resources.
            :param type_: The expected type of the target of the reference. If both Reference.type and
        Reference.reference are populated and Reference.reference is a FHIR URL, both
        SHALL be consistent.

        The type is the Canonical URL of Resource Definition that is the type this
        reference refers to. References are URLs that are relative to
        http://hl7.org/fhir/StructureDefinition/ e.g. "Patient" is a reference to
        http://hl7.org/fhir/StructureDefinition/Patient. Absolute URLs are only
        allowed for logical models (and can only be used in references in logical
        models, not resources).
            :param identifier: An identifier for the target resource. This is used when there is no way to
        reference the other resource directly, either because the entity it represents
        is not available through a FHIR server, or because there is no way for the
        author of the resource to convert a known identifier to an actual location.
        There is no requirement that a Reference.identifier point to something that is
        actually exposed as a FHIR instance, but it SHALL point to a business concept
        that would be expected to be exposed as a FHIR instance, and that instance
        would need to be of a FHIR resource type allowed by the reference.
            :param display: Plain text narrative that identifies the resource in addition to the resource
        reference.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            reference=reference,
            type_=type_,
            identifier=identifier,
            display=display,
        )
