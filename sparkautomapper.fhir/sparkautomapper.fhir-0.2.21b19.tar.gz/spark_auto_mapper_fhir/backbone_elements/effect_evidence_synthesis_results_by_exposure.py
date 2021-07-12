from __future__ import annotations
from typing import Optional, TYPE_CHECKING

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
    # description (string)
    # exposureState (ExposureState)
    from spark_auto_mapper_fhir.value_sets.exposure_state import ExposureStateCode

    # variantState (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # End Import for References for variantState
    # Import for CodeableConcept for variantState
    from spark_auto_mapper_fhir.value_sets.evidence_variant_state import (
        EvidenceVariantStateCode,
    )

    # End Import for CodeableConcept for variantState
    # riskEvidenceSynthesis (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for riskEvidenceSynthesis
    from spark_auto_mapper_fhir.resources.risk_evidence_synthesis import (
        RiskEvidenceSynthesis,
    )


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class EffectEvidenceSynthesisResultsByExposure(FhirBackboneElementBase):
    """
    EffectEvidenceSynthesis.ResultsByExposure
        The EffectEvidenceSynthesis resource describes the difference in an outcome between exposures states in a population where the effect estimate is derived from a combination of research studies.
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        modifierExtension: Optional[FhirList[ExtensionBase]] = None,
        description: Optional[FhirString] = None,
        exposureState: Optional[ExposureStateCode] = None,
        variantState: Optional[CodeableConcept[EvidenceVariantStateCode]] = None,
        riskEvidenceSynthesis: Reference[RiskEvidenceSynthesis],
    ) -> None:
        """
            The EffectEvidenceSynthesis resource describes the difference in an outcome
        between exposures states in a population where the effect estimate is derived
        from a combination of research studies.

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
            :param description: Human-readable summary of results by exposure state.
            :param exposureState: Whether these results are for the exposure state or alternative exposure
        state.
            :param variantState: Used to define variant exposure states such as low-risk state.
            :param riskEvidenceSynthesis: Reference to a RiskEvidenceSynthesis resource.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            modifierExtension=modifierExtension,
            description=description,
            exposureState=exposureState,
            variantState=variantState,
            riskEvidenceSynthesis=riskEvidenceSynthesis,
        )
