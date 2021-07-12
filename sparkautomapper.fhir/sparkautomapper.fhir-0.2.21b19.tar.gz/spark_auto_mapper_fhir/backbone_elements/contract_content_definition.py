from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase

from spark_auto_mapper_fhir.base_types.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)

if TYPE_CHECKING:
    pass
    # id_ (string)
    # extension (Extension)
    # modifierExtension (Extension)
    # type_ (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # End Import for References for type_
    # Import for CodeableConcept for type_
    from spark_auto_mapper_fhir.value_sets.contract_resource_definition_type_codes import (
        ContractResourceDefinitionTypeCodesCode,
    )

    # End Import for CodeableConcept for type_
    # subType (CodeableConcept)
    # End Import for References for subType
    # Import for CodeableConcept for subType
    from spark_auto_mapper_fhir.value_sets.contract_resource_definition_subtype_codes import (
        ContractResourceDefinitionSubtypeCodesCode,
    )

    # End Import for CodeableConcept for subType
    # publisher (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for publisher
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
    from spark_auto_mapper_fhir.resources.organization import Organization

    # publicationDate (dateTime)
    # publicationStatus (ContractResourcePublicationStatusCodes)
    from spark_auto_mapper_fhir.value_sets.contract_resource_publication_status_codes import (
        ContractResourcePublicationStatusCodesCode,
    )

    # copyright (markdown)
    from spark_auto_mapper_fhir.fhir_types.markdown import FhirMarkdown


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ContractContentDefinition(FhirBackboneElementBase):
    """
    Contract.ContentDefinition
        Legally enforceable, formally recorded unilateral or bilateral directive i.e., a policy or agreement.
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        modifierExtension: Optional[FhirList[ExtensionBase]] = None,
        type_: CodeableConcept[ContractResourceDefinitionTypeCodesCode],
        subType: Optional[
            CodeableConcept[ContractResourceDefinitionSubtypeCodesCode]
        ] = None,
        publisher: Optional[
            Reference[Union[Practitioner, PractitionerRole, Organization]]
        ] = None,
        publicationDate: Optional[FhirDateTime] = None,
        publicationStatus: ContractResourcePublicationStatusCodesCode,
        copyright: Optional[FhirMarkdown] = None,
    ) -> None:
        """
            Legally enforceable, formally recorded unilateral or bilateral directive i.e.,
        a policy or agreement.

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
            :param type_: Precusory content structure and use, i.e., a boilerplate, template,
        application for a contract such as an insurance policy or benefits under a
        program, e.g., workers compensation.
            :param subType: Detailed Precusory content type.
            :param publisher: The  individual or organization that published the Contract precursor content.
            :param publicationDate: The date (and optionally time) when the contract was published. The date must
        change when the business version changes and it must change if the status code
        changes. In addition, it should change when the substantive content of the
        contract changes.
            :param publicationStatus: amended | appended | cancelled | disputed | entered-in-error | executable |
        executed | negotiable | offered | policy | rejected | renewed | revoked |
        resolved | terminated.
            :param copyright: A copyright statement relating to Contract precursor content. Copyright
        statements are generally legal restrictions on the use and publishing of the
        Contract precursor content.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            modifierExtension=modifierExtension,
            type_=type_,
            subType=subType,
            publisher=publisher,
            publicationDate=publicationDate,
            publicationStatus=publicationStatus,
            copyright=copyright,
        )
