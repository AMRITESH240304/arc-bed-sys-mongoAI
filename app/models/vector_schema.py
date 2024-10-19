from pydantic import BaseModel

class VectorSchema(BaseModel):
    vector: list
    metadata: str