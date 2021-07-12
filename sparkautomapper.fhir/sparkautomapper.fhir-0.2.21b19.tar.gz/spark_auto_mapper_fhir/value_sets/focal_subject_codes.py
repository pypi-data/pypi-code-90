from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class FocalSubjectCodesCode(GenericTypeCode):
    """
    FocalSubjectCodes
    From: http://hl7.org/fhir/ValueSet/focal-subject in valuesets.xml
        Example value set composed from SNOMED CT and HL7 V3 codes for observation
    targets such as donor, fetus or spouse. As use cases are discovered, more
    values may be added.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://snomed.info/sct
    """
    codeset_sct: FhirUri = "http://snomed.info/sct"
    """
    http://terminology.hl7.org/CodeSystem/v3-ParticipationType
    """
    codeset_v3_ParticipationType: FhirUri = (
        "http://terminology.hl7.org/CodeSystem/v3-ParticipationType"
    )
    """
    http://terminology.hl7.org/CodeSystem/v3-RoleCode
    """
    codeset_v3_RoleCode: FhirUri = "http://terminology.hl7.org/CodeSystem/v3-RoleCode"


class FocalSubjectCodesCodeValues:
    """
    From: http://hl7.org/fhir/ValueSet/focal-subject in valuesets.xml
    """

    Fetus = FocalSubjectCodesCode("83418008")
    """
    Indicates that the target of the participation is involved in some manner in
    the act, but does not qualify how.
    From: http://terminology.hl7.org/CodeSystem/v3-ParticipationType in v3-codesystems.xml
    """
    Participation = FocalSubjectCodesCode("PART")
    """
    From: http://hl7.org/fhir/ValueSet/focal-subject in valuesets.xml
    """
    Donor = FocalSubjectCodesCode("DON")
    """
    Concepts characterizing the type of association formed by player and scoper
    when there is a recognized Affiliate role by which the two parties are
    related.
    
    
                               Examples: Business Partner, Business Associate,
    Colleague
    From: http://terminology.hl7.org/CodeSystem/v3-RoleCode in v3-codesystems.xml
    """
    AffiliationRoleType = FocalSubjectCodesCode("_AffiliationRoleType")
    """
    AssignedRoleType
    From: http://terminology.hl7.org/CodeSystem/v3-RoleCode in v3-codesystems.xml
    """
    AssignedRoleType = FocalSubjectCodesCode("_AssignedRoleType")
    """
    Defines types of certifications for all entities
    From: http://terminology.hl7.org/CodeSystem/v3-RoleCode in v3-codesystems.xml
    """
    CertifiedEntityType = FocalSubjectCodesCode("_CertifiedEntityType")
    """
    A role type used to qualify a person's legal status within a country or
    nation.
    From: http://terminology.hl7.org/CodeSystem/v3-RoleCode in v3-codesystems.xml
    """
    CitizenRoleType = FocalSubjectCodesCode("_CitizenRoleType")
    """
    Types of contact for Role code "CON"
    From: http://terminology.hl7.org/CodeSystem/v3-RoleCode in v3-codesystems.xml
    """
    ContactRoleType = FocalSubjectCodesCode("_ContactRoleType")
    """
    Definition: A code representing the type of identifier that has been assigned
    to the identified entity (IDENT).
    
    
                               Examples: Example values include Social Insurance
    Number, Product Catalog ID, Product Model Number.
    From: http://terminology.hl7.org/CodeSystem/v3-RoleCode in v3-codesystems.xml
    """
    IdentifiedEntityType = FocalSubjectCodesCode("_IdentifiedEntityType")
    """
    Code indicating the primary use for which a living subject is bred or grown
    From: http://terminology.hl7.org/CodeSystem/v3-RoleCode in v3-codesystems.xml
    """
    LivingSubjectProductionClass = FocalSubjectCodesCode(
        "_LivingSubjectProductionClass"
    )
    """
    Identifies the specific hierarchical relationship between the playing and
    scoping medications.
    
    
                               Examples: Generic, Generic Formulation, Therapeutic
    Class, etc.
    From: http://terminology.hl7.org/CodeSystem/v3-RoleCode in v3-codesystems.xml
    """
    MedicationGeneralizationRoleType = FocalSubjectCodesCode(
        "_MedicationGeneralizationRoleType"
    )
    """
    Types of membership for Role code "MBR"
    From: http://terminology.hl7.org/CodeSystem/v3-RoleCode in v3-codesystems.xml
    """
    MemberRoleType = FocalSubjectCodesCode("_MemberRoleType")
    """
    PersonalRelationshipRoleType
    From: http://terminology.hl7.org/CodeSystem/v3-RoleCode in v3-codesystems.xml
    """
    PersonalRelationshipRoleType = FocalSubjectCodesCode(
        "_PersonalRelationshipRoleType"
    )
    """
    Description: A role recognized through the eligibility of an identified party
    for benefits covered under an insurance policy or a program based on meeting
    eligibility criteria.
    
                            Eligibility as a covered party may be conditioned on
    the party meeting criteria to qualify for coverage under a policy or program,
    which may be mandated by law.  These criteria may be:
    
    
    
                                  The sole basis for coverage, e.g., being
    differently abled may qualify a person for disability coverage
    
    
    
                                  May more fully qualify a covered party role e.g,
    being differently abled may qualify an adult child as a dependent
    
    
    
                                  May impact the level of coverage for a covered
    party under a policy or program, e.g., being differently abled may qualify a
    program eligible for additional benefits.
    
    
    
    
                               Discussion:  The Abstract Value Set
    "CoverageRoleType", which was developed for use in the Canadian realm "pre-
    coordinate" coverage roles with other roles that a covered party must play in
    order to be eligible for coverage, e.g., "handicapped dependent".   These
    role.codes may only be used with COVPTY to avoid overlapping concepts that
    would result from using them to specify the specializations of COVPTY, e.g.,
    the role.class DEPEN should not be used with the role.code family dependent
    because that relationship has overlapping concepts due to the role.code
    precoodination and is conveyed in FICO with the personal relationship role
    that has a PART role link to the covered party role.  For the same reasons,
    the role.class DEPEN should not be used with the role.code HANDIC (handicapped
    dependent); the role.code DIFFABLE (differently abled) should be used instead.
    
                            In summary, the coded concepts in the Abstract Value
    Set "CoveredPartyRoleType" can be "post-coordinated" with the
    "RoleClassCoveredParty" Abstract Value Set.  Decoupling these concepts is
    intended to support an expansive range of covered party concepts and their
    semantic comparability.
    From: http://terminology.hl7.org/CodeSystem/v3-RoleCode in v3-codesystems.xml
    """
    PolicyOrProgramCoverageRoleType = FocalSubjectCodesCode(
        "_PolicyOrProgramCoverageRoleType"
    )
    """
    Specifies the administrative functionality within a formal experimental design
    for which the ResearchSubject role was established.  Examples: screening -
    role is used for pre-enrollment evaluation portion of the design; enrolled -
    role is used for subjects admitted to the active treatment portion of the
    design.
    From: http://terminology.hl7.org/CodeSystem/v3-RoleCode in v3-codesystems.xml
    """
    ResearchSubjectRoleBasis = FocalSubjectCodesCode("_ResearchSubjectRoleBasis")
    """
    A role of a place that further classifies the setting (e.g., accident site,
    road side, work site, community location) in which services are delivered.
    From: http://terminology.hl7.org/CodeSystem/v3-RoleCode in v3-codesystems.xml
    """
    ServiceDeliveryLocationRoleType = FocalSubjectCodesCode(
        "_ServiceDeliveryLocationRoleType"
    )
    """
    SpecimenRoleType
    From: http://terminology.hl7.org/CodeSystem/v3-RoleCode in v3-codesystems.xml
    """
    SpecimenRoleType = FocalSubjectCodesCode("_SpecimenRoleType")
    """
    A party that makes a claim for coverage under a policy.
    From: http://terminology.hl7.org/CodeSystem/v3-RoleCode in v3-codesystems.xml
    """
    Claimant = FocalSubjectCodesCode("CLAIM")
    """
    Community Laboratory
    From: http://terminology.hl7.org/CodeSystem/v3-RoleCode in v3-codesystems.xml
    """
    CommunityLaboratory = FocalSubjectCodesCode("communityLaboratory")
    """
    An individual or organization that makes or gives a promise, assurance, pledge
    to pay or has paid the healthcare service provider.
    From: http://terminology.hl7.org/CodeSystem/v3-RoleCode in v3-codesystems.xml
    """
    Guarantor = FocalSubjectCodesCode("GT")
    """
    Home Health
    From: http://terminology.hl7.org/CodeSystem/v3-RoleCode in v3-codesystems.xml
    """
    HomeHealth = FocalSubjectCodesCode("homeHealth")
    """
    Laboratory
    From: http://terminology.hl7.org/CodeSystem/v3-RoleCode in v3-codesystems.xml
    """
    Laboratory = FocalSubjectCodesCode("laboratory")
    """
    Pathologist
    From: http://terminology.hl7.org/CodeSystem/v3-RoleCode in v3-codesystems.xml
    """
    Pathologist = FocalSubjectCodesCode("pathologist")
    """
    Policy holder for the insurance policy.
    From: http://terminology.hl7.org/CodeSystem/v3-RoleCode in v3-codesystems.xml
    """
    PolicyHolder = FocalSubjectCodesCode("PH")
    """
    Phlebotomist
    From: http://terminology.hl7.org/CodeSystem/v3-RoleCode in v3-codesystems.xml
    """
    Phlebotomist = FocalSubjectCodesCode("phlebotomist")
    """
    A party that meets the eligibility criteria for coverage under a program.
    From: http://terminology.hl7.org/CodeSystem/v3-RoleCode in v3-codesystems.xml
    """
    ProgramEligible = FocalSubjectCodesCode("PROG")
    """
    The recipient for the service(s) and/or product(s) when they are not the
    covered party.
    From: http://terminology.hl7.org/CodeSystem/v3-RoleCode in v3-codesystems.xml
    """
    Patient = FocalSubjectCodesCode("PT")
    """
    Self
    From: http://terminology.hl7.org/CodeSystem/v3-RoleCode in v3-codesystems.xml
    """
    Self = FocalSubjectCodesCode("subject")
    """
    Third Party
    From: http://terminology.hl7.org/CodeSystem/v3-RoleCode in v3-codesystems.xml
    """
    ThirdParty = FocalSubjectCodesCode("thirdParty")
    """
    From: http://terminology.hl7.org/CodeSystem/v3-RoleCode in v3-codesystems.xml
    """
    DEP = FocalSubjectCodesCode("DEP")
    """
    A party covered under a policy based on association with a subscriber.
    From: http://terminology.hl7.org/CodeSystem/v3-RoleCode in v3-codesystems.xml
    """
    Dependent = FocalSubjectCodesCode("DEPEN")
    """
    A member of the covered party's family. This could be the spouse, a parent, a
    grand parent, a sibling, etc.
    From: http://terminology.hl7.org/CodeSystem/v3-RoleCode in v3-codesystems.xml
    """
    FamilyMember = FocalSubjectCodesCode("FM")
    """
    A party covered under a policy as the policyholder.
    From: http://terminology.hl7.org/CodeSystem/v3-RoleCode in v3-codesystems.xml
    """
    Individual = FocalSubjectCodesCode("INDIV")
    """
    A party to an insurance policy to whom the insurer agrees to indemnify for
    losses, provides benefits for, or renders services.
    From: http://terminology.hl7.org/CodeSystem/v3-RoleCode in v3-codesystems.xml
    """
    NamedInsured = FocalSubjectCodesCode("NAMED")
    """
    From: http://terminology.hl7.org/CodeSystem/v3-RoleCode in v3-codesystems.xml
    """
    PSYCHCF = FocalSubjectCodesCode("PSYCHCF")
    """
    A party covered under a policy based on association with a sponsor who is the
    policy holder, and whose association may provide for the eligibility of
    dependents for coverage
    From: http://terminology.hl7.org/CodeSystem/v3-RoleCode in v3-codesystems.xml
    """
    Subscriber = FocalSubjectCodesCode("SUBSCR")
    """
    From: http://hl7.org/fhir/ValueSet/focal-subject in valuesets.xml
    """
    Spouse = FocalSubjectCodesCode("SPS")
