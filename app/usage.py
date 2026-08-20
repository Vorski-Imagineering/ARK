"""Usage and cost accounting for model calls.

The run log records identifiers and counts only, never prompt text, question
text, or generated output. That constraint is what allows a sanitised usage
summary to be published while the raw content stays local.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Usage:
    input_tokens: int
    output_tokens: int
    estimated_cost_usd: float
