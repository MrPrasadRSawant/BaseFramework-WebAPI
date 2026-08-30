from .custom_basemodel import CustomBaseModel
from pydantic import Field, field_validator


class HealthResponse(CustomBaseModel):
    status: str = Field(default="OK")
    version_major: int = Field(default=1, serialization_alias="versionMajor")
    version_minor: int = Field(default=0, serialization_alias="versionMinor")
    version_patch: int = Field(default=0, serialization_alias="versionPatch")

    @field_validator("status")
    @classmethod
    def validate_status(cls, value: str) -> str:
        if value not in ["OK", "DOWN"]:
            raise ValueError("Status must be either 'OK' or 'DOWN'")
        return value
