from __future__ import annotations
from typing import Optional, TYPE_CHECKING

from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
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
    # isDerived (boolean)
    # type_ (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # End Import for References for type_
    # Import for CodeableConcept for type_
    from spark_auto_mapper_fhir.value_sets.v2_0487 import V2_0487

    # End Import for CodeableConcept for type_
    # preference (SpecimenContainedPreference)
    from spark_auto_mapper_fhir.value_sets.specimen_contained_preference import (
        SpecimenContainedPreferenceCode,
    )

    # container (SpecimenDefinition.Container)
    from spark_auto_mapper_fhir.backbone_elements.specimen_definition_container import (
        SpecimenDefinitionContainer,
    )

    # requirement (string)
    # retentionTime (Duration)
    from spark_auto_mapper_fhir.complex_types.duration import Duration

    # rejectionCriterion (CodeableConcept)
    # End Import for References for rejectionCriterion
    # Import for CodeableConcept for rejectionCriterion
    from spark_auto_mapper_fhir.value_sets.rejection_criterion import (
        RejectionCriterionCode,
    )

    # End Import for CodeableConcept for rejectionCriterion
    # handling (SpecimenDefinition.Handling)
    from spark_auto_mapper_fhir.backbone_elements.specimen_definition_handling import (
        SpecimenDefinitionHandling,
    )


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class SpecimenDefinitionTypeTested(FhirBackboneElementBase):
    """
    SpecimenDefinition.TypeTested
        A kind of specimen with associated set of requirements.
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[Extension]] = None,
        modifierExtension: Optional[FhirList[Extension]] = None,
        isDerived: Optional[FhirBoolean] = None,
        type_: Optional[CodeableConcept[V2_0487]] = None,
        preference: SpecimenContainedPreferenceCode,
        container: Optional[SpecimenDefinitionContainer] = None,
        requirement: Optional[FhirString] = None,
        retentionTime: Optional[Duration] = None,
        rejectionCriterion: Optional[
            FhirList[CodeableConcept[RejectionCriterionCode]]
        ] = None,
        handling: Optional[FhirList[SpecimenDefinitionHandling]] = None,
    ) -> None:
        """
            A kind of specimen with associated set of requirements.

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
            :param isDerived: Primary of secondary specimen.
            :param type_: The kind of specimen conditioned for testing expected by lab.
            :param preference: The preference for this type of conditioned specimen.
            :param container: The specimen's container.
            :param requirement: Requirements for delivery and special handling of this kind of conditioned
        specimen.
            :param retentionTime: The usual time that a specimen of this kind is retained after the ordered
        tests are completed, for the purpose of additional testing.
            :param rejectionCriterion: Criterion for rejection of the specimen in its container by the laboratory.
            :param handling: Set of instructions for preservation/transport of the specimen at a defined
        temperature interval, prior the testing process.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            modifierExtension=modifierExtension,
            isDerived=isDerived,
            type_=type_,
            preference=preference,
            container=container,
            requirement=requirement,
            retentionTime=retentionTime,
            rejectionCriterion=rejectionCriterion,
            handling=handling,
        )
