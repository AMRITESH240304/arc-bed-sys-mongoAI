from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class GoogleAuthUser(BaseModel):
    google_user_id:str
    display_name:str
    email:str
    created_at:datetime