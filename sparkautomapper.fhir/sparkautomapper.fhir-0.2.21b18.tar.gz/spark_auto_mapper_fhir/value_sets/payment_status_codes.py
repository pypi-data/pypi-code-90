from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class PaymentStatusCodesCode(GenericTypeCode):
    """
    PaymentStatusCodes
    From: http://terminology.hl7.org/CodeSystem/paymentstatus in valuesets.xml
        This value set includes a sample set of Payment Status codes.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/paymentstatus
    """
    codeset: FhirUri = "http://terminology.hl7.org/CodeSystem/paymentstatus"


class PaymentStatusCodesCodeValues:
    """
    The payment has been sent physically or electronically.
    From: http://terminology.hl7.org/CodeSystem/paymentstatus in valuesets.xml
    """

    Paid = PaymentStatusCodesCode("paid")
    """
    The payment has been received by the payee.
    From: http://terminology.hl7.org/CodeSystem/paymentstatus in valuesets.xml
    """
    Cleared = PaymentStatusCodesCode("cleared")
