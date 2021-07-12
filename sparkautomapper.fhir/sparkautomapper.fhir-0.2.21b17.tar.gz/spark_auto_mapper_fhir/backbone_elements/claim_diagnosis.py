from __future__ import annotations
from typing import Optional, TYPE_CHECKING

from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase

from spark_auto_mapper_fhir.base_types.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)

if TYPE_CHECKING:
    pass
    # id_ (string)
    # extension (Extension)
    # modifierExtension (Extension)
    # sequence (positiveInt)
    from spark_auto_mapper_fhir.fhir_types.positive_int import FhirPositiveInt

    # diagnosisCodeableConcept (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # End Import for References for diagnosisCodeableConcept
    # Import for CodeableConcept for diagnosisCodeableConcept
    from spark_auto_mapper_fhir.value_sets.icd_10_codes import ICD_10CodesCode

    # End Import for CodeableConcept for diagnosisCodeableConcept
    # diagnosisReference (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for diagnosisReference
    from spark_auto_mapper_fhir.resources.condition import Condition

    # type_ (CodeableConcept)
    # End Import for References for type_
    # Import for CodeableConcept for type_
    from spark_auto_mapper_fhir.value_sets.example_diagnosis_type_codes import (
        ExampleDiagnosisTypeCodesCode,
    )

    # End Import for CodeableConcept for type_
    # onAdmission (CodeableConcept)
    # End Import for References for onAdmission
    # Import for CodeableConcept for onAdmission
    from spark_auto_mapper_fhir.value_sets.example_diagnosis_on_admission_codes import (
        ExampleDiagnosisOnAdmissionCodesCode,
    )

    # End Import for CodeableConcept for onAdmission
    # packageCode (CodeableConcept)
    # End Import for References for packageCode
    # Import for CodeableConcept for packageCode
    from spark_auto_mapper_fhir.value_sets.example_diagnosis_related_group_codes import (
        ExampleDiagnosisRelatedGroupCodesCode,
    )

    # End Import for CodeableConcept for packageCode


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ClaimDiagnosis(FhirBackboneElementBase):
    """
    Claim.Diagnosis
        A provider issued list of professional services and products which have been provided, or are to be provided, to a patient which is sent to an insurer for reimbursement.
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        modifierExtension: Optional[FhirList[ExtensionBase]] = None,
        sequence: FhirPositiveInt,
        diagnosisCodeableConcept: Optional[CodeableConcept[ICD_10CodesCode]] = None,
        diagnosisReference: Optional[Reference[Condition]] = None,
        type_: Optional[
            FhirList[CodeableConcept[ExampleDiagnosisTypeCodesCode]]
        ] = None,
        onAdmission: Optional[
            CodeableConcept[ExampleDiagnosisOnAdmissionCodesCode]
        ] = None,
        packageCode: Optional[
            CodeableConcept[ExampleDiagnosisRelatedGroupCodesCode]
        ] = None,
    ) -> None:
        """
            A provider issued list of professional services and products which have been
        provided, or are to be provided, to a patient which is sent to an insurer for
        reimbursement.

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
            :param sequence: A number to uniquely identify diagnosis entries.
            :param diagnosisCodeableConcept: None
            :param diagnosisReference: None
            :param type_: When the condition was observed or the relative ranking.
            :param onAdmission: Indication of whether the diagnosis was present on admission to a facility.
            :param packageCode: A package billing code or bundle code used to group products and services to a
        particular health condition (such as heart attack) which is based on a
        predetermined grouping code system.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            modifierExtension=modifierExtension,
            sequence=sequence,
            diagnosisCodeableConcept=diagnosisCodeableConcept,
            diagnosisReference=diagnosisReference,
            type_=type_,
            onAdmission=onAdmission,
            packageCode=packageCode,
        )
