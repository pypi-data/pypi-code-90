from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ProcedureOutcomeCodes_SNOMEDCT_Code(GenericTypeCode):
    """
    ProcedureOutcomeCodes(SNOMEDCT)
    From: http://hl7.org/fhir/ValueSet/procedure-outcome in valuesets.xml
        Procedure Outcome code: A selection of relevant SNOMED CT codes.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://snomed.info/sct
    """
    codeset: FhirUri = "http://snomed.info/sct"


class ProcedureOutcomeCodes_SNOMEDCT_CodeValues:
    """
    From: http://hl7.org/fhir/ValueSet/procedure-outcome in valuesets.xml
    """

    _385669000 = ProcedureOutcomeCodes_SNOMEDCT_Code("385669000")
    """
    From: http://hl7.org/fhir/ValueSet/procedure-outcome in valuesets.xml
    """
    _385671000 = ProcedureOutcomeCodes_SNOMEDCT_Code("385671000")
    """
    From: http://hl7.org/fhir/ValueSet/procedure-outcome in valuesets.xml
    """
    _385670004 = ProcedureOutcomeCodes_SNOMEDCT_Code("385670004")
