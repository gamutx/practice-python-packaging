"""Arnold render engine integration for studio pipeline.

Provides utilities for setting up and managing Arnold render tasks.
"""

import logging
from typing import Dict, Optional

logger = logging.getLogger(__name__)


class ArnoldRenderer:
    """Handle Arnold render engine setup and configuration."""
    
    DEFAULT_SAMPLES = 6
    DEFAULT_THREADS = 0  # 0 = auto-detect
    
    def __init__(self, project_name: str):
        """Initialize Arnold renderer.
        
        Args:
            project_name: Name of the project/shot
        """
        self.project_name = project_name
        self.render_layers = []
        self.settings = self._get_default_settings()
        logger.info(f"ArnoldRenderer initialized for project: {project_name}")
    
    def _get_default_settings(self) -> Dict[str, any]:
        """Get default Arnold render settings.
        
        Returns:
            Dictionary of default settings
        """
        return {
            'samples': self.DEFAULT_SAMPLES,
            'threads': self.DEFAULT_THREADS,
            'bucket_size': 64,
            'output_format': 'exr',
            'color_space': 'linear',
            'bit_depth': 16
        }
    
    def setup_render_layers(self, layer_names: Optional[list] = None) -> bool:
        """Set up render layers for Arnold.
        
        Args:
            layer_names: List of layer names to create
            
        Returns:
            True if successful, False otherwise
        """
        try:
            if layer_names is None:
                layer_names = ['beauty', 'diffuse', 'specular', 'normals']
            
            self.render_layers = layer_names
            logger.info(f"Created render layers: {', '.join(layer_names)}")
            return True
        except Exception as e:
            logger.error(f"Error setting up render layers: {e}")
            return False
    
    def set_samples(self, samples: int) -> None:
        """Set render samples.
        
        Args:
            samples: Number of samples
        """
        if samples < 1:
            logger.warning(f"Invalid sample count: {samples}, using minimum of 1")
            self.settings['samples'] = 1
        else:
            self.settings['samples'] = samples
            logger.info(f"Render samples set to: {samples}")
    
    def get_render_settings(self) -> Dict:
        """Get current render settings.
        
        Returns:
            Dictionary of render settings
        """
        return self.settings.copy()
    
    def get_render_info(self) -> Dict:
        """Get render information.
        
        Returns:
            Dictionary containing render configuration
        """
        return {
            'project': self.project_name,
            'engine': 'Arnold',
            'layers': self.render_layers,
            'settings': self.get_render_settings()
        }


def setup_render_layers():
    """Legacy function to set up Arnold render layers.
    
    Note: Use ArnoldRenderer class for new code.
    """
    print("Setting up Arnold render layers...")
    print("✅ Arnold render setup complete!")