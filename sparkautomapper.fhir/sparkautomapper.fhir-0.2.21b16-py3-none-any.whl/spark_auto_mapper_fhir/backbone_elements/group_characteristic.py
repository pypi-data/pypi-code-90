from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.fhir_types.list import FhirList
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
    # code (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # End Import for References for code
    # Import for CodeableConcept for code
    from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode

    # End Import for CodeableConcept for code
    # valueCodeableConcept (CodeableConcept)
    # End Import for References for valueCodeableConcept
    # Import for CodeableConcept for valueCodeableConcept
    # End Import for CodeableConcept for valueCodeableConcept
    # valueBoolean (boolean)
    # valueQuantity (Quantity)
    from spark_auto_mapper_fhir.complex_types.quantity import Quantity

    # valueRange (Range)
    from spark_auto_mapper_fhir.complex_types.range import Range

    # valueReference (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for valueReference
    # exclude (boolean)
    # period (Period)
    from spark_auto_mapper_fhir.complex_types.period import Period


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class GroupCharacteristic(FhirBackboneElementBase):
    """
    Group.Characteristic
        Represents a defined collection of entities that may be discussed or acted upon collectively but which are not expected to act collectively, and are not formally or legally recognized; i.e. a collection of entities that isn't an Organization.
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[Extension]] = None,
        modifierExtension: Optional[FhirList[Extension]] = None,
        code: CodeableConcept[GenericTypeCode],
        valueCodeableConcept: Optional[CodeableConcept[GenericTypeCode]] = None,
        valueBoolean: Optional[FhirBoolean] = None,
        valueQuantity: Optional[Quantity] = None,
        valueRange: Optional[Range] = None,
        valueReference: Optional[Reference[Union[Resource]]] = None,
        exclude: FhirBoolean,
        period: Optional[Period] = None,
    ) -> None:
        """
            Represents a defined collection of entities that may be discussed or acted
        upon collectively but which are not expected to act collectively, and are not
        formally or legally recognized; i.e. a collection of entities that isn't an
        Organization.

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
            :param code: A code that identifies the kind of trait being asserted.
            :param valueCodeableConcept: None
            :param valueBoolean: None
            :param valueQuantity: None
            :param valueRange: None
            :param valueReference: None
            :param exclude: If true, indicates the characteristic is one that is NOT held by members of
        the group.
            :param period: The period over which the characteristic is tested; e.g. the patient had an
        operation during the month of June.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            modifierExtension=modifierExtension,
            code=code,
            valueCodeableConcept=valueCodeableConcept,
            valueBoolean=valueBoolean,
            valueQuantity=valueQuantity,
            valueRange=valueRange,
            valueReference=valueReference,
            exclude=exclude,
            period=period,
        )
