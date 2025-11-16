"""Configuration module for studio_tools package.

This module provides utilities for loading and managing configuration files
included with the package. This demonstrates how to access non-Python files
bundled with a Python package.
"""

from pathlib import Path
import json
import yaml

# Get the config directory path
CONFIG_DIR = Path(__file__).parent


def load_yaml_config(filename: str) -> dict:
    """Load a YAML configuration file.
    
    Args:
        filename: Name of the YAML file in the config directory
        
    Returns:
        Dictionary containing the loaded configuration
    """
    config_file = CONFIG_DIR / filename
    if not config_file.exists():
        raise FileNotFoundError(f"Configuration file not found: {filename}")
    
    try:
        with open(config_file, 'r') as f:
            return yaml.safe_load(f)
    except yaml.YAMLError as e:
        raise ValueError(f"Error parsing YAML file {filename}: {e}")


def load_json_config(filename: str) -> dict:
    """Load a JSON configuration file.
    
    Args:
        filename: Name of the JSON file in the config directory
        
    Returns:
        Dictionary containing the loaded configuration
    """
    config_file = CONFIG_DIR / filename
    if not config_file.exists():
        raise FileNotFoundError(f"Configuration file not found: {filename}")
    
    try:
        with open(config_file, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f"Error parsing JSON file {filename}: {e}")


# Load default configurations
try:
    PIPELINE_CONFIG = load_yaml_config("pipeline.yaml")
    STUDIO_STANDARDS = load_yaml_config("studio_standards.yaml")
    RENDER_ENGINES = load_json_config("render_engines.json")
except Exception as e:
    print(f"Warning: Could not load default configurations: {e}")
    PIPELINE_CONFIG = {}
    STUDIO_STANDARDS = {}
    RENDER_ENGINES = {}


__all__ = [
    'CONFIG_DIR',
    'load_yaml_config',
    'load_json_config',
    'PIPELINE_CONFIG',
    'STUDIO_STANDARDS',
    'RENDER_ENGINES',
]
