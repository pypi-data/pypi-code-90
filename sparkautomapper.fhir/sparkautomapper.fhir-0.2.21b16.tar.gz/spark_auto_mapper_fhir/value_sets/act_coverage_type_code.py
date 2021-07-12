from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ActCoverageTypeCode(GenericTypeCode):
    """
    v3.ActCoverageTypeCode
    From: http://terminology.hl7.org/ValueSet/v3-ActCoverageTypeCode in v3-codesystems.xml
          Definition:
    Set of codes indicating the type of insurance policy or program that pays for
    the cost of benefits provided to covered parties.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/v3-ActCode
    """
    codeset: FhirUri = "http://terminology.hl7.org/CodeSystem/v3-ActCode"


class ActCoverageTypeCodeValues:
    """
    An account represents a grouping of financial transactions that are tracked
    and reported together with a single balance. 	 	Examples of account codes
    (types) are Patient billing accounts (collection of charges), Cost centers;
    Cash.
    From: http://terminology.hl7.org/CodeSystem/v3-ActCode in v3-codesystems.xml
    """

    ActAccountCode = ActCoverageTypeCode("_ActAccountCode")
    """
    Includes coded responses that will occur as a result of the adjudication of an
    electronic invoice at a summary level and provides guidance on interpretation
    of the referenced adjudication results.
    From: http://terminology.hl7.org/CodeSystem/v3-ActCode in v3-codesystems.xml
    """
    ActAdjudicationCode = ActCoverageTypeCode("_ActAdjudicationCode")
    """
    Actions to be carried out by the recipient of the Adjudication Result
    information.
    From: http://terminology.hl7.org/CodeSystem/v3-ActCode in v3-codesystems.xml
    """
    ActAdjudicationResultActionCode = ActCoverageTypeCode(
        "_ActAdjudicationResultActionCode"
    )
    """
    Definition:An identifying modifier code for healthcare interventions or
    procedures.
    From: http://terminology.hl7.org/CodeSystem/v3-ActCode in v3-codesystems.xml
    """
    ActBillableModifierCode = ActCoverageTypeCode("_ActBillableModifierCode")
    """
    The type of provision(s)  made for reimbursing for the deliver of healthcare
    services and/or goods provided by a Provider, over a specified period.
    From: http://terminology.hl7.org/CodeSystem/v3-ActCode in v3-codesystems.xml
    """
    ActBillingArrangementCode = ActCoverageTypeCode("_ActBillingArrangementCode")
    """
    Type of bounded ROI.
    From: http://terminology.hl7.org/CodeSystem/v3-ActCode in v3-codesystems.xml
    """
    ActBoundedROICode = ActCoverageTypeCode("_ActBoundedROICode")
    """
    Description:The type and scope of responsibility taken-on by the performer of
    the Act for a specific subject of care.
    From: http://terminology.hl7.org/CodeSystem/v3-ActCode in v3-codesystems.xml
    """
    ActCareProvision = ActCoverageTypeCode("_ActCareProvisionCode")
    """
    Description: Coded types of attachments included to support a healthcare
    claim.
    From: http://terminology.hl7.org/CodeSystem/v3-ActCode in v3-codesystems.xml
    """
    ActClaimAttachmentCategoryCode = ActCoverageTypeCode(
        "_ActClaimAttachmentCategoryCode"
    )
    """
    Definition: The type of consent directive, e.g., to consent or dissent to
    collect, access, or use in specific ways within an EHRS or for health
    information exchange; or to disclose  health information  for purposes such as
    research.
    From: http://terminology.hl7.org/CodeSystem/v3-ActCode in v3-codesystems.xml
    """
    ActConsentType = ActCoverageTypeCode("_ActConsentType")
    """
    Constrains the ActCode to the domain of Container Registration
    From: http://terminology.hl7.org/CodeSystem/v3-ActCode in v3-codesystems.xml
    """
    ActContainerRegistrationCode = ActCoverageTypeCode("_ActContainerRegistrationCode")
    """
    An observation form that determines parameters or attributes of an Act.
    Examples are the settings of a ventilator machine as parameters of a
    ventilator treatment act; the controls on dillution factors of a chemical
    analyzer as a parameter of a laboratory observation act; the settings of a
    physiologic measurement assembly (e.g., time skew) or the position of the body
    while measuring blood pressure.
    
                            Control variables are forms of observations because
    just as with clinical observations, the Observation.code determines the
    parameter and the Observation.value assigns the value. While control variables
    sometimes can be observed (by noting the control settings or an actually
    measured feedback loop) they are not primary observations, in the sense that a
    control variable without a primary act is of no use (e.g., it makes no sense
    to record a blood pressure position without recording a blood pressure,
    whereas it does make sense to record a systolic blood pressure without a
    diastolic blood pressure).
    From: http://terminology.hl7.org/CodeSystem/v3-ActCode in v3-codesystems.xml
    """
    ActControlVariable = ActCoverageTypeCode("_ActControlVariable")
    """
    Response to an insurance coverage eligibility query or authorization request.
    From: http://terminology.hl7.org/CodeSystem/v3-ActCode in v3-codesystems.xml
    """
    ActCoverageConfirmationCode = ActCoverageTypeCode("_ActCoverageConfirmationCode")
    """
    Criteria that are applicable to the authorized coverage.
    From: http://terminology.hl7.org/CodeSystem/v3-ActCode in v3-codesystems.xml
    """
    ActCoverageLimitCode = ActCoverageTypeCode("_ActCoverageLimitCode")
    """
    Definition: Set of codes indicating the type of insurance policy or program
    that pays for the cost of benefits provided to covered parties.
    From: http://terminology.hl7.org/CodeSystem/v3-ActCode in v3-codesystems.xml
    """
    ActCoverageTypeCode_ = ActCoverageTypeCode("_ActCoverageTypeCode")
    """
    Codes dealing with the management of Detected Issue observations
    From: http://terminology.hl7.org/CodeSystem/v3-ActCode in v3-codesystems.xml
    """
    ActDetectedIssueManagementCode = ActCoverageTypeCode(
        "_ActDetectedIssueManagementCode"
    )
    """
    Concepts that identify the type or nature of exposure interaction.  Examples
    include "household", "care giver", "intimate partner", "common space", "common
    substance", etc. to further describe the nature of interaction.
    From: http://terminology.hl7.org/CodeSystem/v3-ActCode in v3-codesystems.xml
    """
    ActExposureCode = ActCoverageTypeCode("_ActExposureCode")
    """
    ActFinancialTransactionCode
    From: http://terminology.hl7.org/CodeSystem/v3-ActCode in v3-codesystems.xml
    """
    ActFinancialTransactionCode = ActCoverageTypeCode("_ActFinancialTransactionCode")
    """
    Set of codes indicating the type of incident or accident.
    From: http://terminology.hl7.org/CodeSystem/v3-ActCode in v3-codesystems.xml
    """
    ActIncidentCode = ActCoverageTypeCode("_ActIncidentCode")
    """
    Description: The type of health information to which the subject of the
    information or the subject's delegate consents or dissents.
    From: http://terminology.hl7.org/CodeSystem/v3-ActCode in v3-codesystems.xml
    """
    ActInformationAccessCode = ActCoverageTypeCode("_ActInformationAccessCode")
    """
    Concepts conveying the context in which authorization given under
    jurisdictional law, by organizational policy, or by a patient consent
    directive permits the collection, access, use or disclosure of specified
    patient health information.
    From: http://terminology.hl7.org/CodeSystem/v3-ActCode in v3-codesystems.xml
    """
    ActInformationAccessContextCode = ActCoverageTypeCode(
        "_ActInformationAccessContextCode"
    )
    """
    Definition:Indicates the set of information types which may be manipulated or
    referenced, such as for recommending access restrictions.
    From: http://terminology.hl7.org/CodeSystem/v3-ActCode in v3-codesystems.xml
    """
    ActInformationCategoryCode = ActCoverageTypeCode("_ActInformationCategoryCode")
    """
    Type of invoice element that is used to assist in describing an Invoice that
    is either submitted for adjudication or for which is returned on adjudication
    results.
    From: http://terminology.hl7.org/CodeSystem/v3-ActCode in v3-codesystems.xml
    """
    ActInvoiceElementCode = ActCoverageTypeCode("_ActInvoiceElementCode")
    """
    Identifies the different types of summary information that can be reported by
    queries dealing with Statement of Financial Activity (SOFA).  The summary
    information is generally used to help resolve balance discrepancies between
    providers and payors.
    From: http://terminology.hl7.org/CodeSystem/v3-ActCode in v3-codesystems.xml
    """
    ActInvoiceElementSummaryCode = ActCoverageTypeCode("_ActInvoiceElementSummaryCode")
    """
    Includes coded responses that will occur as a result of the adjudication of an
    electronic invoice at a summary level and provides guidance on interpretation
    of the referenced adjudication results.
    From: http://terminology.hl7.org/CodeSystem/v3-ActCode in v3-codesystems.xml
    """
    ActInvoiceOverrideCode = ActCoverageTypeCode("_ActInvoiceOverrideCode")
    """
    Provides codes associated with ActClass value of LIST (working list)
    From: http://terminology.hl7.org/CodeSystem/v3-ActCode in v3-codesystems.xml
    """
    ActListCode = ActCoverageTypeCode("_ActListCode")
    """
    Identifies types of monitoring programs
    From: http://terminology.hl7.org/CodeSystem/v3-ActCode in v3-codesystems.xml
    """
    ActMonitoringProtocolCode = ActCoverageTypeCode("_ActMonitoringProtocolCode")
    """
    Description:Concepts representing indications (reasons for clinical action)
    other than diagnosis and symptoms.
    From: http://terminology.hl7.org/CodeSystem/v3-ActCode in v3-codesystems.xml
    """
    ActNonObservationIndicationCode = ActCoverageTypeCode(
        "_ActNonObservationIndicationCode"
    )
    """
    Identifies the type of verification investigation being undertaken with
    respect to the subject of the verification activity.
    
    
                               Examples:
    
    
    
    
                                  Verification of eligibility for coverage under a
    policy or program - aka enrolled/covered by a policy or program
    
    
    
                                  Verification of record - e.g., person has record
    in an immunization registry
    
    
    
                                  Verification of enumeration - e.g. NPI
    
    
    
                                  Verification of Board Certification - provider
    specific
    
    
    
                                  Verification of Certification - e.g. JAHCO,
    NCQA, URAC
    
    
    
                                  Verification of Conformance - e.g. entity use
    with HIPAA, conformant to the CCHIT EHR system criteria
    
    
    
                                  Verification of Provider Credentials
    
    
    
                                  Verification of no adverse findings - e.g. on
    National Provider Data Bank, Health Integrity Protection Data Base (HIPDB)
    From: http://terminology.hl7.org/CodeSystem/v3-ActCode in v3-codesystems.xml
    """
    ActObservationVerification = ActCoverageTypeCode("_ActObservationVerificationType")
    """
    Code identifying the method or the movement of payment instructions.
    
                            Codes are drawn from X12 data element 591
    (PaymentMethodCode)
    From: http://terminology.hl7.org/CodeSystem/v3-ActCode in v3-codesystems.xml
    """
    ActPaymentCode = ActCoverageTypeCode("_ActPaymentCode")
    """
    Identifies types of dispensing events
    From: http://terminology.hl7.org/CodeSystem/v3-ActCode in v3-codesystems.xml
    """
    ActPharmacySupplyType = ActCoverageTypeCode("_ActPharmacySupplyType")
    """
    Description:Types of policies that further specify the ActClassPolicy value
    set.
    From: http://terminology.hl7.org/CodeSystem/v3-ActCode in v3-codesystems.xml
    """
    ActPolicyType = ActCoverageTypeCode("_ActPolicyType")
    """
    The method that a product is obtained for use by the subject of the supply act
    (e.g. patient).  Product examples are consumable or durable goods.
    From: http://terminology.hl7.org/CodeSystem/v3-ActCode in v3-codesystems.xml
    """
    ActProductAcquisitionCode = ActCoverageTypeCode("_ActProductAcquisitionCode")
    """
    Transportation of a specimen.
    From: http://terminology.hl7.org/CodeSystem/v3-ActCode in v3-codesystems.xml
    """
    ActSpecimenTransportCode = ActCoverageTypeCode("_ActSpecimenTransportCode")
    """
    Set of codes related to specimen treatments
    From: http://terminology.hl7.org/CodeSystem/v3-ActCode in v3-codesystems.xml
    """
    ActSpecimenTreatmentCode = ActCoverageTypeCode("_ActSpecimenTreatmentCode")
    """
    Description: Describes the type of substance administration being performed.
    This should not be used to carry codes for identification of products.  Use an
    associated role or entity to carry such information.
    From: http://terminology.hl7.org/CodeSystem/v3-ActCode in v3-codesystems.xml
    """
    ActSubstanceAdministrationCode = ActCoverageTypeCode(
        "_ActSubstanceAdministrationCode"
    )
    """
    Description: A task or action that a user may perform in a clinical
    information system (e.g., medication order entry, laboratory test results
    review, problem list entry).
    From: http://terminology.hl7.org/CodeSystem/v3-ActCode in v3-codesystems.xml
    """
    ActTaskCode = ActCoverageTypeCode("_ActTaskCode")
    """
    Characterizes how a transportation act was or will be carried out.
    
    
                               Examples: Via private transport, via public
    transit, via courier.
    From: http://terminology.hl7.org/CodeSystem/v3-ActCode in v3-codesystems.xml
    """
    ActTransportationModeCode = ActCoverageTypeCode("_ActTransportationModeCode")
    """
    Identifies the kinds of observations that can be performed
    From: http://terminology.hl7.org/CodeSystem/v3-ActCode in v3-codesystems.xml
    """
    ObservationType = ActCoverageTypeCode("_ObservationType")
    """
    Shape of the region on the object being referenced
    From: http://terminology.hl7.org/CodeSystem/v3-ActCode in v3-codesystems.xml
    """
    ROIOverlayShape = ActCoverageTypeCode("_ROIOverlayShape")
    """
    Description:Indicates that result data has been corrected.
    From: http://terminology.hl7.org/CodeSystem/v3-ActCode in v3-codesystems.xml
    """
    Corrected = ActCoverageTypeCode("C")
    """
    Code set to define specialized/allowed diets
    From: http://terminology.hl7.org/CodeSystem/v3-ActCode in v3-codesystems.xml
    """
    Diet = ActCoverageTypeCode("DIET")
    """
    Definition: A public or government health program that administers and funds
    coverage for prescription drugs to assist program eligible who meet financial
    and health status criteria.
    From: http://terminology.hl7.org/CodeSystem/v3-ActCode in v3-codesystems.xml
    """
    DrugProgram = ActCoverageTypeCode("DRUGPRG")
    """
    Description:Indicates that a result is complete.  No further results are to
    come.  This maps to the 'complete' state in the observation result status
    code.
    From: http://terminology.hl7.org/CodeSystem/v3-ActCode in v3-codesystems.xml
    """
    Final = ActCoverageTypeCode("F")
    """
    Description:Indicates that a result is incomplete.  There are further results
    to come.  This maps to the 'active' state in the observation result status
    code.
    From: http://terminology.hl7.org/CodeSystem/v3-ActCode in v3-codesystems.xml
    """
    Preliminary = ActCoverageTypeCode("PRLMN")
    """
    An observation identifying security metadata about an IT resource (data,
    information object, service, or system capability), which may be used to make
    access control decisions.  Security metadata are used to name security labels.
    
    
                               Rationale: According to ISO/TS 22600-3:2009(E)
    A.9.1.7 SECURITY LABEL MATCHING, Security label matching compares the
    initiator's clearance to the target's security label.  All of the following
    must be true for authorization to be granted:
    
    
                               The security policy identifiers shall be identical
                               The classification level of the initiator shall be
    greater than or equal to that of the target (that is, there shall be at least
    one value in the classification list of the clearance greater than or equal to
    the classification of the target), and
                               For each security category in the target label,
    there shall be a security category of the same type in the initiator's
    clearance and the initiator's classification level shall dominate that of the
    target.
    
    
                               Examples: SecurityObservationType  security label
    fields include:
    
    
                               Confidentiality classification
                               Compartment category
                               Sensitivity category
                               Security mechanisms used to ensure data integrity
    or to perform authorized data transformation
                               Indicators of an IT resource completeness,
    veracity, reliability, trustworthiness, or provenance.
    
    
                               Usage Note: SecurityObservationType codes designate
    security label field types, which are valued with an applicable
    SecurityObservationValue code as the "security label tag".
    From: http://terminology.hl7.org/CodeSystem/v3-ActCode in v3-codesystems.xml
    """
    SecurityObservationType = ActCoverageTypeCode("SECOBS")
    """
    Definition: A government health program that provides coverage on a fee for
    service basis for health services to persons meeting eligibility criteria such
    as income, location of residence, access to other coverages, health condition,
    and age, the cost of which is to some extent subsidized by public funds.
    
    
                               Discussion: The structure and business processes
    for underwriting and administering a subsidized fee for service program is
    further specified by the Underwriter and Payer Role.class and Role.code.
    From: http://terminology.hl7.org/CodeSystem/v3-ActCode in v3-codesystems.xml
    """
    SubsidizedFeeForServiceProgram = ActCoverageTypeCode("SUBSIDFFS")
    """
    Definition: Government mandated program providing coverage, disability income,
    and vocational rehabilitation for injuries sustained in the work place or in
    the course of employment.  Employers may either self-fund the program,
    purchase commercial coverage, or pay a premium to a government entity that
    administers the program.  Employees may be required to pay premiums toward the
    cost of coverage as well.
    From: http://terminology.hl7.org/CodeSystem/v3-ActCode in v3-codesystems.xml
    """
    _workersCompensationProgram = ActCoverageTypeCode("WRKCOMP")
    """
    An identifying code for healthcare interventions/procedures.
    From: http://terminology.hl7.org/CodeSystem/v3-ActCode in v3-codesystems.xml
    """
    ActProcedureCode = ActCoverageTypeCode("_ActProcedureCode")
    """
    Domain provides the root for HL7-defined detailed or rich codes for the Act
    classes.
    From: http://terminology.hl7.org/CodeSystem/v3-ActCode in v3-codesystems.xml
    """
    HL7DefinedActCodes = ActCoverageTypeCode("_HL7DefinedActCodes")
    """
    From: http://terminology.hl7.org/CodeSystem/v3-ActCode in v3-codesystems.xml
    """
    COPAY = ActCoverageTypeCode("COPAY")
    """
    From: http://terminology.hl7.org/CodeSystem/v3-ActCode in v3-codesystems.xml
    """
    DEDUCT = ActCoverageTypeCode("DEDUCT")
    """
    From: http://terminology.hl7.org/CodeSystem/v3-ActCode in v3-codesystems.xml
    """
    DOSEIND = ActCoverageTypeCode("DOSEIND")
    """
    From: http://terminology.hl7.org/CodeSystem/v3-ActCode in v3-codesystems.xml
    """
    PRA = ActCoverageTypeCode("PRA")
    """
    The act of putting something away for safe keeping. The "something" may be
    physical object such as a specimen, or information, such as observations
    regarding a specimen.
    From: http://terminology.hl7.org/CodeSystem/v3-ActCode in v3-codesystems.xml
    """
    Storage = ActCoverageTypeCode("STORE")
