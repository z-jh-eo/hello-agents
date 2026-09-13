import os
from pathlib import Path
from dotenv import load_dotenv
from dataclasses import dataclass
from openai import OpenAI, AsyncOpenAI

load_dotenv(Path(__file__).resolve().parents[1]/".env")

@dataclass
class LLMResponse:
    content: str
    model: str


class MyLLM:
    def __init__(
            self,
            model: str|None = None,
            base_url: str|None = None,
            api_key: str|None = None,
            timeout: int|None = None,
        ):
        self.model = model or os.getenv("LLM_MODEL_ID")
        self.base_url = base_url or os.getenv("LLM_BASE_URL")
        self.api_key = api_key or os.getenv("LLM_API_KEY")
        self.timeout = timeout or int(os.getenv("LLM_TIMEOUT", "60"))

        if not self.model:
            raise Exception("Model ID not found")
        if not self.base_url:
            raise Exception("Base URL not found")
        if not self.api_key:
            raise Exception("API key not found")

        self._llm = OpenAI(
            base_url=self.base_url,
            api_key=self.api_key,
            timeout=self.timeout,
        )

    def invoke(self, messages: list[dict[str, str]]) -> LLMResponse:

        try:
            completion = self._llm.chat.completions.create(
                model=self.model,
                messages=messages
            )
            response = LLMResponse(
                model=self.model,
                content=completion.choices[0].message.content,
            )
            return response 

        except Exception as e:
            raise RuntimeError(f"LLM call failed: {e}") from e
