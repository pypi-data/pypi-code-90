from __future__ import annotations
from typing import Optional, TYPE_CHECKING

from spark_auto_mapper_fhir.fhir_types.date import FhirDate
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
    # type_ (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # End Import for References for type_
    # Import for CodeableConcept for type_
    from spark_auto_mapper_fhir.value_sets.example_payment_type_codes import (
        ExamplePaymentTypeCodesCode,
    )

    # End Import for CodeableConcept for type_
    # adjustment (Money)
    from spark_auto_mapper_fhir.complex_types.money import Money

    # adjustmentReason (CodeableConcept)
    # End Import for References for adjustmentReason
    # Import for CodeableConcept for adjustmentReason
    from spark_auto_mapper_fhir.value_sets.payment_adjustment_reason_codes import (
        PaymentAdjustmentReasonCodesCode,
    )

    # End Import for CodeableConcept for adjustmentReason
    # date (date)
    # amount (Money)
    # identifier (Identifier)
    from spark_auto_mapper_fhir.complex_types.identifier import Identifier


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ClaimResponsePayment(FhirBackboneElementBase):
    """
    ClaimResponse.Payment
        This resource provides the adjudication details from the processing of a Claim resource.
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[Extension]] = None,
        modifierExtension: Optional[FhirList[Extension]] = None,
        type_: CodeableConcept[ExamplePaymentTypeCodesCode],
        adjustment: Optional[Money] = None,
        adjustmentReason: Optional[
            CodeableConcept[PaymentAdjustmentReasonCodesCode]
        ] = None,
        date: Optional[FhirDate] = None,
        amount: Money,
        identifier: Optional[Identifier] = None,
    ) -> None:
        """
            This resource provides the adjudication details from the processing of a Claim
        resource.

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
            :param type_: Whether this represents partial or complete payment of the benefits payable.
            :param adjustment: Total amount of all adjustments to this payment included in this transaction
        which are not related to this claim's adjudication.
            :param adjustmentReason: Reason for the payment adjustment.
            :param date: Estimated date the payment will be issued or the actual issue date of payment.
            :param amount: Benefits payable less any payment adjustment.
            :param identifier: Issuer's unique identifier for the payment instrument.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            modifierExtension=modifierExtension,
            type_=type_,
            adjustment=adjustment,
            adjustmentReason=adjustmentReason,
            date=date,
            amount=amount,
            identifier=identifier,
        )
