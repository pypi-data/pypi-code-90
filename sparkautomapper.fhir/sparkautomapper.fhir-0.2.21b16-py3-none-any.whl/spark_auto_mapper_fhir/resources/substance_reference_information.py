from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.substancereferenceinformation import (
    SubstanceReferenceInformationSchema,
)

if TYPE_CHECKING:
    pass
    # id_ (id)
    # meta (Meta)
    # implicitRules (uri)
    # language (CommonLanguages)
    from spark_auto_mapper_fhir.value_sets.common_languages import CommonLanguagesCode

    # text (Narrative)
    from spark_auto_mapper_fhir.complex_types.narrative import Narrative

    # contained (ResourceContainer)
    from spark_auto_mapper_fhir.complex_types.resource_container import (
        ResourceContainer,
    )

    # extension (Extension)
    from spark_auto_mapper_fhir.extensions.extension import Extension

    # modifierExtension (Extension)
    # comment (string)
    # gene (SubstanceReferenceInformation.Gene)
    from spark_auto_mapper_fhir.backbone_elements.substance_reference_information_gene import (
        SubstanceReferenceInformationGene,
    )

    # geneElement (SubstanceReferenceInformation.GeneElement)
    from spark_auto_mapper_fhir.backbone_elements.substance_reference_information_gene_element import (
        SubstanceReferenceInformationGeneElement,
    )

    # classification (SubstanceReferenceInformation.Classification)
    from spark_auto_mapper_fhir.backbone_elements.substance_reference_information_classification import (
        SubstanceReferenceInformationClassification,
    )

    # target (SubstanceReferenceInformation.Target)
    from spark_auto_mapper_fhir.backbone_elements.substance_reference_information_target import (
        SubstanceReferenceInformationTarget,
    )


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class SubstanceReferenceInformation(FhirResourceBase):
    """
    SubstanceReferenceInformation
    substancereferenceinformation.xsd
        Todo.
        If the element is present, it must have either a @value, an @id, or extensions
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        meta: Optional[Meta] = None,
        implicitRules: Optional[FhirUri] = None,
        language: Optional[CommonLanguagesCode] = None,
        text: Optional[Narrative] = None,
        contained: Optional[FhirList[ResourceContainer]] = None,
        extension: Optional[FhirList[Extension]] = None,
        modifierExtension: Optional[FhirList[Extension]] = None,
        comment: Optional[FhirString] = None,
        gene: Optional[FhirList[SubstanceReferenceInformationGene]] = None,
        geneElement: Optional[
            FhirList[SubstanceReferenceInformationGeneElement]
        ] = None,
        classification: Optional[
            FhirList[SubstanceReferenceInformationClassification]
        ] = None,
        target: Optional[FhirList[SubstanceReferenceInformationTarget]] = None,
    ) -> None:
        """
            Todo.
            If the element is present, it must have either a @value, an @id, or extensions

            :param id_: The logical id of the resource, as used in the URL for the resource. Once
        assigned, this value never changes.
            :param meta: The metadata about the resource. This is content that is maintained by the
        infrastructure. Changes to the content might not always be associated with
        version changes to the resource.
            :param implicitRules: A reference to a set of rules that were followed when the resource was
        constructed, and which must be understood when processing the content. Often,
        this is a reference to an implementation guide that defines the special rules
        along with other profiles etc.
            :param language: The base language in which the resource is written.
            :param text: A human-readable narrative that contains a summary of the resource and can be
        used to represent the content of the resource to a human. The narrative need
        not encode all the structured data, but is required to contain sufficient
        detail to make it "clinically safe" for a human to just read the narrative.
        Resource definitions may define what content should be represented in the
        narrative to ensure clinical safety.
            :param contained: These resources do not have an independent existence apart from the resource
        that contains them - they cannot be identified independently, and nor can they
        have their own independent transaction scope.
            :param extension: May be used to represent additional information that is not part of the basic
        definition of the resource. To make the use of extensions safe and manageable,
        there is a strict set of governance  applied to the definition and use of
        extensions. Though any implementer can define an extension, there is a set of
        requirements that SHALL be met as part of the definition of the extension.
            :param modifierExtension: May be used to represent additional information that is not part of the basic
        definition of the resource and that modifies the understanding of the element
        that contains it and/or the understanding of the containing element's
        descendants. Usually modifier elements provide negation or qualification. To
        make the use of extensions safe and manageable, there is a strict set of
        governance applied to the definition and use of extensions. Though any
        implementer is allowed to define an extension, there is a set of requirements
        that SHALL be met as part of the definition of the extension. Applications
        processing a resource are required to check for modifier extensions.

        Modifier extensions SHALL NOT change the meaning of any elements on Resource
        or DomainResource (including cannot change the meaning of modifierExtension
        itself).
            :param comment: Todo.
            :param gene: Todo.
            :param geneElement: Todo.
            :param classification: Todo.
            :param target: Todo.
        """
        super().__init__(
            resourceType="SubstanceReferenceInformation",
            id_=id_,
            meta=meta,
            implicitRules=implicitRules,
            language=language,
            text=text,
            contained=contained,
            extension=extension,
            modifierExtension=modifierExtension,
            comment=comment,
            gene=gene,
            geneElement=geneElement,
            classification=classification,
            target=target,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return SubstanceReferenceInformationSchema.get_schema(
            include_extension=include_extension
        )
