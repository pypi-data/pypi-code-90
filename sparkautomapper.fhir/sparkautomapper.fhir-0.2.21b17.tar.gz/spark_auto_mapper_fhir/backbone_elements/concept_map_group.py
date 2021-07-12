from __future__ import annotations
from typing import Optional, TYPE_CHECKING

from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)

if TYPE_CHECKING:
    pass
    # id_ (string)
    # extension (Extension)
    # modifierExtension (Extension)
    # source (uri)
    # sourceVersion (string)
    # target (uri)
    # targetVersion (string)
    # element (ConceptMap.Element)
    from spark_auto_mapper_fhir.backbone_elements.concept_map_element import (
        ConceptMapElement,
    )

    # unmapped (ConceptMap.Unmapped)
    from spark_auto_mapper_fhir.backbone_elements.concept_map_unmapped import (
        ConceptMapUnmapped,
    )


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ConceptMapGroup(FhirBackboneElementBase):
    """
    ConceptMap.Group
        A statement of relationships from one set of concepts to one or more other concepts - either concepts in code systems, or data element/data element concepts, or classes in class models.
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        modifierExtension: Optional[FhirList[ExtensionBase]] = None,
        source: Optional[FhirUri] = None,
        sourceVersion: Optional[FhirString] = None,
        target: Optional[FhirUri] = None,
        targetVersion: Optional[FhirString] = None,
        element: FhirList[ConceptMapElement],
        unmapped: Optional[ConceptMapUnmapped] = None,
    ) -> None:
        """
            A statement of relationships from one set of concepts to one or more other
        concepts - either concepts in code systems, or data element/data element
        concepts, or classes in class models.

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
            :param source: An absolute URI that identifies the source system where the concepts to be
        mapped are defined.
            :param sourceVersion: The specific version of the code system, as determined by the code system
        authority.
            :param target: An absolute URI that identifies the target system that the concepts will be
        mapped to.
            :param targetVersion: The specific version of the code system, as determined by the code system
        authority.
            :param element: Mappings for an individual concept in the source to one or more concepts in
        the target.
            :param unmapped: What to do when there is no mapping for the source concept. "Unmapped" does
        not include codes that are unmatched, and the unmapped element is ignored in a
        code is specified to have equivalence = unmatched.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            modifierExtension=modifierExtension,
            source=source,
            sourceVersion=sourceVersion,
            target=target,
            targetVersion=targetVersion,
            element=element,
            unmapped=unmapped,
        )
