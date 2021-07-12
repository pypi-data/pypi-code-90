from __future__ import annotations
from typing import Optional, TYPE_CHECKING

from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase

from spark_auto_mapper_fhir.base_types.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)

if TYPE_CHECKING:
    pass
    # id_ (string)
    # extension (Extension)
    # modifierExtension (Extension)
    # baseFormulaType (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # End Import for References for baseFormulaType
    # Import for CodeableConcept for baseFormulaType
    from spark_auto_mapper_fhir.value_sets.enteral_formula_type_codes import (
        EnteralFormulaTypeCodesCode,
    )

    # End Import for CodeableConcept for baseFormulaType
    # baseFormulaProductName (string)
    # additiveType (CodeableConcept)
    # End Import for References for additiveType
    # Import for CodeableConcept for additiveType
    from spark_auto_mapper_fhir.value_sets.enteral_formula_additive_type_code import (
        EnteralFormulaAdditiveTypeCodeCode,
    )

    # End Import for CodeableConcept for additiveType
    # additiveProductName (string)
    # caloricDensity (Quantity)
    from spark_auto_mapper_fhir.complex_types.quantity import Quantity

    # routeofAdministration (CodeableConcept)
    # End Import for References for routeofAdministration
    # Import for CodeableConcept for routeofAdministration
    from spark_auto_mapper_fhir.value_sets.enteral_route_codes import (
        EnteralRouteCodesCode,
    )

    # End Import for CodeableConcept for routeofAdministration
    # administration (NutritionOrder.Administration)
    from spark_auto_mapper_fhir.backbone_elements.nutrition_order_administration import (
        NutritionOrderAdministration,
    )

    # maxVolumeToDeliver (Quantity)
    # administrationInstruction (string)


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class NutritionOrderEnteralFormula(FhirBackboneElementBase):
    """
    NutritionOrder.EnteralFormula
        A request to supply a diet, formula feeding (enteral) or oral nutritional supplement to a patient/resident.
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        modifierExtension: Optional[FhirList[ExtensionBase]] = None,
        baseFormulaType: Optional[CodeableConcept[EnteralFormulaTypeCodesCode]] = None,
        baseFormulaProductName: Optional[FhirString] = None,
        additiveType: Optional[
            CodeableConcept[EnteralFormulaAdditiveTypeCodeCode]
        ] = None,
        additiveProductName: Optional[FhirString] = None,
        caloricDensity: Optional[Quantity] = None,
        routeofAdministration: Optional[CodeableConcept[EnteralRouteCodesCode]] = None,
        administration: Optional[FhirList[NutritionOrderAdministration]] = None,
        maxVolumeToDeliver: Optional[Quantity] = None,
        administrationInstruction: Optional[FhirString] = None,
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
            :param baseFormulaType: The type of enteral or infant formula such as an adult standard formula with
        fiber or a soy-based infant formula.
            :param baseFormulaProductName: The product or brand name of the enteral or infant formula product such as
        "ACME Adult Standard Formula".
            :param additiveType: Indicates the type of modular component such as protein, carbohydrate, fat or
        fiber to be provided in addition to or mixed with the base formula.
            :param additiveProductName: The product or brand name of the type of modular component to be added to the
        formula.
            :param caloricDensity: The amount of energy (calories) that the formula should provide per specified
        volume, typically per mL or fluid oz.  For example, an infant may require a
        formula that provides 24 calories per fluid ounce or an adult may require an
        enteral formula that provides 1.5 calorie/mL.
            :param routeofAdministration: The route or physiological path of administration into the patient's
        gastrointestinal  tract for purposes of providing the formula feeding, e.g.
        nasogastric tube.
            :param administration: Formula administration instructions as structured data.  This repeating
        structure allows for changing the administration rate or volume over time for
        both bolus and continuous feeding.  An example of this would be an instruction
        to increase the rate of continuous feeding every 2 hours.
            :param maxVolumeToDeliver: The maximum total quantity of formula that may be administered to a subject
        over the period of time, e.g. 1440 mL over 24 hours.
            :param administrationInstruction: Free text formula administration, feeding instructions or additional
        instructions or information.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            modifierExtension=modifierExtension,
            baseFormulaType=baseFormulaType,
            baseFormulaProductName=baseFormulaProductName,
            additiveType=additiveType,
            additiveProductName=additiveProductName,
            caloricDensity=caloricDensity,
            routeofAdministration=routeofAdministration,
            administration=administration,
            maxVolumeToDeliver=maxVolumeToDeliver,
            administrationInstruction=administrationInstruction,
        )
