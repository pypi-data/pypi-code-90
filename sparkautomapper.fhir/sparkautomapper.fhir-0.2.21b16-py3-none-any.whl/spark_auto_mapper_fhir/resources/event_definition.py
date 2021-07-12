from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.fhir_types.date import FhirDate
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.eventdefinition import EventDefinitionSchema

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
    from spark_auto_mapper_fhir.extensions.extension import Extension

    # modifierExtension (Extension)
    # url (uri)
    # identifier (Identifier)
    from spark_auto_mapper_fhir.complex_types.identifier import Identifier

    # version (string)
    # name (string)
    # title (string)
    # subtitle (string)
    # status (PublicationStatus)
    from spark_auto_mapper_fhir.value_sets.publication_status import (
        PublicationStatusCode,
    )

    # experimental (boolean)
    # subjectCodeableConcept (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for subjectCodeableConcept
    from spark_auto_mapper_fhir.value_sets.subject_type import SubjectTypeCode

    # End Import for CodeableConcept for subjectCodeableConcept
    # subjectReference (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for subjectReference
    from spark_auto_mapper_fhir.resources.group import Group

    # date (dateTime)
    # publisher (string)
    # contact (ContactDetail)
    from spark_auto_mapper_fhir.complex_types.contact_detail import ContactDetail

    # description (markdown)
    from spark_auto_mapper_fhir.fhir_types.markdown import FhirMarkdown

    # useContext (UsageContext)
    from spark_auto_mapper_fhir.complex_types.usage_context import UsageContext

    # jurisdiction (CodeableConcept)
    # Import for CodeableConcept for jurisdiction
    from spark_auto_mapper_fhir.value_sets.jurisdiction_value_set import (
        JurisdictionValueSetCode,
    )

    # End Import for CodeableConcept for jurisdiction
    # purpose (markdown)
    # usage (string)
    # copyright (markdown)
    # approvalDate (date)
    # lastReviewDate (date)
    # effectivePeriod (Period)
    from spark_auto_mapper_fhir.complex_types.period import Period

    # topic (CodeableConcept)
    # Import for CodeableConcept for topic
    from spark_auto_mapper_fhir.value_sets.definition_topic import DefinitionTopicCode

    # End Import for CodeableConcept for topic
    # author (ContactDetail)
    # editor (ContactDetail)
    # reviewer (ContactDetail)
    # endorser (ContactDetail)
    # relatedArtifact (RelatedArtifact)
    from spark_auto_mapper_fhir.complex_types.related_artifact import RelatedArtifact

    # trigger (TriggerDefinition)
    from spark_auto_mapper_fhir.complex_types.trigger_definition import (
        TriggerDefinition,
    )


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class EventDefinition(FhirResourceBase):
    """
    EventDefinition
    eventdefinition.xsd
        The EventDefinition resource provides a reusable description of when a
    particular event can occur.
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
        extension: Optional[FhirList[Extension]] = None,
        modifierExtension: Optional[FhirList[Extension]] = None,
        url: Optional[FhirUri] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        version: Optional[FhirString] = None,
        name: Optional[FhirString] = None,
        title: Optional[FhirString] = None,
        subtitle: Optional[FhirString] = None,
        status: PublicationStatusCode,
        experimental: Optional[FhirBoolean] = None,
        subjectCodeableConcept: Optional[CodeableConcept[SubjectTypeCode]] = None,
        subjectReference: Optional[Reference[Union[Group]]] = None,
        date: Optional[FhirDateTime] = None,
        publisher: Optional[FhirString] = None,
        contact: Optional[FhirList[ContactDetail]] = None,
        description: Optional[FhirMarkdown] = None,
        useContext: Optional[FhirList[UsageContext]] = None,
        jurisdiction: Optional[
            FhirList[CodeableConcept[JurisdictionValueSetCode]]
        ] = None,
        purpose: Optional[FhirMarkdown] = None,
        usage: Optional[FhirString] = None,
        copyright: Optional[FhirMarkdown] = None,
        approvalDate: Optional[FhirDate] = None,
        lastReviewDate: Optional[FhirDate] = None,
        effectivePeriod: Optional[Period] = None,
        topic: Optional[FhirList[CodeableConcept[DefinitionTopicCode]]] = None,
        author: Optional[FhirList[ContactDetail]] = None,
        editor: Optional[FhirList[ContactDetail]] = None,
        reviewer: Optional[FhirList[ContactDetail]] = None,
        endorser: Optional[FhirList[ContactDetail]] = None,
        relatedArtifact: Optional[FhirList[RelatedArtifact]] = None,
        trigger: FhirList[TriggerDefinition],
    ) -> None:
        """
            The EventDefinition resource provides a reusable description of when a
        particular event can occur.
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
            :param url: An absolute URI that is used to identify this event definition when it is
        referenced in a specification, model, design or an instance; also called its
        canonical identifier. This SHOULD be globally unique and SHOULD be a literal
        address at which at which an authoritative instance of this event definition
        is (or will be) published. This URL can be the target of a canonical
        reference. It SHALL remain the same when the event definition is stored on
        different servers.
            :param identifier: A formal identifier that is used to identify this event definition when it is
        represented in other formats, or referenced in a specification, model, design
        or an instance.
            :param version: The identifier that is used to identify this version of the event definition
        when it is referenced in a specification, model, design or instance. This is
        an arbitrary value managed by the event definition author and is not expected
        to be globally unique. For example, it might be a timestamp (e.g. yyyymmdd) if
        a managed version is not available. There is also no expectation that versions
        can be placed in a lexicographical sequence.
            :param name: A natural language name identifying the event definition. This name should be
        usable as an identifier for the module by machine processing applications such
        as code generation.
            :param title: A short, descriptive, user-friendly title for the event definition.
            :param subtitle: An explanatory or alternate title for the event definition giving additional
        information about its content.
            :param status: The status of this event definition. Enables tracking the life-cycle of the
        content.
            :param experimental: A Boolean value to indicate that this event definition is authored for testing
        purposes (or education/evaluation/marketing) and is not intended to be used
        for genuine usage.
            :param subjectCodeableConcept: None
            :param subjectReference: None
            :param date: The date  (and optionally time) when the event definition was published. The
        date must change when the business version changes and it must change if the
        status code changes. In addition, it should change when the substantive
        content of the event definition changes.
            :param publisher: The name of the organization or individual that published the event
        definition.
            :param contact: Contact details to assist a user in finding and communicating with the
        publisher.
            :param description: A free text natural language description of the event definition from a
        consumer's perspective.
            :param useContext: The content was developed with a focus and intent of supporting the contexts
        that are listed. These contexts may be general categories (gender, age, ...)
        or may be references to specific programs (insurance plans, studies, ...) and
        may be used to assist with indexing and searching for appropriate event
        definition instances.
            :param jurisdiction: A legal or geographic region in which the event definition is intended to be
        used.
            :param purpose: Explanation of why this event definition is needed and why it has been
        designed as it has.
            :param usage: A detailed description of how the event definition is used from a clinical
        perspective.
            :param copyright: A copyright statement relating to the event definition and/or its contents.
        Copyright statements are generally legal restrictions on the use and
        publishing of the event definition.
            :param approvalDate: The date on which the resource content was approved by the publisher. Approval
        happens once when the content is officially approved for usage.
            :param lastReviewDate: The date on which the resource content was last reviewed. Review happens
        periodically after approval but does not change the original approval date.
            :param effectivePeriod: The period during which the event definition content was or is planned to be
        in active use.
            :param topic: Descriptive topics related to the module. Topics provide a high-level
        categorization of the module that can be useful for filtering and searching.
            :param author: An individiual or organization primarily involved in the creation and
        maintenance of the content.
            :param editor: An individual or organization primarily responsible for internal coherence of
        the content.
            :param reviewer: An individual or organization primarily responsible for review of some aspect
        of the content.
            :param endorser: An individual or organization responsible for officially endorsing the content
        for use in some setting.
            :param relatedArtifact: Related resources such as additional documentation, justification, or
        bibliographic references.
            :param trigger: The trigger element defines when the event occurs. If more than one trigger
        condition is specified, the event fires whenever any one of the trigger
        conditions is met.
        """
        super().__init__(
            resourceType="EventDefinition",
            id_=id_,
            meta=meta,
            implicitRules=implicitRules,
            language=language,
            text=text,
            contained=contained,
            extension=extension,
            modifierExtension=modifierExtension,
            url=url,
            identifier=identifier,
            version=version,
            name=name,
            title=title,
            subtitle=subtitle,
            status=status,
            experimental=experimental,
            subjectCodeableConcept=subjectCodeableConcept,
            subjectReference=subjectReference,
            date=date,
            publisher=publisher,
            contact=contact,
            description=description,
            useContext=useContext,
            jurisdiction=jurisdiction,
            purpose=purpose,
            usage=usage,
            copyright=copyright,
            approvalDate=approvalDate,
            lastReviewDate=lastReviewDate,
            effectivePeriod=effectivePeriod,
            topic=topic,
            author=author,
            editor=editor,
            reviewer=reviewer,
            endorser=endorser,
            relatedArtifact=relatedArtifact,
            trigger=trigger,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return EventDefinitionSchema.get_schema(include_extension=include_extension)
