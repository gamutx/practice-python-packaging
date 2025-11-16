"""
Publishing Sub-package

Tools for versioning and publishing assets to the pipeline.
"""

from .publisher import publish_asset

__all__ = [
    "publish_asset"
]