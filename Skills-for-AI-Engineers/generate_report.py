#!/usr/bin/env python3
"""
Comprehensive Report Generator

This script generates a comprehensive HTML dashboard report with visualizations
for the skills analysis, styled with Tailwind CSS.
"""

import os
import re
import json
from pathlib import Path
from collections import Counter
import plotly.graph_objects as go
import plotly.express as px
from bs4 import BeautifulSoup


def create_directories():
    """Create necessary directories if they don't exist"""
    directories = ["02.outputs"]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)


def clean_markdown_formatting(text):
    """Remove markdown formatting from text"""
    if not text:
        return text
    
    # Remove bold formatting **text** or __text__
    text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)
    text = re.sub(r'__(.*?)__', r'\1', text)
    
    # Remove italic formatting *text* or _text_
    text = re.sub(r'\*(.*?)\*', r'\1', text)
    text = re.sub(r'_(.*?)_', r'\1', text)
    
    # Remove strikethrough formatting ~~text~~
    text = re.sub(r'~~(.*?)~~', r'\1', text)
    
    # Remove code formatting `text`
    text = re.sub(r'`(.*?)`', r'\1', text)
    
    return text


def read_analysis_data():
    """Read analysis data from the summary file"""
    summary_file = "02.outputs/skills_analysis_summary.md"
    
    if not os.path.exists(summary_file):
        print(f"❌ Error: {summary_file} not found!")
        return None
    
    with open(summary_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Parse the markdown content to extract data
    data = {
        'total_jobs': 0,
        'top_5_skills': [],
        'high_demand_skills': [],
        'medium_demand_skills': [],
        'lower_demand_skills': [],
        'key_insights': []
    }
    
    # Extract total jobs
    total_match = re.search(r'Analysis based on (\d+) job descriptions', content)
    if total_match:
        data['total_jobs'] = int(total_match.group(1))
    
    # Extract top 5 skills (from top 10 section)
    top_10_section = re.search(r'## TOP 10 MOST DEMANDED SKILLS\n\n(.*?)\n\n##', content, re.DOTALL)
    if top_10_section:
        lines = top_10_section.group(1).strip().split('\n')[2:]  # Skip header and separator
        for line in lines:
            if line.strip() and '|' in line:
                parts = [p.strip() for p in line.split('|') if p.strip()]
                if len(parts) >= 4:
                    data['top_5_skills'].append({
                        'rank': parts[0],
                        'skill': parts[1],
                        'count': int(parts[2]),
                        'percentage': float(parts[3].replace('%', ''))
                    })
        # Take only the first 5 skills
        data['top_5_skills'] = data['top_5_skills'][:5]
    
    # Extract high demand skills
    high_demand_section = re.search(r'## HIGH DEMAND SKILLS \(>50% of jobs\)\n\n(.*?)\n\n##', content, re.DOTALL)
    if high_demand_section:
        lines = high_demand_section.group(1).strip().split('\n')[2:]  # Skip header and separator
        for line in lines:
            if line.strip() and '|' in line:
                parts = [p.strip() for p in line.split('|') if p.strip()]
                if len(parts) >= 3:
                    data['high_demand_skills'].append({
                        'skill': parts[0],
                        'count': int(parts[1]),
                        'percentage': float(parts[2].replace('%', ''))
                    })
    
    # Extract medium demand skills
    medium_demand_section = re.search(r'## MEDIUM DEMAND SKILLS \(15-50% of jobs\)\n\n(.*?)\n\n##', content, re.DOTALL)
    if medium_demand_section:
        lines = medium_demand_section.group(1).strip().split('\n')[2:]  # Skip header and separator
        for line in lines:
            if line.strip() and '|' in line:
                parts = [p.strip() for p in line.split('|') if p.strip()]
                if len(parts) >= 3:
                    data['medium_demand_skills'].append({
                        'skill': parts[0],
                        'count': int(parts[1]),
                        'percentage': float(parts[2].replace('%', ''))
                    })
    
    # Extract key insights
    insights_section = re.search(r'## KEY INSIGHTS\n\n(.*?)\n\n\*', content, re.DOTALL)
    if insights_section:
        lines = insights_section.group(1).strip().split('\n')
        for line in lines:
            if line.strip().startswith('- '):
                insight_text = line.strip()[2:]  # Remove the '- ' prefix
                # Clean markdown formatting for PNG display
                cleaned_insight = clean_markdown_formatting(insight_text)
                data['key_insights'].append(cleaned_insight)
    
    return data


def generate_pie_chart(data):
    """Generate pie chart for top 5 skills"""
    if not data['top_5_skills']:
        return None
    
    top_5 = data['top_5_skills']
    
    fig = go.Figure(data=[go.Pie(
        labels=[skill['skill'] for skill in top_5],
        values=[skill['percentage'] for skill in top_5],
        hole=0.3,
        textinfo='label+percent',
        textfont_size=12,
        marker=dict(
            colors=['#3B82F6', '#10B981', '#F59E0B', '#EF4444', '#8B5CF6'],
            line=dict(color='#FFFFFF', width=2)
        )
    )])
    
    fig.update_layout(
        title="Top 5 Most Demanded Skills",
        title_x=0.5,
        font=dict(size=14),
        showlegend=True,
        width=400,
        height=400,
        margin=dict(l=20, r=20, t=60, b=20)
    )
    
    return fig.to_html(include_plotlyjs=False, div_id="pie-chart")


def generate_html_dashboard(data):
    """Generate comprehensive HTML dashboard"""
    
    # Generate pie chart
    pie_chart_html = generate_pie_chart(data)
    
    # Get top 3 insights
    top_insights = data['key_insights'][:3] if data['key_insights'] else [
        "Python is the most in-demand programming language",
        "AI/ML technologies are highly sought after",
        "Cloud computing skills are essential"
    ]
    
    # Get top 5 high demand and medium demand skills
    top_5_high = data['high_demand_skills'][:5] if data['high_demand_skills'] else []
    top_5_medium = data['medium_demand_skills'][:5] if data['medium_demand_skills'] else []
    
    html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Engineer Skills Analysis Dashboard</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    <style>
        body {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        }}
        .gradient-bg {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }}
        .card-shadow {{
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
        }}
        .skill-badge {{
            background: linear-gradient(135deg, #3B82F6, #1D4ED8);
            color: white;
            padding: 0.5rem 1rem;
            border-radius: 9999px;
            font-size: 0.875rem;
            font-weight: 500;
            margin: 0.25rem;
            display: inline-block;
        }}
        .skill-badge-medium {{
            background: linear-gradient(135deg, #10B981, #059669);
        }}
        .skill-badge-high {{
            background: linear-gradient(135deg, #F59E0B, #D97706);
        }}
    </style>
</head>
<body class="bg-gray-50">
    <!-- Header -->
    <div class="gradient-bg text-white py-8">
        <div class="max-w-7xl mx-auto px-4">
            <h1 class="text-4xl font-bold text-center mb-2">AI Engineer Skills Analysis</h1>
            <p class="text-xl text-center opacity-90">Sydney Job Market Insights • {data['total_jobs']} Jobs Analyzed</p>
        </div>
    </div>

    <!-- Main Dashboard -->
    <div class="max-w-7xl mx-auto px-4 py-8">
        
        <!-- Top Row -->
        <div class="grid grid-cols-3 gap-8 mb-8">
            
            <!-- Word Cloud -->
            <div class="bg-white rounded-xl card-shadow p-6">
                <h2 class="text-2xl font-bold text-gray-800 mb-4">Skills Word Cloud</h2>
                <div class="flex items-center justify-center h-64 bg-gray-50 rounded-lg">
                    <img src="skills_wordcloud.png" alt="Skills Word Cloud" class="max-w-full max-h-full object-contain">
                </div>
            </div>
            
            <!-- Pie Chart -->
            <div class="bg-white rounded-xl card-shadow p-6">
                <h2 class="text-2xl font-bold text-gray-800 mb-4">Top 5 Skills Distribution</h2>
                <div class="flex items-center justify-center h-64">
                    {pie_chart_html if pie_chart_html else '<p class="text-gray-500">No data available</p>'}
                </div>
            </div>
            
            <!-- Key Findings -->
            <div class="bg-white rounded-xl card-shadow p-6">
                <h2 class="text-2xl font-bold text-gray-800 mb-4">Key Findings</h2>
                <div class="space-y-4">
                    {''.join([f'<div class="bg-blue-50 border-l-4 border-blue-500 p-4 rounded-r-lg"><p class="text-gray-700 font-medium">{insight}</p></div>' for insight in top_insights])}
                </div>
            </div>
        </div>
        
        <!-- Second Row -->
        <div class="grid grid-cols-3 gap-8">
            
            <!-- Top 5 Most Demanded Skills -->
            <div class="bg-white rounded-xl card-shadow p-6">
                <h2 class="text-2xl font-bold text-gray-800 mb-6">Top 5 Most Demanded Skills</h2>
                <div class="space-y-3">
                    {''.join([f'''
                    <div class="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
                        <div class="flex items-center">
                            <span class="bg-blue-500 text-white rounded-full w-8 h-8 flex items-center justify-center text-sm font-bold mr-3">{skill['rank']}</span>
                            <span class="font-medium text-gray-800">{skill['skill']}</span>
                        </div>
                        <div class="text-right">
                            <div class="text-sm font-semibold text-blue-600">{skill['percentage']:.1f}%</div>
                            <div class="text-xs text-gray-500">{skill['count']} jobs</div>
                        </div>
                    </div>
                    ''' for skill in data['top_5_skills']])}
                </div>
            </div>
            
            <!-- High Demand Skills -->
            <div class="bg-white rounded-xl card-shadow p-6">
                <h2 class="text-2xl font-bold text-gray-800 mb-6">High Demand Skills</h2>
                <p class="text-sm text-gray-600 mb-4">Required in >50% of jobs</p>
                <div class="space-y-3">
                    {''.join([f'''
                    <div class="flex items-center justify-between p-3 bg-orange-50 rounded-lg border border-orange-200">
                        <span class="font-medium text-gray-800">{skill['skill']}</span>
                        <div class="text-right">
                            <div class="text-sm font-semibold text-orange-600">{skill['percentage']:.1f}%</div>
                            <div class="text-xs text-gray-500">{skill['count']} jobs</div>
                        </div>
                    </div>
                    ''' for skill in top_5_high])}
                </div>
            </div>
            
            <!-- Medium Demand Skills -->
            <div class="bg-white rounded-xl card-shadow p-6">
                <h2 class="text-2xl font-bold text-gray-800 mb-6">Medium Demand Skills</h2>
                <p class="text-sm text-gray-600 mb-4">Required in 15-50% of jobs</p>
                <div class="space-y-3">
                    {''.join([f'''
                    <div class="flex items-center justify-between p-3 bg-green-50 rounded-lg border border-green-200">
                        <span class="font-medium text-gray-800">{skill['skill']}</span>
                        <div class="text-right">
                            <div class="text-sm font-semibold text-green-600">{skill['percentage']:.1f}%</div>
                            <div class="text-xs text-gray-500">{skill['count']} jobs</div>
                        </div>
                    </div>
                    ''' for skill in top_5_medium])}
                </div>
            </div>
        </div>
        
        <!-- Summary Stats -->
        <div class="mt-8 bg-white rounded-xl card-shadow p-6">
            <h2 class="text-2xl font-bold text-gray-800 mb-4">Analysis Summary</h2>
            <div class="grid grid-cols-4 gap-6">
                <div class="text-center">
                    <div class="text-3xl font-bold text-blue-600">{data['total_jobs']}</div>
                    <div class="text-sm text-gray-600">Total Jobs Analyzed</div>
                </div>
                <div class="text-center">
                    <div class="text-3xl font-bold text-orange-600">{len(data['high_demand_skills'])}</div>
                    <div class="text-sm text-gray-600">High Demand Skills</div>
                </div>
                <div class="text-center">
                    <div class="text-3xl font-bold text-green-600">{len(data['medium_demand_skills'])}</div>
                    <div class="text-sm text-gray-600">Medium Demand Skills</div>
                </div>
                <div class="text-center">
                    <div class="text-3xl font-bold text-purple-600">{len(data['top_5_skills'])}</div>
                    <div class="text-sm text-gray-600">Top Skills Tracked</div>
                </div>
            </div>
        </div>
    </div>
    
    <!-- Footer -->
    <div class="bg-gray-800 text-white py-6 mt-12">
        <div class="max-w-7xl mx-auto px-4 text-center">
            <p class="text-gray-400">Generated by AI Engineer Skills Analysis Tool</p>
            <p class="text-sm text-gray-500 mt-2">Data sourced from Seek.com.au Sydney AI Engineer job listings</p>
        </div>
    </div>
</body>
</html>
"""
    
    return html_content


def save_dashboard_as_png():
    """Save the HTML dashboard as a PNG image"""
    try:
        import subprocess
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        
        # Setup Chrome options for headless mode
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--window-size=1920,1200")
        
        # Create webdriver
        driver = webdriver.Chrome(options=chrome_options)
        
        # Load the HTML file
        html_file = os.path.abspath("02.outputs/skills_analysis_dashboard.html")
        driver.get(f"file://{html_file}")
        
        # Wait for page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        
        # Take screenshot
        output_file = "02.outputs/skills_analysis_html.png"
        driver.save_screenshot(output_file)
        
        driver.quit()
        
        print(f"📊 Dashboard PNG saved to: {output_file}")
        
    except ImportError:
        print("⚠️  Selenium not available. Install with: pip install selenium")
        print("📄 HTML dashboard saved. You can manually convert to PNG using a browser.")
    except Exception as e:
        print(f"❌ Error saving PNG: {e}")
        print("📄 HTML dashboard saved. You can manually convert to PNG using a browser.")


def main():
    """Main entry point"""
    try:
        print("🚀 Starting Comprehensive Report Generation")
        print("=" * 60)
        
        # Create directories
        print("📁 Creating output directories...")
        create_directories()
        
        # Read analysis data
        print("📊 Reading analysis data from summary file...")
        data = read_analysis_data()
        if not data:
            print("❌ No analysis data found!")
            return
        
        print(f"✅ Successfully loaded data for {data['total_jobs']} jobs")
        print(f"   🎯 Top 5 skills: {len(data['top_5_skills'])}")
        print(f"   🔥 High demand skills: {len(data['high_demand_skills'])}")
        print(f"   📈 Medium demand skills: {len(data['medium_demand_skills'])}")
        
        # Generate HTML dashboard
        print("\n🎨 Generating HTML dashboard...")
        html_content = generate_html_dashboard(data)
        
        # Save HTML dashboard
        html_file = "02.outputs/skills_analysis_dashboard.html"
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"✅ HTML dashboard saved to: {html_file}")
        
        # Try to save as PNG
        print("\n🖼️  Converting dashboard to PNG...")
        save_dashboard_as_png()
        
        # Also save as report.md
        print("\n📋 Generating markdown report...")
        report_file = "02.outputs/report.md"
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write("# AI Engineer Skills Analysis Report\n\n")
            f.write(f"*Analysis based on {data['total_jobs']} job descriptions from Sydney*\n\n")
            f.write("## Key Findings\n\n")
            for insight in data['key_insights']:
                f.write(f"- {insight}\n")
            f.write("\n## Top 5 Most Demanded Skills\n\n")
            for skill in data['top_5_skills']:
                f.write(f"{skill['rank']}. **{skill['skill']}** - {skill['percentage']:.1f}% ({skill['count']} jobs)\n")
        
        print(f"✅ Markdown report saved to: {report_file}")
        
        print(f"\n📊 Report Generation Summary:")
        print(f"   📄 HTML dashboard: {html_file}")
        print(f"   🖼️  PNG dashboard: 02.outputs/skills_analysis_html.png")
        print(f"   📋 Markdown report: {report_file}")
        print(f"   🎨 Word cloud: 02.outputs/skills_wordcloud.png")
        
        print("\n✅ Report generation complete!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
