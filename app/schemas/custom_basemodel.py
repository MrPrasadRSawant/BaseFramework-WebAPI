from pydantic import BaseModel, ConfigDict


class CustomBaseModel(BaseModel):
    """
    Common base model for all Pydantic schemas.

    Internal Python field names remain in snake_case,
    while API aliases can use PascalCase.
    """
    model_config = ConfigDict(
        # Reject fields that are not defined in the model.
        # Helps catch unexpected or incorrect input fields.
        extra="forbid",

        # Automatically remove leading/trailing spaces from strings.
        # Example: "  Prasad  " -> "Prasad"
        str_strip_whitespace=True,

        # Re-validate a field when its value is changed after model creation.
        validate_assignment=True,

        # Allow creating Pydantic models from object attributes.
        # Useful when converting SQLAlchemy ORM objects into response models.
        from_attributes=True,
    )
