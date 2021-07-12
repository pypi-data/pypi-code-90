from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ProbabilityDistributionTypeCode(GenericTypeCode):
    """
    ProbabilityDistributionType
    From: http://hl7.org/fhir/ValueSet/probability-distribution-type in valuesets.xml
        Codes specifying the type of probability distribution.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/v3-ProbabilityDistributionType
    """
    codeset: FhirUri = (
        "http://terminology.hl7.org/CodeSystem/v3-ProbabilityDistributionType"
    )


class ProbabilityDistributionTypeCodeValues:
    """
    The beta-distribution is used for data that is bounded on both sides and may
    or may not be skewed (e.g., occurs when probabilities are estimated.)  Two
    parameters a and b  are available to adjust the curve.  The mean m and
    variance s2 relate as follows: m = a/ (a + b) and s2 = ab/((a + b)2 (a + b +
    1)).
    From: http://terminology.hl7.org/CodeSystem/v3-ProbabilityDistributionType in v3-codesystems.xml
    """

    Beta = ProbabilityDistributionTypeCode("B")
    """
    Used for data that describes extinction.  The exponential distribution is a
    special form of g-distribution where a = 1, hence, the relationship to mean m
    and variance s2 are m = b and s2 = b2.
    From: http://terminology.hl7.org/CodeSystem/v3-ProbabilityDistributionType in v3-codesystems.xml
    """
    Exponential = ProbabilityDistributionTypeCode("E")
    """
    Used to describe the quotient of two c2 random variables.  The F-distribution
    has two parameters n1 and n2, which are the numbers of degrees of freedom of
    the numerator and denominator variable respectively. The relationship to mean
    m  and variance s2 are: m = n2 / (n2 - 2) and s2 = (2 n2 (n2 + n1 - 2)) / (n1
    (n2 - 2)2 (n2 - 4)).
    From: http://terminology.hl7.org/CodeSystem/v3-ProbabilityDistributionType in v3-codesystems.xml
    """
    F = ProbabilityDistributionTypeCode("F")
    """
    The gamma-distribution used for data that is skewed and bounded to the right,
    i.e. where the maximum of the distribution curve is located near the origin.
    The g-distribution has a two parameters a and b.  The relationship to mean m
    and variance s2 is m = a b and s2 = a b2.
    From: http://terminology.hl7.org/CodeSystem/v3-ProbabilityDistributionType in v3-codesystems.xml
    """
    _gamma_ = ProbabilityDistributionTypeCode("G")
    """
    The logarithmic normal distribution is used to transform skewed random
    variable X into a normally distributed random variable U = log X. The log-
    normal distribution can be specified with the properties mean m and standard
    deviation s.  Note however that mean m and standard deviation s are the
    parameters of the raw value distribution, not the transformed parameters of
    the lognormal distribution that are conventionally referred to by the same
    letters.  Those log-normal parameters mlog and slog relate to the mean m and
    standard deviation s of the data value through slog2 = log (s2/m2 + 1) and
    mlog = log m - slog2/2.
    From: http://terminology.hl7.org/CodeSystem/v3-ProbabilityDistributionType in v3-codesystems.xml
    """
    Log_normal = ProbabilityDistributionTypeCode("LN")
    """
    This is the well-known bell-shaped normal distribution.  Because of the
    central limit theorem, the normal distribution is the distribution of choice
    for an unbounded random variable that is an outcome of a combination of many
    stochastic processes.  Even for values bounded on a single side (i.e. greater
    than 0) the normal distribution may be accurate enough if the mean is "far
    away" from the bound of the scale measured in terms of standard deviations.
    From: http://terminology.hl7.org/CodeSystem/v3-ProbabilityDistributionType in v3-codesystems.xml
    """
    Normal_Gaussian_ = ProbabilityDistributionTypeCode("N")
    """
    Used to describe the quotient of a normal random variable and the square root
    of a c2 random variable.  The t-distribution has one parameter n, the number
    of degrees of freedom. The relationship to mean m  and variance s2 are: m = 0
    and s2 = n / (n - 2)
    From: http://terminology.hl7.org/CodeSystem/v3-ProbabilityDistributionType in v3-codesystems.xml
    """
    T = ProbabilityDistributionTypeCode("T")
    """
    The uniform distribution assigns a constant probability over the entire
    interval of possible outcomes, while all outcomes outside this interval are
    assumed to have zero probability.  The width of this interval is 2s sqrt(3).
    Thus, the uniform distribution assigns the probability densities f(x) = sqrt(2
    s sqrt(3))  to values m - s sqrt(3) >= x <= m + s sqrt(3) and f(x) = 0
    otherwise.
    From: http://terminology.hl7.org/CodeSystem/v3-ProbabilityDistributionType in v3-codesystems.xml
    """
    Uniform = ProbabilityDistributionTypeCode("U")
    """
    Used to describe the sum of squares of random variables which occurs when a
    variance is estimated (rather than presumed) from the sample.  The only
    parameter of the c2-distribution is n, so called the number of degrees of
    freedom (which is the number of independent parts in the sum).  The
    c2-distribution is a special type of g-distribution with parameter a = n /2
    and b  = 2.  Hence, m = n and s2 = 2 n.
    From: http://terminology.hl7.org/CodeSystem/v3-ProbabilityDistributionType in v3-codesystems.xml
    """
    ChiSquare = ProbabilityDistributionTypeCode("X2")
    """
    From: http://hl7.org/fhir/ValueSet/probability-distribution-type in valuesets.xml
    """
    Beta = ProbabilityDistributionTypeCode("B")
    """
    From: http://hl7.org/fhir/ValueSet/probability-distribution-type in valuesets.xml
    """
    Exponential = ProbabilityDistributionTypeCode("E")
    """
    From: http://hl7.org/fhir/ValueSet/probability-distribution-type in valuesets.xml
    """
    F = ProbabilityDistributionTypeCode("F")
    """
    From: http://hl7.org/fhir/ValueSet/probability-distribution-type in valuesets.xml
    """
    _gamma_ = ProbabilityDistributionTypeCode("G")
    """
    From: http://hl7.org/fhir/ValueSet/probability-distribution-type in valuesets.xml
    """
    Log_normal = ProbabilityDistributionTypeCode("LN")
    """
    From: http://hl7.org/fhir/ValueSet/probability-distribution-type in valuesets.xml
    """
    Normal_Gaussian_ = ProbabilityDistributionTypeCode("N")
    """
    From: http://hl7.org/fhir/ValueSet/probability-distribution-type in valuesets.xml
    """
    T = ProbabilityDistributionTypeCode("T")
    """
    From: http://hl7.org/fhir/ValueSet/probability-distribution-type in valuesets.xml
    """
    Uniform = ProbabilityDistributionTypeCode("U")
    """
    From: http://hl7.org/fhir/ValueSet/probability-distribution-type in valuesets.xml
    """
    ChiSquare = ProbabilityDistributionTypeCode("X2")
