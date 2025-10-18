"""
Assignment 8: Micro-Coach (On-Demand Streaming)

Goal: Provide a short plan non-streamed, and when `stream=True` deliver
encouraging guidance token-by-token via a callback.
"""

import os
from typing import Any


class PrintTokens:
    """Minimal callback-like interface for printing tokens.

    Implement compatibility with LangChain callback protocol if desired.
    """

    def on_llm_new_token(self, token: str, **kwargs: Any) -> None:
        print(token, end="")


class MicroCoach:
    def __init__(self):
        """Store prompt strings and prepare placeholders.

        Provide:
        - `system_prompt` motivating but practical tone
        - `user_prompt` with variables {goal}, {time_available}
        - `self.llm_streaming` and `self.llm_plain` placeholders (None), with TODOs
        - `self.stream_prompt` and `self.plain_prompt` placeholders (None), with TODOs
        """
        self.system_prompt = (
            "You are a supportive micro-coach. Keep plans realistic and brief."
        )
        self.user_prompt = "Goal: {goal}\nTime: {time_available}\nReturn a 3-step plan."

        # TODO: Build prompts and LLMs (streaming and non-streaming)
        self.llm_streaming = None
        self.llm_plain = None
        self.stream_prompt = None
        self.plain_prompt = None
        self.stream_chain = None
        self.plain_chain = None

    def coach(self, goal: str, time_available: str, stream: bool = False) -> str:
        """Return guidance using streaming or non-streaming path.

        Implement:
        - If `stream=True`, attach a token printer callback and stream output.
        - Else, return a compact non-streamed plan string.
        """
        raise NotImplementedError("Implement streaming vs non-streaming coaching.")


def _demo():
    if not os.getenv("OPENAI_API_KEY"):
        print("⚠️ Set OPENAI_API_KEY before running.")
    coach = MicroCoach()
    try:
        print("\n🏃 Micro-Coach — demo\n" + "-" * 40)
        print(coach.coach("resume drafting", "25 minutes", stream=False))
        print()
        print("\nStreaming example:")
        coach.coach("push-ups habit", "10 minutes", stream=True)
        print()
    except NotImplementedError as e:
        print(e)


if __name__ == "__main__":
    _demo()
