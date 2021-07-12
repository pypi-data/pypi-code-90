from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.medicinalproductindication import (
    MedicinalProductIndicationSchema,
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
    # subject (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for subject
    from spark_auto_mapper_fhir.resources.medicinal_product import MedicinalProduct
    from spark_auto_mapper_fhir.resources.medication import Medication

    # diseaseSymptomProcedure (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for diseaseSymptomProcedure
    from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode

    # End Import for CodeableConcept for diseaseSymptomProcedure
    # diseaseStatus (CodeableConcept)
    # Import for CodeableConcept for diseaseStatus
    # End Import for CodeableConcept for diseaseStatus
    # comorbidity (CodeableConcept)
    # Import for CodeableConcept for comorbidity
    # End Import for CodeableConcept for comorbidity
    # intendedEffect (CodeableConcept)
    # Import for CodeableConcept for intendedEffect
    # End Import for CodeableConcept for intendedEffect
    # duration (Quantity)
    from spark_auto_mapper_fhir.complex_types.quantity import Quantity

    # otherTherapy (MedicinalProductIndication.OtherTherapy)
    from spark_auto_mapper_fhir.backbone_elements.medicinal_product_indication_other_therapy import (
        MedicinalProductIndicationOtherTherapy,
    )

    # undesirableEffect (Reference)
    # Imports for References for undesirableEffect
    from spark_auto_mapper_fhir.resources.medicinal_product_undesirable_effect import (
        MedicinalProductUndesirableEffect,
    )

    # population (Population)
    from spark_auto_mapper_fhir.backbone_elements.population import Population


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class MedicinalProductIndication(FhirResourceBase):
    """
    MedicinalProductIndication
    medicinalproductindication.xsd
        Indication for the Medicinal Product.
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
        subject: Optional[
            FhirList[Reference[Union[MedicinalProduct, Medication]]]
        ] = None,
        diseaseSymptomProcedure: Optional[CodeableConcept[GenericTypeCode]] = None,
        diseaseStatus: Optional[CodeableConcept[GenericTypeCode]] = None,
        comorbidity: Optional[FhirList[CodeableConcept[GenericTypeCode]]] = None,
        intendedEffect: Optional[CodeableConcept[GenericTypeCode]] = None,
        duration: Optional[Quantity] = None,
        otherTherapy: Optional[FhirList[MedicinalProductIndicationOtherTherapy]] = None,
        undesirableEffect: Optional[
            FhirList[Reference[Union[MedicinalProductUndesirableEffect]]]
        ] = None,
        population: Optional[FhirList[Population]] = None,
    ) -> None:
        """
            Indication for the Medicinal Product.
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
            :param subject: The medication for which this is an indication.
            :param diseaseSymptomProcedure: The disease, symptom or procedure that is the indication for treatment.
            :param diseaseStatus: The status of the disease or symptom for which the indication applies.
            :param comorbidity: Comorbidity (concurrent condition) or co-infection as part of the indication.
            :param intendedEffect: The intended effect, aim or strategy to be achieved by the indication.
            :param duration: Timing or duration information as part of the indication.
            :param otherTherapy: Information about the use of the medicinal product in relation to other
        therapies described as part of the indication.
            :param undesirableEffect: Describe the undesirable effects of the medicinal product.
            :param population: The population group to which this applies.
        """
        super().__init__(
            resourceType="MedicinalProductIndication",
            id_=id_,
            meta=meta,
            implicitRules=implicitRules,
            language=language,
            text=text,
            contained=contained,
            extension=extension,
            modifierExtension=modifierExtension,
            subject=subject,
            diseaseSymptomProcedure=diseaseSymptomProcedure,
            diseaseStatus=diseaseStatus,
            comorbidity=comorbidity,
            intendedEffect=intendedEffect,
            duration=duration,
            otherTherapy=otherTherapy,
            undesirableEffect=undesirableEffect,
            population=population,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return MedicinalProductIndicationSchema.get_schema(
            include_extension=include_extension
        )
