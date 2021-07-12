from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class HL7WorkgroupCode(GenericTypeCode):
    """
    HL7Workgroup
    From: http://terminology.hl7.org/CodeSystem/hl7-work-group in valuesets.xml
        An HL7 administrative unit that owns artifacts in the FHIR specification.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/hl7-work-group
    """
    codeset: FhirUri = "http://terminology.hl7.org/CodeSystem/hl7-work-group"


class HL7WorkgroupCodeValues:
    """
    Community Based Collaborative Care
    (http://www.hl7.org/Special/committees/cbcc/index.cfm).
    From: http://terminology.hl7.org/CodeSystem/hl7-work-group in valuesets.xml
    """

    CommunityBasedCollaborativeCare = HL7WorkgroupCode("cbcc")
    """
    Clinical Decision Support
    (http://www.hl7.org/Special/committees/dss/index.cfm).
    From: http://terminology.hl7.org/CodeSystem/hl7-work-group in valuesets.xml
    """
    ClinicalDecisionSupport = HL7WorkgroupCode("cds")
    """
    Clinical Quality Information
    (http://www.hl7.org/Special/committees/cqi/index.cfm).
    From: http://terminology.hl7.org/CodeSystem/hl7-work-group in valuesets.xml
    """
    ClinicalQualityInformation = HL7WorkgroupCode("cqi")
    """
    Clinical Genomics
    (http://www.hl7.org/Special/committees/clingenomics/index.cfm).
    From: http://terminology.hl7.org/CodeSystem/hl7-work-group in valuesets.xml
    """
    ClinicalGenomics = HL7WorkgroupCode("cg")
    """
    Health Care Devices
    (http://www.hl7.org/Special/committees/healthcaredevices/index.cfm).
    From: http://terminology.hl7.org/CodeSystem/hl7-work-group in valuesets.xml
    """
    HealthCareDevices = HL7WorkgroupCode("dev")
    """
    Electronic Health Records
    (http://www.hl7.org/special/committees/ehr/index.cfm).
    From: http://terminology.hl7.org/CodeSystem/hl7-work-group in valuesets.xml
    """
    ElectronicHealthRecords = HL7WorkgroupCode("ehr")
    """
    FHIR Infrastructure (http://www.hl7.org/Special/committees/fiwg/index.cfm).
    From: http://terminology.hl7.org/CodeSystem/hl7-work-group in valuesets.xml
    """
    FHIRInfrastructure = HL7WorkgroupCode("fhir")
    """
    Financial Management (http://www.hl7.org/Special/committees/fm/index.cfm).
    From: http://terminology.hl7.org/CodeSystem/hl7-work-group in valuesets.xml
    """
    FinancialManagement = HL7WorkgroupCode("fm")
    """
    Health Standards Integration
    (http://www.hl7.org/Special/committees/hsi/index.cfm).
    From: http://terminology.hl7.org/CodeSystem/hl7-work-group in valuesets.xml
    """
    HealthStandardsIntegration = HL7WorkgroupCode("hsi")
    """
    Imaging Integration
    (http://www.hl7.org/Special/committees/imagemgt/index.cfm).
    From: http://terminology.hl7.org/CodeSystem/hl7-work-group in valuesets.xml
    """
    ImagingIntegration = HL7WorkgroupCode("ii")
    """
    Infrastructure And Messaging
    (http://www.hl7.org/special/committees/inm/index.cfm).
    From: http://terminology.hl7.org/CodeSystem/hl7-work-group in valuesets.xml
    """
    InfrastructureAndMessaging = HL7WorkgroupCode("inm")
    """
    Implementable Technology Specifications
    (http://www.hl7.org/special/committees/xml/index.cfm).
    From: http://terminology.hl7.org/CodeSystem/hl7-work-group in valuesets.xml
    """
    ImplementableTechnologySpecifications = HL7WorkgroupCode("its")
    """
    Modeling and Methodology
    (http://www.hl7.org/Special/committees/mnm/index.cfm).
    From: http://terminology.hl7.org/CodeSystem/hl7-work-group in valuesets.xml
    """
    ModelingAndMethodology = HL7WorkgroupCode("mnm")
    """
    Orders and Observations
    (http://www.hl7.org/Special/committees/orders/index.cfm).
    From: http://terminology.hl7.org/CodeSystem/hl7-work-group in valuesets.xml
    """
    OrdersAndObservations = HL7WorkgroupCode("oo")
    """
    Patient Administration (http://www.hl7.org/Special/committees/pafm/index.cfm).
    From: http://terminology.hl7.org/CodeSystem/hl7-work-group in valuesets.xml
    """
    PatientAdministration = HL7WorkgroupCode("pa")
    """
    Patient Care (http://www.hl7.org/Special/committees/patientcare/index.cfm).
    From: http://terminology.hl7.org/CodeSystem/hl7-work-group in valuesets.xml
    """
    PatientCare = HL7WorkgroupCode("pc")
    """
    Public Health and Emergency Response
    (http://www.hl7.org/Special/committees/pher/index.cfm).
    From: http://terminology.hl7.org/CodeSystem/hl7-work-group in valuesets.xml
    """
    PublicHealthAndEmergencyResponse = HL7WorkgroupCode("pher")
    """
    Pharmacy (http://www.hl7.org/Special/committees/medication/index.cfm).
    From: http://terminology.hl7.org/CodeSystem/hl7-work-group in valuesets.xml
    """
    Pharmacy = HL7WorkgroupCode("phx")
    """
    Biomedical Research and Regulation
    (http://www.hl7.org/Special/committees/rcrim/index.cfm).
    From: http://terminology.hl7.org/CodeSystem/hl7-work-group in valuesets.xml
    """
    BiomedicalResearchAndRegulation = HL7WorkgroupCode("brr")
    """
    Structured Documents
    (http://www.hl7.org/Special/committees/structure/index.cfm).
    From: http://terminology.hl7.org/CodeSystem/hl7-work-group in valuesets.xml
    """
    StructuredDocuments = HL7WorkgroupCode("sd")
    """
    Security (http://www.hl7.org/Special/committees/secure/index.cfm).
    From: http://terminology.hl7.org/CodeSystem/hl7-work-group in valuesets.xml
    """
    Security = HL7WorkgroupCode("sec")
    """
    US Realm Taskforce (http://www.hl7.org/Special/committees/usrealm/index.cfm).
    From: http://terminology.hl7.org/CodeSystem/hl7-work-group in valuesets.xml
    """
    USRealmTaskforce = HL7WorkgroupCode("us")
    """
    Vocabulary (http://www.hl7.org/Special/committees/Vocab/index.cfm).
    From: http://terminology.hl7.org/CodeSystem/hl7-work-group in valuesets.xml
    """
    Vocabulary = HL7WorkgroupCode("vocab")
    """
    Application Implementation and Design
    (http://www.hl7.org/Special/committees/java/index.cfm).
    From: http://terminology.hl7.org/CodeSystem/hl7-work-group in valuesets.xml
    """
    ApplicationImplementationAndDesign = HL7WorkgroupCode("aid")
