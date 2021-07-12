from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ContractContentDerivationCodesCode(GenericTypeCode):
    """
    ContractContentDerivationCodes
    From: http://terminology.hl7.org/CodeSystem/contract-content-derivative in valuesets.xml
        This is an example set of Content Derivative type codes, which represent the
    minimal content derived from the basal information source at a specific stage
    in its lifecycle, which is sufficient to manage that source information, for
    example, in a repository, registry, processes and workflows, for making access
    control decisions, and providing query responses.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/contract-content-derivative
    """
    codeset: FhirUri = (
        "http://terminology.hl7.org/CodeSystem/contract-content-derivative"
    )


class ContractContentDerivationCodesCodeValues:
    """
    Content derivative that conveys sufficient information needed to register the
    source basal content from which it is derived.  This derivative content may be
    used to register the basal content as it changes status in its lifecycle.  For
    example, content registration may occur when the basal content is created,
    updated, inactive, or deleted.
    From: http://terminology.hl7.org/CodeSystem/contract-content-derivative in valuesets.xml
    """

    ContentRegistration = ContractContentDerivationCodesCode("registration")
    """
    A content derivative that conveys sufficient information to locate and
    retrieve the content.
    From: http://terminology.hl7.org/CodeSystem/contract-content-derivative in valuesets.xml
    """
    ContentRetrieval = ContractContentDerivationCodesCode("retrieval")
    """
    Content derivative that has less than full fidelity to the basal information
    source from which it was 'transcribed'. It provides recipients with the full
    content representation they may require for compliance purposes, and typically
    include a reference to or an attached unstructured representation for
    recipients needing an exact copy of the legal agreement.
    From: http://terminology.hl7.org/CodeSystem/contract-content-derivative in valuesets.xml
    """
    ContentStatement = ContractContentDerivationCodesCode("statement")
    """
    A Content Derivative that conveys sufficient information to determine the
    authorized entities with which the content may be shared.
    From: http://terminology.hl7.org/CodeSystem/contract-content-derivative in valuesets.xml
    """
    ShareableContent = ContractContentDerivationCodesCode("shareable")
