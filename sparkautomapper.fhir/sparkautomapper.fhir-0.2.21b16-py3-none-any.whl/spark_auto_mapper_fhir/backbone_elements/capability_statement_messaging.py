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
    # endpoint (CapabilityStatement.Endpoint)
    from spark_auto_mapper_fhir.backbone_elements.capability_statement_endpoint import (
        CapabilityStatementEndpoint,
    )

    # reliableCache (unsignedInt)
    from spark_auto_mapper_fhir.fhir_types.unsigned_int import FhirUnsignedInt

    # documentation (markdown)
    from spark_auto_mapper_fhir.fhir_types.markdown import FhirMarkdown

    # supportedMessage (CapabilityStatement.SupportedMessage)
    from spark_auto_mapper_fhir.backbone_elements.capability_statement_supported_message import (
        CapabilityStatementSupportedMessage,
    )


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class CapabilityStatementMessaging(FhirBackboneElementBase):
    """
    CapabilityStatement.Messaging
        A Capability Statement documents a set of capabilities (behaviors) of a FHIR Server for a particular version of FHIR that may be used as a statement of actual server functionality or a statement of required or desired server implementation.
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[Extension]] = None,
        modifierExtension: Optional[FhirList[Extension]] = None,
        endpoint: Optional[FhirList[CapabilityStatementEndpoint]] = None,
        reliableCache: Optional[FhirUnsignedInt] = None,
        documentation: Optional[FhirMarkdown] = None,
        supportedMessage: Optional[
            FhirList[CapabilityStatementSupportedMessage]
        ] = None,
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
            :param endpoint: An endpoint (network accessible address) to which messages and/or replies are
        to be sent.
            :param reliableCache: Length if the receiver's reliable messaging cache in minutes (if a receiver)
        or how long the cache length on the receiver should be (if a sender).
            :param documentation: Documentation about the system's messaging capabilities for this endpoint not
        otherwise documented by the capability statement.  For example, the process
        for becoming an authorized messaging exchange partner.
            :param supportedMessage: References to message definitions for messages this system can send or
        receive.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            modifierExtension=modifierExtension,
            endpoint=endpoint,
            reliableCache=reliableCache,
            documentation=documentation,
            supportedMessage=supportedMessage,
        )
