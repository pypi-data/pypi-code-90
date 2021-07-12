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
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.library import LibrarySchema

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
    # type_ (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for type_
    from spark_auto_mapper_fhir.value_sets.library_type import LibraryTypeCode

    # End Import for CodeableConcept for type_
    # subjectCodeableConcept (CodeableConcept)
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

    # parameter (ParameterDefinition)
    from spark_auto_mapper_fhir.complex_types.parameter_definition import (
        ParameterDefinition,
    )

    # dataRequirement (DataRequirement)
    from spark_auto_mapper_fhir.complex_types.data_requirement import DataRequirement

    # content (Attachment)
    from spark_auto_mapper_fhir.complex_types.attachment import Attachment


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class Library(FhirResourceBase):
    """
    Library
    library.xsd
        The Library resource is a general-purpose container for knowledge asset
    definitions. It can be used to describe and expose existing knowledge assets
    such as logic libraries and information model descriptions, as well as to
    describe a collection of knowledge assets.
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
        url: Optional[FhirUri] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        version: Optional[FhirString] = None,
        name: Optional[FhirString] = None,
        title: Optional[FhirString] = None,
        subtitle: Optional[FhirString] = None,
        status: PublicationStatusCode,
        experimental: Optional[FhirBoolean] = None,
        type_: CodeableConcept[LibraryTypeCode],
        subjectCodeableConcept: Optional[CodeableConcept[SubjectTypeCode]] = None,
        subjectReference: Optional[Reference[Group]] = None,
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
        parameter: Optional[FhirList[ParameterDefinition]] = None,
        dataRequirement: Optional[FhirList[DataRequirement]] = None,
        content: Optional[FhirList[Attachment]] = None,
    ) -> None:
        """
            The Library resource is a general-purpose container for knowledge asset
        definitions. It can be used to describe and expose existing knowledge assets
        such as logic libraries and information model descriptions, as well as to
        describe a collection of knowledge assets.
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
            :param url: An absolute URI that is used to identify this library when it is referenced in
        a specification, model, design or an instance; also called its canonical
        identifier. This SHOULD be globally unique and SHOULD be a literal address at
        which at which an authoritative instance of this library is (or will be)
        published. This URL can be the target of a canonical reference. It SHALL
        remain the same when the library is stored on different servers.
            :param identifier: A formal identifier that is used to identify this library when it is
        represented in other formats, or referenced in a specification, model, design
        or an instance. e.g. CMS or NQF identifiers for a measure artifact. Note that
        at least one identifier is required for non-experimental active artifacts.
            :param version: The identifier that is used to identify this version of the library when it is
        referenced in a specification, model, design or instance. This is an arbitrary
        value managed by the library author and is not expected to be globally unique.
        For example, it might be a timestamp (e.g. yyyymmdd) if a managed version is
        not available. There is also no expectation that versions can be placed in a
        lexicographical sequence. To provide a version consistent with the Decision
        Support Service specification, use the format Major.Minor.Revision (e.g.
        1.0.0). For more information on versioning knowledge assets, refer to the
        Decision Support Service specification. Note that a version is required for
        non-experimental active artifacts.
            :param name: A natural language name identifying the library. This name should be usable as
        an identifier for the module by machine processing applications such as code
        generation.
            :param title: A short, descriptive, user-friendly title for the library.
            :param subtitle: An explanatory or alternate title for the library giving additional
        information about its content.
            :param status: The status of this library. Enables tracking the life-cycle of the content.
            :param experimental: A Boolean value to indicate that this library is authored for testing purposes
        (or education/evaluation/marketing) and is not intended to be used for genuine
        usage.
            :param type_: Identifies the type of library such as a Logic Library, Model Definition,
        Asset Collection, or Module Definition.
            :param subjectCodeableConcept: None
            :param subjectReference: None
            :param date: The date  (and optionally time) when the library was published. The date must
        change when the business version changes and it must change if the status code
        changes. In addition, it should change when the substantive content of the
        library changes.
            :param publisher: The name of the organization or individual that published the library.
            :param contact: Contact details to assist a user in finding and communicating with the
        publisher.
            :param description: A free text natural language description of the library from a consumer's
        perspective.
            :param useContext: The content was developed with a focus and intent of supporting the contexts
        that are listed. These contexts may be general categories (gender, age, ...)
        or may be references to specific programs (insurance plans, studies, ...) and
        may be used to assist with indexing and searching for appropriate library
        instances.
            :param jurisdiction: A legal or geographic region in which the library is intended to be used.
            :param purpose: Explanation of why this library is needed and why it has been designed as it
        has.
            :param usage: A detailed description of how the library is used from a clinical perspective.
            :param copyright: A copyright statement relating to the library and/or its contents. Copyright
        statements are generally legal restrictions on the use and publishing of the
        library.
            :param approvalDate: The date on which the resource content was approved by the publisher. Approval
        happens once when the content is officially approved for usage.
            :param lastReviewDate: The date on which the resource content was last reviewed. Review happens
        periodically after approval but does not change the original approval date.
            :param effectivePeriod: The period during which the library content was or is planned to be in active
        use.
            :param topic: Descriptive topics related to the content of the library. Topics provide a
        high-level categorization of the library that can be useful for filtering and
        searching.
            :param author: An individiual or organization primarily involved in the creation and
        maintenance of the content.
            :param editor: An individual or organization primarily responsible for internal coherence of
        the content.
            :param reviewer: An individual or organization primarily responsible for review of some aspect
        of the content.
            :param endorser: An individual or organization responsible for officially endorsing the content
        for use in some setting.
            :param relatedArtifact: Related artifacts such as additional documentation, justification, or
        bibliographic references.
            :param parameter: The parameter element defines parameters used by the library.
            :param dataRequirement: Describes a set of data that must be provided in order to be able to
        successfully perform the computations defined by the library.
            :param content: The content of the library as an Attachment. The content may be a reference to
        a url, or may be directly embedded as a base-64 string. Either way, the
        contentType of the attachment determines how to interpret the content.
        """
        super().__init__(
            resourceType="Library",
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
            type_=type_,
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
            parameter=parameter,
            dataRequirement=dataRequirement,
            content=content,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return LibrarySchema.get_schema(include_extension=include_extension)
