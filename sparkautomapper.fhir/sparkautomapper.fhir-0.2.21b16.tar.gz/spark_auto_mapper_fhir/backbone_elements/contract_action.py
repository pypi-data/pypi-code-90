from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
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
    # doNotPerform (boolean)
    # type_ (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # End Import for References for type_
    # Import for CodeableConcept for type_
    from spark_auto_mapper_fhir.value_sets.contract_action_codes import (
        ContractActionCodesCode,
    )

    # End Import for CodeableConcept for type_
    # subject (Contract.Subject)
    from spark_auto_mapper_fhir.backbone_elements.contract_subject import (
        ContractSubject,
    )

    # intent (CodeableConcept)
    # End Import for References for intent
    # Import for CodeableConcept for intent
    from spark_auto_mapper_fhir.value_sets.purpose_of_use import PurposeOfUse

    # End Import for CodeableConcept for intent
    # linkId (string)
    # status (CodeableConcept)
    # End Import for References for status
    # Import for CodeableConcept for status
    from spark_auto_mapper_fhir.value_sets.contract_resource_action_status_codes import (
        ContractResourceActionStatusCodesCode,
    )

    # End Import for CodeableConcept for status
    # context (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for context
    from spark_auto_mapper_fhir.resources.encounter import Encounter
    from spark_auto_mapper_fhir.resources.episode_of_care import EpisodeOfCare

    # contextLinkId (string)
    # occurrenceDateTime (dateTime)
    # occurrencePeriod (Period)
    from spark_auto_mapper_fhir.complex_types.period import Period

    # occurrenceTiming (Timing)
    from spark_auto_mapper_fhir.backbone_elements.timing import Timing

    # requester (Reference)
    # Imports for References for requester
    from spark_auto_mapper_fhir.resources.patient import Patient
    from spark_auto_mapper_fhir.resources.related_person import RelatedPerson
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
    from spark_auto_mapper_fhir.resources.device import Device
    from spark_auto_mapper_fhir.resources.group import Group
    from spark_auto_mapper_fhir.resources.organization import Organization

    # requesterLinkId (string)
    # performerType (CodeableConcept)
    # End Import for References for performerType
    # Import for CodeableConcept for performerType
    from spark_auto_mapper_fhir.value_sets.provenance_participant_type import (
        ProvenanceParticipantTypeCode,
    )

    # End Import for CodeableConcept for performerType
    # performerRole (CodeableConcept)
    # End Import for References for performerRole
    # Import for CodeableConcept for performerRole
    from spark_auto_mapper_fhir.value_sets.provenance_participant_role import (
        ProvenanceParticipantRoleCode,
    )

    # End Import for CodeableConcept for performerRole
    # performer (Reference)
    # Imports for References for performer
    from spark_auto_mapper_fhir.resources.care_team import CareTeam
    from spark_auto_mapper_fhir.resources.substance import Substance
    from spark_auto_mapper_fhir.resources.location import Location

    # performerLinkId (string)
    # reasonCode (CodeableConcept)
    # End Import for References for reasonCode
    # Import for CodeableConcept for reasonCode
    # End Import for CodeableConcept for reasonCode
    # reasonReference (Reference)
    # Imports for References for reasonReference
    from spark_auto_mapper_fhir.resources.condition import Condition
    from spark_auto_mapper_fhir.resources.observation import Observation
    from spark_auto_mapper_fhir.resources.diagnostic_report import DiagnosticReport
    from spark_auto_mapper_fhir.resources.document_reference import DocumentReference
    from spark_auto_mapper_fhir.resources.questionnaire import Questionnaire
    from spark_auto_mapper_fhir.resources.questionnaire_response import (
        QuestionnaireResponse,
    )

    # reason (string)
    # reasonLinkId (string)
    # note (Annotation)
    from spark_auto_mapper_fhir.complex_types.annotation import Annotation

    # securityLabelNumber (unsignedInt)
    from spark_auto_mapper_fhir.fhir_types.unsigned_int import FhirUnsignedInt


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ContractAction(FhirBackboneElementBase):
    """
    Contract.Action
        Legally enforceable, formally recorded unilateral or bilateral directive i.e., a policy or agreement.
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[Extension]] = None,
        modifierExtension: Optional[FhirList[Extension]] = None,
        doNotPerform: Optional[FhirBoolean] = None,
        type_: CodeableConcept[ContractActionCodesCode],
        subject: Optional[FhirList[ContractSubject]] = None,
        intent: CodeableConcept[PurposeOfUse],
        linkId: Optional[FhirList[FhirString]] = None,
        status: CodeableConcept[ContractResourceActionStatusCodesCode],
        context: Optional[Reference[Union[Encounter, EpisodeOfCare]]] = None,
        contextLinkId: Optional[FhirList[FhirString]] = None,
        occurrenceDateTime: Optional[FhirDateTime] = None,
        occurrencePeriod: Optional[Period] = None,
        occurrenceTiming: Optional[Timing] = None,
        requester: Optional[
            FhirList[
                Reference[
                    Union[
                        Patient,
                        RelatedPerson,
                        Practitioner,
                        PractitionerRole,
                        Device,
                        Group,
                        Organization,
                    ]
                ]
            ]
        ] = None,
        requesterLinkId: Optional[FhirList[FhirString]] = None,
        performerType: Optional[
            FhirList[CodeableConcept[ProvenanceParticipantTypeCode]]
        ] = None,
        performerRole: Optional[CodeableConcept[ProvenanceParticipantRoleCode]] = None,
        performer: Optional[
            Reference[
                Union[
                    RelatedPerson,
                    Patient,
                    Practitioner,
                    PractitionerRole,
                    CareTeam,
                    Device,
                    Substance,
                    Organization,
                    Location,
                ]
            ]
        ] = None,
        performerLinkId: Optional[FhirList[FhirString]] = None,
        reasonCode: Optional[FhirList[CodeableConcept[PurposeOfUse]]] = None,
        reasonReference: Optional[
            FhirList[
                Reference[
                    Union[
                        Condition,
                        Observation,
                        DiagnosticReport,
                        DocumentReference,
                        Questionnaire,
                        QuestionnaireResponse,
                    ]
                ]
            ]
        ] = None,
        reason: Optional[FhirList[FhirString]] = None,
        reasonLinkId: Optional[FhirList[FhirString]] = None,
        note: Optional[FhirList[Annotation]] = None,
        securityLabelNumber: Optional[FhirList[FhirUnsignedInt]] = None,
    ) -> None:
        """
            Legally enforceable, formally recorded unilateral or bilateral directive i.e.,
        a policy or agreement.

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
            :param doNotPerform: True if the term prohibits the  action.
            :param type_: Activity or service obligation to be done or not done, performed or not
        performed, effectuated or not by this Contract term.
            :param subject: Entity of the action.
            :param intent: Reason or purpose for the action stipulated by this Contract Provision.
            :param linkId: Id [identifier??] of the clause or question text related to this action in the
        referenced form or QuestionnaireResponse.
            :param status: Current state of the term action.
            :param context: Encounter or Episode with primary association to specified term activity.
            :param contextLinkId: Id [identifier??] of the clause or question text related to the requester of
        this action in the referenced form or QuestionnaireResponse.
            :param occurrenceDateTime: None
            :param occurrencePeriod: None
            :param occurrenceTiming: None
            :param requester: Who or what initiated the action and has responsibility for its activation.
            :param requesterLinkId: Id [identifier??] of the clause or question text related to the requester of
        this action in the referenced form or QuestionnaireResponse.
            :param performerType: The type of individual that is desired or required to perform or not perform
        the action.
            :param performerRole: The type of role or competency of an individual desired or required to perform
        or not perform the action.
            :param performer: Indicates who or what is being asked to perform (or not perform) the ction.
            :param performerLinkId: Id [identifier??] of the clause or question text related to the reason type or
        reference of this  action in the referenced form or QuestionnaireResponse.
            :param reasonCode: Rationale for the action to be performed or not performed. Describes why the
        action is permitted or prohibited.
            :param reasonReference: Indicates another resource whose existence justifies permitting or not
        permitting this action.
            :param reason: Describes why the action is to be performed or not performed in textual form.
            :param reasonLinkId: Id [identifier??] of the clause or question text related to the reason type or
        reference of this  action in the referenced form or QuestionnaireResponse.
            :param note: Comments made about the term action made by the requester, performer, subject
        or other participants.
            :param securityLabelNumber: Security labels that protects the action.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            modifierExtension=modifierExtension,
            doNotPerform=doNotPerform,
            type_=type_,
            subject=subject,
            intent=intent,
            linkId=linkId,
            status=status,
            context=context,
            contextLinkId=contextLinkId,
            occurrenceDateTime=occurrenceDateTime,
            occurrencePeriod=occurrencePeriod,
            occurrenceTiming=occurrenceTiming,
            requester=requester,
            requesterLinkId=requesterLinkId,
            performerType=performerType,
            performerRole=performerRole,
            performer=performer,
            performerLinkId=performerLinkId,
            reasonCode=reasonCode,
            reasonReference=reasonReference,
            reason=reason,
            reasonLinkId=reasonLinkId,
            note=note,
            securityLabelNumber=securityLabelNumber,
        )
