#!/usr/bin/env python3
"""
Test script for MathMate app functionality
"""

import os
import sys

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Test all required imports."""
    try:
        print("Testing imports...")
        
        # Test basic imports
        import streamlit as st
        import asyncio
        import dataclasses
        from typing import AsyncIterable, AsyncGenerator, List
        import traceback
        print("✓ Basic imports successful")
        
        # Test genai-processors imports
        from genai_processors import content_api
        from genai_processors import context
        from genai_processors import processor
        from genai_processors import streams
        from genai_processors.core import pdf
        from genai_processors.core import realtime
        from genai_processors.core import text
        print("✓ GenAI Processors imports successful")
        
        # Test research imports
        from genai_processors.examples import research
        print("✓ Research module imports successful")
        
        # Test httpx
        import httpx
        print("✓ HTTPX import successful")
        
        # Test config import
        import config
        print("✓ Config import successful")
        
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def test_app_structure():
    """Test the app structure and main functions."""
    try:
        print("\nTesting app structure...")
        
        # Import the app module
        import app
        print("✓ App module imported successfully")
        
        # Check if main functions exist
        if hasattr(app, 'main'):
            print("✓ main() function exists")
        else:
            print("❌ main() function missing")
            return False
            
        if hasattr(app, 'initialize_session_state'):
            print("✓ initialize_session_state() function exists")
        else:
            print("❌ initialize_session_state() function missing")
            return False
            
        if hasattr(app, 'chat_mode'):
            print("✓ chat_mode() function exists")
        else:
            print("❌ chat_mode() function missing")
            return False
            
        if hasattr(app, 'research_mode'):
            print("✓ research_mode() function exists")
        else:
            print("❌ research_mode() function missing")
            return False
            
        if hasattr(app, 'run_research_agent'):
            print("✓ run_research_agent() function exists")
        else:
            print("❌ run_research_agent() function missing")
            return False
            
        if hasattr(app, 'generate_topics_only'):
            print("✓ generate_topics_only() function exists")
        else:
            print("❌ generate_topics_only() function missing")
            return False
        
        print("✓ All required functions present")
        return True
        
    except Exception as e:
        print(f"❌ Error testing app structure: {e}")
        return False

def test_config():
    """Test configuration values."""
    try:
        print("\nTesting configuration...")
        
        import config
        
        # Check required config values
        required_configs = [
            'DEFAULT_MODEL_NAME',
            'APP_TITLE', 
            'APP_SUBTITLE',
            'PAGE_ICON',
            'SYSTEM_INSTRUCTION',
            'DEFAULT_NUM_TOPICS',
            'AVAILABLE_MODELS',
            'EXAMPLE_RESEARCH_PROMPTS'
        ]
        
        for config_name in required_configs:
            if hasattr(config, config_name):
                value = getattr(config, config_name)
                print(f"✓ {config_name}: {type(value).__name__}")
            else:
                print(f"❌ Missing config: {config_name}")
                return False
        
        # Check if API key is configured (but don't print it)
        if hasattr(config, 'GOOGLE_API_KEY'):
            api_key = getattr(config, 'GOOGLE_API_KEY')
            if api_key:
                print("✓ GOOGLE_API_KEY is configured")
            else:
                print("⚠️  GOOGLE_API_KEY is not set (expected for testing)")
        
        return True
        
    except Exception as e:
        print(f"❌ Error testing config: {e}")
        return False

def main():
    """Run all tests."""
    print("=== MathMate App Test Suite ===\n")
    
    tests = [
        test_imports,
        test_app_structure,
        test_config
    ]
    
    results = []
    for test in tests:
        result = test()
        results.append(result)
    
    print(f"\n=== Test Results ===")
    passed = sum(results)
    total = len(results)
    print(f"Passed: {passed}/{total}")
    
    if passed == total:
        print("🎉 All tests passed! Your MathMate app is ready to run.")
        print("\nTo start the app, run:")
        print("streamlit run app.py")
    else:
        print("❌ Some tests failed. Please check the errors above.")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
