#!/bin/bash
# Studio Tools Pipeline Runner - Linux/macOS
# This script demonstrates entry point scripts for the package
# Entry points can also be configured in setup.py/pyproject.toml

set -e  # Exit on error

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}=== Studio Tools Pipeline Runner ===${NC}"
echo "Platform: Linux/macOS"

# Check if studio_tools is installed
if ! python3 -c "import studio_tools" 2>/dev/null; then
    echo -e "${BLUE}Installing studio_tools...${NC}"
    pip install -e "$(dirname "$0")/.."
fi

# Run the pipeline
echo -e "${BLUE}Starting pipeline tasks...${NC}"

# Import and use the studio_tools package
python3 << 'EOF'
from studio_tools.shots.shot_creator import ShotCreator
from studio_tools.publishing.publisher import AssetPublisher
from studio_tools.validation.asset_checker import AssetChecker

print("\nInitializing pipeline components...")

# Create a shot
shot = ShotCreator("SQ001_SH010", "/tmp/studio_project")
print(f"✓ Shot created: {shot.shot_name}")
print(f"  Path: {shot.shot_path}")

# Initialize publisher
publisher = AssetPublisher("/tmp/studio_archive")
print(f"✓ Publisher initialized")

# Initialize checker
checker = AssetChecker()
print(f"✓ Asset checker ready")

print("\n" + "="*50)
print("Pipeline components ready for use!")
print("="*50)
EOF

echo -e "${GREEN}✓ Pipeline runner completed successfully${NC}"
