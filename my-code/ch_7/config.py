import os
from typing import Optional, Any
from pydantic import BaseModel


class Config(BaseModel):

    default_model: str = "deepseek-v4-flash"
    default_provider: str = "openai"
    temperature: float = 1.0
    max_tok: Optional[int] = None

    debug: bool = False
    log_level: str = "INFO"

    max_history_length: int = 100

    @classmethod
    def from_env(cls) -> "Config":
        return cls(
            debug=os.getenv("DEBUG", "false").lower() == "true",
            log_level=os.getenv("LOG_LEVEL", "INFO"),
            temperature=float(os.getenv("TEMPERATURE", "1.0")),
            max_tokens=int(os.getenv("MAX_TOEKNS")) if os.getenv("MAX_TOKENS") else None,
        )

    def to_dict(self) -> dict[str, Any]:
        return self.dict()
