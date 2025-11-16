"""Unit tests for studio_tools package.

Demonstrates how to test package functionality.
"""

import pytest
from pathlib import Path
from studio_tools.assets.importer import AssetImporter
from studio_tools.shots.shot_creator import ShotCreator
from studio_tools.publishing.publisher import AssetPublisher
from studio_tools.validation.asset_checker import AssetChecker
from studio_tools.rendering.arnold import ArnoldRenderer


class TestAssetImporter:
    """Tests for AssetImporter class."""
    
    def test_importer_initialization(self):
        """Test AssetImporter initialization."""
        importer = AssetImporter("/test/assets")
        assert importer.base_path.name == "assets"
        assert importer.imported_assets == []
    
    def test_import_asset_with_valid_format(self):
        """Test importing asset with valid format."""
        importer = AssetImporter("/test/assets")
        # This will fail on Windows since file doesn't exist, but tests logic
        result = importer.import_asset("nonexistent.fbx")
        assert result is False  # File doesn't exist
    
    def test_get_imported_assets(self):
        """Test getting list of imported assets."""
        importer = AssetImporter("/test/assets")
        assets = importer.get_imported_assets()
        assert isinstance(assets, list)
        assert len(assets) == 0


class TestShotCreator:
    """Tests for ShotCreator class."""
    
    def test_shot_creator_initialization(self):
        """Test ShotCreator initialization."""
        shot = ShotCreator("SQ010_SH020")
        assert shot.shot_name == "SQ010_SH020"
        assert shot.shot_path.name == "SQ010_SH020"
    
    def test_get_shot_info(self):
        """Test getting shot information."""
        shot = ShotCreator("SQ010_SH020")
        info = shot.get_shot_info()
        assert info['shot_name'] == "SQ010_SH020"
        assert 'created_at' in info
        assert 'shot_path' in info


class TestAssetPublisher:
    """Tests for AssetPublisher class."""
    
    def test_publisher_initialization(self):
        """Test AssetPublisher initialization."""
        publisher = AssetPublisher("/archive")
        assert publisher.archive_path.name == "archive"
        assert publisher.published_assets == []
    
    def test_get_published_assets(self):
        """Test getting published assets list."""
        publisher = AssetPublisher()
        assets = publisher.get_published_assets()
        assert isinstance(assets, list)
        assert len(assets) == 0


class TestAssetChecker:
    """Tests for AssetChecker class."""
    
    def test_checker_initialization(self):
        """Test AssetChecker initialization."""
        checker = AssetChecker()
        assert checker.check_results == []
    
    def test_check_naming_convention_valid(self):
        """Test naming convention check with valid name."""
        checker = AssetChecker()
        valid, msg = checker.check_naming_convention("character_model_v001")
        assert valid is True
    
    def test_check_naming_convention_invalid_spaces(self):
        """Test naming convention check with invalid spaces."""
        checker = AssetChecker()
        valid, msg = checker.check_naming_convention("character model")
        assert valid is False
    
    def test_check_naming_convention_no_underscore(self):
        """Test naming convention check without underscore."""
        checker = AssetChecker()
        valid, msg = checker.check_naming_convention("charactermodel")
        assert valid is False


class TestArnoldRenderer:
    """Tests for ArnoldRenderer class."""
    
    def test_renderer_initialization(self):
        """Test ArnoldRenderer initialization."""
        renderer = ArnoldRenderer("MyProject")
        assert renderer.project_name == "MyProject"
        assert isinstance(renderer.settings, dict)
    
    def test_setup_render_layers(self):
        """Test setting up render layers."""
        renderer = ArnoldRenderer("MyProject")
        result = renderer.setup_render_layers()
        assert result is True
        assert len(renderer.render_layers) > 0
    
    def test_set_samples(self):
        """Test setting render samples."""
        renderer = ArnoldRenderer("MyProject")
        renderer.set_samples(12)
        assert renderer.settings['samples'] == 12
    
    def test_set_invalid_samples(self):
        """Test setting invalid sample count."""
        renderer = ArnoldRenderer("MyProject")
        renderer.set_samples(-5)
        assert renderer.settings['samples'] == 1
    
    def test_get_render_settings(self):
        """Test getting render settings."""
        renderer = ArnoldRenderer("MyProject")
        settings = renderer.get_render_settings()
        assert isinstance(settings, dict)
        assert 'samples' in settings
        assert 'threads' in settings
    
    def test_get_render_info(self):
        """Test getting render information."""
        renderer = ArnoldRenderer("MyProject")
        info = renderer.get_render_info()
        assert info['project'] == "MyProject"
        assert info['engine'] == "Arnold"
        assert 'layers' in info
        assert 'settings' in info


if __name__ == "__main__":
    pytest.main([__file__, "-v"])