from typing import Union, List, Optional

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class SignatureSchema:
    """
    A digital signature along with supporting context. The signature may be
    electronic/cryptographic in nature, or a graphical image representing a hand-
    written signature, or a signature process. Different signature approaches have
    different utilities.
    """

    # noinspection PyDefaultArgument
    @staticmethod
    def get_schema(
        max_nesting_depth: Optional[int] = 6,
        nesting_depth: int = 0,
        nesting_list: List[str] = [],
        max_recursion_limit: Optional[int] = 2,
        include_extension: Optional[bool] = False,
        extension_fields: Optional[List[str]] = [
            "valueBoolean",
            "valueCode",
            "valueDate",
            "valueDateTime",
            "valueDecimal",
            "valueId",
            "valueInteger",
            "valuePositiveInt",
            "valueString",
            "valueTime",
            "valueUnsignedInt",
            "valueUri",
            "valueUrl",
        ],
        extension_depth: int = 0,
        max_extension_depth: Optional[int] = 2,
    ) -> Union[StructType, DataType]:
        """
        A digital signature along with supporting context. The signature may be
        electronic/cryptographic in nature, or a graphical image representing a hand-
        written signature, or a signature process. Different signature approaches have
        different utilities.


        id: unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. In order to make the use of extensions safe and
            manageable, there is a strict set of governance  applied to the definition and
            use of extensions. Though any implementer is allowed to define an extension,
            there is a set of requirements that SHALL be met as part of the definition of
            the extension.

        type: An indication of the reason that the entity signed this document. This may be
            explicitly included as part of the signature information and can be used when
            determining accountability for various actions concerning the document.

        when: When the digital signature was signed.

        whoUri: A reference to an application-usable description of the identity that signed
            (e.g. the signature used their private key).

        whoReference: A reference to an application-usable description of the identity that signed
            (e.g. the signature used their private key).

        onBehalfOfUri: A reference to an application-usable description of the identity that is
            represented by the signature.

        onBehalfOfReference: A reference to an application-usable description of the identity that is
            represented by the signature.

        contentType: A mime type that indicates the technical format of the signature. Important
            mime types are application/signature+xml for X ML DigSig, application/jwt for
            JWT, and image/* for a graphical image of a signature, etc.

        blob: The base64 encoding of the Signature content. When signature is not recorded
            electronically this element would be empty.

        """
        from spark_fhir_schemas.stu3.complex_types.extension import ExtensionSchema
        from spark_fhir_schemas.stu3.complex_types.coding import CodingSchema
        from spark_fhir_schemas.stu3.complex_types.reference import ReferenceSchema

        if (
            max_recursion_limit
            and nesting_list.count("Signature") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Signature"]
        schema = StructType(
            [
                # unique id for the element within a resource (for internal references). This
                # may be any string value that does not contain spaces.
                StructField("id", StringType(), True),
                # May be used to represent additional information that is not part of the basic
                # definition of the element. In order to make the use of extensions safe and
                # manageable, there is a strict set of governance  applied to the definition and
                # use of extensions. Though any implementer is allowed to define an extension,
                # there is a set of requirements that SHALL be met as part of the definition of
                # the extension.
                StructField(
                    "extension",
                    ArrayType(
                        ExtensionSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                            extension_fields=extension_fields,
                            extension_depth=extension_depth,
                            max_extension_depth=max_extension_depth,
                        )
                    ),
                    True,
                ),
                # An indication of the reason that the entity signed this document. This may be
                # explicitly included as part of the signature information and can be used when
                # determining accountability for various actions concerning the document.
                StructField(
                    "type",
                    ArrayType(
                        CodingSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                            extension_fields=extension_fields,
                            extension_depth=extension_depth,
                            max_extension_depth=max_extension_depth,
                        )
                    ),
                    True,
                ),
                # When the digital signature was signed.
                StructField("when", StringType(), True),
                # A reference to an application-usable description of the identity that signed
                # (e.g. the signature used their private key).
                StructField("whoUri", StringType(), True),
                # A reference to an application-usable description of the identity that signed
                # (e.g. the signature used their private key).
                StructField(
                    "whoReference",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                    ),
                    True,
                ),
                # A reference to an application-usable description of the identity that is
                # represented by the signature.
                StructField("onBehalfOfUri", StringType(), True),
                # A reference to an application-usable description of the identity that is
                # represented by the signature.
                StructField(
                    "onBehalfOfReference",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                    ),
                    True,
                ),
                # A mime type that indicates the technical format of the signature. Important
                # mime types are application/signature+xml for X ML DigSig, application/jwt for
                # JWT, and image/* for a graphical image of a signature, etc.
                StructField("contentType", StringType(), True),
                # The base64 encoding of the Signature content. When signature is not recorded
                # electronically this element would be empty.
                StructField("blob", StringType(), True),
            ]
        )
        if not include_extension:
            schema.fields = [
                c
                if c.name != "extension"
                else StructField("extension", StringType(), True)
                for c in schema.fields
            ]

        return schema
