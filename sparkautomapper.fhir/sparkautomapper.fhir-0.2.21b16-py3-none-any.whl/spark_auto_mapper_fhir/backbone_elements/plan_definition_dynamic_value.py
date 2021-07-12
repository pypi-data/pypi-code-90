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
    # path (string)
    # expression (Expression)
    from spark_auto_mapper_fhir.complex_types.expression import Expression


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class PlanDefinitionDynamicValue(FhirBackboneElementBase):
    """
    PlanDefinition.DynamicValue
        This resource allows for the definition of various types of plans as a sharable, consumable, and executable artifact. The resource is general enough to support the description of a broad range of clinical artifacts such as clinical decision support rules, order sets and protocols.
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[Extension]] = None,
        modifierExtension: Optional[FhirList[Extension]] = None,
        path: Optional[FhirString] = None,
        expression: Optional[Expression] = None,
    ) -> None:
        """
            This resource allows for the definition of various types of plans as a
        sharable, consumable, and executable artifact. The resource is general enough
        to support the description of a broad range of clinical artifacts such as
        clinical decision support rules, order sets and protocols.

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
            :param path: The path to the element to be customized. This is the path on the resource
        that will hold the result of the calculation defined by the expression. The
        specified path SHALL be a FHIRPath resolveable on the specified target type of
        the ActivityDefinition, and SHALL consist only of identifiers, constant
        indexers, and a restricted subset of functions. The path is allowed to contain
        qualifiers (.) to traverse sub-elements, as well as indexers ([x]) to traverse
        multiple-cardinality sub-elements (see the [Simple FHIRPath
        Profile](fhirpath.html#simple) for full details).
            :param expression: An expression specifying the value of the customized element.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            modifierExtension=modifierExtension,
            path=path,
            expression=expression,
        )
