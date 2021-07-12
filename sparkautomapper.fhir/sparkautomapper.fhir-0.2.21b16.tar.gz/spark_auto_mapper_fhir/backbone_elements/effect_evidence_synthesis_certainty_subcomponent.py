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
    # type_ (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # End Import for References for type_
    # Import for CodeableConcept for type_
    from spark_auto_mapper_fhir.value_sets.certainty_subcomponent_type import (
        CertaintySubcomponentTypeCode,
    )

    # End Import for CodeableConcept for type_
    # rating (CodeableConcept)
    # End Import for References for rating
    # Import for CodeableConcept for rating
    from spark_auto_mapper_fhir.value_sets.certainty_subcomponent_rating import (
        CertaintySubcomponentRatingCode,
    )

    # End Import for CodeableConcept for rating
    # note (Annotation)
    from spark_auto_mapper_fhir.complex_types.annotation import Annotation


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class EffectEvidenceSynthesisCertaintySubcomponent(FhirBackboneElementBase):
    """
    EffectEvidenceSynthesis.CertaintySubcomponent
        The EffectEvidenceSynthesis resource describes the difference in an outcome between exposures states in a population where the effect estimate is derived from a combination of research studies.
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[Extension]] = None,
        modifierExtension: Optional[FhirList[Extension]] = None,
        type_: Optional[CodeableConcept[CertaintySubcomponentTypeCode]] = None,
        rating: Optional[
            FhirList[CodeableConcept[CertaintySubcomponentRatingCode]]
        ] = None,
        note: Optional[FhirList[Annotation]] = None,
    ) -> None:
        """
            The EffectEvidenceSynthesis resource describes the difference in an outcome
        between exposures states in a population where the effect estimate is derived
        from a combination of research studies.

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
            :param type_: Type of subcomponent of certainty rating.
            :param rating: A rating of a subcomponent of rating certainty.
            :param note: A human-readable string to clarify or explain concepts about the resource.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            modifierExtension=modifierExtension,
            type_=type_,
            rating=rating,
            note=note,
        )
