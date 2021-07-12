from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.organization import OrganizationSchema

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
    # identifier (Identifier)
    from spark_auto_mapper_fhir.complex_types.identifier import Identifier

    # active (boolean)
    # type_ (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for type_
    from spark_auto_mapper_fhir.value_sets.organization_type import OrganizationTypeCode

    # End Import for CodeableConcept for type_
    # name (string)
    # alias (string)
    # telecom (ContactPoint)
    from spark_auto_mapper_fhir.complex_types.contact_point import ContactPoint

    # address (Address)
    from spark_auto_mapper_fhir.complex_types.address import Address

    # partOf (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for partOf
    # contact (Organization.Contact)
    from spark_auto_mapper_fhir.backbone_elements.organization_contact import (
        OrganizationContact,
    )

    # endpoint (Reference)
    # Imports for References for endpoint
    from spark_auto_mapper_fhir.resources.endpoint import Endpoint


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class Organization(FhirResourceBase):
    """
    Organization
    organization.xsd
        A formally or informally recognized grouping of people or organizations formed
    for the purpose of achieving some form of collective action.  Includes
    companies, institutions, corporations, departments, community groups,
    healthcare practice groups, payer/insurer, etc.
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
        identifier: Optional[FhirList[Identifier]] = None,
        active: Optional[FhirBoolean] = None,
        type_: Optional[FhirList[CodeableConcept[OrganizationTypeCode]]] = None,
        name: Optional[FhirString] = None,
        alias: Optional[FhirList[FhirString]] = None,
        telecom: Optional[FhirList[ContactPoint]] = None,
        address: Optional[FhirList[Address]] = None,
        partOf: Optional[Reference[Organization]] = None,
        contact: Optional[FhirList[OrganizationContact]] = None,
        endpoint: Optional[FhirList[Reference[Endpoint]]] = None,
    ) -> None:
        """
            A formally or informally recognized grouping of people or organizations formed
        for the purpose of achieving some form of collective action.  Includes
        companies, institutions, corporations, departments, community groups,
        healthcare practice groups, payer/insurer, etc.
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
            :param identifier: Identifier for the organization that is used to identify the organization
        across multiple disparate systems.
            :param active: Whether the organization's record is still in active use.
            :param type_: The kind(s) of organization that this is.
            :param name: A name associated with the organization.
            :param alias: A list of alternate names that the organization is known as, or was known as
        in the past.
            :param telecom: A contact detail for the organization.
            :param address: An address for the organization.
            :param partOf: The organization of which this organization forms a part.
            :param contact: Contact for the organization for a certain purpose.
            :param endpoint: Technical endpoints providing access to services operated for the
        organization.
        """
        super().__init__(
            resourceType="Organization",
            id_=id_,
            meta=meta,
            implicitRules=implicitRules,
            language=language,
            text=text,
            contained=contained,
            extension=extension,
            modifierExtension=modifierExtension,
            identifier=identifier,
            active=active,
            type_=type_,
            name=name,
            alias=alias,
            telecom=telecom,
            address=address,
            partOf=partOf,
            contact=contact,
            endpoint=endpoint,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return OrganizationSchema.get_schema(include_extension=include_extension)
