from pydantic import BaseModel
from typing import Dict, Any


class EveModel(BaseModel):
    @classmethod
    def cerberus_schema(cls) -> Dict[str, Any]:
        json_schema = cls.model_json_schema()
        props = json_schema.get("properties", {})
        required = json_schema.get("required", [])

        cerberus_schema = {}

        for field, details in props.items():
            field_schema = {}
            json_type = details.get("type")

            if json_type == "string":
                field_schema["type"] = "string"

                if "minLength" in details:
                    field_schema["minlength"] = details["minLength"]

                if "maxLength" in details:
                    field_schema["maxlength"] = details["maxLength"]

                if details.get("format") == "email":
                    field_schema["regex"] = r"^[^@]+@[^@]+\.[^@]+$"

            elif json_type == "integer":
                field_schema["type"] = "integer"

                if "minimum" in details:
                    field_schema["min"] = details["minimum"]

                if "maximum" in details:
                    field_schema["max"] = details["maximum"]

            elif json_type == "number":
                field_schema["type"] = "float"

            elif json_type == "boolean":
                field_schema["type"] = "boolean"

            elif json_type == "array":
                field_schema["type"] = "list"

            elif json_type == "object":
                field_schema["type"] = "dict"

            else:
                field_schema["type"] = "string" 

            if field in ["password", "token"]:
                field_schema["writeonly"] = True

            if field in required:
                field_schema["required"] = True

            cerberus_schema[field] = field_schema

        return cerberus_schema
