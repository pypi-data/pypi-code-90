from __future__ import annotations
from typing import Optional, TYPE_CHECKING

from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase

from spark_auto_mapper_fhir.base_types.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)

if TYPE_CHECKING:
    pass
    # id_ (string)
    # extension (Extension)
    # modifierExtension (Extension)
    # number (positiveInt)
    from spark_auto_mapper_fhir.fhir_types.positive_int import FhirPositiveInt

    # type_ (NoteType)
    from spark_auto_mapper_fhir.value_sets.note_type import NoteTypeCode

    # text (string)
    # language (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # End Import for References for language
    # Import for CodeableConcept for language
    from spark_auto_mapper_fhir.value_sets.common_languages import CommonLanguagesCode

    # End Import for CodeableConcept for language


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ExplanationOfBenefitProcessNote(FhirBackboneElementBase):
    """
    ExplanationOfBenefit.ProcessNote
        This resource provides: the claim details; adjudication details from the processing of a Claim; and optionally account balance information, for informing the subscriber of the benefits provided.
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        modifierExtension: Optional[FhirList[ExtensionBase]] = None,
        number: Optional[FhirPositiveInt] = None,
        type_: Optional[NoteTypeCode] = None,
        text: Optional[FhirString] = None,
        language: Optional[CodeableConcept[CommonLanguagesCode]] = None,
    ) -> None:
        """
            This resource provides: the claim details; adjudication details from the
        processing of a Claim; and optionally account balance information, for
        informing the subscriber of the benefits provided.

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
            :param number: A number to uniquely identify a note entry.
            :param type_: The business purpose of the note text.
            :param text: The explanation or description associated with the processing.
            :param language: A code to define the language used in the text of the note.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            modifierExtension=modifierExtension,
            number=number,
            type_=type_,
            text=text,
            language=language,
        )
