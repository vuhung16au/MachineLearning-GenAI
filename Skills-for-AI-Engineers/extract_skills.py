#!/usr/bin/env python3
"""
Job Description Skills Extractor

This script downloads job descriptions from URLs and extracts skills from them.
It generates analysis reports showing skill frequency and demand levels.
"""

import os
import re
import sys
import time
import urllib.parse
from collections import Counter
from pathlib import Path
import requests
from bs4 import BeautifulSoup
import docx
import subprocess


def create_directories():
    """Create necessary directories if they don't exist"""
    directories = [
        "00.inputs/job_descriptions",
        "01.processing",
        "02.outputs"
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"✓ Created directory: {directory}")


def download_job_description(url, output_dir):
    """Download job description from URL and save to file"""
    try:
        # Parse the URL to get a filename
        parsed_url = urllib.parse.urlparse(url)
        job_id = parsed_url.path.split('/')[-1] if parsed_url.path else 'unknown'
        filename = f"job_{job_id}.html"
        filepath = os.path.join(output_dir, filename)

        # Use wget to download politely with a browser-like user agent
        user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        print(f"Downloading: {url}")
        subprocess.run([
            "wget",
            "-q",
            "--user-agent", user_agent,
            "-O", filepath,
            url
        ], check=True)

        print(f"✓ Saved: {filepath}")
        return filepath

    except Exception as e:
        print(f"✗ Error downloading {url}: {e}")
        return None


def extract_text_from_html(filepath):
    """Extract text content from HTML file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Parse HTML with BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.decompose()
        
        # Extract text content
        text = soup.get_text()
        
        # Clean up whitespace
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = ' '.join(chunk for chunk in chunks if chunk)
        
        return text
        
    except Exception as e:
        print(f"Error extracting text from {filepath}: {e}")
        return ""


def extract_text_from_docx(file_path):
    """Extract text from a .docx file"""
    try:
        doc = docx.Document(file_path)
        text = []
        for paragraph in doc.paragraphs:
            text.append(paragraph.text)
        return '\n'.join(text)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return ""


def extract_skills(text):
    """Extract skills from text using various patterns"""
    skills = []
    
    # Common skill patterns
    skill_patterns = [
        r'\b(Python|Java|JavaScript|TypeScript|C\+\+|C#|Go|Rust|Swift|Kotlin|Scala|PHP|Ruby|Perl|R|MATLAB|Julia)\b',
        r'\b(React|Angular|Vue\.js|Node\.js|Express|Django|Flask|Spring|Laravel|ASP\.NET|FastAPI|Gin|Echo)\b',
        r'\b(AWS|Azure|GCP|Google Cloud|Amazon Web Services|Microsoft Azure|Docker|Kubernetes|Terraform|Ansible)\b',
        r'\b(MySQL|PostgreSQL|MongoDB|Redis|Cassandra|DynamoDB|SQLite|Oracle|SQL Server|MariaDB)\b',
        r'\b(Machine Learning|ML|Deep Learning|AI|Artificial Intelligence|Neural Networks|TensorFlow|PyTorch|Scikit-learn|Keras)\b',
        r'\b(Data Science|Data Analysis|Pandas|NumPy|Matplotlib|Seaborn|Plotly|Jupyter|R Studio|Tableau|Power BI)\b',
        r'\b(Git|GitHub|GitLab|Bitbucket|SVN|Mercurial|CI/CD|Jenkins|GitHub Actions|GitLab CI|CircleCI)\b',
        r'\b(HTML|CSS|Sass|Less|Bootstrap|Tailwind CSS|Material-UI|Ant Design|jQuery|Webpack|Babel)\b',
        r'\b(REST API|GraphQL|SOAP|Microservices|API Gateway|Load Balancing|CDN|WebSockets|gRPC)\b',
        r'\b(Agile|Scrum|Kanban|Waterfall|DevOps|SRE|Site Reliability Engineering|TDD|BDD|DDD)\b',
        r'\b(Linux|Unix|Windows|macOS|Shell Scripting|Bash|PowerShell|SSH|VPN|Firewall|Security)\b',
        r'\b(Testing|Unit Testing|Integration Testing|E2E Testing|Selenium|Jest|PyTest|JUnit|Cypress|Playwright)\b',
        r'\b(Cloud Computing|Serverless|Lambda|Functions|Containers|Virtualization|VMware|Hyper-V|KVM)\b',
        r'\b(Big Data|Hadoop|Spark|Kafka|Flink|Storm|Hive|Pig|HBase|Zookeeper|Elasticsearch|Logstash|Kibana)\b',
        r'\b(Blockchain|Cryptocurrency|Bitcoin|Ethereum|Smart Contracts|Solidity|Web3|DeFi|NFT)\b',
        r'\b(Mobile Development|iOS|Android|React Native|Flutter|Xamarin|Swift|Kotlin|Objective-C)\b',
        r'\b(Computer Vision|OpenCV|Image Processing|NLP|Natural Language Processing|BERT|GPT|Transformers)\b',
        r'\b(Statistics|Probability|Linear Algebra|Calculus|Optimization|Operations Research|Game Theory)\b',
        r'\b(Project Management|PMP|PRINCE2|Lean|Six Sigma|Change Management|Risk Management)\b',
        r'\b(Communication|Leadership|Team Management|Problem Solving|Critical Thinking|Analytical Skills)\b',
        r'\b(LangChain|Semantic Kernel|OpenAI|Claude|Anthropic|Mistral|RAG|Retrieval Augmented Generation)\b',
        r'\b(LLM|Large Language Models|Generative AI|GenAI|Prompt Engineering|Fine-tuning)\b',
        r'\b(MLOps|ModelOps|Model Deployment|Model Monitoring|A/B Testing|Feature Engineering)\b',
        r'\b(DataDog|NewRelic|Splunk|Prometheus|Grafana|Observability|Monitoring|Logging)\b',
        r'\b(SQL|NoSQL|Database Design|Data Modeling|ETL|Data Pipeline|Data Warehouse|Data Lake)\b',
        r'\b(API Development|Web Services|Microservices Architecture|Service Mesh|API Gateway)\b',
        r'\b(Software Engineering|Software Development|System Design|Architecture|Design Patterns)\b',
        r'\b(Computer Science|Information Technology|Software Engineering|Data Engineering)\b'
    ]
    
    # Extract skills using patterns
    for pattern in skill_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        skills.extend(matches)
    
    # Look for common skill keywords in context
    skill_keywords = [
        'experience with', 'proficient in', 'expertise in', 'knowledge of', 'familiar with',
        'skills in', 'background in', 'competency in', 'capability in', 'ability to',
        'required:', 'requirements:', 'qualifications:', 'skills:', 'technologies:',
        'must have:', 'should have:', 'preferred:', 'desired:', 'nice to have:'
    ]
    
    lines = text.split('\n')
    for i, line in enumerate(lines):
        line_lower = line.lower()
        for keyword in skill_keywords:
            if keyword in line_lower:
                # Extract potential skills from this line and next few lines
                context = ' '.join(lines[i:i+3])
                # Look for capitalized words that might be skills
                potential_skills = re.findall(r'\b[A-Z][a-zA-Z0-9\s&\.\+]+(?:\s+[A-Z][a-zA-Z0-9\s&\.\+]+)*\b', context)
                skills.extend(potential_skills)
    
    # Clean and normalize skills
    cleaned_skills = []
    
    # Common website text to filter out
    filter_words = {
        'Australia', 'New Zealand', 'Sydney', 'Melbourne', 'Brisbane', 'Perth', 'Adelaide',
        'Jobstreet', 'Jora', 'Jobsdb', 'SEEK', 'All rights reserved', 'Report this job',
        'Learn how to protect yourself', 'Artwork by Bitja', 'Gunnai', 'Yorta Yorta',
        'Dhudhuroa', 'Gunditjmara', 'Dixon Patten Jnr', 'Worldwide', 'SE Asia',
        'Yorta Yorta and Dhudhuroa',
        'Information & Communication Technology', 'Bangladesh', 'What You', 'What you',
        'Why you', 'If you', 'You are', 'You', 'Other', 'Hybrid', 'Here', 'World',
        'Every day', 'Together', 'Let', 'But you', 'The work', 'The amount of travel',
        'StrategyMore than 10', 'At Accenture', 'Accenture', 'Best Workplaces',
        'View all jobs', 'More roles and info', 'CareersSee what we', 'What we',
        'What', 'Follow Us On Linkedin', 'For The Latest Jobs', 'Introduce A Friend',
        'Referral Fee', 'Bonus Points If You Have', 'Progressive Leave Options',
        'Report this job advertBe carefulDon', 'Temple & Webster is where design meets technology',
        'To bring that vision to life', 'A tight', 'A bachelor', 'A collaborative',
        'A Machine Learning Engineer', 'As a Machine Learning Engineer', 'As a Responsible AI professional',
        'Working with cyber and information security teams', 'We work with rich',
        'Data & AI team that', 'Leverage AWS', 'TheDriveGroup is 100', 'Bring Proficient in Python and SQL with hands',
        'Join a fast', 'ML solutions that make a measurable impact', 'For The Latest Jobs',
        'Follow Us On Linkedin', 'Do Design', 'Machine Learning Engineer Job in Sydney NSW',
        'ML deployment in real', 'Machine Learning', 'New Zealand', 'Bachelor', 'Master',
        'You are', 'AI model Fairness', 'What You Need', 'AI systems', 'The amount of travel will vary from 0 to 100',
        'StrategyMore than 10', 'Transparency', 'Bonus Points If You Have', 'AI activities. We',
        'Wellbeing', 'machine learning', 'At Accenture', 'Technology and Operations services',
        'Here', 'World', 'Certifications in AI', 'Progressive Leave Options', 'Responsible AI clients. Some of the areas you',
        'AI related risksConfiguring', 'risk management', 'Strategy and Consulting', 'data science',
        'Every day', 'Artificial Intelligence', 'Report this job advertBe carefulDon',
        'View all jobsSydney NSW', 'Accenture', 'Best Workplaces', 'As a Responsible AI professional',
        'Working with cyber and information security teams', 'But you', 'Master', 'Together',
        'The work', 'AI systems on cloud and on', 'DevOps', 'analytical skills', 'Interactive',
        'Experience in working on cloud', 'Robustness', 'Soundness and Privacy', 'security',
        'Responsible AI principles', 'Data Science', 'We actively foster a workplace free from bias',
        'Let', 'Sustainability', 'Explainability', 'RAI Specialist Job in Sydney NSW',
        'AI Operations tools and frameworks', 'SQL', 'AI in real', 'GenAI', 'Hands on experience with SQL A creative',
        'What we', 'APIs Experience with GenAI tools and LLMs', 'Why you', 'What you',
        'MLOps workflows Bonus points if you', 'AI experience', 'PHP', 'What', 'Sydney NSW',
        'Google Cloud', 'Build and launch GenAI', 'CareersSee what we', 'If you',
        'More roles and info', 'A tight', 'Comfortable in the cloud', 'Google Cloud Platform',
        'A bachelor', 'cloud computing', 'Use AI to replace time', 'Temple & Webster is where design meets technology',
        'To bring that vision to life', 'AI solutions that actually move the needle', 'Bash',
        'Software Engineering', 'AI Implementation Engineer Job in St Peters'
    }
    
    for skill in skills:
        skill = skill.strip()
        # Filter out common website text and very short/long skills
        if (len(skill) > 2 and len(skill) < 50 and 
            skill not in filter_words and
            not skill.startswith('http') and
            not skill.startswith('www') and
            not skill.isdigit() and
            not any(word in skill.lower() for word in ['job', 'advert', 'report', 'learn', 'protect', 'artwork', 'rights reserved', 'yorta', 'gunnai', 'gunditjmara']) and
            not any(word in skill for word in ['Yorta', 'Gunnai', 'Gunditjmara', 'Dhudhuroa'])):
            cleaned_skills.append(skill)
    
    # Normalize skills to remove case variations
    normalized_skills = []
    seen_lowercase = set()
    
    for skill in cleaned_skills:
        skill_lower = skill.lower()
        if skill_lower not in seen_lowercase:
            # Use the first occurrence (usually the properly capitalized version)
            normalized_skills.append(skill)
            seen_lowercase.add(skill_lower)
    
    return normalized_skills


def process_job_descriptions():
    """Main function to process job descriptions"""
    print("🚀 Starting Job Description Skills Extraction")
    print("=" * 50)
    
    # Create directories
    create_directories()
    
    # Read URLs from job_description.txt
    urls_file = "00.inputs/job_description.txt"
    if not os.path.exists(urls_file):
        print(f"❌ Error: {urls_file} not found!")
        return
    
    with open(urls_file, 'r') as f:
        raw_urls = [line.strip() for line in f if line.strip()]
    
    # Deduplicate by job id from URL path to avoid processing duplicates
    urls = []
    seen_job_ids = set()
    for url in raw_urls:
        try:
            parsed = urllib.parse.urlparse(url)
            job_id = parsed.path.split('/')[-1] if parsed.path else url
        except Exception:
            job_id = url
        if job_id in seen_job_ids:
            continue
        seen_job_ids.add(job_id)
        urls.append(url)
    
    print(f"📋 Found {len(urls)} unique URLs to process (from {len(raw_urls)} lines)")
    
    # Download job descriptions
    job_descriptions_dir = "01.processing"
    downloaded_files = []
    
    for url in urls:
        filepath = download_job_description(url, job_descriptions_dir)
        if filepath:
            downloaded_files.append(filepath)
        time.sleep(2)  # Be polite: wait 2s between downloads
    
    print(f"📥 Downloaded {len(downloaded_files)} job descriptions")
    
    # Process each job description
    all_skills = []
    file_skills = {}
    
    for filepath in downloaded_files:
        print(f"🔍 Processing: {os.path.basename(filepath)}")
        
        if filepath.endswith('.html'):
            text = extract_text_from_html(filepath)
        elif filepath.endswith('.docx'):
            text = extract_text_from_docx(filepath)
        else:
            continue
        
        if text:
            skills = extract_skills(text)
            file_skills[filepath] = skills
            all_skills.extend(skills)
            print(f"  ✓ Found {len(skills)} skills")
        else:
            print(f"  ✗ No text extracted")
    
    # Count skill frequency
    skill_counts = Counter(all_skills)
    total_jobs = len(file_skills)
    
    if total_jobs == 0:
        print("❌ No job descriptions processed successfully!")
        return
    
    # Generate analysis
    generate_analysis(skill_counts, file_skills, total_jobs)
    
    print("\n✅ Analysis complete! Check the 02.outputs directory for results.")


def generate_analysis(skill_counts, file_skills, total_jobs):
    """Generate analysis reports"""
    
    # Calculate percentages based on how many jobs contain each skill
    skill_percentages = {}
    skill_job_counts = {}
    
    # Count how many jobs contain each skill (not total occurrences)
    for skill in skill_counts.keys():
        job_count = 0
        for job_skills in file_skills.values():
            if skill in job_skills:
                job_count += 1
        skill_job_counts[skill] = job_count
        percentage = (job_count / total_jobs) * 100
        skill_percentages[skill] = percentage
    
    # Categorize skills by demand
    high_demand = {skill: count for skill, count in skill_counts.items() if skill_percentages[skill] > 50}
    medium_demand = {skill: count for skill, count in skill_counts.items() if 15 <= skill_percentages[skill] <= 50}
    lower_demand = {skill: count for skill, count in skill_counts.items() if skill_percentages[skill] < 15}
    
    # Generate summary report
    generate_summary_report(skill_counts, skill_percentages, skill_job_counts, high_demand, medium_demand, lower_demand, total_jobs)
    
    # Generate detailed report
    generate_detailed_report(skill_counts, file_skills, total_jobs)


def generate_summary_report(skill_counts, skill_percentages, skill_job_counts, high_demand, medium_demand, lower_demand, total_jobs):
    """Generate summary report in markdown table format"""
    
    output_file = "02.outputs/skills_analysis_summary.md"
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# Job Skills Analysis Summary\n\n")
        f.write(f"*Analysis based on {total_jobs} job descriptions*\n\n")
        
        # Top 10 Most Demanded Skills Table
        f.write("## TOP 10 MOST DEMANDED SKILLS\n\n")
        f.write("| Rank | Skill | Count | Percentage |\n")
        f.write("|------|-------|-------|------------|\n")
        
        # Sort by job count (not total occurrences) for top 10
        top_10_by_jobs = sorted(skill_job_counts.items(), key=lambda x: x[1], reverse=True)[:10]
        for rank, (skill, job_count) in enumerate(top_10_by_jobs, 1):
            percentage = skill_percentages[skill]
            f.write(f"| {rank} | {skill} | {job_count} | {percentage:.1f}% |\n")
        
        f.write("\n")
        
        # High Demand Skills Table
        f.write("## HIGH DEMAND SKILLS (>50% of jobs)\n\n")
        f.write("| Skill | Count | Percentage |\n")
        f.write("|-------|-------|------------|\n")
        
        for skill, count in sorted(high_demand.items(), key=lambda x: skill_job_counts[x[0]], reverse=True):
            percentage = skill_percentages[skill]
            job_count = skill_job_counts[skill]
            f.write(f"| {skill} | {job_count} | {percentage:.1f}% |\n")
        
        f.write("\n")
        
        # Medium Demand Skills Table
        f.write("## MEDIUM DEMAND SKILLS (15-50% of jobs)\n\n")
        f.write("| Skill | Count | Percentage |\n")
        f.write("|-------|-------|------------|\n")
        
        for skill, count in sorted(medium_demand.items(), key=lambda x: skill_job_counts[x[0]], reverse=True):
            percentage = skill_percentages[skill]
            job_count = skill_job_counts[skill]
            f.write(f"| {skill} | {job_count} | {percentage:.1f}% |\n")
        
        f.write("\n")
        
        # Lower Demand Skills Table
        f.write("## LOWER DEMAND SKILLS (<15% of jobs)\n\n")
        f.write("| Skill | Count | Percentage |\n")
        f.write("|-------|-------|------------|\n")
        
        for skill, count in sorted(lower_demand.items(), key=lambda x: skill_job_counts[x[0]], reverse=True):
            percentage = skill_percentages[skill]
            job_count = skill_job_counts[skill]
            f.write(f"| {skill} | {job_count} | {percentage:.1f}% |\n")
        
        f.write("\n")
        
        # Key Insights
        f.write("## KEY INSIGHTS\n\n")
        
        if high_demand:
            # Find the skill with the highest job count
            top_skill = max(skill_job_counts.items(), key=lambda x: x[1])[0]
            top_percentage = skill_percentages[top_skill]
            f.write(f"- **{top_skill}** is the most in-demand skill - required in {top_percentage:.1f}% of all jobs\n")
        
        if len(high_demand) > 0:
            f.write(f"- **{len(high_demand)} skills** are in high demand (required by >50% of jobs)\n")
        
        if len(medium_demand) > 0:
            f.write(f"- **{len(medium_demand)} skills** are in medium demand (required by 15-50% of jobs)\n")
        
        if len(lower_demand) > 0:
            f.write(f"- **{len(lower_demand)} skills** are in lower demand (required by <15% of jobs)\n")
        
        # Technology trends
        tech_trends = []
        if any('Python' in skill for skill in skill_counts.keys()):
            tech_trends.append("Python programming")
        if any('AI' in skill or 'Machine Learning' in skill for skill in skill_counts.keys()):
            tech_trends.append("AI/ML technologies")
        if any('Cloud' in skill or 'AWS' in skill or 'Azure' in skill for skill in skill_counts.keys()):
            tech_trends.append("Cloud computing")
        if any('DevOps' in skill or 'CI/CD' in skill for skill in skill_counts.keys()):
            tech_trends.append("DevOps practices")
        
        if tech_trends:
            f.write(f"- Strong focus on: {', '.join(tech_trends)}\n")
        
        f.write(f"\n*Analysis completed on {time.strftime('%Y-%m-%d %H:%M:%S')}*\n")
    
    print(f"📊 Summary report saved to: {output_file}")


def generate_detailed_report(skill_counts, file_skills, total_jobs):
    """Generate detailed analysis report"""
    
    output_file = "02.outputs/skills_analysis_detail.md"
    
    # Calculate job counts for each skill
    skill_job_counts = {}
    for skill in skill_counts.keys():
        job_count = 0
        for job_skills in file_skills.values():
            if skill in job_skills:
                job_count += 1
        skill_job_counts[skill] = job_count
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# SKILLS ANALYSIS DETAILED REPORT\n")
        f.write("=" * 50 + "\n\n")
        
        # Top 10 Most Demanded Skills
        f.write("## TOP 10 MOST DEMANDED SKILLS\n")
        f.write("-" * 35 + "\n")
        top_10_by_jobs = sorted(skill_job_counts.items(), key=lambda x: x[1], reverse=True)[:10]
        for skill, job_count in top_10_by_jobs:
            percentage = (job_count / total_jobs) * 100
            f.write(f"{skill}: {job_count} jobs ({percentage:.1f}%)\n")
        
        f.write("\n")
        
        # Skills Analysis
        f.write("## SKILLS ANALYSIS\n")
        f.write("-" * 20 + "\n")
        f.write(f"Total jobs analyzed: {total_jobs}\n")
        f.write(f"Total unique skills found: {len(skill_counts)}\n")
        f.write(f"Average skills per job: {sum(skill_counts.values()) / total_jobs:.1f}\n")
        
        f.write("\n")
        
        # All Skills by Frequency
        f.write("## ALL SKILLS BY FREQUENCY\n")
        f.write("-" * 30 + "\n")
        for skill, job_count in sorted(skill_job_counts.items(), key=lambda x: x[1], reverse=True):
            percentage = (job_count / total_jobs) * 100
            f.write(f"{skill}: {job_count} jobs ({percentage:.1f}%)\n")
        
        f.write("\n")
        
        # Skills by Job
        f.write("## SKILLS BY JOB (Details)\n")
        f.write("-" * 25 + "\n")
        for filepath, skills in file_skills.items():
            job_name = os.path.basename(filepath).replace('.html', '').replace('.docx', '')
            f.write(f"\n**{job_name}:**\n")
            for skill in skills:
                f.write(f"  - {skill}\n")
    
    print(f"📋 Detailed report saved to: {output_file}")


def main():
    """Main entry point"""
    try:
        process_job_descriptions()
    except KeyboardInterrupt:
        print("\n⚠️  Process interrupted by user")
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
