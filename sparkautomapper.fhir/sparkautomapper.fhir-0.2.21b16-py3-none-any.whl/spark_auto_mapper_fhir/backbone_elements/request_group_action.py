from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
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
    # prefix (string)
    # title (string)
    # description (string)
    # textEquivalent (string)
    # priority (RequestPriority)
    from spark_auto_mapper_fhir.value_sets.request_priority import RequestPriorityCode

    # code (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # End Import for References for code
    # Import for CodeableConcept for code
    from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode

    # End Import for CodeableConcept for code
    # documentation (RelatedArtifact)
    from spark_auto_mapper_fhir.complex_types.related_artifact import RelatedArtifact

    # condition (RequestGroup.Condition)
    from spark_auto_mapper_fhir.backbone_elements.request_group_condition import (
        RequestGroupCondition,
    )

    # relatedAction (RequestGroup.RelatedAction)
    from spark_auto_mapper_fhir.backbone_elements.request_group_related_action import (
        RequestGroupRelatedAction,
    )

    # timingDateTime (dateTime)
    # timingAge (Age)
    from spark_auto_mapper_fhir.complex_types.age import Age

    # timingPeriod (Period)
    from spark_auto_mapper_fhir.complex_types.period import Period

    # timingDuration (Duration)
    from spark_auto_mapper_fhir.complex_types.duration import Duration

    # timingRange (Range)
    from spark_auto_mapper_fhir.complex_types.range import Range

    # timingTiming (Timing)
    from spark_auto_mapper_fhir.backbone_elements.timing import Timing

    # participant (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for participant
    from spark_auto_mapper_fhir.resources.patient import Patient
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
    from spark_auto_mapper_fhir.resources.related_person import RelatedPerson
    from spark_auto_mapper_fhir.resources.device import Device

    # type_ (CodeableConcept)
    # End Import for References for type_
    # Import for CodeableConcept for type_
    from spark_auto_mapper_fhir.value_sets.action_type import ActionTypeCode

    # End Import for CodeableConcept for type_
    # groupingBehavior (ActionGroupingBehavior)
    from spark_auto_mapper_fhir.value_sets.action_grouping_behavior import (
        ActionGroupingBehaviorCode,
    )

    # selectionBehavior (ActionSelectionBehavior)
    from spark_auto_mapper_fhir.value_sets.action_selection_behavior import (
        ActionSelectionBehaviorCode,
    )

    # requiredBehavior (ActionRequiredBehavior)
    from spark_auto_mapper_fhir.value_sets.action_required_behavior import (
        ActionRequiredBehaviorCode,
    )

    # precheckBehavior (ActionPrecheckBehavior)
    from spark_auto_mapper_fhir.value_sets.action_precheck_behavior import (
        ActionPrecheckBehaviorCode,
    )

    # cardinalityBehavior (ActionCardinalityBehavior)
    from spark_auto_mapper_fhir.value_sets.action_cardinality_behavior import (
        ActionCardinalityBehaviorCode,
    )

    # resource (Reference)
    # Imports for References for resource


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class RequestGroupAction(FhirBackboneElementBase):
    """
    RequestGroup.Action
        A group of related requests that can be used to capture intended activities that have inter-dependencies such as "give this medication after that one".
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[Extension]] = None,
        modifierExtension: Optional[FhirList[Extension]] = None,
        prefix: Optional[FhirString] = None,
        title: Optional[FhirString] = None,
        description: Optional[FhirString] = None,
        textEquivalent: Optional[FhirString] = None,
        priority: Optional[RequestPriorityCode] = None,
        code: Optional[FhirList[CodeableConcept[GenericTypeCode]]] = None,
        documentation: Optional[FhirList[RelatedArtifact]] = None,
        condition: Optional[FhirList[RequestGroupCondition]] = None,
        relatedAction: Optional[FhirList[RequestGroupRelatedAction]] = None,
        timingDateTime: Optional[FhirDateTime] = None,
        timingAge: Optional[Age] = None,
        timingPeriod: Optional[Period] = None,
        timingDuration: Optional[Duration] = None,
        timingRange: Optional[Range] = None,
        timingTiming: Optional[Timing] = None,
        participant: Optional[
            FhirList[
                Reference[
                    Union[
                        Patient, Practitioner, PractitionerRole, RelatedPerson, Device
                    ]
                ]
            ]
        ] = None,
        type_: Optional[CodeableConcept[ActionTypeCode]] = None,
        groupingBehavior: Optional[ActionGroupingBehaviorCode] = None,
        selectionBehavior: Optional[ActionSelectionBehaviorCode] = None,
        requiredBehavior: Optional[ActionRequiredBehaviorCode] = None,
        precheckBehavior: Optional[ActionPrecheckBehaviorCode] = None,
        cardinalityBehavior: Optional[ActionCardinalityBehaviorCode] = None,
        resource: Optional[Reference[Union[Resource]]] = None,
        action: Optional[FhirList[RequestGroupAction]] = None,
    ) -> None:
        """
            A group of related requests that can be used to capture intended activities
        that have inter-dependencies such as "give this medication after that one".

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
            :param prefix: A user-visible prefix for the action.
            :param title: The title of the action displayed to a user.
            :param description: A short description of the action used to provide a summary to display to the
        user.
            :param textEquivalent: A text equivalent of the action to be performed. This provides a human-
        interpretable description of the action when the definition is consumed by a
        system that might not be capable of interpreting it dynamically.
            :param priority: Indicates how quickly the action should be addressed with respect to other
        actions.
            :param code: A code that provides meaning for the action or action group. For example, a
        section may have a LOINC code for a section of a documentation template.
            :param documentation: Didactic or other informational resources associated with the action that can
        be provided to the CDS recipient. Information resources can include inline
        text commentary and links to web resources.
            :param condition: An expression that describes applicability criteria, or start/stop conditions
        for the action.
            :param relatedAction: A relationship to another action such as "before" or "30-60 minutes after
        start of".
            :param timingDateTime: None
            :param timingAge: None
            :param timingPeriod: None
            :param timingDuration: None
            :param timingRange: None
            :param timingTiming: None
            :param participant: The participant that should perform or be responsible for this action.
            :param type_: The type of action to perform (create, update, remove).
            :param groupingBehavior: Defines the grouping behavior for the action and its children.
            :param selectionBehavior: Defines the selection behavior for the action and its children.
            :param requiredBehavior: Defines expectations around whether an action is required.
            :param precheckBehavior: Defines whether the action should usually be preselected.
            :param cardinalityBehavior: Defines whether the action can be selected multiple times.
            :param resource: The resource that is the target of the action (e.g. CommunicationRequest).
            :param action: Sub actions.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            modifierExtension=modifierExtension,
            prefix=prefix,
            title=title,
            description=description,
            textEquivalent=textEquivalent,
            priority=priority,
            code=code,
            documentation=documentation,
            condition=condition,
            relatedAction=relatedAction,
            timingDateTime=timingDateTime,
            timingAge=timingAge,
            timingPeriod=timingPeriod,
            timingDuration=timingDuration,
            timingRange=timingRange,
            timingTiming=timingTiming,
            participant=participant,
            type_=type_,
            groupingBehavior=groupingBehavior,
            selectionBehavior=selectionBehavior,
            requiredBehavior=requiredBehavior,
            precheckBehavior=precheckBehavior,
            cardinalityBehavior=cardinalityBehavior,
            resource=resource,
            action=action,
        )
