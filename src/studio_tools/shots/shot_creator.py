"""Shot management tools for studio pipeline.

Provides utilities for creating and managing shots in the production pipeline.
"""

import logging
from pathlib import Path
from datetime import datetime

logger = logging.getLogger(__name__)


class ShotCreator:
    """Handle creation and management of shots in the pipeline."""
    
    REQUIRED_FOLDERS = ['cache', 'geo', 'renders', 'scenes', 'textures', 'fx']
    
    def __init__(self, shot_name: str, project_path: str = "/studio/projects"):
        """Initialize shot creator.
        
        Args:
            shot_name: Name of the shot (e.g., "SQ010_SH020")
            project_path: Base project directory path
        """
        self.shot_name = shot_name
        self.project_path = Path(project_path)
        self.shot_path = self.project_path / shot_name
        self.created_at = datetime.now().isoformat()
        logger.info(f"ShotCreator initialized for shot: {shot_name}")
    
    def create_shot_directory(self) -> bool:
        """Create shot directory structure.
        
        Returns:
            True if successful, False otherwise
        """
        try:
            for folder in self.REQUIRED_FOLDERS:
                folder_path = self.shot_path / folder
                folder_path.mkdir(parents=True, exist_ok=True)
                logger.info(f"Created folder: {folder_path}")
            
            logger.info(f"Shot directory structure created for: {self.shot_name}")
            return True
        except Exception as e:
            logger.error(f"Error creating shot directory: {e}")
            return False
    
    def setup_maya_scene(self) -> bool:
        """Set up a Maya scene for the shot.
        
        Returns:
            True if successful, False otherwise
        """
        try:
            scene_dir = self.shot_path / 'scenes'
            scene_file = scene_dir / f"{self.shot_name}_main.ma"
            
            # Create a placeholder Maya scene file
            scene_file.touch()
            logger.info(f"Maya scene created: {scene_file}")
            return True
        except Exception as e:
            logger.error(f"Error setting up Maya scene: {e}")
            return False
    
    def get_shot_info(self) -> dict:
        """Get shot information.
        
        Returns:
            Dictionary containing shot metadata
        """
        return {
            'shot_name': self.shot_name,
            'project_path': str(self.project_path),
            'shot_path': str(self.shot_path),
            'created_at': self.created_at,
            'exists': self.shot_path.exists()
        }


def create_new_shot(shot_name, project_path="/studio/projects"):
    """Legacy function to create a new shot.
    
    Note: Use ShotCreator class for new code.
    """
    creator = ShotCreator(shot_name, project_path)
    success = creator.create_shot_directory()
    print(f"🎬 Creating new shot: {shot_name}")
    if success:
        print(f"✅ Shot '{shot_name}' created successfully!")
    else:
        print(f"❌ Failed to create shot '{shot_name}'")
    return success


def setup_maya_scene(shot_name, project_path="/studio/projects"):
    """Legacy function to set up a Maya scene.
    
    Note: Use ShotCreator class for new code.
    """
    creator = ShotCreator(shot_name, project_path)
    success = creator.setup_maya_scene()
    print(f"🖥️ Setting up Maya scene for shot: {shot_name}")
    if success:
        print(f"✅ Maya scene for shot '{shot_name}' set up successfully!")
    else:
        print(f"❌ Failed to set up Maya scene for '{shot_name}'")
    return success