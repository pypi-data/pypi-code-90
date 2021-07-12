from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class Verificationresult_communication_methodCode(GenericTypeCode):
    """
    verificationresult-communication-method
    From: http://terminology.hl7.org/CodeSystem/verificationresult-communication-method in valuesets.xml
        Attested information may be validated by process that are manual or automated.
    For automated processes it may accomplished by the system of record reaching
    out through another system's API or information may be sent to the system of
    record. This value set defines a set of codes to describing the process, the
    how, a resource or data element is validated.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/verificationresult-communication-method
    """
    codeset: FhirUri = (
        "http://terminology.hl7.org/CodeSystem/verificationresult-communication-method"
    )


class Verificationresult_communication_methodCodeValues:
    """
    The information is submitted/retrieved manually (e.g. by phone, fax, paper-
    based)
    From: http://terminology.hl7.org/CodeSystem/verificationresult-communication-method in valuesets.xml
    """

    Manual = Verificationresult_communication_methodCode("manual")
    """
    The information is submitted/retrieved via a portal
    From: http://terminology.hl7.org/CodeSystem/verificationresult-communication-method in valuesets.xml
    """
    Portal = Verificationresult_communication_methodCode("portal")
    """
    The information is retrieved (i.e. pulled) from a source (e.g. over an API)
    From: http://terminology.hl7.org/CodeSystem/verificationresult-communication-method in valuesets.xml
    """
    Pull = Verificationresult_communication_methodCode("pull")
    """
    The information is sent (i.e. pushed) from a source (e.g. over an API,
    asynchronously, secure messaging)
    From: http://terminology.hl7.org/CodeSystem/verificationresult-communication-method in valuesets.xml
    """
    Push = Verificationresult_communication_methodCode("push")
