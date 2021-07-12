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
    # applicability (ChargeItemDefinition.Applicability)
    from spark_auto_mapper_fhir.backbone_elements.charge_item_definition_applicability import (
        ChargeItemDefinitionApplicability,
    )

    # priceComponent (ChargeItemDefinition.PriceComponent)
    from spark_auto_mapper_fhir.backbone_elements.charge_item_definition_price_component import (
        ChargeItemDefinitionPriceComponent,
    )


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ChargeItemDefinitionPropertyGroup(FhirBackboneElementBase):
    """
    ChargeItemDefinition.PropertyGroup
        The ChargeItemDefinition resource provides the properties that apply to the (billing) codes necessary to calculate costs and prices. The properties may differ largely depending on type and realm, therefore this resource gives only a rough structure and requires profiling for each type of billing code system.
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[Extension]] = None,
        modifierExtension: Optional[FhirList[Extension]] = None,
        applicability: Optional[FhirList[ChargeItemDefinitionApplicability]] = None,
        priceComponent: Optional[FhirList[ChargeItemDefinitionPriceComponent]] = None,
    ) -> None:
        """
            The ChargeItemDefinition resource provides the properties that apply to the
        (billing) codes necessary to calculate costs and prices. The properties may
        differ largely depending on type and realm, therefore this resource gives only
        a rough structure and requires profiling for each type of billing code system.

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
            :param applicability: Expressions that describe applicability criteria for the priceComponent.
            :param priceComponent: The price for a ChargeItem may be calculated as a base price with
        surcharges/deductions that apply in certain conditions. A ChargeItemDefinition
        resource that defines the prices, factors and conditions that apply to a
        billing code is currently under development. The priceComponent element can be
        used to offer transparency to the recipient of the Invoice of how the prices
        have been calculated.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            modifierExtension=modifierExtension,
            applicability=applicability,
            priceComponent=priceComponent,
        )
