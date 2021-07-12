from __future__ import annotations
from typing import Optional, TYPE_CHECKING

from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.resources.resource import Resource

from spark_auto_mapper_fhir.base_types.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)

if TYPE_CHECKING:
    pass
    # id_ (string)
    # extension (Extension)
    # modifierExtension (Extension)
    # flag (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # End Import for References for flag
    # Import for CodeableConcept for flag
    from spark_auto_mapper_fhir.value_sets.patient_medicine_change_types import (
        PatientMedicineChangeTypesCode,
    )

    # End Import for CodeableConcept for flag
    # deleted (boolean)
    # date (dateTime)
    # item (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for item


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ListEntry(FhirBackboneElementBase):
    """
    List.Entry
        A list is a curated collection of resources.
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        modifierExtension: Optional[FhirList[ExtensionBase]] = None,
        flag: Optional[CodeableConcept[PatientMedicineChangeTypesCode]] = None,
        deleted: Optional[FhirBoolean] = None,
        date: Optional[FhirDateTime] = None,
        item: Reference[Resource],
    ) -> None:
        """
            A list is a curated collection of resources.

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
            :param flag: The flag allows the system constructing the list to indicate the role and
        significance of the item in the list.
            :param deleted: True if this item is marked as deleted in the list.
            :param date: When this item was added to the list.
            :param item: A reference to the actual resource from which data was derived.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            modifierExtension=modifierExtension,
            flag=flag,
            deleted=deleted,
            date=date,
            item=item,
        )
