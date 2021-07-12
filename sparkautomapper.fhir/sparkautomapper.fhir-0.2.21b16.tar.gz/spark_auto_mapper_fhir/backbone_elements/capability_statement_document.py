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
    # mode (DocumentMode)
    from spark_auto_mapper_fhir.value_sets.document_mode import DocumentModeCode

    # documentation (markdown)
    from spark_auto_mapper_fhir.fhir_types.markdown import FhirMarkdown

    # profile (canonical)
    from spark_auto_mapper_fhir.fhir_types.canonical import FhirCanonical


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class CapabilityStatementDocument(FhirBackboneElementBase):
    """
    CapabilityStatement.Document
        A Capability Statement documents a set of capabilities (behaviors) of a FHIR Server for a particular version of FHIR that may be used as a statement of actual server functionality or a statement of required or desired server implementation.
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[Extension]] = None,
        modifierExtension: Optional[FhirList[Extension]] = None,
        mode: DocumentModeCode,
        documentation: Optional[FhirMarkdown] = None,
        profile: FhirCanonical,
    ) -> None:
        """
            A Capability Statement documents a set of capabilities (behaviors) of a FHIR
        Server for a particular version of FHIR that may be used as a statement of
        actual server functionality or a statement of required or desired server
        implementation.

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
            :param mode: Mode of this document declaration - whether an application is a producer or
        consumer.
            :param documentation: A description of how the application supports or uses the specified document
        profile.  For example, when documents are created, what action is taken with
        consumed documents, etc.
            :param profile: A profile on the document Bundle that constrains which resources are present,
        and their contents.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            modifierExtension=modifierExtension,
            mode=mode,
            documentation=documentation,
            profile=profile,
        )
