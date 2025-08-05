#!/usr/bin/env python3
"""
Research Agent Setup Script

This script helps set up the Research Agent Streamlit application by:
1. Checking for required dependencies
2. Installing missing packages
3. Providing setup instructions
"""

import subprocess
import sys
import os
from pathlib import Path

def check_python_version():
    """Check if Python version is compatible."""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required.")
        print(f"Current version: {sys.version}")
        return False
    print(f"✅ Python version: {sys.version.split()[0]}")
    return True

def check_package(package_name):
    """Check if a package is installed."""
    try:
        __import__(package_name)
        return True
    except ImportError:
        return False

def install_requirements():
    """Install requirements from requirements.txt."""
    requirements_file = Path(__file__).parent / "requirements.txt"
    
    if not requirements_file.exists():
        print("❌ requirements.txt not found!")
        return False
    
    print("📦 Installing requirements...")
    try:
        subprocess.run([
            sys.executable, "-m", "pip", "install", "-r", str(requirements_file)
        ], check=True)
        print("✅ Requirements installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing requirements: {e}")
        return False

def main():
    """Main setup function."""
    print("🔬 Research Agent Setup")
    print("=" * 40)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Check for required packages
    packages_to_check = ["streamlit", "genai_processors", "google.genai"]
    missing_packages = []
    
    for package in packages_to_check:
        if check_package(package):
            print(f"✅ {package} is installed")
        else:
            print(f"❌ {package} is NOT installed")
            missing_packages.append(package)
    
    # Install missing packages
    if missing_packages:
        print(f"\n📦 Missing packages: {', '.join(missing_packages)}")
        response = input("Install missing packages? (y/n): ").lower().strip()
        
        if response == 'y':
            if install_requirements():
                print("\n🎉 Setup completed successfully!")
            else:
                print("\n❌ Setup failed. Please install packages manually:")
                print("pip install -r requirements.txt")
                sys.exit(1)
        else:
            print("\n⚠️  Please install the required packages manually:")
            print("pip install -r requirements.txt")
            sys.exit(1)
    else:
        print("\n✅ All required packages are installed!")
    
    # Additional setup instructions
    print("\n📋 Next Steps:")
    print("1. Get a Google API key from: https://aistudio.google.com/")
    print("2. Run the application with: python run_app.py")
    print("   Or directly with: streamlit run streamlit_app.py")
    print("3. Enter your API key in the sidebar")
    print("4. Start researching!")
    
    print("\n🚀 Ready to launch the Research Agent!")

if __name__ == "__main__":
    main()
