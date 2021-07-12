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
    # role (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # End Import for References for role
    # Import for CodeableConcept for role
    from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode

    # End Import for CodeableConcept for role
    # identifier (Identifier)
    from spark_auto_mapper_fhir.complex_types.identifier import Identifier

    # name (string)
    # stereochemistry (CodeableConcept)
    # End Import for References for stereochemistry
    # Import for CodeableConcept for stereochemistry
    # End Import for CodeableConcept for stereochemistry
    # opticalActivity (CodeableConcept)
    # End Import for References for opticalActivity
    # Import for CodeableConcept for opticalActivity
    # End Import for CodeableConcept for opticalActivity
    # molecularFormula (string)
    # amountQuantity (Quantity)
    from spark_auto_mapper_fhir.complex_types.quantity import Quantity

    # amountString (string)


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class SubstanceSpecificationMoiety(FhirBackboneElementBase):
    """
    SubstanceSpecification.Moiety
        The detailed description of a substance, typically at a level beyond what is used for prescribing.
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        modifierExtension: Optional[FhirList[ExtensionBase]] = None,
        role: Optional[CodeableConcept[GenericTypeCode]] = None,
        identifier: Optional[Identifier] = None,
        name: Optional[FhirString] = None,
        stereochemistry: Optional[CodeableConcept[GenericTypeCode]] = None,
        opticalActivity: Optional[CodeableConcept[GenericTypeCode]] = None,
        molecularFormula: Optional[FhirString] = None,
        amountQuantity: Optional[Quantity] = None,
        amountString: Optional[FhirString] = None,
    ) -> None:
        """
            The detailed description of a substance, typically at a level beyond what is
        used for prescribing.

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
            :param role: Role that the moiety is playing.
            :param identifier: Identifier by which this moiety substance is known.
            :param name: Textual name for this moiety substance.
            :param stereochemistry: Stereochemistry type.
            :param opticalActivity: Optical activity type.
            :param molecularFormula: Molecular formula.
            :param amountQuantity: None
            :param amountString: None
        """
        super().__init__(
            id_=id_,
            extension=extension,
            modifierExtension=modifierExtension,
            role=role,
            identifier=identifier,
            name=name,
            stereochemistry=stereochemistry,
            opticalActivity=opticalActivity,
            molecularFormula=molecularFormula,
            amountQuantity=amountQuantity,
            amountString=amountString,
        )
