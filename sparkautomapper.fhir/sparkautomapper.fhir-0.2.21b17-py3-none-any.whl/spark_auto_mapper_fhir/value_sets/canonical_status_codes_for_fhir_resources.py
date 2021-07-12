from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class CanonicalStatusCodesForFHIRResourcesCode(GenericTypeCode):
    """
    Canonical Status Codes for FHIR Resources
    From: http://hl7.org/fhir/resource-status in valuesets.xml
        The master set of status codes used throughout FHIR. All status codes are
    mapped to one of these codes.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/resource-status
    """
    codeset: FhirUri = "http://hl7.org/fhir/resource-status"


class CanonicalStatusCodesForFHIRResourcesCodeValues:
    """
    The resource was created in error, and should not be treated as valid (note:
    in many cases, for various data integrity related reasons, the information
    cannot be removed from the record)
    From: http://hl7.org/fhir/resource-status in valuesets.xml
    """

    Error = CanonicalStatusCodesForFHIRResourcesCode("error")
    """
    The resource describes an action or plan that is proposed, and not yet
    approved by the participants
    From: http://hl7.org/fhir/resource-status in valuesets.xml
    """
    Proposed = CanonicalStatusCodesForFHIRResourcesCode("proposed")
    """
    The resource describes a course of action that is planned and agreed/approved,
    but at the time of recording was still future
    From: http://hl7.org/fhir/resource-status in valuesets.xml
    """
    Planned = CanonicalStatusCodesForFHIRResourcesCode("planned")
    """
    The information in the resource is still being prepared and edited
    From: http://hl7.org/fhir/resource-status in valuesets.xml
    """
    Draft = CanonicalStatusCodesForFHIRResourcesCode("draft")
    """
    A fulfiller has been asked to perform this action, but it has not yet occurred
    From: http://hl7.org/fhir/resource-status in valuesets.xml
    """
    Requested = CanonicalStatusCodesForFHIRResourcesCode("requested")
    """
    The fulfiller has received the request, but not yet agreed to carry out the
    action
    From: http://hl7.org/fhir/resource-status in valuesets.xml
    """
    Received = CanonicalStatusCodesForFHIRResourcesCode("received")
    """
    The fulfiller chose not to perform the action
    From: http://hl7.org/fhir/resource-status in valuesets.xml
    """
    Declined = CanonicalStatusCodesForFHIRResourcesCode("declined")
    """
    The fulfiller has decided to perform the action, and plans are in train to do
    this in the future
    From: http://hl7.org/fhir/resource-status in valuesets.xml
    """
    Accepted = CanonicalStatusCodesForFHIRResourcesCode("accepted")
    """
    The pre-conditions for the action are all fulfilled, and it is imminent
    From: http://hl7.org/fhir/resource-status in valuesets.xml
    """
    Arrived = CanonicalStatusCodesForFHIRResourcesCode("arrived")
    """
    The resource describes information that is currently valid or a process that
    is presently occuring
    From: http://hl7.org/fhir/resource-status in valuesets.xml
    """
    Active = CanonicalStatusCodesForFHIRResourcesCode("active")
    """
    The process described/requested in this resource has been halted for some
    reason
    From: http://hl7.org/fhir/resource-status in valuesets.xml
    """
    Suspended = CanonicalStatusCodesForFHIRResourcesCode("suspended")
    """
    The process described/requested in the resource could not be completed, and no
    further action is planned
    From: http://hl7.org/fhir/resource-status in valuesets.xml
    """
    Failed = CanonicalStatusCodesForFHIRResourcesCode("failed")
    """
    The information in this resource has been replaced by information in another
    resource
    From: http://hl7.org/fhir/resource-status in valuesets.xml
    """
    Replaced = CanonicalStatusCodesForFHIRResourcesCode("replaced")
    """
    The process described/requested in the resource has been completed, and no
    further action is planned
    From: http://hl7.org/fhir/resource-status in valuesets.xml
    """
    Complete = CanonicalStatusCodesForFHIRResourcesCode("complete")
    """
    The resource describes information that is no longer valid or a process that
    is stopped occurring
    From: http://hl7.org/fhir/resource-status in valuesets.xml
    """
    Inactive = CanonicalStatusCodesForFHIRResourcesCode("inactive")
    """
    The process described/requested in the resource did not complete - usually due
    to some workflow error, and no further action is planned
    From: http://hl7.org/fhir/resource-status in valuesets.xml
    """
    Abandoned = CanonicalStatusCodesForFHIRResourcesCode("abandoned")
    """
    Authoring system does not know the status
    From: http://hl7.org/fhir/resource-status in valuesets.xml
    """
    Unknown = CanonicalStatusCodesForFHIRResourcesCode("unknown")
    """
    The information in this resource is not yet approved
    From: http://hl7.org/fhir/resource-status in valuesets.xml
    """
    Unconfirmed = CanonicalStatusCodesForFHIRResourcesCode("unconfirmed")
    """
    The information in this resource is approved
    From: http://hl7.org/fhir/resource-status in valuesets.xml
    """
    Confirmed = CanonicalStatusCodesForFHIRResourcesCode("confirmed")
    """
    The issue identified by this resource is no longer of concern
    From: http://hl7.org/fhir/resource-status in valuesets.xml
    """
    Resolved = CanonicalStatusCodesForFHIRResourcesCode("resolved")
    """
    This information has been ruled out by testing and evaluation
    From: http://hl7.org/fhir/resource-status in valuesets.xml
    """
    Refuted = CanonicalStatusCodesForFHIRResourcesCode("refuted")
    """
    Potentially true?
    From: http://hl7.org/fhir/resource-status in valuesets.xml
    """
    Differential = CanonicalStatusCodesForFHIRResourcesCode("differential")
    """
    This information is still being assembled
    From: http://hl7.org/fhir/resource-status in valuesets.xml
    """
    Partial = CanonicalStatusCodesForFHIRResourcesCode("partial")
    """
    not available at this time/location
    From: http://hl7.org/fhir/resource-status in valuesets.xml
    """
    Busy_unavailable = CanonicalStatusCodesForFHIRResourcesCode("busy-unavailable")
    """
    Free for scheduling
    From: http://hl7.org/fhir/resource-status in valuesets.xml
    """
    Free = CanonicalStatusCodesForFHIRResourcesCode("free")
    """
    Ready to act
    From: http://hl7.org/fhir/resource-status in valuesets.xml
    """
    On_target = CanonicalStatusCodesForFHIRResourcesCode("on-target")
    """
    Ahead of the planned timelines
    From: http://hl7.org/fhir/resource-status in valuesets.xml
    """
    Ahead_of_target = CanonicalStatusCodesForFHIRResourcesCode("ahead-of-target")
    """
    From: http://hl7.org/fhir/resource-status in valuesets.xml
    """
    Behind_target = CanonicalStatusCodesForFHIRResourcesCode("behind-target")
    """
    Behind the planned timelines
    From: http://hl7.org/fhir/resource-status in valuesets.xml
    """
    Not_ready = CanonicalStatusCodesForFHIRResourcesCode("not-ready")
    """
    The device transducer is disconnected
    From: http://hl7.org/fhir/resource-status in valuesets.xml
    """
    Transduc_discon = CanonicalStatusCodesForFHIRResourcesCode("transduc-discon")
    """
    The hardware is disconnected
    From: http://hl7.org/fhir/resource-status in valuesets.xml
    """
    Hw_discon = CanonicalStatusCodesForFHIRResourcesCode("hw-discon")
