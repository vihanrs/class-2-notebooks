"""
Assignment 10: Synthesis Orchestrator (Two-Stage Pipeline)

Goal: Extract key claims from multiple short notes in parallel, then synthesize
them into a single, coherent summary highlighting agreements and conflicts.
"""

import os
from typing import List, Dict


class SynthesisOrchestrator:
    """Two-stage pipeline: extractor (batch) → synthesizer (single).

    Implementations should build two chains and wire them together.
    """

    def __init__(self):
        """Prepare prompt strings and placeholders.

        Provide:
        - extractor_system / extractor_user (variables: {note})
        - synthesizer_system / synthesizer_user (variables: {claims})
        - placeholders for prompts, llm(s), and chains; keep None with TODOs.
        """
        self.extractor_system = "You extract 1-2 key claims from a note, neutral voice."
        self.extractor_user = "Note: {note}\nReturn bullet points of key claims."
        self.synth_system = "You synthesize claims into a compact, balanced summary."
        self.synth_user = (
            "Claims from multiple notes:\n{claims}\n"
            "Return: Overall Summary; Agreements; Conflicts. Keep concise."
        )

        # TODO: Build prompts and LLM(s)
        self.extract_prompt = None
        self.synth_prompt = None
        self.llm = None
        self.extract_chain = None
        self.synth_chain = None

    def extract_claims(self, notes: List[str]) -> List[str]:
        """Return a list of extracted claims lists (as strings), one per note.

        Implement using `.batch()` on the extractor chain.
        """
        raise NotImplementedError("Implement batch claim extraction.")

    def synthesize(self, claims: List[str]) -> str:
        """Return a synthesis from already-extracted claims.

        Implement: invoke synthesizer chain with a joined claims string.
        """
        raise NotImplementedError("Implement final synthesis step.")

    def run(self, notes: List[str]) -> str:
        """End-to-end: extract claims (batch) then synthesize a final output."""
        raise NotImplementedError("Wire extract→synthesize end-to-end.")


def _demo():
    if not os.getenv("OPENAI_API_KEY"):
        print("⚠️ Set OPENAI_API_KEY before running.")
    orch = SynthesisOrchestrator()
    notes = [
        "Team A reduced latency by 20% after switching cache strategy.",
        "Users report fewer timeouts; however, spikes still occur on Mondays.",
        "Data suggests cache hit rate improved but cold-starts remain high.",
    ]
    try:
        print("\n🧪 Synthesis Orchestrator — demo\n" + "-" * 42)
        print(orch.run(notes))
    except NotImplementedError as e:
        print(e)


if __name__ == "__main__":
    _demo()
