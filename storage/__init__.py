"""Storage layer.

BigQuery is the economic truth store.
Local JSON is for fast iteration and testing.

This layer handles I/O. Pipelines don't do I/O.
"""

from storage.bigquery import BigQueryStorage
from storage.local import LocalStorage

__all__ = ["BigQueryStorage", "LocalStorage"]
