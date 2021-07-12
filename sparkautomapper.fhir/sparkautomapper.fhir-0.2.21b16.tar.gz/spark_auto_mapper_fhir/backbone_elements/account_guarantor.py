from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString

from spark_auto_mapper_fhir.base_types.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)

if TYPE_CHECKING:
    pass
    # id_ (string)
    # extension (Extension)
    from spark_auto_mapper_fhir.extensions.extension import Extension

    # modifierExtension (Extension)
    # party (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for party
    from spark_auto_mapper_fhir.resources.patient import Patient
    from spark_auto_mapper_fhir.resources.related_person import RelatedPerson
    from spark_auto_mapper_fhir.resources.organization import Organization

    # onHold (boolean)
    # period (Period)
    from spark_auto_mapper_fhir.complex_types.period import Period


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class AccountGuarantor(FhirBackboneElementBase):
    """
    Account.Guarantor
        A financial tool for tracking value accrued for a particular purpose.  In the healthcare field, used to track charges for a patient, cost centers, etc.
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[Extension]] = None,
        modifierExtension: Optional[FhirList[Extension]] = None,
        party: Reference[Union[Patient, RelatedPerson, Organization]],
        onHold: Optional[FhirBoolean] = None,
        period: Optional[Period] = None,
    ) -> None:
        """
            A financial tool for tracking value accrued for a particular purpose.  In the
        healthcare field, used to track charges for a patient, cost centers, etc.

            :param id_: None
            :param extension: May be used to represent additional information that is not part of the basic
        definition of the element. To make the use of extensions safe and manageable,
        there is a strict set of governance  applied to the definition and use of
        extensions. Though any implementer can define an extension, there is a set of
        requirements that SHALL be met as part of the definition of the extension.
            :param modifierExtension: May be used to represent additional information that is not part of the basic
        definition of the element and that modifies the understanding of the element
        in which it is contained and/or the understanding of the containing element's
        descendants. Usually modifier elements provide negation or qualification. To
        make the use of extensions safe and manageable, there is a strict set of
        governance applied to the definition and use of extensions. Though any
        implementer can define an extension, there is a set of requirements that SHALL
        be met as part of the definition of the extension. Applications processing a
        resource are required to check for modifier extensions.

        Modifier extensions SHALL NOT change the meaning of any elements on Resource
        or DomainResource (including cannot change the meaning of modifierExtension
        itself).
            :param party: The entity who is responsible.
            :param onHold: A guarantor may be placed on credit hold or otherwise have their role
        temporarily suspended.
            :param period: The timeframe during which the guarantor accepts responsibility for the
        account.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            modifierExtension=modifierExtension,
            party=party,
            onHold=onHold,
            period=period,
        )
