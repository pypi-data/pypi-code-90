from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

from spark_auto_mapper_fhir.fhir_types.date import FhirDate
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString


from spark_auto_mapper_fhir.base_types.fhir_complex_type_base import FhirComplexTypeBase

if TYPE_CHECKING:
    pass
    # id_ (string)
    # extension (Extension)
    from spark_auto_mapper_fhir.extensions.extension import Extension

    # type_ (TriggerType)
    from spark_auto_mapper_fhir.value_sets.trigger_type import TriggerTypeCode

    # name (string)
    # timingTiming (Timing)
    from spark_auto_mapper_fhir.backbone_elements.timing import Timing

    # timingReference (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for timingReference
    from spark_auto_mapper_fhir.resources.schedule import Schedule

    # timingDate (date)
    # timingDateTime (dateTime)
    # data (DataRequirement)
    from spark_auto_mapper_fhir.complex_types.data_requirement import DataRequirement

    # condition (Expression)
    from spark_auto_mapper_fhir.complex_types.expression import Expression


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class TriggerDefinition(FhirComplexTypeBase):
    """
    TriggerDefinition
    fhir-base.xsd
        A description of a triggering event. Triggering events can be named events, data events, or periodic, as determined by the type element.
        If the element is present, it must have a value for at least one of the defined elements, an @id referenced from the Narrative, or extensions
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[Extension]] = None,
        type_: TriggerTypeCode,
        name: Optional[FhirString] = None,
        timingTiming: Optional[Timing] = None,
        timingReference: Optional[Reference[Union[Schedule]]] = None,
        timingDate: Optional[FhirDate] = None,
        timingDateTime: Optional[FhirDateTime] = None,
        data: Optional[FhirList[DataRequirement]] = None,
        condition: Optional[Expression] = None,
    ) -> None:
        """
            A description of a triggering event. Triggering events can be named events,
        data events, or periodic, as determined by the type element.
            If the element is present, it must have a value for at least one of the
        defined elements, an @id referenced from the Narrative, or extensions

            :param id_: None
            :param extension: May be used to represent additional information that is not part of the basic
        definition of the element. To make the use of extensions safe and manageable,
        there is a strict set of governance  applied to the definition and use of
        extensions. Though any implementer can define an extension, there is a set of
        requirements that SHALL be met as part of the definition of the extension.
            :param type_: The type of triggering event.
            :param name: A formal name for the event. This may be an absolute URI that identifies the
        event formally (e.g. from a trigger registry), or a simple relative URI that
        identifies the event in a local context.
            :param timingTiming: None
            :param timingReference: None
            :param timingDate: None
            :param timingDateTime: None
            :param data: The triggering data of the event (if this is a data trigger). If more than one
        data is requirement is specified, then all the data requirements must be true.
            :param condition: A boolean-valued expression that is evaluated in the context of the container
        of the trigger definition and returns whether or not the trigger fires.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            type_=type_,
            name=name,
            timingTiming=timingTiming,
            timingReference=timingReference,
            timingDate=timingDate,
            timingDateTime=timingDateTime,
            data=data,
            condition=condition,
        )
