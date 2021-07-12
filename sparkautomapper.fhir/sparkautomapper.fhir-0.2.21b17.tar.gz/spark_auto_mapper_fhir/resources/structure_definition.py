from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.structuredefinition import (
    StructureDefinitionSchema,
)

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
    # status (PublicationStatus)
    from spark_auto_mapper_fhir.value_sets.publication_status import (
        PublicationStatusCode,
    )

    # experimental (boolean)
    # date (dateTime)
    # publisher (string)
    # contact (ContactDetail)
    from spark_auto_mapper_fhir.complex_types.contact_detail import ContactDetail

    # description (markdown)
    from spark_auto_mapper_fhir.fhir_types.markdown import FhirMarkdown

    # useContext (UsageContext)
    from spark_auto_mapper_fhir.complex_types.usage_context import UsageContext

    # jurisdiction (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for jurisdiction
    from spark_auto_mapper_fhir.value_sets.jurisdiction_value_set import (
        JurisdictionValueSetCode,
    )

    # End Import for CodeableConcept for jurisdiction
    # purpose (markdown)
    # copyright (markdown)
    # keyword (Coding)
    from spark_auto_mapper_fhir.complex_types.coding import Coding

    # Import for CodeableConcept for keyword
    from spark_auto_mapper_fhir.value_sets.definition_use_codes import (
        DefinitionUseCodesCode,
    )

    # End Import for CodeableConcept for keyword
    # fhirVersion (FHIRVersion)
    from spark_auto_mapper_fhir.value_sets.fhir_version import FHIRVersionCode

    # mapping (StructureDefinition.Mapping)
    from spark_auto_mapper_fhir.backbone_elements.structure_definition_mapping import (
        StructureDefinitionMapping,
    )

    # kind (StructureDefinitionKind)
    from spark_auto_mapper_fhir.value_sets.structure_definition_kind import (
        StructureDefinitionKindCode,
    )

    # abstract (boolean)
    # context (StructureDefinition.Context)
    from spark_auto_mapper_fhir.backbone_elements.structure_definition_context import (
        StructureDefinitionContext,
    )

    # contextInvariant (string)
    # type_ (uri)
    # baseDefinition (canonical)
    from spark_auto_mapper_fhir.fhir_types.canonical import FhirCanonical

    # derivation (TypeDerivationRule)
    from spark_auto_mapper_fhir.value_sets.type_derivation_rule import (
        TypeDerivationRuleCode,
    )

    # snapshot (StructureDefinition.Snapshot)
    from spark_auto_mapper_fhir.backbone_elements.structure_definition_snapshot import (
        StructureDefinitionSnapshot,
    )

    # differential (StructureDefinition.Differential)
    from spark_auto_mapper_fhir.backbone_elements.structure_definition_differential import (
        StructureDefinitionDifferential,
    )


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class StructureDefinition(FhirResourceBase):
    """
    StructureDefinition
    structuredefinition.xsd
        A definition of a FHIR structure. This resource is used to describe the
    underlying resources, data types defined in FHIR, and also for describing
    extensions and constraints on resources and data types.
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
        url: FhirUri,
        identifier: Optional[FhirList[Identifier]] = None,
        version: Optional[FhirString] = None,
        name: FhirString,
        title: Optional[FhirString] = None,
        status: PublicationStatusCode,
        experimental: Optional[FhirBoolean] = None,
        date: Optional[FhirDateTime] = None,
        publisher: Optional[FhirString] = None,
        contact: Optional[FhirList[ContactDetail]] = None,
        description: Optional[FhirMarkdown] = None,
        useContext: Optional[FhirList[UsageContext]] = None,
        jurisdiction: Optional[
            FhirList[CodeableConcept[JurisdictionValueSetCode]]
        ] = None,
        purpose: Optional[FhirMarkdown] = None,
        copyright: Optional[FhirMarkdown] = None,
        keyword: Optional[FhirList[Coding[DefinitionUseCodesCode]]] = None,
        fhirVersion: Optional[FHIRVersionCode] = None,
        mapping: Optional[FhirList[StructureDefinitionMapping]] = None,
        kind: StructureDefinitionKindCode,
        abstract: FhirBoolean,
        context: Optional[FhirList[StructureDefinitionContext]] = None,
        contextInvariant: Optional[FhirList[FhirString]] = None,
        type_: FhirUri,
        baseDefinition: Optional[FhirCanonical] = None,
        derivation: Optional[TypeDerivationRuleCode] = None,
        snapshot: Optional[StructureDefinitionSnapshot] = None,
        differential: Optional[StructureDefinitionDifferential] = None,
    ) -> None:
        """
            A definition of a FHIR structure. This resource is used to describe the
        underlying resources, data types defined in FHIR, and also for describing
        extensions and constraints on resources and data types.
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
            :param url: An absolute URI that is used to identify this structure definition when it is
        referenced in a specification, model, design or an instance; also called its
        canonical identifier. This SHOULD be globally unique and SHOULD be a literal
        address at which at which an authoritative instance of this structure
        definition is (or will be) published. This URL can be the target of a
        canonical reference. It SHALL remain the same when the structure definition is
        stored on different servers.
            :param identifier: A formal identifier that is used to identify this structure definition when it
        is represented in other formats, or referenced in a specification, model,
        design or an instance.
            :param version: The identifier that is used to identify this version of the structure
        definition when it is referenced in a specification, model, design or
        instance. This is an arbitrary value managed by the structure definition
        author and is not expected to be globally unique. For example, it might be a
        timestamp (e.g. yyyymmdd) if a managed version is not available. There is also
        no expectation that versions can be placed in a lexicographical sequence.
            :param name: A natural language name identifying the structure definition. This name should
        be usable as an identifier for the module by machine processing applications
        such as code generation.
            :param title: A short, descriptive, user-friendly title for the structure definition.
            :param status: The status of this structure definition. Enables tracking the life-cycle of
        the content.
            :param experimental: A Boolean value to indicate that this structure definition is authored for
        testing purposes (or education/evaluation/marketing) and is not intended to be
        used for genuine usage.
            :param date: The date  (and optionally time) when the structure definition was published.
        The date must change when the business version changes and it must change if
        the status code changes. In addition, it should change when the substantive
        content of the structure definition changes.
            :param publisher: The name of the organization or individual that published the structure
        definition.
            :param contact: Contact details to assist a user in finding and communicating with the
        publisher.
            :param description: A free text natural language description of the structure definition from a
        consumer's perspective.
            :param useContext: The content was developed with a focus and intent of supporting the contexts
        that are listed. These contexts may be general categories (gender, age, ...)
        or may be references to specific programs (insurance plans, studies, ...) and
        may be used to assist with indexing and searching for appropriate structure
        definition instances.
            :param jurisdiction: A legal or geographic region in which the structure definition is intended to
        be used.
            :param purpose: Explanation of why this structure definition is needed and why it has been
        designed as it has.
            :param copyright: A copyright statement relating to the structure definition and/or its
        contents. Copyright statements are generally legal restrictions on the use and
        publishing of the structure definition.
            :param keyword: A set of key words or terms from external terminologies that may be used to
        assist with indexing and searching of templates nby describing the use of this
        structure definition, or the content it describes.
            :param fhirVersion: The version of the FHIR specification on which this StructureDefinition is
        based - this is the formal version of the specification, without the revision
        number, e.g. [publication].[major].[minor], which is 4.0.1. for this version.
            :param mapping: An external specification that the content is mapped to.
            :param kind: Defines the kind of structure that this definition is describing.
            :param abstract: Whether structure this definition describes is abstract or not  - that is,
        whether the structure is not intended to be instantiated. For Resources and
        Data types, abstract types will never be exchanged  between systems.
            :param context: Identifies the types of resource or data type elements to which the extension
        can be applied.
            :param contextInvariant: A set of rules as FHIRPath Invariants about when the extension can be used
        (e.g. co-occurrence variants for the extension). All the rules must be true.
            :param type_: The type this structure describes. If the derivation kind is 'specialization'
        then this is the master definition for a type, and there is always one of
        these (a data type, an extension, a resource, including abstract ones).
        Otherwise the structure definition is a constraint on the stated type (and in
        this case, the type cannot be an abstract type).  References are URLs that are
        relative to http://hl7.org/fhir/StructureDefinition e.g. "string" is a
        reference to http://hl7.org/fhir/StructureDefinition/string. Absolute URLs are
        only allowed in logical models.
            :param baseDefinition: An absolute URI that is the base structure from which this type is derived,
        either by specialization or constraint.
            :param derivation: How the type relates to the baseDefinition.
            :param snapshot: A snapshot view is expressed in a standalone form that can be used and
        interpreted without considering the base StructureDefinition.
            :param differential: A differential view is expressed relative to the base StructureDefinition - a
        statement of differences that it applies.
        """
        super().__init__(
            resourceType="StructureDefinition",
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
            status=status,
            experimental=experimental,
            date=date,
            publisher=publisher,
            contact=contact,
            description=description,
            useContext=useContext,
            jurisdiction=jurisdiction,
            purpose=purpose,
            copyright=copyright,
            keyword=keyword,
            fhirVersion=fhirVersion,
            mapping=mapping,
            kind=kind,
            abstract=abstract,
            context=context,
            contextInvariant=contextInvariant,
            type_=type_,
            baseDefinition=baseDefinition,
            derivation=derivation,
            snapshot=snapshot,
            differential=differential,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return StructureDefinitionSchema.get_schema(include_extension=include_extension)
