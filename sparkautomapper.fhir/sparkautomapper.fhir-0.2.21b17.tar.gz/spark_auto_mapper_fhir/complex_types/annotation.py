from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString

from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase

from spark_auto_mapper_fhir.base_types.fhir_complex_type_base import FhirComplexTypeBase

if TYPE_CHECKING:
    pass
    # id_ (string)
    # extension (Extension)
    # authorReference (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for authorReference
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.patient import Patient
    from spark_auto_mapper_fhir.resources.related_person import RelatedPerson
    from spark_auto_mapper_fhir.resources.organization import Organization

    # authorString (string)
    # time (dateTime)
    # text (markdown)
    from spark_auto_mapper_fhir.fhir_types.markdown import FhirMarkdown


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class Annotation(FhirComplexTypeBase):
    """
    Annotation
    fhir-base.xsd
        A  text note which also  contains information about who made the statement and when.
        If the element is present, it must have a value for at least one of the defined elements, an @id referenced from the Narrative, or extensions
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        authorReference: Optional[
            Reference[Union[Practitioner, Patient, RelatedPerson, Organization]]
        ] = None,
        authorString: Optional[FhirString] = None,
        time: Optional[FhirDateTime] = None,
        text: FhirMarkdown,
    ) -> None:
        """
            A  text note which also  contains information about who made the statement and
        when.
            If the element is present, it must have a value for at least one of the
        defined elements, an @id referenced from the Narrative, or extensions

            :param id_: None
            :param extension: May be used to represent additional information that is not part of the basic
        definition of the element. To make the use of extensions safe and manageable,
        there is a strict set of governance  applied to the definition and use of
        extensions. Though any implementer can define an extension, there is a set of
        requirements that SHALL be met as part of the definition of the extension.
            :param authorReference: None
            :param authorString: None
            :param time: Indicates when this particular annotation was made.
            :param text: The text of the annotation in markdown format.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            authorReference=authorReference,
            authorString=authorString,
            time=time,
            text=text,
        )
