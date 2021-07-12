from typing import Union, List, Optional

from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    ArrayType,
    BooleanType,
    IntegerType,
    DataType,
)


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class TestScript_OperationSchema:
    """
    A structured set of tests against a FHIR server implementation to determine
    compliance against the FHIR specification.
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
        A structured set of tests against a FHIR server implementation to determine
        compliance against the FHIR specification.


        id: unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. In order to make the use of extensions safe and
            manageable, there is a strict set of governance  applied to the definition and
            use of extensions. Though any implementer is allowed to define an extension,
            there is a set of requirements that SHALL be met as part of the definition of
            the extension.

        type: Server interaction or operation type.

        resource: The type of the resource.  See http://build.fhir.org/resourcelist.html.

        label: The label would be used for tracking/logging purposes by test engines.

        description: The description would be used by test engines for tracking and reporting
            purposes.

        accept: The content-type or mime-type to use for RESTful operation in the 'Accept'
            header.

        contentType: The content-type or mime-type to use for RESTful operation in the 'Content-
            Type' header.

        destination: The server where the request message is destined for.  Must be one of the
            server numbers listed in TestScript.destination section.

        encodeRequestUrl: Whether or not to implicitly send the request url in encoded format. The
            default is true to match the standard RESTful client behavior. Set to false
            when communicating with a server that does not support encoded url paths.

        origin: The server where the request message originates from.  Must be one of the
            server numbers listed in TestScript.origin section.

        params: Path plus parameters after [type].  Used to set parts of the request URL
            explicitly.

        requestHeader: Header elements would be used to set HTTP headers.

        requestId: The fixture id (maybe new) to map to the request.

        responseId: The fixture id (maybe new) to map to the response.

        sourceId: The id of the fixture used as the body of a PUT or POST request.

        targetId: Id of fixture used for extracting the [id],  [type], and [vid] for GET
            requests.

        url: Complete request URL.

        """
        from spark_fhir_schemas.stu3.complex_types.extension import ExtensionSchema
        from spark_fhir_schemas.stu3.complex_types.coding import CodingSchema
        from spark_fhir_schemas.stu3.complex_types.testscript_requestheader import (
            TestScript_RequestHeaderSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("TestScript_Operation") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["TestScript_Operation"]
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
                # Server interaction or operation type.
                StructField(
                    "type",
                    CodingSchema.get_schema(
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
                # The type of the resource.  See http://build.fhir.org/resourcelist.html.
                StructField("resource", StringType(), True),
                # The label would be used for tracking/logging purposes by test engines.
                StructField("label", StringType(), True),
                # The description would be used by test engines for tracking and reporting
                # purposes.
                StructField("description", StringType(), True),
                # The content-type or mime-type to use for RESTful operation in the 'Accept'
                # header.
                StructField("accept", StringType(), True),
                # The content-type or mime-type to use for RESTful operation in the 'Content-
                # Type' header.
                StructField("contentType", StringType(), True),
                # The server where the request message is destined for.  Must be one of the
                # server numbers listed in TestScript.destination section.
                StructField("destination", IntegerType(), True),
                # Whether or not to implicitly send the request url in encoded format. The
                # default is true to match the standard RESTful client behavior. Set to false
                # when communicating with a server that does not support encoded url paths.
                StructField("encodeRequestUrl", BooleanType(), True),
                # The server where the request message originates from.  Must be one of the
                # server numbers listed in TestScript.origin section.
                StructField("origin", IntegerType(), True),
                # Path plus parameters after [type].  Used to set parts of the request URL
                # explicitly.
                StructField("params", StringType(), True),
                # Header elements would be used to set HTTP headers.
                StructField(
                    "requestHeader",
                    ArrayType(
                        TestScript_RequestHeaderSchema.get_schema(
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
                # The fixture id (maybe new) to map to the request.
                StructField("requestId", StringType(), True),
                # The fixture id (maybe new) to map to the response.
                StructField("responseId", StringType(), True),
                # The id of the fixture used as the body of a PUT or POST request.
                StructField("sourceId", StringType(), True),
                # Id of fixture used for extracting the [id],  [type], and [vid] for GET
                # requests.
                StructField("targetId", StringType(), True),
                # Complete request URL.
                StructField("url", StringType(), True),
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
