from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

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
    # function (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # End Import for References for function
    # Import for CodeableConcept for function
    from spark_auto_mapper_fhir.value_sets.procedure_performer_role_codes import (
        ProcedurePerformerRoleCodesCode,
    )

    # End Import for CodeableConcept for function
    # actor (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for actor
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
    from spark_auto_mapper_fhir.resources.organization import Organization
    from spark_auto_mapper_fhir.resources.care_team import CareTeam
    from spark_auto_mapper_fhir.resources.patient import Patient
    from spark_auto_mapper_fhir.resources.device import Device
    from spark_auto_mapper_fhir.resources.related_person import RelatedPerson


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ChargeItemPerformer(FhirBackboneElementBase):
    """
    ChargeItem.Performer
        The resource ChargeItem describes the provision of healthcare provider products for a certain patient, therefore referring not only to the product, but containing in addition details of the provision, like date, time, amounts and participating organizations and persons. Main Usage of the ChargeItem is to enable the billing process and internal cost allocation.
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[Extension]] = None,
        modifierExtension: Optional[FhirList[Extension]] = None,
        function: Optional[CodeableConcept[ProcedurePerformerRoleCodesCode]] = None,
        actor: Reference[
            Union[
                Practitioner,
                PractitionerRole,
                Organization,
                CareTeam,
                Patient,
                Device,
                RelatedPerson,
            ]
        ],
    ) -> None:
        """
            The resource ChargeItem describes the provision of healthcare provider
        products for a certain patient, therefore referring not only to the product,
        but containing in addition details of the provision, like date, time, amounts
        and participating organizations and persons. Main Usage of the ChargeItem is
        to enable the billing process and internal cost allocation.

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
            :param function: Describes the type of performance or participation(e.g. primary surgeon,
        anesthesiologiest, etc.).
            :param actor: The device, practitioner, etc. who performed or participated in the service.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            modifierExtension=modifierExtension,
            function=function,
            actor=actor,
        )
