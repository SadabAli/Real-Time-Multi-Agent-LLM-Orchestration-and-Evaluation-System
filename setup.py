import os
from pathlib import Path

def create_project_structure():
    # Define the root directory
    base_path = Path("mega_ai_assignment")
    
    # Define the directory structure
    directories = [
        "app/agents",
        "app/api",
        "app/core",
        "app/db",
        "app/evaluation",
        "app/tools",
        "app/logs",
    ]
    
    # Define the base files
    files = [
        "docker-compose.yml",
        "Dockerfile",
        "requirements.txt",
        ".env",
    ]

    # Create directories and add __init__.py to make them packages
    for dir_path in directories:
        full_dir = base_path / dir_path
        full_dir.mkdir(parents=True, exist_ok=True)
        # Create an __init__.py in each subdirectory within 'app'
        (full_dir / "__init__.py").touch()

    # Create the top-level files
    for file_name in files:
        file_path = base_path / file_name
        file_path.touch()

    print(f"Successfully created structure at: {base_path.absolute()}")

if __name__ == "__main__":
    create_project_structure()