from __future__ import annotations
from typing import Optional, TYPE_CHECKING

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
    # category (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # End Import for References for category
    # Import for CodeableConcept for category
    from spark_auto_mapper_fhir.value_sets.adjudication_value_codes import (
        AdjudicationValueCodesCode,
    )

    # End Import for CodeableConcept for category
    # reason (CodeableConcept)
    # End Import for References for reason
    # Import for CodeableConcept for reason
    from spark_auto_mapper_fhir.value_sets.adjudication_reason_codes import (
        AdjudicationReasonCodesCode,
    )

    # End Import for CodeableConcept for reason
    # amount (Money)
    from spark_auto_mapper_fhir.complex_types.money import Money

    # value (decimal)
    from spark_auto_mapper_fhir.fhir_types.decimal import FhirDecimal


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ClaimResponseAdjudication(FhirBackboneElementBase):
    """
    ClaimResponse.Adjudication
        This resource provides the adjudication details from the processing of a Claim resource.
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[Extension]] = None,
        modifierExtension: Optional[FhirList[Extension]] = None,
        category: CodeableConcept[AdjudicationValueCodesCode],
        reason: Optional[CodeableConcept[AdjudicationReasonCodesCode]] = None,
        amount: Optional[Money] = None,
        value: Optional[FhirDecimal] = None,
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
            :param category: A code to indicate the information type of this adjudication record.
        Information types may include the value submitted, maximum values or
        percentages allowed or payable under the plan, amounts that: the patient is
        responsible for in aggregate or pertaining to this item; amounts paid by other
        coverages; and, the benefit payable for this item.
            :param reason: A code supporting the understanding of the adjudication result and explaining
        variance from expected amount.
            :param amount: Monetary amount associated with the category.
            :param value: A non-monetary value associated with the category. Mutually exclusive to the
        amount element above.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            modifierExtension=modifierExtension,
            category=category,
            reason=reason,
            amount=amount,
            value=value,
        )
