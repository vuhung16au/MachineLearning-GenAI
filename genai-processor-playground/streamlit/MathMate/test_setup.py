#!/usr/bin/env python3
"""Test script to verify MathMate Streamlit app setup."""

import os
import sys
import importlib.util

def check_environment():
    """Check if environment is properly set up."""
    print("🔍 Checking environment setup...")
    
    # Check Python version
    python_version = sys.version_info
    print(f"✅ Python version: {python_version.major}.{python_version.minor}.{python_version.micro}")
    
    if python_version < (3, 8):
        print("❌ Python 3.8 or higher is required")
        return False
    
    # Check API key
    api_key = os.environ.get('GOOGLE_API_KEY')
    if api_key:
        print("✅ GOOGLE_API_KEY is set")
    else:
        print("❌ GOOGLE_API_KEY environment variable is not set")
        print("   Please set your Google AI Studio API key:")
        print("   export GOOGLE_API_KEY='your-api-key-here'")
    
    return True

def check_dependencies():
    """Check if required dependencies are installed."""
    print("\n📦 Checking dependencies...")
    
    required_packages = [
        'streamlit',
        'httpx',
        'genai_processors',
        'google.genai'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            if package == 'google.genai':
                import google.genai
            else:
                importlib.import_module(package)
            print(f"✅ {package} is installed")
        except ImportError:
            print(f"❌ {package} is not installed")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n📥 To install missing packages, run:")
        print(f"   pip install {' '.join(missing_packages)}")
        print(f"   Or: pip install -r requirements.txt")
        return False
    
    return True

def check_files():
    """Check if required files exist."""
    print("\n📁 Checking files...")
    
    required_files = [
        'app.py',
        'config.py',
        'requirements.txt',
        'README.md'
    ]
    
    missing_files = []
    
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file} exists")
        else:
            print(f"❌ {file} is missing")
            missing_files.append(file)
    
    return len(missing_files) == 0

def main():
    """Run all checks."""
    print("🧮 MathMate Streamlit App - Setup Verification")
    print("=" * 50)
    
    env_ok = check_environment()
    deps_ok = check_dependencies()
    files_ok = check_files()
    
    print("\n" + "=" * 50)
    
    if env_ok and deps_ok and files_ok:
        print("🎉 Setup verification complete! Everything looks good.")
        print("\n🚀 To start the app, run:")
        print("   streamlit run app.py")
        print("   Or: ./run.sh")
    else:
        print("❌ Setup verification failed. Please fix the issues above.")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
