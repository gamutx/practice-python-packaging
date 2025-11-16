"""Asset validation and verification tools for studio pipeline.

Provides utilities for validating assets against studio standards.
"""

import logging
from pathlib import Path
from typing import List, Tuple

logger = logging.getLogger(__name__)


class AssetChecker:
    """Validate assets against studio standards."""
    
    def __init__(self):
        """Initialize asset checker."""
        self.check_results = []
        logger.info("AssetChecker initialized")
    
    def run_asset_checks(self, asset_path: str) -> Tuple[bool, List[str]]:
        """Run all validation checks on an asset.
        
        Args:
            asset_path: Path to the asset file
            
        Returns:
            Tuple of (success: bool, messages: List[str])
        """
        asset_file = Path(asset_path)
        messages = []
        
        # Check file exists
        if not asset_file.exists():
            messages.append(f"❌ Asset file not found: {asset_path}")
            return False, messages
        
        messages.append(f"✓ Asset file found: {asset_file.name}")
        
        # Check file size
        file_size_mb = asset_file.stat().st_size / (1024 * 1024)
        if file_size_mb > 500:
            messages.append(f"⚠ Large file size: {file_size_mb:.2f}MB (>500MB)")
        else:
            messages.append(f"✓ File size acceptable: {file_size_mb:.2f}MB")
        
        # Check file extension
        supported_extensions = ['.fbx', '.abc', '.usd', '.obj']
        if asset_file.suffix.lower() not in supported_extensions:
            messages.append(f"❌ Unsupported file format: {asset_file.suffix}")
            return False, messages
        
        messages.append(f"✓ Supported file format: {asset_file.suffix}")
        
        # Store results
        self.check_results.append({
            'asset': str(asset_path),
            'passed': True,
            'messages': messages
        })
        
        return True, messages
    
    def check_naming_convention(self, asset_name: str) -> Tuple[bool, str]:
        """Check if asset name follows studio conventions.
        
        Args:
            asset_name: Name of the asset
            
        Returns:
            Tuple of (valid: bool, message: str)
        """
        # Simple validation: must contain underscore, no spaces
        if ' ' in asset_name:
            return False, "Asset name cannot contain spaces"
        
        if '_' not in asset_name:
            return False, "Asset name must follow format: type_name_version"
        
        return True, "Asset name follows naming conventions"
    
    def get_check_results(self):
        """Get all check results.
        
        Returns:
            List of check result dictionaries
        """
        return self.check_results.copy()


def run_asset_checks(asset_name):
    """Legacy function to run asset checks.
    
    Note: Use AssetChecker class for new code.
    """
    checker = AssetChecker()
    print(f"🔍 Running asset checks for: {asset_name}")
    success, messages = checker.run_asset_checks(asset_name)
    if success:
        print("✅ All checks passed!")
    else:
        print("❌ Some checks failed")
        for msg in messages:
            print(f"  {msg}")
    return success