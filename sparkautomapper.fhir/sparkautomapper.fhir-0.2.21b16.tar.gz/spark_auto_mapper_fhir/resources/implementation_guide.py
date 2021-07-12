from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.implementationguide import (
    ImplementationGuideSchema,
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
    from spark_auto_mapper_fhir.extensions.extension import Extension

    # modifierExtension (Extension)
    # url (uri)
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
    # copyright (markdown)
    # packageId (id)
    # license (SPDXLicense)
    from spark_auto_mapper_fhir.value_sets.spdx_license import SPDXLicenseCode

    # fhirVersion (FHIRVersion)
    from spark_auto_mapper_fhir.value_sets.fhir_version import FHIRVersionCode

    # dependsOn (ImplementationGuide.DependsOn)
    from spark_auto_mapper_fhir.backbone_elements.implementation_guide_depends_on import (
        ImplementationGuideDependsOn,
    )

    # global_ (ImplementationGuide.Global)
    from spark_auto_mapper_fhir.backbone_elements.implementation_guide_global import (
        ImplementationGuideGlobal,
    )

    # definition (ImplementationGuide.Definition)
    from spark_auto_mapper_fhir.backbone_elements.implementation_guide_definition import (
        ImplementationGuideDefinition,
    )

    # manifest (ImplementationGuide.Manifest)
    from spark_auto_mapper_fhir.backbone_elements.implementation_guide_manifest import (
        ImplementationGuideManifest,
    )


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ImplementationGuide(FhirResourceBase):
    """
    ImplementationGuide
    implementationguide.xsd
        A set of rules of how a particular interoperability or standards problem is
    solved - typically through the use of FHIR resources. This resource is used to
    gather all the parts of an implementation guide into a logical whole and to
    publish a computable definition of all the parts.
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
        url: FhirUri,
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
        copyright: Optional[FhirMarkdown] = None,
        packageId: FhirId,
        license: Optional[SPDXLicenseCode] = None,
        fhirVersion: FhirList[FHIRVersionCode],
        dependsOn: Optional[FhirList[ImplementationGuideDependsOn]] = None,
        global_: Optional[FhirList[ImplementationGuideGlobal]] = None,
        definition: Optional[ImplementationGuideDefinition] = None,
        manifest: Optional[ImplementationGuideManifest] = None,
    ) -> None:
        """
            A set of rules of how a particular interoperability or standards problem is
        solved - typically through the use of FHIR resources. This resource is used to
        gather all the parts of an implementation guide into a logical whole and to
        publish a computable definition of all the parts.
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
            :param url: An absolute URI that is used to identify this implementation guide when it is
        referenced in a specification, model, design or an instance; also called its
        canonical identifier. This SHOULD be globally unique and SHOULD be a literal
        address at which at which an authoritative instance of this implementation
        guide is (or will be) published. This URL can be the target of a canonical
        reference. It SHALL remain the same when the implementation guide is stored on
        different servers.
            :param version: The identifier that is used to identify this version of the implementation
        guide when it is referenced in a specification, model, design or instance.
        This is an arbitrary value managed by the implementation guide author and is
        not expected to be globally unique. For example, it might be a timestamp (e.g.
        yyyymmdd) if a managed version is not available. There is also no expectation
        that versions can be placed in a lexicographical sequence.
            :param name: A natural language name identifying the implementation guide. This name should
        be usable as an identifier for the module by machine processing applications
        such as code generation.
            :param title: A short, descriptive, user-friendly title for the implementation guide.
            :param status: The status of this implementation guide. Enables tracking the life-cycle of
        the content.
            :param experimental: A Boolean value to indicate that this implementation guide is authored for
        testing purposes (or education/evaluation/marketing) and is not intended to be
        used for genuine usage.
            :param date: The date  (and optionally time) when the implementation guide was published.
        The date must change when the business version changes and it must change if
        the status code changes. In addition, it should change when the substantive
        content of the implementation guide changes.
            :param publisher: The name of the organization or individual that published the implementation
        guide.
            :param contact: Contact details to assist a user in finding and communicating with the
        publisher.
            :param description: A free text natural language description of the implementation guide from a
        consumer's perspective.
            :param useContext: The content was developed with a focus and intent of supporting the contexts
        that are listed. These contexts may be general categories (gender, age, ...)
        or may be references to specific programs (insurance plans, studies, ...) and
        may be used to assist with indexing and searching for appropriate
        implementation guide instances.
            :param jurisdiction: A legal or geographic region in which the implementation guide is intended to
        be used.
            :param copyright: A copyright statement relating to the implementation guide and/or its
        contents. Copyright statements are generally legal restrictions on the use and
        publishing of the implementation guide.
            :param packageId: The NPM package name for this Implementation Guide, used in the NPM package
        distribution, which is the primary mechanism by which FHIR based tooling
        manages IG dependencies. This value must be globally unique, and should be
        assigned with care.
            :param license: The license that applies to this Implementation Guide, using an SPDX license
        code, or 'not-open-source'.
            :param fhirVersion: The version(s) of the FHIR specification that this ImplementationGuide targets
        - e.g. describes how to use. The value of this element is the formal version
        of the specification, without the revision number, e.g.
        [publication].[major].[minor], which is 4.0.1. for this version.
            :param dependsOn: Another implementation guide that this implementation depends on. Typically,
        an implementation guide uses value sets, profiles etc.defined in other
        implementation guides.
            :param global_: A set of profiles that all resources covered by this implementation guide must
        conform to.
            :param definition: The information needed by an IG publisher tool to publish the whole
        implementation guide.
            :param manifest: Information about an assembled implementation guide, created by the
        publication tooling.
        """
        super().__init__(
            resourceType="ImplementationGuide",
            id_=id_,
            meta=meta,
            implicitRules=implicitRules,
            language=language,
            text=text,
            contained=contained,
            extension=extension,
            modifierExtension=modifierExtension,
            url=url,
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
            copyright=copyright,
            packageId=packageId,
            license=license,
            fhirVersion=fhirVersion,
            dependsOn=dependsOn,
            global_=global_,
            definition=definition,
            manifest=manifest,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return ImplementationGuideSchema.get_schema(include_extension=include_extension)
