from __future__ import annotations
from typing import Optional, TYPE_CHECKING

from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.integer import FhirInteger
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
    # code (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # End Import for References for code
    # Import for CodeableConcept for code
    from spark_auto_mapper_fhir.value_sets.loinc_codes import LOINCCodesCode

    # End Import for CodeableConcept for code
    # valueQuantity (Quantity)
    from spark_auto_mapper_fhir.complex_types.quantity import Quantity

    # valueCodeableConcept (CodeableConcept)
    # End Import for References for valueCodeableConcept
    # Import for CodeableConcept for valueCodeableConcept
    from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode

    # End Import for CodeableConcept for valueCodeableConcept
    # valueString (string)
    # valueBoolean (boolean)
    # valueInteger (integer)
    # valueRange (Range)
    from spark_auto_mapper_fhir.complex_types.range import Range

    # valueRatio (Ratio)
    from spark_auto_mapper_fhir.complex_types.ratio import Ratio

    # valueSampledData (SampledData)
    from spark_auto_mapper_fhir.complex_types.sampled_data import SampledData

    # valueTime (time)
    from spark_auto_mapper_fhir.fhir_types.time import FhirTime

    # valueDateTime (dateTime)
    # valuePeriod (Period)
    from spark_auto_mapper_fhir.complex_types.period import Period

    # dataAbsentReason (CodeableConcept)
    # End Import for References for dataAbsentReason
    # Import for CodeableConcept for dataAbsentReason
    from spark_auto_mapper_fhir.value_sets.data_absent_reason import (
        DataAbsentReasonCode,
    )

    # End Import for CodeableConcept for dataAbsentReason
    # interpretation (CodeableConcept)
    # End Import for References for interpretation
    # Import for CodeableConcept for interpretation
    from spark_auto_mapper_fhir.value_sets.observation_interpretation_codes import (
        ObservationInterpretationCodesCode,
    )

    # End Import for CodeableConcept for interpretation
    # referenceRange (Observation.ReferenceRange)
    from spark_auto_mapper_fhir.backbone_elements.observation_reference_range import (
        ObservationReferenceRange,
    )


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ObservationComponent(FhirBackboneElementBase):
    """
    Observation.Component
        Measurements and simple assertions made about a patient, device or other subject.
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        modifierExtension: Optional[FhirList[ExtensionBase]] = None,
        code: CodeableConcept[LOINCCodesCode],
        valueQuantity: Optional[Quantity] = None,
        valueCodeableConcept: Optional[CodeableConcept[GenericTypeCode]] = None,
        valueString: Optional[FhirString] = None,
        valueBoolean: Optional[FhirBoolean] = None,
        valueInteger: Optional[FhirInteger] = None,
        valueRange: Optional[Range] = None,
        valueRatio: Optional[Ratio] = None,
        valueSampledData: Optional[SampledData] = None,
        valueTime: Optional[FhirTime] = None,
        valueDateTime: Optional[FhirDateTime] = None,
        valuePeriod: Optional[Period] = None,
        dataAbsentReason: Optional[CodeableConcept[DataAbsentReasonCode]] = None,
        interpretation: Optional[
            FhirList[CodeableConcept[ObservationInterpretationCodesCode]]
        ] = None,
        referenceRange: Optional[FhirList[ObservationReferenceRange]] = None,
    ) -> None:
        """
            Measurements and simple assertions made about a patient, device or other
        subject.

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
            :param code: Describes what was observed. Sometimes this is called the observation "code".
            :param valueQuantity: None
            :param valueCodeableConcept: None
            :param valueString: None
            :param valueBoolean: None
            :param valueInteger: None
            :param valueRange: None
            :param valueRatio: None
            :param valueSampledData: None
            :param valueTime: None
            :param valueDateTime: None
            :param valuePeriod: None
            :param dataAbsentReason: Provides a reason why the expected value in the element
        Observation.component.value[x] is missing.
            :param interpretation: A categorical assessment of an observation value.  For example, high, low,
        normal.
            :param referenceRange: Guidance on how to interpret the value by comparison to a normal or
        recommended range.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            modifierExtension=modifierExtension,
            code=code,
            valueQuantity=valueQuantity,
            valueCodeableConcept=valueCodeableConcept,
            valueString=valueString,
            valueBoolean=valueBoolean,
            valueInteger=valueInteger,
            valueRange=valueRange,
            valueRatio=valueRatio,
            valueSampledData=valueSampledData,
            valueTime=valueTime,
            valueDateTime=valueDateTime,
            valuePeriod=valuePeriod,
            dataAbsentReason=dataAbsentReason,
            interpretation=interpretation,
            referenceRange=referenceRange,
        )
