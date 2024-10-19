from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class HistoryModel(BaseModel):
    user_refrence:str
    urls:List[str]
    accessed_at:datetime
    metadata:Optional[str] = None
    
