# Studio Tools

A comprehensive VFX/Animation studio pipeline tools package demonstrating professional Python packaging best practices.

## Features

- **Asset Management**: Tools for managing 3D assets (characters, props, environments)
- **Shot Management**: Tools for production tracking and shot organization
- **Publishing Pipeline**: Version control and asset publishing to studio pipeline
- **Rendering Tools**: Support for multiple render engines (Arnold, Renderman)
- **Validation Framework**: Enforce studio standards and data validation

## Installation

```bash
pip install studio-tools
```

Or from source:

```bash
git clone https://github.com/gamutx/practice-python-packaging
cd practice-python-packaging
pip install -e .
```

## Quick Start

```python
from studio_tools.assets import AssetImporter
from studio_tools.shots import ShotCreator

# Import assets
importer = AssetImporter("path/to/assets")
importer.import_asset("character_model.fbx")

# Create shots
shot = ShotCreator("SH010")
shot.create_shot_directory()
```

## Package Structure

- `src/studio_tools/` - Main package directory
  - `assets/` - Asset management tools
  - `shots/` - Shot management tools
  - `publishing/` - Publishing pipeline tools
  - `rendering/` - Render engine integrations
  - `validation/` - Validation and verification tools
  - `config/` - Configuration files for the pipeline

## Configuration

Configuration files are located in the `config/` directory:
- `pipeline.yaml` - Main pipeline configuration
- `render_engines.json` - Render engine settings
- `studio_standards.yaml` - Studio validation standards

## Development

This project is designed as a learning resource for Python packaging best practices including:
- Using `setup.py` for package configuration
- Understanding `MANIFEST.in` for file inclusion
- Package metadata and classifiers
- Creating distribution formats (wheels and source distributions)

## Testing

```bash
python -m pytest tests/
```

## License

MIT License - See LICENSE file for details

## Contributing

This is an educational project for learning Python packaging principles.