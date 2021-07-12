from __future__ import annotations
from typing import Optional, TYPE_CHECKING

from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString

from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase

from spark_auto_mapper_fhir.base_types.fhir_complex_type_base import FhirComplexTypeBase

if TYPE_CHECKING:
    pass
    # id_ (string)
    # extension (Extension)


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class Element(FhirComplexTypeBase):
    """
    Element
    fhir-base.xsd
        Base definition for all elements in a resource.
        If the element is present, it must have a value for at least one of the defined elements, an @id referenced from the Narrative, or extensions
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
    ) -> None:
        """
            Base definition for all elements in a resource.
            If the element is present, it must have a value for at least one of the
        defined elements, an @id referenced from the Narrative, or extensions

            :param id_: None
            :param extension: May be used to represent additional information that is not part of the basic
        definition of the element. To make the use of extensions safe and manageable,
        there is a strict set of governance  applied to the definition and use of
        extensions. Though any implementer can define an extension, there is a set of
        requirements that SHALL be met as part of the definition of the extension.
        """
        super().__init__(
            id_=id_,
            extension=extension,
        )
