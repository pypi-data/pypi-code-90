from __future__ import annotations
from typing import Optional, TYPE_CHECKING

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
    # part (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # End Import for References for part
    # Import for CodeableConcept for part
    from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode

    # End Import for CodeableConcept for part
    # partLocation (CodeableConcept)
    # End Import for References for partLocation
    # Import for CodeableConcept for partLocation
    # End Import for CodeableConcept for partLocation


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class SubstanceSourceMaterialPartDescription(FhirBackboneElementBase):
    """
    SubstanceSourceMaterial.PartDescription
        Source material shall capture information on the taxonomic and anatomical origins as well as the fraction of a material that can result in or can be modified to form a substance. This set of data elements shall be used to define polymer substances isolated from biological matrices. Taxonomic and anatomical origins shall be described using a controlled vocabulary as required. This information is captured for naturally derived polymers ( . starch) and structurally diverse substances. For Organisms belonging to the Kingdom Plantae the Substance level defines the fresh material of a single species or infraspecies, the Herbal Drug and the Herbal preparation. For Herbal preparations, the fraction information will be captured at the Substance information level and additional information for herbal extracts will be captured at the Specified Substance Group 1 information level. See for further explanation the Substance Class: Structurally Diverse and the herbal annex.
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[Extension]] = None,
        modifierExtension: Optional[FhirList[Extension]] = None,
        part: Optional[CodeableConcept[GenericTypeCode]] = None,
        partLocation: Optional[CodeableConcept[GenericTypeCode]] = None,
    ) -> None:
        """
            Source material shall capture information on the taxonomic and anatomical
        origins as well as the fraction of a material that can result in or can be
        modified to form a substance. This set of data elements shall be used to
        define polymer substances isolated from biological matrices. Taxonomic and
        anatomical origins shall be described using a controlled vocabulary as
        required. This information is captured for naturally derived polymers ( .
        starch) and structurally diverse substances. For Organisms belonging to the
        Kingdom Plantae the Substance level defines the fresh material of a single
        species or infraspecies, the Herbal Drug and the Herbal preparation. For
        Herbal preparations, the fraction information will be captured at the
        Substance information level and additional information for herbal extracts
        will be captured at the Specified Substance Group 1 information level. See for
        further explanation the Substance Class: Structurally Diverse and the herbal
        annex.

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
            :param part: Entity of anatomical origin of source material within an organism.
            :param partLocation: The detailed anatomic location when the part can be extracted from different
        anatomical locations of the organism. Multiple alternative locations may
        apply.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            modifierExtension=modifierExtension,
            part=part,
            partLocation=partLocation,
        )
