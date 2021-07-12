from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class EffectEstimateTypeCode(GenericTypeCode):
    """
    EffectEstimateType
    From: http://terminology.hl7.org/CodeSystem/effect-estimate-type in valuesets.xml
        Whether the effect estimate is an absolute effect estimate (absolute
    difference) or a relative effect estimate (relative difference), and the
    specific type of effect estimate (eg relative risk or median difference).
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/effect-estimate-type
    """
    codeset: FhirUri = "http://terminology.hl7.org/CodeSystem/effect-estimate-type"


class EffectEstimateTypeCodeValues:
    """
    relative risk (a type of relative effect estimate).
    From: http://terminology.hl7.org/CodeSystem/effect-estimate-type in valuesets.xml
    """

    RelativeRisk = EffectEstimateTypeCode("relative-RR")
    """
    odds ratio (a type of relative effect estimate).
    From: http://terminology.hl7.org/CodeSystem/effect-estimate-type in valuesets.xml
    """
    OddsRatio = EffectEstimateTypeCode("relative-OR")
    """
    hazard ratio (a type of relative effect estimate).
    From: http://terminology.hl7.org/CodeSystem/effect-estimate-type in valuesets.xml
    """
    HazardRatio = EffectEstimateTypeCode("relative-HR")
    """
    absolute risk difference (a type of absolute effect estimate).
    From: http://terminology.hl7.org/CodeSystem/effect-estimate-type in valuesets.xml
    """
    AbsoluteRiskDifference = EffectEstimateTypeCode("absolute-ARD")
    """
    mean difference (a type of absolute effect estimate).
    From: http://terminology.hl7.org/CodeSystem/effect-estimate-type in valuesets.xml
    """
    MeanDifference = EffectEstimateTypeCode("absolute-MeanDiff")
    """
    standardized mean difference (a type of absolute effect estimate).
    From: http://terminology.hl7.org/CodeSystem/effect-estimate-type in valuesets.xml
    """
    StandardizedMeanDifference = EffectEstimateTypeCode("absolute-SMD")
    """
    median difference (a type of absolute effect estimate).
    From: http://terminology.hl7.org/CodeSystem/effect-estimate-type in valuesets.xml
    """
    MedianDifference = EffectEstimateTypeCode("absolute-MedianDiff")
