# Generated by Django 3.1.8 on 2021-06-04 00:25


from django.db import migrations


def update_initial_user_input_types_image(apps, schema_editor):
    """
    Initialize the database with the WorkflowStepUserInputType that we have schemas available for.
    """
    WorkflowStepUserInputType = apps.get_model(
        "django_workflow_system", "WorkflowStepUserInputType"
    )

    # Single Choice Question
    WorkflowStepUserInputType.objects.update_or_create(
        name="single_choice_image_question",
        defaults={
            "json_schema": {
                "$schema": "http://json-schema.org/draft-07/schema",
                "$id": "http://github.com/crcresearch/",
                "type": "object",
                "title": "User Input: Single Choice Image Question",
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
                        "description": "The options source to be displayed to the user for this question.",
                        "minItems": 2,
                        "uniqueItems": True,
                        "items": {"anyOf": [ {"type": "string"}]},
                    },
                    "correctInput": {
                        "description": "Indicates which answer is the correct one.",
                        "anyOf": [{"type": "string"}],
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
                "inputOptions": ["path_to_image/Red.jpg", "path_to_image/Blue.jpg"],
                "correctInput": "path_to_image/Red.jpg",
                "meta": {"inputRequired": True, "correctInputRequired": True},
            },
        },
    )

    # Multiple Choice Question
    WorkflowStepUserInputType.objects.update_or_create(
        name="multiple_choice_image_question",
        defaults={
            "json_schema": {
                "$schema": "http://json-schema.org/draft-07/schema",
                "$id": "http://github.com/crcresearch/",
                "type": "object",
                "title": "User Input: Multiple Choice Image Question",
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
                        "items": {"anyOf": [ {"type": "string"}]},
                    },
                    "correctInput": {
                        "description": "Indicates which answers are the correct ones.",
                        "type": "array",
                        "items": {"anyOf": [{"type": "string"}]},
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
                "inputOptions": ["path_to_image/Avengers.jpg", "path_to_image/CaptainAmerica.jpg", "path_to_image/WandaVision.jpg"],
                "correctInput": ["path_to_image/Avengers.jpeg", "path_to_image/WandaVision.jpg"],
                "meta": {"inputRequired": True, "correctInputRequired": True},
            },
        },
    )



class Migration(migrations.Migration):

    dependencies = [
        ("django_workflow_system", "0014_auto_20220512_1033"),
    ]

    operations = [
        migrations.RunPython(update_initial_user_input_types_image),
    ]