#!/usr/bin/env python3
"""
Research Agent Streamlit App Launcher

Simple launcher script for the Research Agent Streamlit application.
This script ensures the proper environment setup and launches the app.
"""

import os
import sys
import subprocess
from pathlib import Path

def main():
    """Launch the Streamlit Research Agent app."""
    
    # Get the directory where this script is located
    script_dir = Path(__file__).parent.absolute()
    streamlit_app = script_dir / "streamlit_app.py"
    
    # Check if streamlit_app.py exists
    if not streamlit_app.exists():
        print("❌ Error: streamlit_app.py not found in the current directory.")
        print(f"Expected location: {streamlit_app}")
        sys.exit(1)
    
    # Check if streamlit is installed
    try:
        subprocess.run([sys.executable, "-c", "import streamlit"], 
                      check=True, capture_output=True)
    except subprocess.CalledProcessError:
        print("❌ Streamlit is not installed.")
        print("Please install the requirements first:")
        print("pip install -r requirements.txt")
        sys.exit(1)
    
    print("🚀 Launching Research Agent Streamlit App...")
    print(f"📁 App location: {streamlit_app}")
    print("🌐 The app will open in your default web browser.")
    print("⏹️  Press Ctrl+C to stop the application.")
    print()
    
    # Launch the Streamlit app
    try:
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", str(streamlit_app)
        ], cwd=script_dir)
    except KeyboardInterrupt:
        print("\n👋 Research Agent app stopped.")
    except Exception as e:
        print(f"❌ Error launching the app: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
