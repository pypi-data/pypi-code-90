from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString

from spark_auto_mapper_fhir.base_types.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)

if TYPE_CHECKING:
    pass
    # id_ (string)
    # extension (Extension)
    from spark_auto_mapper_fhir.extensions.extension import Extension

    # modifierExtension (Extension)
    # identifier (Identifier)
    from spark_auto_mapper_fhir.complex_types.identifier import Identifier

    # description (string)
    # type_ (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # End Import for References for type_
    # Import for CodeableConcept for type_
    from spark_auto_mapper_fhir.value_sets.specimen_container_type import (
        SpecimenContainerTypeCode,
    )

    # End Import for CodeableConcept for type_
    # capacity (Quantity)
    from spark_auto_mapper_fhir.complex_types.quantity import Quantity

    # specimenQuantity (Quantity)
    # additiveCodeableConcept (CodeableConcept)
    # End Import for References for additiveCodeableConcept
    # Import for CodeableConcept for additiveCodeableConcept
    from spark_auto_mapper_fhir.value_sets.v2_0371 import V2_0371

    # End Import for CodeableConcept for additiveCodeableConcept
    # additiveReference (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for additiveReference
    from spark_auto_mapper_fhir.resources.substance import Substance


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class SpecimenContainer(FhirBackboneElementBase):
    """
    Specimen.Container
        A sample to be used for analysis.
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[Extension]] = None,
        modifierExtension: Optional[FhirList[Extension]] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        description: Optional[FhirString] = None,
        type_: Optional[CodeableConcept[SpecimenContainerTypeCode]] = None,
        capacity: Optional[Quantity] = None,
        specimenQuantity: Optional[Quantity] = None,
        additiveCodeableConcept: Optional[CodeableConcept[V2_0371]] = None,
        additiveReference: Optional[Reference[Union[Substance]]] = None,
    ) -> None:
        """
            A sample to be used for analysis.

            :param id_: None
            :param extension: May be used to represent additional information that is not part of the basic
        definition of the element. To make the use of extensions safe and manageable,
        there is a strict set of governance  applied to the definition and use of
        extensions. Though any implementer can define an extension, there is a set of
        requirements that SHALL be met as part of the definition of the extension.
            :param modifierExtension: May be used to represent additional information that is not part of the basic
        definition of the element and that modifies the understanding of the element
        in which it is contained and/or the understanding of the containing element's
        descendants. Usually modifier elements provide negation or qualification. To
        make the use of extensions safe and manageable, there is a strict set of
        governance applied to the definition and use of extensions. Though any
        implementer can define an extension, there is a set of requirements that SHALL
        be met as part of the definition of the extension. Applications processing a
        resource are required to check for modifier extensions.

        Modifier extensions SHALL NOT change the meaning of any elements on Resource
        or DomainResource (including cannot change the meaning of modifierExtension
        itself).
            :param identifier: Id for container. There may be multiple; a manufacturer's bar code, lab
        assigned identifier, etc. The container ID may differ from the specimen id in
        some circumstances.
            :param description: Textual description of the container.
            :param type_: The type of container associated with the specimen (e.g. slide, aliquot,
        etc.).
            :param capacity: The capacity (volume or other measure) the container may contain.
            :param specimenQuantity: The quantity of specimen in the container; may be volume, dimensions, or other
        appropriate measurements, depending on the specimen type.
            :param additiveCodeableConcept: None
            :param additiveReference: None
        """
        super().__init__(
            id_=id_,
            extension=extension,
            modifierExtension=modifierExtension,
            identifier=identifier,
            description=description,
            type_=type_,
            capacity=capacity,
            specimenQuantity=specimenQuantity,
            additiveCodeableConcept=additiveCodeableConcept,
            additiveReference=additiveReference,
        )
