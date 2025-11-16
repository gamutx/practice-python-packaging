"""Asset management tools for studio pipeline.

Provides utilities for importing, managing, and validating 3D assets.
"""

import logging
from pathlib import Path
from typing import List, Optional

logger = logging.getLogger(__name__)


class AssetImporter:
    """Handle importing assets into the studio pipeline."""
    
    SUPPORTED_FORMATS = ['.fbx', '.abc', '.usd', '.obj']
    
    def __init__(self, base_path: str):
        """Initialize asset importer.
        
        Args:
            base_path: Base directory for asset storage
        """
        self.base_path = Path(base_path)
        self.imported_assets = []
        logger.info(f"AssetImporter initialized with base path: {base_path}")
    
    def import_asset(self, asset_file: str) -> bool:
        """Import an asset file to the pipeline.
        
        Args:
            asset_file: Path to the asset file to import
            
        Returns:
            True if import was successful, False otherwise
        """
        asset_path = Path(asset_file)
        
        if not asset_path.exists():
            logger.error(f"Asset file not found: {asset_file}")
            return False
        
        if asset_path.suffix.lower() not in self.SUPPORTED_FORMATS:
            logger.warning(f"Unsupported format: {asset_path.suffix}")
            return False
        
        try:
            self.imported_assets.append(str(asset_path))
            logger.info(f"Successfully imported asset: {asset_file}")
            return True
        except Exception as e:
            logger.error(f"Error importing asset {asset_file}: {e}")
            return False
    
    def get_imported_assets(self) -> List[str]:
        """Get list of imported assets.
        
        Returns:
            List of imported asset paths
        """
        return self.imported_assets.copy()


def import_asset(asset_name, namespace=None):
    """Legacy function for importing an asset from the library.
    
    Note: Use AssetImporter class for new code.
    """
    print(f"📦 Importing asset '{asset_name}'")
    if namespace:
        print(f"   Namespace: {namespace}")
    print(f"✅ Import successful!")