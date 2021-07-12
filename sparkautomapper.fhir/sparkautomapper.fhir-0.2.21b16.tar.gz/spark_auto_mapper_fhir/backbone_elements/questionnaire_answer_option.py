from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.fhir_types.date import FhirDate
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.integer import FhirInteger
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.resources.resource import Resource

from spark_auto_mapper_fhir.base_types.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)

if TYPE_CHECKING:
    pass
    # id_ (string)
    # extension (Extension)
    from spark_auto_mapper_fhir.extensions.extension import Extension

    # modifierExtension (Extension)
    # valueInteger (integer)
    # valueDate (date)
    # valueTime (time)
    from spark_auto_mapper_fhir.fhir_types.time import FhirTime

    # valueString (string)
    # valueCoding (Coding)
    from spark_auto_mapper_fhir.complex_types.coding import Coding

    # End Import for References for valueCoding
    # Import for CodeableConcept for valueCoding
    from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode

    # End Import for CodeableConcept for valueCoding
    # valueReference (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for valueReference
    # initialSelected (boolean)


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class QuestionnaireAnswerOption(FhirBackboneElementBase):
    """
    Questionnaire.AnswerOption
        A structured set of questions intended to guide the collection of answers from end-users. Questionnaires provide detailed control over order, presentation, phraseology and grouping to allow coherent, consistent data collection.
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[Extension]] = None,
        modifierExtension: Optional[FhirList[Extension]] = None,
        valueInteger: Optional[FhirInteger] = None,
        valueDate: Optional[FhirDate] = None,
        valueTime: Optional[FhirTime] = None,
        valueString: Optional[FhirString] = None,
        valueCoding: Optional[Coding[GenericTypeCode]] = None,
        valueReference: Optional[Reference[Union[Resource]]] = None,
        initialSelected: Optional[FhirBoolean] = None,
    ) -> None:
        """
            A structured set of questions intended to guide the collection of answers from
        end-users. Questionnaires provide detailed control over order, presentation,
        phraseology and grouping to allow coherent, consistent data collection.

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
            :param valueInteger: None
            :param valueDate: None
            :param valueTime: None
            :param valueString: None
            :param valueCoding: None
            :param valueReference: None
            :param initialSelected: Indicates whether the answer value is selected when the list of possible
        answers is initially shown.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            modifierExtension=modifierExtension,
            valueInteger=valueInteger,
            valueDate=valueDate,
            valueTime=valueTime,
            valueString=valueString,
            valueCoding=valueCoding,
            valueReference=valueReference,
            initialSelected=initialSelected,
        )
