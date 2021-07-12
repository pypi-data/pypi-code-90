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
from spark_fhir_schemas.r4.resources.specimendefinition import SpecimenDefinitionSchema

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
    # identifier (Identifier)
    from spark_auto_mapper_fhir.complex_types.identifier import Identifier

    # typeCollected (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for typeCollected
    from spark_auto_mapper_fhir.value_sets.v2_0487 import V2_0487

    # End Import for CodeableConcept for typeCollected
    # patientPreparation (CodeableConcept)
    # Import for CodeableConcept for patientPreparation
    from spark_auto_mapper_fhir.value_sets.prepare_patient import PreparePatientCode

    # End Import for CodeableConcept for patientPreparation
    # timeAspect (string)
    # collection (CodeableConcept)
    # Import for CodeableConcept for collection
    from spark_auto_mapper_fhir.value_sets.specimen_collection import (
        SpecimenCollectionCode,
    )

    # End Import for CodeableConcept for collection
    # typeTested (SpecimenDefinition.TypeTested)
    from spark_auto_mapper_fhir.backbone_elements.specimen_definition_type_tested import (
        SpecimenDefinitionTypeTested,
    )


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class SpecimenDefinition(FhirResourceBase):
    """
    SpecimenDefinition
    specimendefinition.xsd
        A kind of specimen with associated set of requirements.
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
        identifier: Optional[Identifier] = None,
        typeCollected: Optional[CodeableConcept[V2_0487]] = None,
        patientPreparation: Optional[
            FhirList[CodeableConcept[PreparePatientCode]]
        ] = None,
        timeAspect: Optional[FhirString] = None,
        collection: Optional[FhirList[CodeableConcept[SpecimenCollectionCode]]] = None,
        typeTested: Optional[FhirList[SpecimenDefinitionTypeTested]] = None,
    ) -> None:
        """
            A kind of specimen with associated set of requirements.
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
            :param identifier: A business identifier associated with the kind of specimen.
            :param typeCollected: The kind of material to be collected.
            :param patientPreparation: Preparation of the patient for specimen collection.
            :param timeAspect: Time aspect of specimen collection (duration or offset).
            :param collection: The action to be performed for collecting the specimen.
            :param typeTested: Specimen conditioned in a container as expected by the testing laboratory.
        """
        super().__init__(
            resourceType="SpecimenDefinition",
            id_=id_,
            meta=meta,
            implicitRules=implicitRules,
            language=language,
            text=text,
            contained=contained,
            extension=extension,
            modifierExtension=modifierExtension,
            identifier=identifier,
            typeCollected=typeCollected,
            patientPreparation=patientPreparation,
            timeAspect=timeAspect,
            collection=collection,
            typeTested=typeTested,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return SpecimenDefinitionSchema.get_schema(include_extension=include_extension)
