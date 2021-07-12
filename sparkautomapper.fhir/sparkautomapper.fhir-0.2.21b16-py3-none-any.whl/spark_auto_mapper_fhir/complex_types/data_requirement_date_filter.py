from __future__ import annotations
from typing import Optional, TYPE_CHECKING

from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString


from spark_auto_mapper_fhir.base_types.fhir_complex_type_base import FhirComplexTypeBase

if TYPE_CHECKING:
    pass
    # id_ (string)
    # extension (Extension)
    from spark_auto_mapper_fhir.extensions.extension import Extension

    # path (string)
    # searchParam (string)
    # valueDateTime (dateTime)
    # valuePeriod (Period)
    from spark_auto_mapper_fhir.complex_types.period import Period

    # valueDuration (Duration)
    from spark_auto_mapper_fhir.complex_types.duration import Duration


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class DataRequirementDateFilter(FhirComplexTypeBase):
    """
    DataRequirement.DateFilter
    fhir-base.xsd
        Describes a required data item for evaluation in terms of the type of data, and optional code or date-based filters of the data.
        If the element is present, it must have a value for at least one of the defined elements, an @id referenced from the Narrative, or extensions
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[Extension]] = None,
        path: Optional[FhirString] = None,
        searchParam: Optional[FhirString] = None,
        valueDateTime: Optional[FhirDateTime] = None,
        valuePeriod: Optional[Period] = None,
        valueDuration: Optional[Duration] = None,
    ) -> None:
        """
            Describes a required data item for evaluation in terms of the type of data,
        and optional code or date-based filters of the data.
            If the element is present, it must have a value for at least one of the
        defined elements, an @id referenced from the Narrative, or extensions

            :param id_: None
            :param extension: May be used to represent additional information that is not part of the basic
        definition of the element. To make the use of extensions safe and manageable,
        there is a strict set of governance  applied to the definition and use of
        extensions. Though any implementer can define an extension, there is a set of
        requirements that SHALL be met as part of the definition of the extension.
            :param path: The date-valued attribute of the filter. The specified path SHALL be a
        FHIRPath resolveable on the specified type of the DataRequirement, and SHALL
        consist only of identifiers, constant indexers, and .resolve(). The path is
        allowed to contain qualifiers (.) to traverse sub-elements, as well as
        indexers ([x]) to traverse multiple-cardinality sub-elements (see the [Simple
        FHIRPath Profile](fhirpath.html#simple) for full details). Note that the index
        must be an integer constant. The path must resolve to an element of type date,
        dateTime, Period, Schedule, or Timing.
            :param searchParam: A date parameter that refers to a search parameter defined on the specified
        type of the DataRequirement, and which searches on elements of type date,
        dateTime, Period, Schedule, or Timing.
            :param valueDateTime: None
            :param valuePeriod: None
            :param valueDuration: None
        """
        super().__init__(
            id_=id_,
            extension=extension,
            path=path,
            searchParam=searchParam,
            valueDateTime=valueDateTime,
            valuePeriod=valuePeriod,
            valueDuration=valueDuration,
        )
