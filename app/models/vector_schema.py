from pydantic import BaseModel
from datetime import datetime
from typing import List,Optional
class VectorSchema(BaseModel):
    vector: list
    metadata: str
    description: List[Optional[str]]
    description_score:Optional[List[str]]
    time:datetime