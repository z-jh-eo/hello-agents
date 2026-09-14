from message import Message
from llm import MyLLM
from simple_chat_agent import ChatAgent


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


def test_simple_agent():
    agent = ChatAgent(name="simple_test")
    agent.chat()



if __name__ == "__main__":
    test_simple_agent()
