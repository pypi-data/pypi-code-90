from __future__ import annotations
from typing import Optional, TYPE_CHECKING

from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
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
    # description (string)
    # timeDateTime (dateTime)
    # timePeriod (Period)
    from spark_auto_mapper_fhir.complex_types.period import Period


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class BiologicallyDerivedProductManipulation(FhirBackboneElementBase):
    """
        BiologicallyDerivedProduct.Manipulation
            A material substance originating from a biological entity intended to be transplanted or infused
    into another (possibly the same) biological entity.
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[Extension]] = None,
        modifierExtension: Optional[FhirList[Extension]] = None,
        description: Optional[FhirString] = None,
        timeDateTime: Optional[FhirDateTime] = None,
        timePeriod: Optional[Period] = None,
    ) -> None:
        """
            A material substance originating from a biological entity intended to be
        transplanted or infused
        into another (possibly the same) biological entity.

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
            :param description: Description of manipulation.
            :param timeDateTime: None
            :param timePeriod: None
        """
        super().__init__(
            id_=id_,
            extension=extension,
            modifierExtension=modifierExtension,
            description=description,
            timeDateTime=timeDateTime,
            timePeriod=timePeriod,
        )
