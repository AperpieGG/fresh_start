import os
import subprocess
import sys

def create_requirements_file():
    """Create a requirements.txt file with all installed packages."""
    requirements_file_path = os.path.join(os.path.dirname(__file__), 'requirements.txt')
    
    # Get list of installed packages
    installed_packages = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze']).decode('utf-8')
    
    # Write the packages to requirements.txt
    with open(requirements_file_path, 'w') as f:
        f.write(installed_packages)
    
    print(f"Requirements file created at {requirements_file_path}")

def install_packages():
    """Install packages from the requirements.txt file."""
    requirements_file_path = os.path.join(os.path.dirname(__file__), 'requirements.txt')
    
    if not os.path.exists(requirements_file_path):
        print(f"Requirements file not found at {requirements_file_path}. Please create it first.")
        return
    
    # Install packages from requirements.txt
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', requirements_file_path])
    
    print("All packages installed successfully.")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'install':
        install_packages()
    else:
        create_requirements_file()
