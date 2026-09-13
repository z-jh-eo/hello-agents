from message import Message
from llm import MyLLM


def test_llm():
    system_prompt = Message(
        content="you are a helpfull assistant.",
        role="system",
    ).to_dict()
    user_msg = Message(
        role="user",
        content="Test"
    ).to_dict()
    llm = MyLLM()
    response = llm.invoke(
        messages=[
            system_prompt,
            user_msg,
        ]
    )
    print(response.content)


if __name__ == "__main__":
    test_llm()
