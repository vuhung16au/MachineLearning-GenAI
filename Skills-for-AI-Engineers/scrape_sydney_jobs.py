#!/usr/bin/env python3
"""
Sydney AI Engineer Jobs Scraper

This script scrapes all AI Engineer job listings from Seek.com.au in Sydney,
extracts job description links, and fetches individual job descriptions.
"""

import os
import re
import sys
import time
import urllib.parse
from pathlib import Path
import requests
from bs4 import BeautifulSoup


def create_directories():
    """Create necessary directories if they don't exist"""
    directories = [
        "01.processing",
        "02.outputs"
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"✓ Created directory: {directory}")


def fetch_page(url, output_file):
    """Fetch a single page and save it to file"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
        }
        
        print(f"Fetching: {url}")
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(response.text)
        
        print(f"✓ Saved: {output_file}")
        return True
        
    except Exception as e:
        print(f"✗ Error fetching {url}: {e}")
        return False


def scrape_all_pages():
    """Scrape all 25 pages of Sydney AI Engineer jobs"""
    print("🚀 Starting Sydney AI Engineer Jobs Scraping")
    print("=" * 50)
    
    # Create directories
    create_directories()
    
    base_url = "https://www.seek.com.au/ai-engineer-jobs/in-All-Sydney-NSW"
    successful_pages = 0
    total_pages = 25
    
    for page_num in range(1, total_pages + 1):  # Pages 1 to 25
        print(f"\n📄 Processing page {page_num}/{total_pages}")
        
        if page_num == 1:
            url = base_url
        else:
            url = f"{base_url}?page={page_num}"
        
        output_file = f"01.processing/page_{page_num}.html"
        
        # Skip if file already exists
        if os.path.exists(output_file):
            print(f"⏭️  Page {page_num} already exists - skipping")
            successful_pages += 1
            continue
        
        print(f"🌐 Fetching: {url}")
        if fetch_page(url, output_file):
            successful_pages += 1
            print(f"✅ Page {page_num} completed successfully")
        else:
            print(f"❌ Failed to fetch page {page_num}")
        
        # Sleep 1 second between requests
        print(f"⏳ Waiting 1 second before next request...")
        time.sleep(1)
    
    print(f"\n📊 Scraping Summary:")
    print(f"   ✅ Successfully scraped: {successful_pages}/{total_pages} pages")
    print(f"   ❌ Failed: {total_pages - successful_pages}/{total_pages} pages")
    return successful_pages > 0


def extract_job_links():
    """Extract job description links from all scraped pages"""
    print("\n🔍 Starting job description link extraction...")
    print("=" * 50)
    
    job_links = set()
    jd_list_file = "01.processing/jd-list.txt"
    total_pages = 25
    
    # Read existing links if file exists
    existing_links = set()
    if os.path.exists(jd_list_file):
        with open(jd_list_file, 'r', encoding='utf-8') as f:
            existing_links = {line.strip() for line in f if line.strip()}
        job_links.update(existing_links)
        print(f"📋 Found {len(existing_links)} existing job links")
    
    # Process each page
    processed_pages = 0
    for page_num in range(1, total_pages + 1):
        print(f"\n📄 Processing page {page_num}/{total_pages} for job links...")
        page_file = f"01.processing/page_{page_num}.html"
        
        if not os.path.exists(page_file):
            print(f"⚠️  Page {page_num} not found, skipping...")
            continue
        
        try:
            with open(page_file, 'r', encoding='utf-8') as f:
                html_content = f.read()
            
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # Find job links - Seek uses various selectors
            links = soup.find_all('a', href=True)
            page_job_count = 0
            
            for link in links:
                href = link['href']
                # Look for job description links
                if '/job/' in href:
                    # Convert relative URLs to absolute
                    if href.startswith('/'):
                        href = f"https://www.seek.com.au{href}"
                    elif not href.startswith('http'):
                        href = f"https://www.seek.com.au/{href}"
                    
                    # Extract job ID and create clean URL
                    job_id_match = re.search(r'/job/(\d+)', href)
                    if job_id_match:
                        job_id = job_id_match.group(1)
                        clean_url = f"https://www.seek.com.au/job/{job_id}"
                        if clean_url not in job_links:
                            job_links.add(clean_url)
                            page_job_count += 1
            
            print(f"✅ Page {page_num} processed - found {page_job_count} new job links")
            processed_pages += 1
            
        except Exception as e:
            print(f"❌ Error processing page {page_num}: {e}")
    
    # Sort and save links
    sorted_links = sorted(list(job_links))
    
    with open(jd_list_file, 'w', encoding='utf-8') as f:
        for link in sorted_links:
            f.write(f"{link}\n")
    
    new_links = len(sorted_links) - len(existing_links)
    print(f"\n📊 Link Extraction Summary:")
    print(f"   📄 Pages processed: {processed_pages}/{total_pages}")
    print(f"   🔗 Total job links: {len(sorted_links)}")
    print(f"   🆕 New links found: {new_links}")
    print(f"   📁 Links saved to: {jd_list_file}")
    
    return len(sorted_links)


def fetch_job_descriptions():
    """Fetch individual job descriptions"""
    print("\n📥 Starting job description fetching...")
    print("=" * 50)
    
    jd_list_file = "01.processing/jd-list.txt"
    
    if not os.path.exists(jd_list_file):
        print("❌ No job links file found!")
        return 0
    
    with open(jd_list_file, 'r', encoding='utf-8') as f:
        job_urls = [line.strip() for line in f if line.strip()]
    
    total_jobs = len(job_urls)
    successful_downloads = 0
    skipped = 0
    failed = 0
    
    print(f"📋 Found {total_jobs} job URLs to process")
    
    for i, url in enumerate(job_urls, 1):
        # Extract job ID from URL
        job_id_match = re.search(r'/job/(\d+)', url)
        if not job_id_match:
            print(f"⚠️  [{i}/{total_jobs}] Invalid URL format: {url}")
            failed += 1
            continue
        
        job_id = job_id_match.group(1)
        output_file = f"01.processing/{job_id}.html"
        
        # Skip if file already exists
        if os.path.exists(output_file):
            print(f"⏭️  [{i}/{total_jobs}] Job {job_id} already exists - skipping")
            skipped += 1
            continue
        
        print(f"\n📥 [{i}/{total_jobs}] Fetching job {job_id}")
        print(f"🌐 URL: {url}")
        
        if fetch_page(url, output_file):
            successful_downloads += 1
            print(f"✅ Job {job_id} downloaded successfully")
        else:
            failed += 1
            print(f"❌ Failed to download job {job_id}")
        
        # Sleep 1 second between requests
        if i < total_jobs:  # Don't wait after the last job
            print(f"⏳ Waiting 1 second before next request...")
            time.sleep(1)
    
    print(f"\n📊 Job Description Fetching Summary:")
    print(f"   📋 Total jobs to process: {total_jobs}")
    print(f"   ✅ Successfully downloaded: {successful_downloads}")
    print(f"   ⏭️  Skipped (already exists): {skipped}")
    print(f"   ❌ Failed: {failed}")
    print(f"   📁 Job descriptions saved to: 01.processing/")
    
    return successful_downloads


def main():
    """Main entry point"""
    try:
        # Step 1 & 2: Scrape all pages
        if not scrape_all_pages():
            print("❌ Failed to scrape job listing pages")
            return
        
        # Step 3: Extract job links
        total_links = extract_job_links()
        if total_links == 0:
            print("❌ No job links found")
            return
        
        # Step 4: Fetch job descriptions
        downloaded = fetch_job_descriptions()
        
        print(f"\n✅ Scraping complete!")
        print(f"📊 Total job links: {total_links}")
        print(f"📥 Job descriptions downloaded: {downloaded}")
        print(f"📁 Check 01.processing/ directory for results")
        
    except KeyboardInterrupt:
        print("\n⚠️  Process interrupted by user")
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
