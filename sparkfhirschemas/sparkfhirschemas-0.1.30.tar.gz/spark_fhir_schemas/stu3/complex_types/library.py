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
class LibrarySchema:
    """
    The Library resource is a general-purpose container for knowledge asset
    definitions. It can be used to describe and expose existing knowledge assets
    such as logic libraries and information model descriptions, as well as to
    describe a collection of knowledge assets.
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
        The Library resource is a general-purpose container for knowledge asset
        definitions. It can be used to describe and expose existing knowledge assets
        such as logic libraries and information model descriptions, as well as to
        describe a collection of knowledge assets.


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

        resourceType: This is a Library resource

        url: An absolute URI that is used to identify this library when it is referenced in
            a specification, model, design or an instance. This SHALL be a URL, SHOULD be
            globally unique, and SHOULD be an address at which this library is (or will
            be) published. The URL SHOULD include the major version of the library. For
            more information see [Technical and Business
            Versions](resource.html#versions).

        identifier: A formal identifier that is used to identify this library when it is
            represented in other formats, or referenced in a specification, model, design
            or an instance. e.g. CMS or NQF identifiers for a measure artifact. Note that
            at least one identifier is required for non-experimental active artifacts.

        version: The identifier that is used to identify this version of the library when it is
            referenced in a specification, model, design or instance. This is an arbitrary
            value managed by the library author and is not expected to be globally unique.
            For example, it might be a timestamp (e.g. yyyymmdd) if a managed version is
            not available. There is also no expectation that versions can be placed in a
            lexicographical sequence. To provide a version consistent with the Decision
            Support Service specification, use the format Major.Minor.Revision (e.g.
            1.0.0). For more information on versioning knowledge assets, refer to the
            Decision Support Service specification. Note that a version is required for
            non-experimental active artifacts.

        name: A natural language name identifying the library. This name should be usable as
            an identifier for the module by machine processing applications such as code
            generation.

        title: A short, descriptive, user-friendly title for the library.

        status: The status of this library. Enables tracking the life-cycle of the content.

        experimental: A boolean value to indicate that this library is authored for testing purposes
            (or education/evaluation/marketing), and is not intended to be used for
            genuine usage.

        type: Identifies the type of library such as a Logic Library, Model Definition,
            Asset Collection, or Module Definition.

        date: The date  (and optionally time) when the library was published. The date must
            change if and when the business version changes and it must change if the
            status code changes. In addition, it should change when the substantive
            content of the library changes.

        publisher: The name of the individual or organization that published the library.

        description: A free text natural language description of the library from a consumer's
            perspective.

        purpose: Explaination of why this library is needed and why it has been designed as it
            has.

        usage: A detailed description of how the library is used from a clinical perspective.

        approvalDate: The date on which the resource content was approved by the publisher. Approval
            happens once when the content is officially approved for usage.

        lastReviewDate: The date on which the resource content was last reviewed. Review happens
            periodically after approval, but doesn't change the original approval date.

        effectivePeriod: The period during which the library content was or is planned to be in active
            use.

        useContext: The content was developed with a focus and intent of supporting the contexts
            that are listed. These terms may be used to assist with indexing and searching
            for appropriate library instances.

        jurisdiction: A legal or geographic region in which the library is intended to be used.

        topic: Descriptive topics related to the content of the library. Topics provide a
            high-level categorization of the library that can be useful for filtering and
            searching.

        contributor: A contributor to the content of the library, including authors, editors,
            reviewers, and endorsers.

        contact: Contact details to assist a user in finding and communicating with the
            publisher.

        copyright: A copyright statement relating to the library and/or its contents. Copyright
            statements are generally legal restrictions on the use and publishing of the
            library.

        relatedArtifact: Related artifacts such as additional documentation, justification, or
            bibliographic references.

        parameter: The parameter element defines parameters used by the library.

        dataRequirement: Describes a set of data that must be provided in order to be able to
            successfully perform the computations defined by the library.

        content: The content of the library as an Attachment. The content may be a reference to
            a url, or may be directly embedded as a base-64 string. Either way, the
            contentType of the attachment determines how to interpret the content.

        """
        from spark_fhir_schemas.stu3.complex_types.extension import ExtensionSchema
        from spark_fhir_schemas.stu3.complex_types.meta import MetaSchema
        from spark_fhir_schemas.stu3.complex_types.narrative import NarrativeSchema
        from spark_fhir_schemas.stu3.simple_types.resourcelist import ResourceListSchema
        from spark_fhir_schemas.stu3.complex_types.identifier import IdentifierSchema
        from spark_fhir_schemas.stu3.complex_types.codeableconcept import (
            CodeableConceptSchema,
        )
        from spark_fhir_schemas.stu3.complex_types.period import PeriodSchema
        from spark_fhir_schemas.stu3.complex_types.usagecontext import (
            UsageContextSchema,
        )
        from spark_fhir_schemas.stu3.complex_types.contributor import ContributorSchema
        from spark_fhir_schemas.stu3.complex_types.contactdetail import (
            ContactDetailSchema,
        )
        from spark_fhir_schemas.stu3.complex_types.relatedartifact import (
            RelatedArtifactSchema,
        )
        from spark_fhir_schemas.stu3.complex_types.parameterdefinition import (
            ParameterDefinitionSchema,
        )
        from spark_fhir_schemas.stu3.complex_types.datarequirement import (
            DataRequirementSchema,
        )
        from spark_fhir_schemas.stu3.complex_types.attachment import AttachmentSchema

        if (
            max_recursion_limit and nesting_list.count("Library") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Library"]
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
                # This is a Library resource
                StructField("resourceType", StringType(), True),
                # An absolute URI that is used to identify this library when it is referenced in
                # a specification, model, design or an instance. This SHALL be a URL, SHOULD be
                # globally unique, and SHOULD be an address at which this library is (or will
                # be) published. The URL SHOULD include the major version of the library. For
                # more information see [Technical and Business
                # Versions](resource.html#versions).
                StructField("url", StringType(), True),
                # A formal identifier that is used to identify this library when it is
                # represented in other formats, or referenced in a specification, model, design
                # or an instance. e.g. CMS or NQF identifiers for a measure artifact. Note that
                # at least one identifier is required for non-experimental active artifacts.
                StructField(
                    "identifier",
                    ArrayType(
                        IdentifierSchema.get_schema(
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
                # The identifier that is used to identify this version of the library when it is
                # referenced in a specification, model, design or instance. This is an arbitrary
                # value managed by the library author and is not expected to be globally unique.
                # For example, it might be a timestamp (e.g. yyyymmdd) if a managed version is
                # not available. There is also no expectation that versions can be placed in a
                # lexicographical sequence. To provide a version consistent with the Decision
                # Support Service specification, use the format Major.Minor.Revision (e.g.
                # 1.0.0). For more information on versioning knowledge assets, refer to the
                # Decision Support Service specification. Note that a version is required for
                # non-experimental active artifacts.
                StructField("version", StringType(), True),
                # A natural language name identifying the library. This name should be usable as
                # an identifier for the module by machine processing applications such as code
                # generation.
                StructField("name", StringType(), True),
                # A short, descriptive, user-friendly title for the library.
                StructField("title", StringType(), True),
                # The status of this library. Enables tracking the life-cycle of the content.
                StructField("status", StringType(), True),
                # A boolean value to indicate that this library is authored for testing purposes
                # (or education/evaluation/marketing), and is not intended to be used for
                # genuine usage.
                StructField("experimental", BooleanType(), True),
                # Identifies the type of library such as a Logic Library, Model Definition,
                # Asset Collection, or Module Definition.
                StructField(
                    "type",
                    CodeableConceptSchema.get_schema(
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
                # The date  (and optionally time) when the library was published. The date must
                # change if and when the business version changes and it must change if the
                # status code changes. In addition, it should change when the substantive
                # content of the library changes.
                StructField("date", StringType(), True),
                # The name of the individual or organization that published the library.
                StructField("publisher", StringType(), True),
                # A free text natural language description of the library from a consumer's
                # perspective.
                StructField("description", StringType(), True),
                # Explaination of why this library is needed and why it has been designed as it
                # has.
                StructField("purpose", StringType(), True),
                # A detailed description of how the library is used from a clinical perspective.
                StructField("usage", StringType(), True),
                # The date on which the resource content was approved by the publisher. Approval
                # happens once when the content is officially approved for usage.
                StructField("approvalDate", StringType(), True),
                # The date on which the resource content was last reviewed. Review happens
                # periodically after approval, but doesn't change the original approval date.
                StructField("lastReviewDate", StringType(), True),
                # The period during which the library content was or is planned to be in active
                # use.
                StructField(
                    "effectivePeriod",
                    PeriodSchema.get_schema(
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
                # The content was developed with a focus and intent of supporting the contexts
                # that are listed. These terms may be used to assist with indexing and searching
                # for appropriate library instances.
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
                # A legal or geographic region in which the library is intended to be used.
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
                # Descriptive topics related to the content of the library. Topics provide a
                # high-level categorization of the library that can be useful for filtering and
                # searching.
                StructField(
                    "topic",
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
                # A contributor to the content of the library, including authors, editors,
                # reviewers, and endorsers.
                StructField(
                    "contributor",
                    ArrayType(
                        ContributorSchema.get_schema(
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
                # A copyright statement relating to the library and/or its contents. Copyright
                # statements are generally legal restrictions on the use and publishing of the
                # library.
                StructField("copyright", StringType(), True),
                # Related artifacts such as additional documentation, justification, or
                # bibliographic references.
                StructField(
                    "relatedArtifact",
                    ArrayType(
                        RelatedArtifactSchema.get_schema(
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
                # The parameter element defines parameters used by the library.
                StructField(
                    "parameter",
                    ArrayType(
                        ParameterDefinitionSchema.get_schema(
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
                # Describes a set of data that must be provided in order to be able to
                # successfully perform the computations defined by the library.
                StructField(
                    "dataRequirement",
                    ArrayType(
                        DataRequirementSchema.get_schema(
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
                # The content of the library as an Attachment. The content may be a reference to
                # a url, or may be directly embedded as a base-64 string. Either way, the
                # contentType of the attachment determines how to interpret the content.
                StructField(
                    "content",
                    ArrayType(
                        AttachmentSchema.get_schema(
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
