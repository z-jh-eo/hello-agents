from abc import ABC, abstractmethod
from typing import Any, override

from code.chapter6.CAMEL.DigitalBookWriting import LLM_BASE_URL
from .message import Message
from .config import Config
from .llm import MyLLM


class Agent(ABC):
    def __init__(
        self,
        name: str,
        llm: MyLLM,
        system_prompt: str|None = None,
        config: Config|None = None,
    ):
        self.name = name
        self.llm = llm
        self.system_prompt = system_prompt
        self.config = config or Config()
        self._history: list[Message] = []

    @abstractmethod
    def run(self, input_text: str, **kwargs) -> str:
        pass

    def add_message(self, message: Message):
        self._history.append(message)

    def clear_history(self):
        self._history.clear()

    def get_history(self) -> list[Message]:
        return self._history.copy()

    @override
    def __str__(self) -> str:
        return f"Agent(name={self.name}, provider={self.llm.provider})"
