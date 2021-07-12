from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class X_BasicConfidentialityKind(GenericTypeCode):
    """
    v3.x_BasicConfidentialityKind
    From: http://terminology.hl7.org/ValueSet/v3-xBasicConfidentialityKind in v3-codesystems.xml
          Description:
    Used to enumerate the typical confidentiality constraints placed upon a
    clinical document.  Usage Note:
    x_BasicConfidentialityKind is a subset of Confidentiality codes that are used
    as metadata indicating the receiver responsibility to comply with normally
    applicable jurisdictional privacy law or disclosure authorization; that the
    receiver may not disclose this information except as directed by the
    information custodian, who may be the information subject; or that the
    receiver may not disclose this information except as directed by the
    information custodian, who may be the information subject.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/v3-Confidentiality
    """
    codeset: FhirUri = "http://terminology.hl7.org/CodeSystem/v3-Confidentiality"


class X_BasicConfidentialityKindValues:
    """
    A specializable code and its leaf codes used in Confidentiality value sets to
    value the Act.Confidentiality and Role.Confidentiality attribute in accordance
    with the definition for concept domain "Confidentiality".
    From: http://terminology.hl7.org/CodeSystem/v3-Confidentiality in v3-codesystems.xml
    """

    Confidentiality = X_BasicConfidentialityKind("_Confidentiality")
    """
    Description: By accessing subject / role and relationship based  rights
    (These concepts are mutually exclusive, one and only one is required for a
    valid confidentiality coding.)
    
    
                               Deprecation Comment:Deprecated due to updated
    confidentiality codes under ActCode
    From: http://terminology.hl7.org/CodeSystem/v3-Confidentiality in v3-codesystems.xml
    """
    ConfidentialityByAccessKind = X_BasicConfidentialityKind(
        "_ConfidentialityByAccessKind"
    )
    """
    Description: By information type, only for service catalog entries (multiples
    allowed). Not to be used with actual patient data!
    
    
                               Deprecation Comment:Deprecated due to updated
    confidentiality codes under ActCode
    From: http://terminology.hl7.org/CodeSystem/v3-Confidentiality in v3-codesystems.xml
    """
    ConfidentialityByInfoType = X_BasicConfidentialityKind("_ConfidentialityByInfoType")
    """
    Description: Modifiers of role based access rights  (multiple allowed)
    
    
                               Deprecation Comment:Deprecated due to updated
    confidentiality codes under ActCode
    From: http://terminology.hl7.org/CodeSystem/v3-Confidentiality in v3-codesystems.xml
    """
    ConfidentialityModifiers = X_BasicConfidentialityKind("_ConfidentialityModifiers")
