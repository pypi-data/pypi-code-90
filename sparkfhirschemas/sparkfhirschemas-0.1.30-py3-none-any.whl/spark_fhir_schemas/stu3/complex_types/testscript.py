from typing import Union, List, Optional

from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    ArrayType,
    BooleanType,
    DataType,
)


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class TestScriptSchema:
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


        id: The logical id of the resource, as used in the URL for the resource. Once
            assigned, this value never changes.

        extension: May be used to represent additional information that is not part of the basic
            definition of the resource. In order to make the use of extensions safe and
            manageable, there is a strict set of governance  applied to the definition and
            use of extensions. Though any implementer is allowed to define an extension,
            there is a set of requirements that SHALL be met as part of the definition of
            the extension.

        meta: The metadata about the resource. This is content that is maintained by the
            infrastructure. Changes to the content may not always be associated with
            version changes to the resource.

        implicitRules: A reference to a set of rules that were followed when the resource was
            constructed, and which must be understood when processing the content.

        language: The base language in which the resource is written.

        text: A human-readable narrative that contains a summary of the resource, and may be
            used to represent the content of the resource to a human. The narrative need
            not encode all the structured data, but is required to contain sufficient
            detail to make it "clinically safe" for a human to just read the narrative.
            Resource definitions may define what content should be represented in the
            narrative to ensure clinical safety.

        contained: These resources do not have an independent existence apart from the resource
            that contains them - they cannot be identified independently, and nor can they
            have their own independent transaction scope.

        resourceType: This is a TestScript resource

        url: An absolute URI that is used to identify this test script when it is
            referenced in a specification, model, design or an instance. This SHALL be a
            URL, SHOULD be globally unique, and SHOULD be an address at which this test
            script is (or will be) published. The URL SHOULD include the major version of
            the test script. For more information see [Technical and Business
            Versions](resource.html#versions).

        identifier: A formal identifier that is used to identify this test script when it is
            represented in other formats, or referenced in a specification, model, design
            or an instance.

        version: The identifier that is used to identify this version of the test script when
            it is referenced in a specification, model, design or instance. This is an
            arbitrary value managed by the test script author and is not expected to be
            globally unique. For example, it might be a timestamp (e.g. yyyymmdd) if a
            managed version is not available. There is also no expectation that versions
            can be placed in a lexicographical sequence.

        name: A natural language name identifying the test script. This name should be
            usable as an identifier for the module by machine processing applications such
            as code generation.

        title: A short, descriptive, user-friendly title for the test script.

        status: The status of this test script. Enables tracking the life-cycle of the
            content.

        experimental: A boolean value to indicate that this test script is authored for testing
            purposes (or education/evaluation/marketing), and is not intended to be used
            for genuine usage.

        date: The date  (and optionally time) when the test script was published. The date
            must change if and when the business version changes and it must change if the
            status code changes. In addition, it should change when the substantive
            content of the test script changes.

        publisher: The name of the individual or organization that published the test script.

        contact: Contact details to assist a user in finding and communicating with the
            publisher.

        description: A free text natural language description of the test script from a consumer's
            perspective.

        useContext: The content was developed with a focus and intent of supporting the contexts
            that are listed. These terms may be used to assist with indexing and searching
            for appropriate test script instances.

        jurisdiction: A legal or geographic region in which the test script is intended to be used.

        purpose: Explaination of why this test script is needed and why it has been designed as
            it has.

        copyright: A copyright statement relating to the test script and/or its contents.
            Copyright statements are generally legal restrictions on the use and
            publishing of the test script.

        origin: An abstract server used in operations within this test script in the origin
            element.

        destination: An abstract server used in operations within this test script in the
            destination element.

        metadata: The required capability must exist and are assumed to function correctly on
            the FHIR server being tested.

        fixture: Fixture in the test script - by reference (uri). All fixtures are required for
            the test script to execute.

        profile: Reference to the profile to be used for validation.

        variable: Variable is set based either on element value in response body or on header
            field value in the response headers.

        rule: Assert rule to be used in one or more asserts within the test script.

        ruleset: Contains one or more rules.  Offers a way to group rules so assertions could
            reference the group of rules and have them all applied.

        setup: A series of required setup operations before tests are executed.

        test: A test in this script.

        teardown: A series of operations required to clean up after the all the tests are
            executed (successfully or otherwise).

        """
        from spark_fhir_schemas.stu3.complex_types.extension import ExtensionSchema
        from spark_fhir_schemas.stu3.complex_types.meta import MetaSchema
        from spark_fhir_schemas.stu3.complex_types.narrative import NarrativeSchema
        from spark_fhir_schemas.stu3.simple_types.resourcelist import ResourceListSchema
        from spark_fhir_schemas.stu3.complex_types.identifier import IdentifierSchema
        from spark_fhir_schemas.stu3.complex_types.contactdetail import (
            ContactDetailSchema,
        )
        from spark_fhir_schemas.stu3.complex_types.usagecontext import (
            UsageContextSchema,
        )
        from spark_fhir_schemas.stu3.complex_types.codeableconcept import (
            CodeableConceptSchema,
        )
        from spark_fhir_schemas.stu3.complex_types.testscript_origin import (
            TestScript_OriginSchema,
        )
        from spark_fhir_schemas.stu3.complex_types.testscript_destination import (
            TestScript_DestinationSchema,
        )
        from spark_fhir_schemas.stu3.complex_types.testscript_metadata import (
            TestScript_MetadataSchema,
        )
        from spark_fhir_schemas.stu3.complex_types.testscript_fixture import (
            TestScript_FixtureSchema,
        )
        from spark_fhir_schemas.stu3.complex_types.reference import ReferenceSchema
        from spark_fhir_schemas.stu3.complex_types.testscript_variable import (
            TestScript_VariableSchema,
        )
        from spark_fhir_schemas.stu3.complex_types.testscript_rule import (
            TestScript_RuleSchema,
        )
        from spark_fhir_schemas.stu3.complex_types.testscript_ruleset import (
            TestScript_RulesetSchema,
        )
        from spark_fhir_schemas.stu3.complex_types.testscript_setup import (
            TestScript_SetupSchema,
        )
        from spark_fhir_schemas.stu3.complex_types.testscript_test import (
            TestScript_TestSchema,
        )
        from spark_fhir_schemas.stu3.complex_types.testscript_teardown import (
            TestScript_TeardownSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("TestScript") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["TestScript"]
        schema = StructType(
            [
                # The logical id of the resource, as used in the URL for the resource. Once
                # assigned, this value never changes.
                StructField("id", StringType(), True),
                # May be used to represent additional information that is not part of the basic
                # definition of the resource. In order to make the use of extensions safe and
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
                # The metadata about the resource. This is content that is maintained by the
                # infrastructure. Changes to the content may not always be associated with
                # version changes to the resource.
                StructField(
                    "meta",
                    MetaSchema.get_schema(
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
                # A reference to a set of rules that were followed when the resource was
                # constructed, and which must be understood when processing the content.
                StructField("implicitRules", StringType(), True),
                # The base language in which the resource is written.
                StructField("language", StringType(), True),
                # A human-readable narrative that contains a summary of the resource, and may be
                # used to represent the content of the resource to a human. The narrative need
                # not encode all the structured data, but is required to contain sufficient
                # detail to make it "clinically safe" for a human to just read the narrative.
                # Resource definitions may define what content should be represented in the
                # narrative to ensure clinical safety.
                StructField(
                    "text",
                    NarrativeSchema.get_schema(
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
                # These resources do not have an independent existence apart from the resource
                # that contains them - they cannot be identified independently, and nor can they
                # have their own independent transaction scope.
                StructField(
                    "contained",
                    ArrayType(
                        ResourceListSchema.get_schema(
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
                # This is a TestScript resource
                StructField("resourceType", StringType(), True),
                # An absolute URI that is used to identify this test script when it is
                # referenced in a specification, model, design or an instance. This SHALL be a
                # URL, SHOULD be globally unique, and SHOULD be an address at which this test
                # script is (or will be) published. The URL SHOULD include the major version of
                # the test script. For more information see [Technical and Business
                # Versions](resource.html#versions).
                StructField("url", StringType(), True),
                # A formal identifier that is used to identify this test script when it is
                # represented in other formats, or referenced in a specification, model, design
                # or an instance.
                StructField(
                    "identifier",
                    IdentifierSchema.get_schema(
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
                # The identifier that is used to identify this version of the test script when
                # it is referenced in a specification, model, design or instance. This is an
                # arbitrary value managed by the test script author and is not expected to be
                # globally unique. For example, it might be a timestamp (e.g. yyyymmdd) if a
                # managed version is not available. There is also no expectation that versions
                # can be placed in a lexicographical sequence.
                StructField("version", StringType(), True),
                # A natural language name identifying the test script. This name should be
                # usable as an identifier for the module by machine processing applications such
                # as code generation.
                StructField("name", StringType(), True),
                # A short, descriptive, user-friendly title for the test script.
                StructField("title", StringType(), True),
                # The status of this test script. Enables tracking the life-cycle of the
                # content.
                StructField("status", StringType(), True),
                # A boolean value to indicate that this test script is authored for testing
                # purposes (or education/evaluation/marketing), and is not intended to be used
                # for genuine usage.
                StructField("experimental", BooleanType(), True),
                # The date  (and optionally time) when the test script was published. The date
                # must change if and when the business version changes and it must change if the
                # status code changes. In addition, it should change when the substantive
                # content of the test script changes.
                StructField("date", StringType(), True),
                # The name of the individual or organization that published the test script.
                StructField("publisher", StringType(), True),
                # Contact details to assist a user in finding and communicating with the
                # publisher.
                StructField(
                    "contact",
                    ArrayType(
                        ContactDetailSchema.get_schema(
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
                # A free text natural language description of the test script from a consumer's
                # perspective.
                StructField("description", StringType(), True),
                # The content was developed with a focus and intent of supporting the contexts
                # that are listed. These terms may be used to assist with indexing and searching
                # for appropriate test script instances.
                StructField(
                    "useContext",
                    ArrayType(
                        UsageContextSchema.get_schema(
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
                # A legal or geographic region in which the test script is intended to be used.
                StructField(
                    "jurisdiction",
                    ArrayType(
                        CodeableConceptSchema.get_schema(
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
                # Explaination of why this test script is needed and why it has been designed as
                # it has.
                StructField("purpose", StringType(), True),
                # A copyright statement relating to the test script and/or its contents.
                # Copyright statements are generally legal restrictions on the use and
                # publishing of the test script.
                StructField("copyright", StringType(), True),
                # An abstract server used in operations within this test script in the origin
                # element.
                StructField(
                    "origin",
                    ArrayType(
                        TestScript_OriginSchema.get_schema(
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
                # An abstract server used in operations within this test script in the
                # destination element.
                StructField(
                    "destination",
                    ArrayType(
                        TestScript_DestinationSchema.get_schema(
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
                # The required capability must exist and are assumed to function correctly on
                # the FHIR server being tested.
                StructField(
                    "metadata",
                    TestScript_MetadataSchema.get_schema(
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
                # Fixture in the test script - by reference (uri). All fixtures are required for
                # the test script to execute.
                StructField(
                    "fixture",
                    ArrayType(
                        TestScript_FixtureSchema.get_schema(
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
                # Reference to the profile to be used for validation.
                StructField(
                    "profile",
                    ArrayType(
                        ReferenceSchema.get_schema(
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
                # Variable is set based either on element value in response body or on header
                # field value in the response headers.
                StructField(
                    "variable",
                    ArrayType(
                        TestScript_VariableSchema.get_schema(
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
                # Assert rule to be used in one or more asserts within the test script.
                StructField(
                    "rule",
                    ArrayType(
                        TestScript_RuleSchema.get_schema(
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
                # Contains one or more rules.  Offers a way to group rules so assertions could
                # reference the group of rules and have them all applied.
                StructField(
                    "ruleset",
                    ArrayType(
                        TestScript_RulesetSchema.get_schema(
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
                # A series of required setup operations before tests are executed.
                StructField(
                    "setup",
                    TestScript_SetupSchema.get_schema(
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
                # A test in this script.
                StructField(
                    "test",
                    ArrayType(
                        TestScript_TestSchema.get_schema(
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
                # A series of operations required to clean up after the all the tests are
                # executed (successfully or otherwise).
                StructField(
                    "teardown",
                    TestScript_TeardownSchema.get_schema(
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
