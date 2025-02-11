import os
import sys
import subprocess
import platform

# Ensure Conda is Installed
print("Checking for Conda installation...")
try:
    subprocess.run(["conda", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print("Conda is installed.")
except FileNotFoundError:
    print("Conda is not installed! Please install Miniconda or Anaconda before running this script.")
    sys.exit(1)

# Create Conda Environment
env_name = "amap"
python_version = "3.12"
print(f"Creating Conda environment '{env_name}' with Python {python_version}...")
try:
    subprocess.run(["conda", "create", "-n", env_name, f"python={python_version}", "-y"], check=True)
    print(f"Conda environment '{env_name}' created successfully.")
except subprocess.CalledProcessError:
    print(f"Failed to create Conda environment '{env_name}'.")
    sys.exit(1)

# Activate Conda Environment
OS_NAME = platform.system()
if OS_NAME == "Windows":
    activate_cmd = f"conda activate {env_name} &&"
else:
    activate_cmd = f"source $(conda info --base)/etc/profile.d/conda.sh && conda activate {env_name} &&"

# Install Required Dependencies
dependencies = [
    "trimesh",
    "pyyaml",
    "open3d",
    "pyvista",
    "point-cloud-utils",
    "rtree",
    "seaborn"
]
print(f"Installing dependencies: {', '.join(dependencies)} inside '{env_name}' environment...")
try:
    subprocess.run(f"{activate_cmd} pip install " + " ".join(dependencies), shell=True, check=True, executable="/bin/bash" if OS_NAME != "Windows" else None)
    print("All dependencies installed successfully within the Conda environment.")
except subprocess.CalledProcessError:
    print("Failed to install some dependencies. Please check your internet connection or Conda setup.")
    sys.exit(1)

print("Setup Complete! Your Conda environment is activated.")