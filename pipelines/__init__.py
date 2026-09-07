"""Pipeline layer.

Pipelines are pure transform functions: Input → Transform → Output.
They don't do I/O. Storage layer handles persistence.

Each pipeline:
1. Takes typed input (Pydantic models)
2. Applies transformations (pure functions)
3. Returns typed output (Pydantic models)
4. Has no side effects
"""

from pipelines.gmail_import import GmailImportPipeline
from pipelines.state_machine import StateMachinePipeline
from pipelines.hypothesis_ledger import HypothesisLedgerPipeline
from pipelines.evi_planner import EVIPlannerPipeline
from pipelines.kernel_generator import KernelGeneratorPipeline

__all__ = [
    "GmailImportPipeline",
    "StateMachinePipeline",
    "HypothesisLedgerPipeline",
    "EVIPlannerPipeline",
    "KernelGeneratorPipeline",
]
