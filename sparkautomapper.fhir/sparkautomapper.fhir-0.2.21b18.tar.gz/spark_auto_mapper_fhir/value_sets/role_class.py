from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class RoleClass(GenericTypeCode):
    """
    v3.RoleClass
    From: http://terminology.hl7.org/ValueSet/v3-RoleClass in v3-codesystems.xml
         Codes for the Role class hierarchy.  The values in this hierarchy, represent
    a Role which is an association or relationship between two entities - the
    entity that plays the role and the entity that scopes the role.  Roles names
    are derived from the name of the playing entity in that role. The role
    hierarchy stems from three core concepts, or abstract domains:
    RoleClassOntological
    is an abstract domain that collects roles in which the playing entity is
    defined or specified by the scoping entity.   RoleClassPartitive
    collects roles in which the playing entity is in some sense a "part" of the
    scoping entity.   RoleClassAssociative
    collects all of the remaining forms of association between the playing entity
    and the scoping entity. This set of roles is further partitioned between:
    RoleClassPassive
    which are roles in which the playing entity is used, known, treated, handled,
    built, or destroyed, etc. under the auspices of the scoping entity. The
    playing entity is passive in these roles in that the role exists without an
    agreement from the playing entity.   RoleClassMutualRelationship
    which are relationships based on mutual behavior of the two entities. The
    basis of these relationship may be formal agreements or they may bede facto
    behavior.  Thus, this sub-domain is further divided into:
    RoleClassRelationshipFormal
    in which the relationship is formally defined, frequently by a contract or
    agreement.   Personal relationship
    which inks two people in a personal relationship. The hierarchy discussed
    above is represented In the current vocabulary tables as a set of abstract
    domains, with the exception of the  "Personal relationship" which is a leaf
    concept.  OpenIssue:
    Description copied from Concept Domain of same name.  Must be verified.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/v3-RoleClass
    """
    codeset: FhirUri = "http://terminology.hl7.org/CodeSystem/v3-RoleClass"


class RoleClassValues:
    """
    Corresponds to the Role class
    From: http://terminology.hl7.org/CodeSystem/v3-RoleClass in v3-codesystems.xml
    """

    Role = RoleClass("ROL")
    """
    The player of the role is a child of the scoping entity, in a generic sense.
    From: http://terminology.hl7.org/CodeSystem/v3-RoleClass in v3-codesystems.xml
    """
    Child = RoleClass("CHILD")
    """
    A role played by an entity that receives credentials from the scoping entity.
    From: http://terminology.hl7.org/CodeSystem/v3-RoleClass in v3-codesystems.xml
    """
    CredentialedEntity = RoleClass("CRED")
    """
    nurse practitioner
    From: http://terminology.hl7.org/CodeSystem/v3-RoleClass in v3-codesystems.xml
    """
    NursePractitioner = RoleClass("NURPRAC")
    """
    nurse
    From: http://terminology.hl7.org/CodeSystem/v3-RoleClass in v3-codesystems.xml
    """
    Nurse = RoleClass("NURS")
    """
    physician assistant
    From: http://terminology.hl7.org/CodeSystem/v3-RoleClass in v3-codesystems.xml
    """
    PhysicianAssistant = RoleClass("PA")
    """
    physician
    From: http://terminology.hl7.org/CodeSystem/v3-RoleClass in v3-codesystems.xml
    """
    Physician = RoleClass("PHYS")
