from typing import Literal, Optional, Any, override
from datetime import datetime
from pydantic import BaseModel


MessageRoles = Literal["user", "assistant", "system", "tool"]
# ensure a legal role for OpenAI api

class Message(BaseModel):
    content: str
    role: MessageRoles
    timestamp:  datetime = None
    metadata: Optional[dict[str, Any]] = None

    def  __init__(self, content:str, role: MessageRoles, **kwargs):
        super().__init__(
            content=content,
            role=role,
            timestamp=kwargs.get("timestamp", datetime.now()),
            metadata=kwargs.get("metadata", {})
        )
    def to_dict(self) -> dict[str, Any]:
        return {
            "role": self.role,
            "content": self.content,
        }
    @override
    def __str__(self) -> str:
        return f"[{self.role}] {self.content}"
