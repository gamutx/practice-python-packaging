"""Example usage of the studio_tools package.

This demonstrates how to use the various modules in the package
for a typical VFX studio workflow.
"""

from studio_tools.assets.importer import AssetImporter
from studio_tools.shots.shot_creator import ShotCreator
from studio_tools.publishing.publisher import AssetPublisher
from studio_tools.validation.asset_checker import AssetChecker
from studio_tools.rendering.arnold import ArnoldRenderer


def main():
    """Main example demonstrating package usage."""
    
    print("=" * 60)
    print("Studio Tools Package - Usage Examples")
    print("=" * 60)
    
    # Example 1: Create a shot
    print("\n[1] Creating a new shot...")
    shot = ShotCreator("SQ010_SH020", "/studio/projects")
    shot_info = shot.get_shot_info()
    print(f"    Shot: {shot_info['shot_name']}")
    print(f"    Path: {shot_info['shot_path']}")
    
    # Example 2: Import assets
    print("\n[2] Asset Importer...")
    importer = AssetImporter("/studio/assets")
    print(f"    Base path: {importer.base_path}")
    print(f"    Supported formats: {', '.join(AssetImporter.SUPPORTED_FORMATS)}")
    
    # Example 3: Validate assets
    print("\n[3] Validating assets...")
    checker = AssetChecker()
    valid, msg = checker.check_naming_convention("character_model_v001")
    print(f"    Asset name validation: {msg}")
    
    # Example 4: Publish assets
    print("\n[4] Publishing assets...")
    publisher = AssetPublisher("/studio/archive")
    print(f"    Archive path: {publisher.archive_path}")
    
    # Example 5: Arnold render setup
    print("\n[5] Arnold Renderer Setup...")
    renderer = ArnoldRenderer("SQ010_SH020")
    renderer.setup_render_layers()
    renderer.set_samples(12)
    info = renderer.get_render_info()
    print(f"    Project: {info['project']}")
    print(f"    Engine: {info['engine']}")
    print(f"    Render layers: {', '.join(info['layers'])}")
    print(f"    Samples: {info['settings']['samples']}")
    
    # Example 6: Load configuration
    print("\n[6] Configuration Management...")
    try:
        from studio_tools.config import PIPELINE_CONFIG, STUDIO_STANDARDS
        print(f"    Pipeline config loaded: {bool(PIPELINE_CONFIG)}")
        print(f"    Studio standards loaded: {bool(STUDIO_STANDARDS)}")
    except ImportError:
        print("    Note: YAML support requires pyyaml package")
    
    print("\n" + "=" * 60)
    print("Examples completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()