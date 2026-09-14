from agent import Agent
from message import Message

SYSTEM_PROMPT = """
You are a helpful assistant.
"""

class ChatAgent(Agent):
    def __init__(
        self,
        name,
        system_prompt = SYSTEM_PROMPT,
        config = None,
        max_turn = 1_000,
    ):
        super().__init__(name, system_prompt, config)
        self._history: list[Message] = []
        self.max_turn = max_turn

    def run(self, input_text: str, **kwargs) -> str:
        messages = []
        messages.append({"role": "system", "content": self.system_prompt})
        for m in self._history:
            messages.append(
                {
                    "role": m.role,
                    "content": m.content,
                }
            )

        user_msg = Message(
            role="user",
            content=input_text,
        )
        messages.append(user_msg.to_dict())

        response = self.llm.invoke(messages)
        llm_res = Message(
            role="assistant",
            content=response.content
        )

        self.add_message(user_msg)
        self.add_message(llm_res)

        return llm_res.content

    def chat(self):
        for _ in range(self.max_turn):
            input_text = input("> ").strip()
            if input_text in ["q", "quit", "exit"]:
                print("Bye")
                break

            resp = self.run(input_text)
            print(resp)
