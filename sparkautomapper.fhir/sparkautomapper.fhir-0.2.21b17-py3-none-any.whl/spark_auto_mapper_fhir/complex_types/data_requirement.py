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
    # type_ (FHIRAllTypes)
    from spark_auto_mapper_fhir.value_sets.fhir_all_types import FHIRAllTypesCode

    # profile (canonical)
    from spark_auto_mapper_fhir.fhir_types.canonical import FhirCanonical

    # subjectCodeableConcept (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for subjectCodeableConcept
    from spark_auto_mapper_fhir.value_sets.subject_type import SubjectTypeCode

    # End Import for CodeableConcept for subjectCodeableConcept
    # subjectReference (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for subjectReference
    from spark_auto_mapper_fhir.resources.group import Group

    # mustSupport (string)
    # codeFilter (DataRequirement.CodeFilter)
    from spark_auto_mapper_fhir.complex_types.data_requirement_code_filter import (
        DataRequirementCodeFilter,
    )

    # dateFilter (DataRequirement.DateFilter)
    from spark_auto_mapper_fhir.complex_types.data_requirement_date_filter import (
        DataRequirementDateFilter,
    )

    # limit (positiveInt)
    from spark_auto_mapper_fhir.fhir_types.positive_int import FhirPositiveInt

    # sort (DataRequirement.Sort)
    from spark_auto_mapper_fhir.complex_types.data_requirement_sort import (
        DataRequirementSort,
    )


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class DataRequirement(FhirComplexTypeBase):
    """
    DataRequirement
    fhir-base.xsd
        Describes a required data item for evaluation in terms of the type of data, and optional code or date-based filters of the data.
        If the element is present, it must have a value for at least one of the defined elements, an @id referenced from the Narrative, or extensions
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        type_: FHIRAllTypesCode,
        profile: Optional[FhirList[FhirCanonical]] = None,
        subjectCodeableConcept: Optional[CodeableConcept[SubjectTypeCode]] = None,
        subjectReference: Optional[Reference[Group]] = None,
        mustSupport: Optional[FhirList[FhirString]] = None,
        codeFilter: Optional[FhirList[DataRequirementCodeFilter]] = None,
        dateFilter: Optional[FhirList[DataRequirementDateFilter]] = None,
        limit: Optional[FhirPositiveInt] = None,
        sort: Optional[FhirList[DataRequirementSort]] = None,
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
            :param type_: The type of the required data, specified as the type name of a resource. For
        profiles, this value is set to the type of the base resource of the profile.
            :param profile: The profile of the required data, specified as the uri of the profile
        definition.
            :param subjectCodeableConcept: None
            :param subjectReference: None
            :param mustSupport: Indicates that specific elements of the type are referenced by the knowledge
        module and must be supported by the consumer in order to obtain an effective
        evaluation. This does not mean that a value is required for this element, only
        that the consuming system must understand the element and be able to provide
        values for it if they are available.

        The value of mustSupport SHALL be a FHIRPath resolveable on the type of the
        DataRequirement. The path SHALL consist only of identifiers, constant
        indexers, and .resolve() (see the [Simple FHIRPath
        Profile](fhirpath.html#simple) for full details).
            :param codeFilter: Code filters specify additional constraints on the data, specifying the value
        set of interest for a particular element of the data. Each code filter defines
        an additional constraint on the data, i.e. code filters are AND'ed, not OR'ed.
            :param dateFilter: Date filters specify additional constraints on the data in terms of the
        applicable date range for specific elements. Each date filter specifies an
        additional constraint on the data, i.e. date filters are AND'ed, not OR'ed.
            :param limit: Specifies a maximum number of results that are required (uses the _count
        search parameter).
            :param sort: Specifies the order of the results to be returned.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            type_=type_,
            profile=profile,
            subjectCodeableConcept=subjectCodeableConcept,
            subjectReference=subjectReference,
            mustSupport=mustSupport,
            codeFilter=codeFilter,
            dateFilter=dateFilter,
            limit=limit,
            sort=sort,
        )
