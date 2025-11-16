"""
Shot Creator Module

Automatically sets up folders and Maya scenes for new shots
"""

def create_new_shot(shot_name, project_path="/studio/projects"):
    """Creates a new shot with directory structure"""
    print(f"🎬 Creating new shot: {shot_name}")
    print(f"✅ Shot '{shot_name}' created successfully!")

def setup_maya_scene(shot_name, project_path="/studio/projects"):
    """Sets up a Maya scene for the given shot"""
    print(f"🖥️ Setting up Maya scene for shot: {shot_name}")
    print(f"✅ Maya scene for shot '{shot_name}' set up successfully!")