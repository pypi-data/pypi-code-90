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
from spark_fhir_schemas.r4.resources.familymemberhistory import (
    FamilyMemberHistorySchema,
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
    # identifier (Identifier)
    from spark_auto_mapper_fhir.complex_types.identifier import Identifier

    # instantiatesCanonical (canonical)
    from spark_auto_mapper_fhir.fhir_types.canonical import FhirCanonical

    # instantiatesUri (uri)
    # status (FamilyHistoryStatus)
    from spark_auto_mapper_fhir.value_sets.family_history_status import (
        FamilyHistoryStatusCode,
    )

    # dataAbsentReason (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for dataAbsentReason
    from spark_auto_mapper_fhir.value_sets.family_history_absent_reason import (
        FamilyHistoryAbsentReasonCode,
    )

    # End Import for CodeableConcept for dataAbsentReason
    # patient (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for patient
    from spark_auto_mapper_fhir.resources.patient import Patient

    # date (dateTime)
    # name (string)
    # relationship (CodeableConcept)
    # Import for CodeableConcept for relationship
    from spark_auto_mapper_fhir.value_sets.family_member import FamilyMember

    # End Import for CodeableConcept for relationship
    # sex (CodeableConcept)
    # Import for CodeableConcept for sex
    from spark_auto_mapper_fhir.value_sets.administrative_gender import (
        AdministrativeGenderCode,
    )

    # End Import for CodeableConcept for sex
    # bornPeriod (Period)
    from spark_auto_mapper_fhir.complex_types.period import Period

    # bornDate (date)
    # bornString (string)
    # ageAge (Age)
    from spark_auto_mapper_fhir.complex_types.age import Age

    # ageRange (Range)
    from spark_auto_mapper_fhir.complex_types.range import Range

    # ageString (string)
    # estimatedAge (boolean)
    # deceasedBoolean (boolean)
    # deceasedAge (Age)
    # deceasedRange (Range)
    # deceasedDate (date)
    # deceasedString (string)
    # reasonCode (CodeableConcept)
    # Import for CodeableConcept for reasonCode
    from spark_auto_mapper_fhir.value_sets.snomedct_clinical_findings import (
        SNOMEDCTClinicalFindingsCode,
    )

    # End Import for CodeableConcept for reasonCode
    # reasonReference (Reference)
    # Imports for References for reasonReference
    from spark_auto_mapper_fhir.resources.condition import Condition
    from spark_auto_mapper_fhir.resources.observation import Observation
    from spark_auto_mapper_fhir.resources.allergy_intolerance import AllergyIntolerance
    from spark_auto_mapper_fhir.resources.questionnaire_response import (
        QuestionnaireResponse,
    )
    from spark_auto_mapper_fhir.resources.diagnostic_report import DiagnosticReport
    from spark_auto_mapper_fhir.resources.document_reference import DocumentReference

    # note (Annotation)
    from spark_auto_mapper_fhir.complex_types.annotation import Annotation

    # condition (FamilyMemberHistory.Condition)
    from spark_auto_mapper_fhir.backbone_elements.family_member_history_condition import (
        FamilyMemberHistoryCondition,
    )


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class FamilyMemberHistory(FhirResourceBase):
    """
    FamilyMemberHistory
    familymemberhistory.xsd
        Significant health conditions for a person related to the patient relevant in
    the context of care for the patient.
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
        instantiatesCanonical: Optional[FhirList[FhirCanonical]] = None,
        instantiatesUri: Optional[FhirList[FhirUri]] = None,
        status: FamilyHistoryStatusCode,
        dataAbsentReason: Optional[
            CodeableConcept[FamilyHistoryAbsentReasonCode]
        ] = None,
        patient: Reference[Patient],
        date: Optional[FhirDateTime] = None,
        name: Optional[FhirString] = None,
        relationship: CodeableConcept[FamilyMember],
        sex: Optional[CodeableConcept[AdministrativeGenderCode]] = None,
        bornPeriod: Optional[Period] = None,
        bornDate: Optional[FhirDate] = None,
        bornString: Optional[FhirString] = None,
        ageAge: Optional[Age] = None,
        ageRange: Optional[Range] = None,
        ageString: Optional[FhirString] = None,
        estimatedAge: Optional[FhirBoolean] = None,
        deceasedBoolean: Optional[FhirBoolean] = None,
        deceasedAge: Optional[Age] = None,
        deceasedRange: Optional[Range] = None,
        deceasedDate: Optional[FhirDate] = None,
        deceasedString: Optional[FhirString] = None,
        reasonCode: Optional[
            FhirList[CodeableConcept[SNOMEDCTClinicalFindingsCode]]
        ] = None,
        reasonReference: Optional[
            FhirList[
                Reference[
                    Union[
                        Condition,
                        Observation,
                        AllergyIntolerance,
                        QuestionnaireResponse,
                        DiagnosticReport,
                        DocumentReference,
                    ]
                ]
            ]
        ] = None,
        note: Optional[FhirList[Annotation]] = None,
        condition: Optional[FhirList[FamilyMemberHistoryCondition]] = None,
    ) -> None:
        """
            Significant health conditions for a person related to the patient relevant in
        the context of care for the patient.
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
            :param identifier: Business identifiers assigned to this family member history by the performer
        or other systems which remain constant as the resource is updated and
        propagates from server to server.
            :param instantiatesCanonical: The URL pointing to a FHIR-defined protocol, guideline, orderset or other
        definition that is adhered to in whole or in part by this FamilyMemberHistory.
            :param instantiatesUri: The URL pointing to an externally maintained protocol, guideline, orderset or
        other definition that is adhered to in whole or in part by this
        FamilyMemberHistory.
            :param status: A code specifying the status of the record of the family history of a specific
        family member.
            :param dataAbsentReason: Describes why the family member's history is not available.
            :param patient: The person who this history concerns.
            :param date: The date (and possibly time) when the family member history was recorded or
        last updated.
            :param name: This will either be a name or a description; e.g. "Aunt Susan", "my cousin
        with the red hair".
            :param relationship: The type of relationship this person has to the patient (father, mother,
        brother etc.).
            :param sex: The birth sex of the family member.
            :param bornPeriod: None
            :param bornDate: None
            :param bornString: None
            :param ageAge: None
            :param ageRange: None
            :param ageString: None
            :param estimatedAge: If true, indicates that the age value specified is an estimated value.
            :param deceasedBoolean: None
            :param deceasedAge: None
            :param deceasedRange: None
            :param deceasedDate: None
            :param deceasedString: None
            :param reasonCode: Describes why the family member history occurred in coded or textual form.
            :param reasonReference: Indicates a Condition, Observation, AllergyIntolerance, or
        QuestionnaireResponse that justifies this family member history event.
            :param note: This property allows a non condition-specific note to the made about the
        related person. Ideally, the note would be in the condition property, but this
        is not always possible.
            :param condition: The significant Conditions (or condition) that the family member had. This is
        a repeating section to allow a system to represent more than one condition per
        resource, though there is nothing stopping multiple resources - one per
        condition.
        """
        super().__init__(
            resourceType="FamilyMemberHistory",
            id_=id_,
            meta=meta,
            implicitRules=implicitRules,
            language=language,
            text=text,
            contained=contained,
            extension=extension,
            modifierExtension=modifierExtension,
            identifier=identifier,
            instantiatesCanonical=instantiatesCanonical,
            instantiatesUri=instantiatesUri,
            status=status,
            dataAbsentReason=dataAbsentReason,
            patient=patient,
            date=date,
            name=name,
            relationship=relationship,
            sex=sex,
            bornPeriod=bornPeriod,
            bornDate=bornDate,
            bornString=bornString,
            ageAge=ageAge,
            ageRange=ageRange,
            ageString=ageString,
            estimatedAge=estimatedAge,
            deceasedBoolean=deceasedBoolean,
            deceasedAge=deceasedAge,
            deceasedRange=deceasedRange,
            deceasedDate=deceasedDate,
            deceasedString=deceasedString,
            reasonCode=reasonCode,
            reasonReference=reasonReference,
            note=note,
            condition=condition,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return FamilyMemberHistorySchema.get_schema(include_extension=include_extension)
