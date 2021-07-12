from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class InvoiceStatusCode(GenericTypeCode):
    """
    InvoiceStatus
    From: http://hl7.org/fhir/invoice-status in valuesets.xml
        Codes identifying the lifecycle stage of an Invoice.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/invoice-status
    """
    codeset: FhirUri = "http://hl7.org/fhir/invoice-status"


class InvoiceStatusCodeValues:
    """
    the invoice has been prepared but not yet finalized.
    From: http://hl7.org/fhir/invoice-status in valuesets.xml
    """

    Draft = InvoiceStatusCode("draft")
    """
    the invoice has been finalized and sent to the recipient.
    From: http://hl7.org/fhir/invoice-status in valuesets.xml
    """
    Issued = InvoiceStatusCode("issued")
    """
    the invoice has been balaced / completely paid.
    From: http://hl7.org/fhir/invoice-status in valuesets.xml
    """
    Balanced = InvoiceStatusCode("balanced")
    """
    the invoice was cancelled.
    From: http://hl7.org/fhir/invoice-status in valuesets.xml
    """
    Cancelled = InvoiceStatusCode("cancelled")
    """
    the invoice was determined as entered in error before it was issued.
    From: http://hl7.org/fhir/invoice-status in valuesets.xml
    """
    EnteredInError = InvoiceStatusCode("entered-in-error")
