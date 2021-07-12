from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.auditevent import AuditEventSchema

if TYPE_CHECKING:
    pass
    # id_ (id)
    # meta (Meta)
    # implicitRules (uri)
    # language (CommonLanguages)
    from spark_auto_mapper_fhir.value_sets.common_languages import CommonLanguagesCode

    # text (Narrative)
    from spark_auto_mapper_fhir.complex_types.narrative import Narrative

    # contained (ResourceContainer)
    from spark_auto_mapper_fhir.complex_types.resource_container import (
        ResourceContainer,
    )

    # extension (Extension)
    # modifierExtension (Extension)
    # type_ (Coding)
    from spark_auto_mapper_fhir.complex_types.coding import Coding

    # Import for CodeableConcept for type_
    from spark_auto_mapper_fhir.value_sets.audit_event_id import AuditEventIDCode

    # End Import for CodeableConcept for type_
    # subtype (Coding)
    # Import for CodeableConcept for subtype
    from spark_auto_mapper_fhir.value_sets.audit_event_sub__type import (
        AuditEventSub_TypeCode,
    )

    # End Import for CodeableConcept for subtype
    # action (AuditEventAction)
    from spark_auto_mapper_fhir.value_sets.audit_event_action import (
        AuditEventActionCode,
    )

    # period (Period)
    from spark_auto_mapper_fhir.complex_types.period import Period

    # recorded (instant)
    from spark_auto_mapper_fhir.fhir_types.instant import FhirInstant

    # outcome (AuditEventOutcome)
    from spark_auto_mapper_fhir.value_sets.audit_event_outcome import (
        AuditEventOutcomeCode,
    )

    # outcomeDesc (string)
    # purposeOfEvent (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for purposeOfEvent
    from spark_auto_mapper_fhir.value_sets.purpose_of_use import PurposeOfUse

    # End Import for CodeableConcept for purposeOfEvent
    # agent (AuditEvent.Agent)
    from spark_auto_mapper_fhir.backbone_elements.audit_event_agent import (
        AuditEventAgent,
    )

    # source (AuditEvent.Source)
    from spark_auto_mapper_fhir.backbone_elements.audit_event_source import (
        AuditEventSource,
    )

    # entity (AuditEvent.Entity)
    from spark_auto_mapper_fhir.backbone_elements.audit_event_entity import (
        AuditEventEntity,
    )


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class AuditEvent(FhirResourceBase):
    """
    AuditEvent
    auditevent.xsd
        A record of an event made for purposes of maintaining a security log. Typical
    uses include detection of intrusion attempts and monitoring for inappropriate
    usage.
        If the element is present, it must have either a @value, an @id, or extensions
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        meta: Optional[Meta] = None,
        implicitRules: Optional[FhirUri] = None,
        language: Optional[CommonLanguagesCode] = None,
        text: Optional[Narrative] = None,
        contained: Optional[FhirList[ResourceContainer]] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        modifierExtension: Optional[FhirList[ExtensionBase]] = None,
        type_: Coding[AuditEventIDCode],
        subtype: Optional[FhirList[Coding[AuditEventSub_TypeCode]]] = None,
        action: Optional[AuditEventActionCode] = None,
        period: Optional[Period] = None,
        recorded: FhirInstant,
        outcome: Optional[AuditEventOutcomeCode] = None,
        outcomeDesc: Optional[FhirString] = None,
        purposeOfEvent: Optional[FhirList[CodeableConcept[PurposeOfUse]]] = None,
        agent: FhirList[AuditEventAgent],
        source: AuditEventSource,
        entity: Optional[FhirList[AuditEventEntity]] = None,
    ) -> None:
        """
            A record of an event made for purposes of maintaining a security log. Typical
        uses include detection of intrusion attempts and monitoring for inappropriate
        usage.
            If the element is present, it must have either a @value, an @id, or extensions

            :param id_: The logical id of the resource, as used in the URL for the resource. Once
        assigned, this value never changes.
            :param meta: The metadata about the resource. This is content that is maintained by the
        infrastructure. Changes to the content might not always be associated with
        version changes to the resource.
            :param implicitRules: A reference to a set of rules that were followed when the resource was
        constructed, and which must be understood when processing the content. Often,
        this is a reference to an implementation guide that defines the special rules
        along with other profiles etc.
            :param language: The base language in which the resource is written.
            :param text: A human-readable narrative that contains a summary of the resource and can be
        used to represent the content of the resource to a human. The narrative need
        not encode all the structured data, but is required to contain sufficient
        detail to make it "clinically safe" for a human to just read the narrative.
        Resource definitions may define what content should be represented in the
        narrative to ensure clinical safety.
            :param contained: These resources do not have an independent existence apart from the resource
        that contains them - they cannot be identified independently, and nor can they
        have their own independent transaction scope.
            :param extension: May be used to represent additional information that is not part of the basic
        definition of the resource. To make the use of extensions safe and manageable,
        there is a strict set of governance  applied to the definition and use of
        extensions. Though any implementer can define an extension, there is a set of
        requirements that SHALL be met as part of the definition of the extension.
            :param modifierExtension: May be used to represent additional information that is not part of the basic
        definition of the resource and that modifies the understanding of the element
        that contains it and/or the understanding of the containing element's
        descendants. Usually modifier elements provide negation or qualification. To
        make the use of extensions safe and manageable, there is a strict set of
        governance applied to the definition and use of extensions. Though any
        implementer is allowed to define an extension, there is a set of requirements
        that SHALL be met as part of the definition of the extension. Applications
        processing a resource are required to check for modifier extensions.

        Modifier extensions SHALL NOT change the meaning of any elements on Resource
        or DomainResource (including cannot change the meaning of modifierExtension
        itself).
            :param type_: Identifier for a family of the event.  For example, a menu item, program,
        rule, policy, function code, application name or URL. It identifies the
        performed function.
            :param subtype: Identifier for the category of event.
            :param action: Indicator for type of action performed during the event that generated the
        audit.
            :param period: The period during which the activity occurred.
            :param recorded: The time when the event was recorded.
            :param outcome: Indicates whether the event succeeded or failed.
            :param outcomeDesc: A free text description of the outcome of the event.
            :param purposeOfEvent: The purposeOfUse (reason) that was used during the event being recorded.
            :param agent: An actor taking an active role in the event or activity that is logged.
            :param source: The system that is reporting the event.
            :param entity: Specific instances of data or objects that have been accessed.
        """
        super().__init__(
            resourceType="AuditEvent",
            id_=id_,
            meta=meta,
            implicitRules=implicitRules,
            language=language,
            text=text,
            contained=contained,
            extension=extension,
            modifierExtension=modifierExtension,
            type_=type_,
            subtype=subtype,
            action=action,
            period=period,
            recorded=recorded,
            outcome=outcome,
            outcomeDesc=outcomeDesc,
            purposeOfEvent=purposeOfEvent,
            agent=agent,
            source=source,
            entity=entity,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return AuditEventSchema.get_schema(include_extension=include_extension)
