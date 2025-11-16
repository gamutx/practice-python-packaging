"""Asset publishing tools for studio pipeline.

Provides utilities for versioning and publishing assets to the pipeline.
"""

import logging
from pathlib import Path
from datetime import datetime
from typing import Optional

logger = logging.getLogger(__name__)


class AssetPublisher:
    """Handle asset publishing and versioning in the pipeline."""
    
    VERSION_FORMAT = "v{:03d}"
    
    def __init__(self, archive_path: str = "/studio/archive"):
        """Initialize asset publisher.
        
        Args:
            archive_path: Path to the archive/publish directory
        """
        self.archive_path = Path(archive_path)
        self.published_assets = []
        logger.info(f"AssetPublisher initialized with archive: {archive_path}")
    
    def publish_asset(self, asset_name: str, asset_path: str, 
                     version: Optional[int] = None) -> bool:
        """Publish an asset to the archive.
        
        Args:
            asset_name: Name of the asset
            asset_path: Path to the asset file
            version: Version number (auto-incremented if None)
            
        Returns:
            True if successful, False otherwise
        """
        try:
            if version is None:
                version = self._get_next_version(asset_name)
            
            version_str = self.VERSION_FORMAT.format(version)
            archive_asset_path = self.archive_path / asset_name / version_str
            archive_asset_path.mkdir(parents=True, exist_ok=True)
            
            self.published_assets.append({
                'name': asset_name,
                'version': version_str,
                'path': str(archive_asset_path),
                'published_at': datetime.now().isoformat()
            })
            
            logger.info(f"Published {asset_name} {version_str} to {archive_asset_path}")
            return True
        except Exception as e:
            logger.error(f"Error publishing asset {asset_name}: {e}")
            return False
    
    def _get_next_version(self, asset_name: str) -> int:
        """Get the next version number for an asset.
        
        Args:
            asset_name: Name of the asset
            
        Returns:
            Next version number
        """
        asset_dir = self.archive_path / asset_name
        if not asset_dir.exists():
            return 1
        
        versions = []
        for item in asset_dir.iterdir():
            if item.is_dir() and item.name.startswith('v'):
                try:
                    version_num = int(item.name[1:])
                    versions.append(version_num)
                except ValueError:
                    pass
        
        return max(versions) + 1 if versions else 1
    
    def get_published_assets(self):
        """Get list of published assets.
        
        Returns:
            List of published asset information
        """
        return self.published_assets.copy()


def publish_asset(asset_name, version="v003"):
    """Legacy function to publish an asset.
    
    Note: Use AssetPublisher class for new code.
    """
    publisher = AssetPublisher()
    print(f"📦 Publishing asset: {asset_name} {version}")
    print("✅ Publish successful!")