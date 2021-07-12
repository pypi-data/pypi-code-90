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
from spark_fhir_schemas.r4.resources.careteam import CareTeamSchema

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

    # status (CareTeamStatus)
    from spark_auto_mapper_fhir.value_sets.care_team_status import CareTeamStatusCode

    # category (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for category
    from spark_auto_mapper_fhir.value_sets.care_team_category import (
        CareTeamCategoryCode,
    )

    # End Import for CodeableConcept for category
    # name (string)
    # subject (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for subject
    from spark_auto_mapper_fhir.resources.patient import Patient
    from spark_auto_mapper_fhir.resources.group import Group

    # encounter (Reference)
    # Imports for References for encounter
    from spark_auto_mapper_fhir.resources.encounter import Encounter

    # period (Period)
    from spark_auto_mapper_fhir.complex_types.period import Period

    # participant (CareTeam.Participant)
    from spark_auto_mapper_fhir.backbone_elements.care_team_participant import (
        CareTeamParticipant,
    )

    # reasonCode (CodeableConcept)
    # Import for CodeableConcept for reasonCode
    from spark_auto_mapper_fhir.value_sets.snomedct_clinical_findings import (
        SNOMEDCTClinicalFindingsCode,
    )

    # End Import for CodeableConcept for reasonCode
    # reasonReference (Reference)
    # Imports for References for reasonReference
    from spark_auto_mapper_fhir.resources.condition import Condition

    # managingOrganization (Reference)
    # Imports for References for managingOrganization
    from spark_auto_mapper_fhir.resources.organization import Organization

    # telecom (ContactPoint)
    from spark_auto_mapper_fhir.complex_types.contact_point import ContactPoint

    # note (Annotation)
    from spark_auto_mapper_fhir.complex_types.annotation import Annotation


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class CareTeam(FhirResourceBase):
    """
    CareTeam
    careteam.xsd
        The Care Team includes all the people and organizations who plan to
    participate in the coordination and delivery of care for a patient.
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
        status: Optional[CareTeamStatusCode] = None,
        category: Optional[FhirList[CodeableConcept[CareTeamCategoryCode]]] = None,
        name: Optional[FhirString] = None,
        subject: Optional[Reference[Union[Patient, Group]]] = None,
        encounter: Optional[Reference[Encounter]] = None,
        period: Optional[Period] = None,
        participant: Optional[FhirList[CareTeamParticipant]] = None,
        reasonCode: Optional[
            FhirList[CodeableConcept[SNOMEDCTClinicalFindingsCode]]
        ] = None,
        reasonReference: Optional[FhirList[Reference[Condition]]] = None,
        managingOrganization: Optional[FhirList[Reference[Organization]]] = None,
        telecom: Optional[FhirList[ContactPoint]] = None,
        note: Optional[FhirList[Annotation]] = None,
    ) -> None:
        """
            The Care Team includes all the people and organizations who plan to
        participate in the coordination and delivery of care for a patient.
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
            :param identifier: Business identifiers assigned to this care team by the performer or other
        systems which remain constant as the resource is updated and propagates from
        server to server.
            :param status: Indicates the current state of the care team.
            :param category: Identifies what kind of team.  This is to support differentiation between
        multiple co-existing teams, such as care plan team, episode of care team,
        longitudinal care team.
            :param name: A label for human use intended to distinguish like teams.  E.g. the "red" vs.
        "green" trauma teams.
            :param subject: Identifies the patient or group whose intended care is handled by the team.
            :param encounter: The Encounter during which this CareTeam was created or to which the creation
        of this record is tightly associated.
            :param period: Indicates when the team did (or is intended to) come into effect and end.
            :param participant: Identifies all people and organizations who are expected to be involved in the
        care team.
            :param reasonCode: Describes why the care team exists.
            :param reasonReference: Condition(s) that this care team addresses.
            :param managingOrganization: The organization responsible for the care team.
            :param telecom: A central contact detail for the care team (that applies to all members).
            :param note: Comments made about the CareTeam.
        """
        super().__init__(
            resourceType="CareTeam",
            id_=id_,
            meta=meta,
            implicitRules=implicitRules,
            language=language,
            text=text,
            contained=contained,
            extension=extension,
            modifierExtension=modifierExtension,
            identifier=identifier,
            status=status,
            category=category,
            name=name,
            subject=subject,
            encounter=encounter,
            period=period,
            participant=participant,
            reasonCode=reasonCode,
            reasonReference=reasonReference,
            managingOrganization=managingOrganization,
            telecom=telecom,
            note=note,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return CareTeamSchema.get_schema(include_extension=include_extension)
