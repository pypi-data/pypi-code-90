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
    # productOrService (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # End Import for References for productOrService
    # Import for CodeableConcept for productOrService
    from spark_auto_mapper_fhir.value_sets.uscls_codes import USCLSCodesCode

    # End Import for CodeableConcept for productOrService
    # modifier (CodeableConcept)
    # End Import for References for modifier
    # Import for CodeableConcept for modifier
    from spark_auto_mapper_fhir.value_sets.modifier_type_codes import (
        ModifierTypeCodesCode,
    )

    # End Import for CodeableConcept for modifier
    # quantity (Quantity)
    from spark_auto_mapper_fhir.complex_types.quantity import Quantity

    # unitPrice (Money)
    from spark_auto_mapper_fhir.complex_types.money import Money

    # factor (decimal)
    from spark_auto_mapper_fhir.fhir_types.decimal import FhirDecimal

    # net (Money)
    # noteNumber (positiveInt)
    from spark_auto_mapper_fhir.fhir_types.positive_int import FhirPositiveInt

    # adjudication (ClaimResponse.Adjudication)
    from spark_auto_mapper_fhir.backbone_elements.claim_response_adjudication import (
        ClaimResponseAdjudication,
    )


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ClaimResponseSubDetail1(FhirBackboneElementBase):
    """
    ClaimResponse.SubDetail1
        This resource provides the adjudication details from the processing of a Claim resource.
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[Extension]] = None,
        modifierExtension: Optional[FhirList[Extension]] = None,
        productOrService: CodeableConcept[USCLSCodesCode],
        modifier: Optional[FhirList[CodeableConcept[ModifierTypeCodesCode]]] = None,
        quantity: Optional[Quantity] = None,
        unitPrice: Optional[Money] = None,
        factor: Optional[FhirDecimal] = None,
        net: Optional[Money] = None,
        noteNumber: Optional[FhirList[FhirPositiveInt]] = None,
        adjudication: FhirList[ClaimResponseAdjudication],
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
            :param productOrService: When the value is a group code then this item collects a set of related claim
        details, otherwise this contains the product, service, drug or other billing
        code for the item.
            :param modifier: Item typification or modifiers codes to convey additional context for the
        product or service.
            :param quantity: The number of repetitions of a service or product.
            :param unitPrice: If the item is not a group then this is the fee for the product or service,
        otherwise this is the total of the fees for the details of the group.
            :param factor: A real number that represents a multiplier used in determining the overall
        value of services delivered and/or goods received. The concept of a Factor
        allows for a discount or surcharge multiplier to be applied to a monetary
        amount.
            :param net: The quantity times the unit price for an additional service or product or
        charge.
            :param noteNumber: The numbers associated with notes below which apply to the adjudication of
        this item.
            :param adjudication: The adjudication results.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            modifierExtension=modifierExtension,
            productOrService=productOrService,
            modifier=modifier,
            quantity=quantity,
            unitPrice=unitPrice,
            factor=factor,
            net=net,
            noteNumber=noteNumber,
            adjudication=adjudication,
        )
