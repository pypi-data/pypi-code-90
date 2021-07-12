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
    # schedule (Timing)
    from spark_auto_mapper_fhir.backbone_elements.timing import Timing

    # quantity (Quantity)
    from spark_auto_mapper_fhir.complex_types.quantity import Quantity

    # rateQuantity (Quantity)
    # rateRatio (Ratio)
    from spark_auto_mapper_fhir.complex_types.ratio import Ratio


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class NutritionOrderAdministration(FhirBackboneElementBase):
    """
    NutritionOrder.Administration
        A request to supply a diet, formula feeding (enteral) or oral nutritional supplement to a patient/resident.
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[Extension]] = None,
        modifierExtension: Optional[FhirList[Extension]] = None,
        schedule: Optional[Timing] = None,
        quantity: Optional[Quantity] = None,
        rateQuantity: Optional[Quantity] = None,
        rateRatio: Optional[Ratio] = None,
    ) -> None:
        """
            A request to supply a diet, formula feeding (enteral) or oral nutritional
        supplement to a patient/resident.

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
            :param schedule: The time period and frequency at which the enteral formula should be delivered
        to the patient.
            :param quantity: The volume of formula to provide to the patient per the specified
        administration schedule.
            :param rateQuantity: None
            :param rateRatio: None
        """
        super().__init__(
            id_=id_,
            extension=extension,
            modifierExtension=modifierExtension,
            schedule=schedule,
            quantity=quantity,
            rateQuantity=rateQuantity,
            rateRatio=rateRatio,
        )
