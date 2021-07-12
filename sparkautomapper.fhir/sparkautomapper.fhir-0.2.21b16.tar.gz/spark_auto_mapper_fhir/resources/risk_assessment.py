from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.riskassessment import RiskAssessmentSchema

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
    # identifier (Identifier)
    from spark_auto_mapper_fhir.complex_types.identifier import Identifier

    # basedOn (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for basedOn
    from spark_auto_mapper_fhir.resources.resource import Resource

    # parent (Reference)
    # Imports for References for parent
    # status (ObservationStatus)
    from spark_auto_mapper_fhir.value_sets.observation_status import (
        ObservationStatusCode,
    )

    # method (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for method
    from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode

    # End Import for CodeableConcept for method
    # code (CodeableConcept)
    # Import for CodeableConcept for code
    # End Import for CodeableConcept for code
    # subject (Reference)
    # Imports for References for subject
    from spark_auto_mapper_fhir.resources.patient import Patient
    from spark_auto_mapper_fhir.resources.group import Group

    # encounter (Reference)
    # Imports for References for encounter
    from spark_auto_mapper_fhir.resources.encounter import Encounter

    # occurrenceDateTime (dateTime)
    # occurrencePeriod (Period)
    from spark_auto_mapper_fhir.complex_types.period import Period

    # condition (Reference)
    # Imports for References for condition
    from spark_auto_mapper_fhir.resources.condition import Condition

    # performer (Reference)
    # Imports for References for performer
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
    from spark_auto_mapper_fhir.resources.device import Device

    # reasonCode (CodeableConcept)
    # Import for CodeableConcept for reasonCode
    # End Import for CodeableConcept for reasonCode
    # reasonReference (Reference)
    # Imports for References for reasonReference
    from spark_auto_mapper_fhir.resources.observation import Observation
    from spark_auto_mapper_fhir.resources.diagnostic_report import DiagnosticReport
    from spark_auto_mapper_fhir.resources.document_reference import DocumentReference

    # basis (Reference)
    # Imports for References for basis
    # prediction (RiskAssessment.Prediction)
    from spark_auto_mapper_fhir.backbone_elements.risk_assessment_prediction import (
        RiskAssessmentPrediction,
    )

    # mitigation (string)
    # note (Annotation)
    from spark_auto_mapper_fhir.complex_types.annotation import Annotation


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class RiskAssessment(FhirResourceBase):
    """
    RiskAssessment
    riskassessment.xsd
        An assessment of the likely outcome(s) for a patient or other subject as well
    as the likelihood of each outcome.
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
        identifier: Optional[FhirList[Identifier]] = None,
        basedOn: Optional[Reference[Union[Resource]]] = None,
        parent: Optional[Reference[Union[Resource]]] = None,
        status: ObservationStatusCode,
        method: Optional[CodeableConcept[GenericTypeCode]] = None,
        code: Optional[CodeableConcept[GenericTypeCode]] = None,
        subject: Reference[Union[Patient, Group]],
        encounter: Optional[Reference[Union[Encounter]]] = None,
        occurrenceDateTime: Optional[FhirDateTime] = None,
        occurrencePeriod: Optional[Period] = None,
        condition: Optional[Reference[Union[Condition]]] = None,
        performer: Optional[
            Reference[Union[Practitioner, PractitionerRole, Device]]
        ] = None,
        reasonCode: Optional[FhirList[CodeableConcept[GenericTypeCode]]] = None,
        reasonReference: Optional[
            FhirList[
                Reference[
                    Union[Condition, Observation, DiagnosticReport, DocumentReference]
                ]
            ]
        ] = None,
        basis: Optional[FhirList[Reference[Union[Resource]]]] = None,
        prediction: Optional[FhirList[RiskAssessmentPrediction]] = None,
        mitigation: Optional[FhirString] = None,
        note: Optional[FhirList[Annotation]] = None,
    ) -> None:
        """
            An assessment of the likely outcome(s) for a patient or other subject as well
        as the likelihood of each outcome.
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
            :param identifier: Business identifier assigned to the risk assessment.
            :param basedOn: A reference to the request that is fulfilled by this risk assessment.
            :param parent: A reference to a resource that this risk assessment is part of, such as a
        Procedure.
            :param status: The status of the RiskAssessment, using the same statuses as an Observation.
            :param method: The algorithm, process or mechanism used to evaluate the risk.
            :param code: The type of the risk assessment performed.
            :param subject: The patient or group the risk assessment applies to.
            :param encounter: The encounter where the assessment was performed.
            :param occurrenceDateTime: None
            :param occurrencePeriod: None
            :param condition: For assessments or prognosis specific to a particular condition, indicates the
        condition being assessed.
            :param performer: The provider or software application that performed the assessment.
            :param reasonCode: The reason the risk assessment was performed.
            :param reasonReference: Resources supporting the reason the risk assessment was performed.
            :param basis: Indicates the source data considered as part of the assessment (for example,
        FamilyHistory, Observations, Procedures, Conditions, etc.).
            :param prediction: Describes the expected outcome for the subject.
            :param mitigation: A description of the steps that might be taken to reduce the identified
        risk(s).
            :param note: Additional comments about the risk assessment.
        """
        super().__init__(
            resourceType="RiskAssessment",
            id_=id_,
            meta=meta,
            implicitRules=implicitRules,
            language=language,
            text=text,
            contained=contained,
            extension=extension,
            modifierExtension=modifierExtension,
            identifier=identifier,
            basedOn=basedOn,
            parent=parent,
            status=status,
            method=method,
            code=code,
            subject=subject,
            encounter=encounter,
            occurrenceDateTime=occurrenceDateTime,
            occurrencePeriod=occurrencePeriod,
            condition=condition,
            performer=performer,
            reasonCode=reasonCode,
            reasonReference=reasonReference,
            basis=basis,
            prediction=prediction,
            mitigation=mitigation,
            note=note,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return RiskAssessmentSchema.get_schema(include_extension=include_extension)
