from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.fhir_types.date import FhirDate
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.integer import FhirInteger
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.resources.resource import Resource
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)

if TYPE_CHECKING:
    pass
    # id_ (string)
    # extension (Extension)
    from spark_auto_mapper_fhir.extensions.extension import Extension

    # modifierExtension (Extension)
    # valueBoolean (boolean)
    # valueDecimal (decimal)
    from spark_auto_mapper_fhir.fhir_types.decimal import FhirDecimal

    # valueInteger (integer)
    # valueDate (date)
    # valueDateTime (dateTime)
    # valueTime (time)
    from spark_auto_mapper_fhir.fhir_types.time import FhirTime

    # valueString (string)
    # valueUri (uri)
    # valueAttachment (Attachment)
    from spark_auto_mapper_fhir.complex_types.attachment import Attachment

    # valueCoding (Coding)
    from spark_auto_mapper_fhir.complex_types.coding import Coding

    # End Import for References for valueCoding
    # Import for CodeableConcept for valueCoding
    from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode

    # End Import for CodeableConcept for valueCoding
    # valueQuantity (Quantity)
    from spark_auto_mapper_fhir.complex_types.quantity import Quantity

    # valueReference (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for valueReference
    # item (QuestionnaireResponse.Item)
    from spark_auto_mapper_fhir.backbone_elements.questionnaire_response_item import (
        QuestionnaireResponseItem,
    )


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class QuestionnaireResponseAnswer(FhirBackboneElementBase):
    """
    QuestionnaireResponse.Answer
        A structured set of questions and their answers. The questions are ordered and grouped into coherent subsets, corresponding to the structure of the grouping of the questionnaire being responded to.
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[Extension]] = None,
        modifierExtension: Optional[FhirList[Extension]] = None,
        valueBoolean: Optional[FhirBoolean] = None,
        valueDecimal: Optional[FhirDecimal] = None,
        valueInteger: Optional[FhirInteger] = None,
        valueDate: Optional[FhirDate] = None,
        valueDateTime: Optional[FhirDateTime] = None,
        valueTime: Optional[FhirTime] = None,
        valueString: Optional[FhirString] = None,
        valueUri: Optional[FhirUri] = None,
        valueAttachment: Optional[Attachment] = None,
        valueCoding: Optional[Coding[GenericTypeCode]] = None,
        valueQuantity: Optional[Quantity] = None,
        valueReference: Optional[Reference[Union[Resource]]] = None,
        item: Optional[FhirList[QuestionnaireResponseItem]] = None,
    ) -> None:
        """
            A structured set of questions and their answers. The questions are ordered and
        grouped into coherent subsets, corresponding to the structure of the grouping
        of the questionnaire being responded to.

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
            :param valueBoolean: None
            :param valueDecimal: None
            :param valueInteger: None
            :param valueDate: None
            :param valueDateTime: None
            :param valueTime: None
            :param valueString: None
            :param valueUri: None
            :param valueAttachment: None
            :param valueCoding: None
            :param valueQuantity: None
            :param valueReference: None
            :param item: Nested groups and/or questions found within this particular answer.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            modifierExtension=modifierExtension,
            valueBoolean=valueBoolean,
            valueDecimal=valueDecimal,
            valueInteger=valueInteger,
            valueDate=valueDate,
            valueDateTime=valueDateTime,
            valueTime=valueTime,
            valueString=valueString,
            valueUri=valueUri,
            valueAttachment=valueAttachment,
            valueCoding=valueCoding,
            valueQuantity=valueQuantity,
            valueReference=valueReference,
            item=item,
        )
