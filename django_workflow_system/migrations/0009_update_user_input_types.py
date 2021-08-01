# Generated by Django 3.1.8 on 2021-06-04 00:25


from django.db import migrations


def update_initial_user_input_types(apps, schema_editor):
    """
    Initialize the database with the WorkflowStepUserInputType that we have schemas available for.
    """
    WorkflowStepUserInputType = apps.get_model(
        "django_workflow_system", "WorkflowStepUserInputType"
    )

    # Single Choice Question
    WorkflowStepUserInputType.objects.update_or_create(
        name="single_choice_question",
        defaults={
            "json_schema": {
                "$schema": "http://json-schema.org/draft-07/schema",
                "$id": "http://github.com/crcresearch/",
                "type": "object",
                "title": "User Input: Single Choice Question",
                "description": "A schema representing a single choice question user input.",
                "required": ["label", "inputOptions", "meta"],
                "properties": {
                    "id": {
                        "type": "string",
                        "title": "A string-based user input identifier.",
                        "description": "This value may be managed outside of the object specification and so is optional.",
                        "examples": ["4125-1351-1251-asfd"],
                    },
                    "label": {
                        "type": "string",
                        "title": "UI Label for Input",
                        "description": "Label that should be displayed by user interfaces for this input.",
                        "examples": ["The label to display for the input/question."],
                    },
                    "inputOptions": {
                        "$id": "#/properties/options",
                        "type": "array",
                        "title": "Question Options",
                        "description": "The options to be displayed to the user for this question.",
                        "minItems": 2,
                        "uniqueItems": True,
                        "items": {"anyOf": [{"type": "number"}, {"type": "string"}]},
                    },
                    "correctInput": {
                        "description": "Indicates which answer is the correct one.",
                        "anyOf": [{"type": "string"}, {"type": "number"}],
                    },
                    "meta": {
                        "type": "object",
                        "required": ["inputRequired", "correctInputRequired"],
                        "properties": {
                            "inputRequired": {
                                "type": "boolean",
                                "description": "Whether or not an answer should be required from the user.",
                            },
                            "correctInputRequired": {
                                "type": "boolean",
                                "description": "Whether or not the correct answer should be required from the user.",
                            },
                        },
                    },
                },
            },
            "example_specification": {
                "label": "What is your favorite color?",
                "inputOptions": ["Red", "Blue"],
                "correctInput": "Red",
                "meta": {"inputRequired": True, "correctInputRequired": True},
            },
        },
    )

    # Multiple Choice Question
    WorkflowStepUserInputType.objects.update_or_create(
        name="multiple_choice_question",
        defaults={
            "json_schema": {
                "$schema": "http://json-schema.org/draft-07/schema",
                "$id": "http://github.com/crcresearch/",
                "type": "object",
                "title": "User Input: Multiple Choice Question",
                "description": "A schema representing a multiple choice question user input.",
                "required": ["label", "inputOptions", "meta"],
                "properties": {
                    "id": {
                        "type": "string",
                        "title": "A string-based user input identifier.",
                        "description": "This value may be managed outside of the object specification and so is optional.",
                        "examples": ["4125-1351-1251-asfd"],
                    },
                    "label": {
                        "type": "string",
                        "title": "UI Label for Input",
                        "description": "Label that should be displayed by user interfaces for this input.",
                        "examples": ["The label to display for the input/question."],
                    },
                    "inputOptions": {
                        "$id": "#/properties/options",
                        "type": "array",
                        "title": "Question Options",
                        "description": "The options to be displayed to the user for this question.",
                        "minItems": 2,
                        "uniqueItems": True,
                        "items": {"anyOf": [{"type": "number"}, {"type": "string"}]},
                    },
                    "correctInput": {
                        "description": "Indicates which answers are the correct ones.",
                        "type": "array",
                        "items": {"anyOf": [{"type": "number"}, {"type": "string"}]},
                    },
                    "meta": {
                        "type": "object",
                        "required": ["inputRequired", "correctInputRequired"],
                        "properties": {
                            "inputRequired": {
                                "type": "boolean",
                                "description": "Whether or not an answer should be required from the user.",
                            },
                            "correctInputRequired": {
                                "type": "boolean",
                                "description": "Whether or not the correct answer should be required from the user.",
                            },
                        },
                    },
                },
            },
            "example_specification": {
                "label": "What are your favorite Marvel movies?",
                "inputOptions": ["Avengers", "Captain America", "WandaVision"],
                "correctInput": ["Avengers", "WandaVision"],
                "meta": {"inputRequired": True, "correctInputRequired": True},
            },
        },
    )

    # Numeric Range
    WorkflowStepUserInputType.objects.update_or_create(
        name="numeric_range_question",
        defaults={
            "json_schema": {
                "$schema": "http://json-schema.org/draft-07/schema",
                "$id": "http://github.com/crcresearch/",
                "type": "object",
                "title": "User Input: Numeric Range Question",
                "description": "A schema representing a numeric range question user input.",
                "required": ["label", "inputOptions", "meta"],
                "properties": {
                    "id": {
                        "type": "string",
                        "title": "A string-based user input identifier.",
                        "description": "This value may be managed outside of the object specification and so is optional.",
                        "examples": ["4125-1351-1251-asfd"],
                    },
                    "label": {
                        "type": "string",
                        "title": "UI Label for Input",
                        "description": "Label that should be displayed by user interfaces for this input.",
                        "examples": ["The label to display for the input/question."],
                    },
                    "inputOptions": {
                        "type": "object",
                        "properties": {
                            "minimumValue": {
                                "$id": "#/properties/options",
                                "type": "number",
                                "title": "Minimum Value",
                                "description": "The minimum value to be displayed to the user for this question.",
                            },
                            "maximumValue": {
                                "$id": "#/properties/options",
                                "type": "number",
                                "title": "Maximum Value",
                                "description": "The maximum value to be displayed to the user for this question.",
                            },
                            "step": {
                                "$id": "#/properties/options",
                                "type": "number",
                                "title": "Step Value",
                                "description": "The number between each entry between minimum and maximum.",
                            },
                        },
                    },
                    "correctInput": {
                        "description": "Indicates which answers are the correct ones.",
                        "type": "number",
                    },
                    "meta": {
                        "type": "object",
                        "required": ["inputRequired", "correctInputRequired"],
                        "properties": {
                            "inputRequired": {
                                "type": "boolean",
                                "description": "Whether or not an answer should be required from the user.",
                            },
                            "correctInputRequired": {
                                "type": "boolean",
                                "description": "Whether or not the correct answer should be required from the user.",
                            },
                        },
                    },
                },
            },
            "example_specification": {
                "label": "What is your favorite number?",
                "inputOptions": {"minimumValue": 0, "maximumValue": 100, "step": 1},
                "correctInput": 57,
                "meta": {"correctInputRequired": True, "inputRequired": True},
            },
        },
    )

    # Date Selection
    WorkflowStepUserInputType.objects.update_or_create(
        name="date_range_question",
        defaults={
            "json_schema": {
                "$schema": "http://json-schema.org/draft-07/schema",
                "$id": "http://github.com/crcresearch/",
                "type": "object",
                "title": "User Input: Date Range Question",
                "description": "A schema representing a date range question user input.",
                "required": ["label", "inputOptions", "meta"],
                "properties": {
                    "id": {
                        "type": "string",
                        "title": "A string-based user input identifier.",
                        "description": "This value may be managed outside of the object specification and so is optional.",
                        "examples": ["4125-1351-1251-asfd"],
                    },
                    "label": {
                        "type": "string",
                        "title": "UI Label for Input",
                        "description": "Label that should be displayed by user interfaces for this input.",
                        "examples": ["The label to display for the input/question."],
                    },
                    "inputOptions": {
                        "type": "object",
                        "properties": {
                            "earliestDate": {
                                "$id": "#/properties/options",
                                "type": "string",
                                "pattern": "(((19|20)([2468][048]|[13579][26]|0[48])|2000)[/-]02[/-]29|((19|20)[0-9]{2}[/-](0[469]|11)[/-](0[1-9]|[12][0-9]|30)|(19|20)[0-9]{2}[/-](0[13578]|1[02])[/-](0[1-9]|[12][0-9]|3[01])|(19|20)[0-9]{2}[/-]02[/-](0[1-9]|1[0-9]|2[0-8])))",
                                "title": "Earliest Date",
                                "description": "The earliest date to be displayed to the user for this question.",
                            },
                            "latestDate": {
                                "$id": "#/properties/options",
                                "type": "string",
                                "pattern": "(((19|20)([2468][048]|[13579][26]|0[48])|2000)[/-]02[/-]29|((19|20)[0-9]{2}[/-](0[469]|11)[/-](0[1-9]|[12][0-9]|30)|(19|20)[0-9]{2}[/-](0[13578]|1[02])[/-](0[1-9]|[12][0-9]|3[01])|(19|20)[0-9]{2}[/-]02[/-](0[1-9]|1[0-9]|2[0-8])))",
                                "title": "Latest Date",
                                "description": "The latest date to be displayed to the user for this question.",
                            },
                            "step": {
                                "$id": "#/properties/options",
                                "type": "number",
                                "title": "Step Value",
                                "description": "The number between each entry between earliest and latest.",
                            },
                            "stepInterval": {
                                "$id": "#/properties/options",
                                "type": "string",
                                "enum": ["year", "month", "day"],
                                "title": "Step Interval Value",
                                "description": "The time between each date entry",
                            },
                        },
                    },
                    "correctInput": {
                        "description": "Indicates which answers are the correct ones.",
                        "type": "string",
                        "pattern": "(((19|20)([2468][048]|[13579][26]|0[48])|2000)[/-]02[/-]29|((19|20)[0-9]{2}[/-](0[469]|11)[/-](0[1-9]|[12][0-9]|30)|(19|20)[0-9]{2}[/-](0[13578]|1[02])[/-](0[1-9]|[12][0-9]|3[01])|(19|20)[0-9]{2}[/-]02[/-](0[1-9]|1[0-9]|2[0-8])))",
                    },
                    "meta": {
                        "type": "object",
                        "required": ["inputRequired", "correctInputRequired"],
                        "properties": {
                            "inputRequired": {
                                "type": "boolean",
                                "description": "Whether or not an answer should be required from the user.",
                            },
                            "correctInputRequired": {
                                "type": "boolean",
                                "description": "Whether or not the correct answer should be required from the user.",
                            },
                        },
                    },
                },
            },
            "example_specification": {
                "label": "What is Ronald Reagan's Birthdate?",
                "meta": {"inputRequired": True, "correctInputRequired": True},
                "inputOptions": {
                    "earliestDate": "1900-01-01",
                    "latestDate": "1970-01-01",
                    "step": 1,
                    "stepInterval": "year",
                },
                "correctInput": "1935-01-01",
            },
        },
    )


class Migration(migrations.Migration):

    dependencies = [
        ("django_workflow_system", "0008_auto_20210723_1601"),
    ]

    operations = [
        migrations.RunPython(update_initial_user_input_types),
    ]
