from typing import Optional, Dict, List
from pydantic import BaseModel

class Document(BaseModel):
    id: str
    text: str