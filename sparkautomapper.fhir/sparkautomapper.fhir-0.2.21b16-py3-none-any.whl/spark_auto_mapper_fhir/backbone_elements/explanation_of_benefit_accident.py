from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

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
    # date (date)
    # type_ (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # End Import for References for type_
    # Import for CodeableConcept for type_
    from spark_auto_mapper_fhir.value_sets.act_incident_code import ActIncidentCode

    # End Import for CodeableConcept for type_
    # locationAddress (Address)
    from spark_auto_mapper_fhir.complex_types.address import Address

    # locationReference (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for locationReference
    from spark_auto_mapper_fhir.resources.location import Location


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ExplanationOfBenefitAccident(FhirBackboneElementBase):
    """
    ExplanationOfBenefit.Accident
        This resource provides: the claim details; adjudication details from the processing of a Claim; and optionally account balance information, for informing the subscriber of the benefits provided.
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[Extension]] = None,
        modifierExtension: Optional[FhirList[Extension]] = None,
        date: Optional[FhirDate] = None,
        type_: Optional[CodeableConcept[ActIncidentCode]] = None,
        locationAddress: Optional[Address] = None,
        locationReference: Optional[Reference[Union[Location]]] = None,
    ) -> None:
        """
            This resource provides: the claim details; adjudication details from the
        processing of a Claim; and optionally account balance information, for
        informing the subscriber of the benefits provided.

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
            :param date: Date of an accident event  related to the products and services contained in
        the claim.
            :param type_: The type or context of the accident event for the purposes of selection of
        potential insurance coverages and determination of coordination between
        insurers.
            :param locationAddress: None
            :param locationReference: None
        """
        super().__init__(
            id_=id_,
            extension=extension,
            modifierExtension=modifierExtension,
            date=date,
            type_=type_,
            locationAddress=locationAddress,
            locationReference=locationReference,
        )
