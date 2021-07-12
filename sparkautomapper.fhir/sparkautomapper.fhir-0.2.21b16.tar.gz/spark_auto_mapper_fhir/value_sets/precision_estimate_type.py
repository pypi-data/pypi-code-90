from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class PrecisionEstimateTypeCode(GenericTypeCode):
    """
    PrecisionEstimateType
    From: http://terminology.hl7.org/CodeSystem/precision-estimate-type in valuesets.xml
        Method of reporting variability of estimates, such as confidence intervals,
    interquartile range or standard deviation.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/precision-estimate-type
    """
    codeset: FhirUri = "http://terminology.hl7.org/CodeSystem/precision-estimate-type"


class PrecisionEstimateTypeCodeValues:
    """
    confidence interval.
    From: http://terminology.hl7.org/CodeSystem/precision-estimate-type in valuesets.xml
    """

    ConfidenceInterval = PrecisionEstimateTypeCode("CI")
    """
    interquartile range.
    From: http://terminology.hl7.org/CodeSystem/precision-estimate-type in valuesets.xml
    """
    InterquartileRange = PrecisionEstimateTypeCode("IQR")
    """
    standard deviation.
    From: http://terminology.hl7.org/CodeSystem/precision-estimate-type in valuesets.xml
    """
    StandardDeviation = PrecisionEstimateTypeCode("SD")
    """
    standard error.
    From: http://terminology.hl7.org/CodeSystem/precision-estimate-type in valuesets.xml
    """
    StandardError = PrecisionEstimateTypeCode("SE")
