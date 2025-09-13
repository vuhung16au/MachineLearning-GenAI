#!/usr/bin/env python3
"""
Complete AI Engineer Skills Analysis Pipeline

This script runs the complete pipeline:
1. Scrape Sydney AI Engineer jobs from Seek.com.au
2. Extract job description links
3. Fetch individual job descriptions
4. Extract skills and generate wordcloud
5. Generate comprehensive reports and dashboard
"""

import os
import sys
import subprocess
import time
from pathlib import Path


def run_script(script_name, description):
    """Run a Python script and handle errors"""
    print(f"\n🚀 {description}")
    print("=" * 60)
    
    try:
        result = subprocess.run([sys.executable, script_name], 
                              capture_output=True, text=True, check=True)
        print(result.stdout)
        if result.stderr:
            print("⚠️  Warnings/Errors:")
            print(result.stderr)
        print(f"✅ {description} completed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error running {script_name}:")
        print(f"Return code: {e.returncode}")
        print(f"STDOUT: {e.stdout}")
        print(f"STDERR: {e.stderr}")
        return False
    except FileNotFoundError:
        print(f"❌ Script {script_name} not found!")
        return False


def check_dependencies():
    """Check if required dependencies are installed"""
    print("🔍 Checking dependencies...")
    
    required_packages = [
        'requests', 'beautifulsoup4', 'wordcloud', 
        'matplotlib', 'plotly', 'kaleido'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            if package == 'beautifulsoup4':
                __import__('bs4')
            else:
                __import__(package.replace('-', '_'))
            print(f"✓ {package}")
        except ImportError:
            missing_packages.append(package)
            print(f"✗ {package}")
    
    if missing_packages:
        print(f"\n❌ Missing packages: {', '.join(missing_packages)}")
        print("Install them with: pip install -r requirements.txt")
        return False
    
    print("✅ All dependencies are installed!")
    return True


def main():
    """Main pipeline execution"""
    print("🎯 AI Engineer Skills Analysis Pipeline")
    print("=" * 60)
    print("This pipeline will:")
    print("1. Scrape all Sydney AI Engineer jobs from Seek.com.au")
    print("2. Extract job description links")
    print("3. Fetch individual job descriptions")
    print("4. Extract skills and generate wordcloud")
    print("5. Generate comprehensive reports and dashboard")
    print("=" * 60)
    
    # Check dependencies
    if not check_dependencies():
        return
    
    # Create output directories
    Path("01.processing").mkdir(exist_ok=True)
    Path("02.outputs").mkdir(exist_ok=True)
    
    # Step 1-4: Scrape jobs and extract links
    print("\n" + "="*80)
    print("STEP 1-4: WEB SCRAPING AND JOB LINK EXTRACTION")
    print("="*80)
    if not run_script("scrape_sydney_jobs.py", "Scraping Sydney AI Engineer jobs (Steps 1-4)"):
        print("❌ Pipeline failed at scraping step")
        return
    
    # Check if we have job descriptions
    job_files = [f for f in os.listdir("01.processing") if f.endswith('.html') and not f.startswith('page_')]
    if not job_files:
        print("❌ No job descriptions found. Pipeline cannot continue.")
        return
    
    print(f"✅ Found {len(job_files)} job descriptions to analyze")
    
    # Step 5: Extract skills and generate wordcloud
    print("\n" + "="*80)
    print("STEP 5: SKILLS EXTRACTION AND WORDCLOUD GENERATION")
    print("="*80)
    if not run_script("extract_skills.py", "Extracting skills and generating wordcloud (Step 5)"):
        print("❌ Pipeline failed at skills extraction step")
        return
    
    # Step 6-7: Generate reports and dashboard
    print("\n" + "="*80)
    print("STEP 6-7: REPORT GENERATION AND DASHBOARD CREATION")
    print("="*80)
    if not run_script("generate_report.py", "Generating comprehensive reports and dashboard (Steps 6-7)"):
        print("❌ Pipeline failed at report generation step")
        return
    
    # Final summary
    print("\n🎉 PIPELINE COMPLETED SUCCESSFULLY!")
    print("=" * 60)
    print("📁 Output files generated:")
    
    output_files = [
        "01.processing/jd-list.txt",
        "02.outputs/skills_analysis_summary.md",
        "02.outputs/skills_analysis_detail.md",
        "02.outputs/skills_wordcloud.png",
        "02.outputs/skills_analysis_dashboard.html",
        "02.outputs/report.md"
    ]
    
    for file_path in output_files:
        if os.path.exists(file_path):
            size = os.path.getsize(file_path)
            print(f"✓ {file_path} ({size:,} bytes)")
        else:
            print(f"✗ {file_path} (not found)")
    
    # Count job descriptions
    job_count = len([f for f in os.listdir("01.processing") if f.endswith('.html') and not f.startswith('page_')])
    page_count = len([f for f in os.listdir("01.processing") if f.startswith('page_')])
    
    print(f"\n📊 Pipeline Statistics:")
    print(f"   • Pages scraped: {page_count}")
    print(f"   • Job descriptions: {job_count}")
    print(f"   • Job links extracted: {len(open('01.processing/jd-list.txt').readlines()) if os.path.exists('01.processing/jd-list.txt') else 0}")
    
    print(f"\n🌐 Open the dashboard: 02.outputs/skills_analysis_dashboard.html")
    print(f"📊 View the wordcloud: 02.outputs/skills_wordcloud.png")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n⚠️  Pipeline interrupted by user")
    except Exception as e:
        print(f"\n❌ Pipeline failed with error: {e}")
        import traceback
        traceback.print_exc()
