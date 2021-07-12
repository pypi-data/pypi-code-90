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
    # identifier (Identifier)
    from spark_auto_mapper_fhir.complex_types.identifier import Identifier

    # country (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # End Import for References for country
    # Import for CodeableConcept for country
    from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode

    # End Import for CodeableConcept for country
    # jurisdiction (CodeableConcept)
    # End Import for References for jurisdiction
    # Import for CodeableConcept for jurisdiction
    # End Import for CodeableConcept for jurisdiction
    # legalStatusOfSupply (CodeableConcept)
    # End Import for References for legalStatusOfSupply
    # Import for CodeableConcept for legalStatusOfSupply
    # End Import for CodeableConcept for legalStatusOfSupply
    # validityPeriod (Period)
    from spark_auto_mapper_fhir.complex_types.period import Period


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class MedicinalProductAuthorizationJurisdictionalAuthorization(FhirBackboneElementBase):
    """
    MedicinalProductAuthorization.JurisdictionalAuthorization
        The regulatory authorization of a medicinal product.
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[Extension]] = None,
        modifierExtension: Optional[FhirList[Extension]] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        country: Optional[CodeableConcept[GenericTypeCode]] = None,
        jurisdiction: Optional[FhirList[CodeableConcept[GenericTypeCode]]] = None,
        legalStatusOfSupply: Optional[CodeableConcept[GenericTypeCode]] = None,
        validityPeriod: Optional[Period] = None,
    ) -> None:
        """
            The regulatory authorization of a medicinal product.

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
            :param identifier: The assigned number for the marketing authorization.
            :param country: Country of authorization.
            :param jurisdiction: Jurisdiction within a country.
            :param legalStatusOfSupply: The legal status of supply in a jurisdiction or region.
            :param validityPeriod: The start and expected end date of the authorization.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            modifierExtension=modifierExtension,
            identifier=identifier,
            country=country,
            jurisdiction=jurisdiction,
            legalStatusOfSupply=legalStatusOfSupply,
            validityPeriod=validityPeriod,
        )
