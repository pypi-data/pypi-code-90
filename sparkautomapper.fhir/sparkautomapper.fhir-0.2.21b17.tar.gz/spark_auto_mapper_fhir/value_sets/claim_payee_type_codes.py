from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ClaimPayeeTypeCodesCode(GenericTypeCode):
    """
    Claim Payee Type Codes
    From: http://terminology.hl7.org/CodeSystem/payeetype in valuesets.xml
        This value set includes sample Payee Type codes.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/payeetype
    """
    codeset: FhirUri = "http://terminology.hl7.org/CodeSystem/payeetype"


class ClaimPayeeTypeCodesCodeValues:
    """
    The subscriber (policy holder) will be reimbursed.
    From: http://terminology.hl7.org/CodeSystem/payeetype in valuesets.xml
    """

    Subscriber = ClaimPayeeTypeCodesCode("subscriber")
    """
    Any benefit payable will be paid to the provider (Assignment of Benefit).
    From: http://terminology.hl7.org/CodeSystem/payeetype in valuesets.xml
    """
    Provider = ClaimPayeeTypeCodesCode("provider")
    """
    Any benefit payable will be paid to a third party such as a guarrantor.
    From: http://terminology.hl7.org/CodeSystem/payeetype in valuesets.xml
    """
    Provider = ClaimPayeeTypeCodesCode("other")
