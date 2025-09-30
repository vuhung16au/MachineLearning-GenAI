"""
Raise awareness about bias in AI and the importance of diversity.

This script creates educational content and visualizations to highlight
the importance of fairness, diversity, and bias awareness in AI systems.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import json
from typing import Dict, List, Any
import warnings
warnings.filterwarnings('ignore')


class BiasAwarenessRaiser:
    """Create awareness content about bias in AI systems."""
    
    def __init__(self):
        """Initialize the awareness raiser."""
        self.colors = {
            'primary': '#2E86AB',
            'secondary': '#A23B72', 
            'accent': '#F18F01',
            'success': '#C73E1D',
            'neutral': '#6C757D'
        }
        
    def create_bias_education_content(self) -> Dict[str, Any]:
        """Create educational content about bias in AI."""
        content = {
            'title': 'Understanding Bias in AI: The Bark Bias Cure Project',
            'introduction': {
                'problem': 'Artificial Intelligence systems can perpetuate and amplify human biases, leading to unfair outcomes for certain groups.',
                'impact': 'Bias in AI affects millions of people daily, from hiring decisions to loan approvals to criminal justice.',
                'solution': 'By understanding, measuring, and addressing bias, we can build fairer AI systems that benefit everyone.'
            },
            'types_of_bias': {
                'historical_bias': {
                    'name': 'Historical Bias',
                    'description': 'Bias that exists in the training data due to historical inequalities.',
                    'example': 'If historical hiring data shows bias against certain groups, an AI trained on this data will perpetuate that bias.',
                    'impact': 'Perpetuates existing social inequalities.'
                },
                'representation_bias': {
                    'name': 'Representation Bias',
                    'description': 'Bias that occurs when certain groups are underrepresented in training data.',
                    'example': 'Facial recognition systems trained primarily on one demographic group perform poorly on others.',
                    'impact': 'Poor performance for underrepresented groups.'
                },
                'measurement_bias': {
                    'name': 'Measurement Bias',
                    'description': 'Bias introduced by how we measure or define success.',
                    'example': 'Using arrest rates as a proxy for crime rates, when arrest rates themselves may be biased.',
                    'impact': 'Skewed understanding of reality.'
                },
                'aggregation_bias': {
                    'name': 'Aggregation Bias',
                    'description': 'Bias that occurs when we assume one model fits all groups.',
                    'example': 'Using the same risk assessment model for all demographics when risk factors may differ.',
                    'impact': 'Poor predictions for groups with different characteristics.'
                },
                'evaluation_bias': {
                    'name': 'Evaluation Bias',
                    'description': 'Bias in how we evaluate model performance across different groups.',
                    'example': 'Focusing only on overall accuracy while ignoring performance disparities across groups.',
                    'impact': 'Hidden unfairness in model deployment.'
                }
            },
            'fairness_principles': {
                'demographic_parity': {
                    'name': 'Demographic Parity',
                    'description': 'The probability of a positive outcome should be the same across all groups.',
                    'formula': 'P(Ŷ=1|A=a) = P(Ŷ=1|A=b) for all groups a, b',
                    'use_case': 'When we want equal opportunity regardless of group membership.'
                },
                'equalized_odds': {
                    'name': 'Equalized Odds',
                    'description': 'True positive and false positive rates should be equal across groups.',
                    'formula': 'P(Ŷ=1|Y=y, A=a) = P(Ŷ=1|Y=y, A=b) for all groups a, b and outcomes y',
                    'use_case': 'When we want equal accuracy for all groups.'
                },
                'equal_opportunity': {
                    'name': 'Equal Opportunity',
                    'description': 'True positive rates should be equal across groups.',
                    'formula': 'P(Ŷ=1|Y=1, A=a) = P(Ŷ=1|Y=1, A=b) for all groups a, b',
                    'use_case': 'When we want equal treatment for positive cases across groups.'
                }
            },
            'mitigation_strategies': {
                'pre_processing': {
                    'name': 'Pre-processing',
                    'description': 'Modify training data to reduce bias before model training.',
                    'techniques': [
                        'Data augmentation for underrepresented groups',
                        'Synthetic data generation',
                        'Reweighting samples',
                        'Feature selection to remove biased features'
                    ]
                },
                'in_processing': {
                    'name': 'In-processing',
                    'description': 'Modify the training process to incorporate fairness constraints.',
                    'techniques': [
                        'Fairness-aware loss functions',
                        'Adversarial debiasing',
                        'Multi-objective optimization',
                        'Regularization for fairness'
                    ]
                },
                'post_processing': {
                    'name': 'Post-processing',
                    'description': 'Modify model predictions to ensure fairness.',
                    'techniques': [
                        'Threshold optimization',
                        'Calibration for different groups',
                        'Rejection sampling',
                        'Outcome modification'
                    ]
                }
            }
        }
        
        return content
    
    def create_bias_visualizations(self, df: pd.DataFrame, output_dir: Path):
        """Create educational visualizations about bias."""
        print("📊 Creating bias awareness visualizations...")
        
        # Set style for educational content
        plt.style.use('default')
        sns.set_palette("husl")
        
        # 1. Bias Impact Visualization
        self._create_bias_impact_chart(output_dir)
        
        # 2. Fairness Metrics Comparison
        self._create_fairness_metrics_chart(output_dir)
        
        # 3. Bias Types Overview
        self._create_bias_types_overview(output_dir)
        
        # 4. Real-world Examples
        self._create_real_world_examples(output_dir)
        
        # 5. Dataset bias analysis
        if df is not None:
            self._create_dataset_bias_analysis(df, output_dir)
        
        print(f"✅ Awareness visualizations saved to {output_dir}/")
    
    def _create_bias_impact_chart(self, output_dir: Path):
        """Create chart showing the impact of bias in AI."""
        fig, ax = plt.subplots(figsize=(14, 8))
        
        # Simulate bias impact data
        domains = ['Hiring', 'Lending', 'Healthcare', 'Criminal Justice', 'Education', 'Insurance']
        bias_impact = [0.15, 0.22, 0.18, 0.35, 0.12, 0.20]  # Simulated bias scores
        affected_people = [50000, 200000, 100000, 30000, 150000, 80000]  # Simulated affected population
        
        # Create bubble chart
        scatter = ax.scatter(domains, bias_impact, s=[p/1000 for p in affected_people], 
                           alpha=0.7, c=bias_impact, cmap='Reds', edgecolors='black')
        
        ax.set_xlabel('AI Application Domain', fontsize=12)
        ax.set_ylabel('Bias Impact Score', fontsize=12)
        ax.set_title('Impact of Bias Across Different AI Applications\n(Bubble size = Number of people affected)', 
                    fontsize=14, fontweight='bold')
        
        # Add colorbar
        cbar = plt.colorbar(scatter)
        cbar.set_label('Bias Impact Score', fontsize=10)
        
        # Rotate x-axis labels
        plt.xticks(rotation=45, ha='right')
        
        # Add annotations
        for i, (domain, impact, people) in enumerate(zip(domains, bias_impact, affected_people)):
            ax.annotate(f'{people:,}', (i, impact), ha='center', va='bottom', fontsize=9)
        
        plt.tight_layout()
        plt.savefig(output_dir / 'bias_impact_across_domains.png', dpi=300, bbox_inches='tight')
        plt.close()
    
    def _create_fairness_metrics_chart(self, output_dir: Path):
        """Create chart explaining different fairness metrics."""
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
        
        # Demographic Parity
        groups = ['Group A', 'Group B', 'Group C']
        positive_rates = [0.3, 0.3, 0.3]  # Equal rates
        colors = ['#2E86AB', '#2E86AB', '#2E86AB']
        
        bars1 = ax1.bar(groups, positive_rates, color=colors, alpha=0.7)
        ax1.set_title('Demographic Parity\n(Equal positive rates across groups)', fontweight='bold')
        ax1.set_ylabel('Positive Rate')
        ax1.set_ylim(0, 0.5)
        
        # Add value labels
        for bar, rate in zip(bars1, positive_rates):
            ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01, 
                    f'{rate:.1%}', ha='center', va='bottom')
        
        # Equalized Odds
        tpr = [0.8, 0.8, 0.8]  # Equal TPR
        fpr = [0.2, 0.2, 0.2]  # Equal FPR
        
        x = np.arange(len(groups))
        width = 0.35
        
        bars2 = ax2.bar(x - width/2, tpr, width, label='True Positive Rate', alpha=0.7)
        bars3 = ax2.bar(x + width/2, fpr, width, label='False Positive Rate', alpha=0.7)
        
        ax2.set_title('Equalized Odds\n(Equal TPR and FPR across groups)', fontweight='bold')
        ax2.set_ylabel('Rate')
        ax2.set_xticks(x)
        ax2.set_xticklabels(groups)
        ax2.legend()
        ax2.set_ylim(0, 1)
        
        # Equal Opportunity
        tpr_equal = [0.8, 0.8, 0.8]  # Equal TPR
        fpr_unequal = [0.1, 0.3, 0.2]  # Unequal FPR
        
        bars4 = ax3.bar(x - width/2, tpr_equal, width, label='True Positive Rate', alpha=0.7)
        bars5 = ax3.bar(x + width/2, fpr_unequal, width, label='False Positive Rate', alpha=0.7)
        
        ax3.set_title('Equal Opportunity\n(Equal TPR, FPR can differ)', fontweight='bold')
        ax3.set_ylabel('Rate')
        ax3.set_xticks(x)
        ax3.set_xticklabels(groups)
        ax3.legend()
        ax3.set_ylim(0, 1)
        
        # Bias over time
        years = np.arange(2020, 2025)
        bias_reduction = [0.3, 0.25, 0.2, 0.15, 0.1]  # Decreasing bias
        
        ax4.plot(years, bias_reduction, marker='o', linewidth=3, markersize=8, color='#C73E1D')
        ax4.set_title('Bias Reduction Over Time\n(With proper interventions)', fontweight='bold')
        ax4.set_xlabel('Year')
        ax4.set_ylabel('Bias Score')
        ax4.grid(True, alpha=0.3)
        ax4.set_ylim(0, 0.35)
        
        # Add trend line
        z = np.polyfit(years, bias_reduction, 1)
        p = np.poly1d(z)
        ax4.plot(years, p(years), "--", alpha=0.7, color='gray')
        
        plt.tight_layout()
        plt.savefig(output_dir / 'fairness_metrics_explanation.png', dpi=300, bbox_inches='tight')
        plt.close()
    
    def _create_bias_types_overview(self, output_dir: Path):
        """Create overview of different types of bias."""
        fig, ax = plt.subplots(figsize=(16, 10))
        
        # Define bias types and their characteristics
        bias_types = [
            ('Historical Bias', 0.8, 'High', 'Training data reflects past inequalities'),
            ('Representation Bias', 0.6, 'Medium', 'Underrepresentation of certain groups'),
            ('Measurement Bias', 0.7, 'High', 'Biased proxies for true outcomes'),
            ('Aggregation Bias', 0.5, 'Medium', 'One-size-fits-all approach'),
            ('Evaluation Bias', 0.4, 'Low', 'Unequal evaluation across groups')
        ]
        
        # Create radar chart
        categories = ['Severity', 'Detectability', 'Impact', 'Complexity', 'Mitigation Difficulty']
        
        # Normalize values for radar chart
        values = np.array([
            [0.8, 0.6, 0.7, 0.5, 0.4],  # Historical Bias
            [0.6, 0.8, 0.6, 0.4, 0.6],  # Representation Bias
            [0.7, 0.4, 0.8, 0.7, 0.8],  # Measurement Bias
            [0.5, 0.7, 0.5, 0.3, 0.5],  # Aggregation Bias
            [0.4, 0.9, 0.4, 0.2, 0.3]   # Evaluation Bias
        ])
        
        # Create subplot for each bias type
        fig, axes = plt.subplots(2, 3, figsize=(18, 12))
        axes = axes.flatten()
        
        colors = ['#2E86AB', '#A23B72', '#F18F01', '#C73E1D', '#6C757D']
        
        for i, (bias_name, severity, detectability, description) in enumerate(bias_types):
            ax = axes[i]
            
            # Create bar chart for each bias type
            metrics = ['Severity', 'Detectability', 'Impact', 'Complexity', 'Mitigation']
            values_bias = values[i]
            
            bars = ax.bar(metrics, values_bias, color=colors[i], alpha=0.7)
            ax.set_title(f'{bias_name}\n{description}', fontweight='bold', fontsize=10)
            ax.set_ylabel('Score (0-1)')
            ax.set_ylim(0, 1)
            
            # Add value labels
            for bar, value in zip(bars, values_bias):
                ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.02, 
                       f'{value:.1f}', ha='center', va='bottom', fontsize=8)
            
            # Rotate x-axis labels
            ax.tick_params(axis='x', rotation=45)
        
        # Remove the last subplot
        fig.delaxes(axes[5])
        
        plt.suptitle('Types of Bias in AI Systems', fontsize=16, fontweight='bold')
        plt.tight_layout()
        plt.savefig(output_dir / 'bias_types_overview.png', dpi=300, bbox_inches='tight')
        plt.close()
    
    def _create_real_world_examples(self, output_dir: Path):
        """Create chart with real-world examples of AI bias."""
        fig, ax = plt.subplots(figsize=(14, 10))
        
        # Real-world bias examples
        examples = [
            {
                'system': 'Facial Recognition',
                'bias': 'Gender and Race',
                'impact': 'Higher error rates for women and people of color',
                'severity': 0.8,
                'year': 2018
            },
            {
                'system': 'Hiring Algorithms',
                'bias': 'Gender',
                'impact': 'Discrimination against female candidates',
                'severity': 0.7,
                'year': 2015
            },
            {
                'system': 'Risk Assessment',
                'bias': 'Race',
                'impact': 'Higher risk scores for minorities',
                'severity': 0.9,
                'year': 2016
            },
            {
                'system': 'Loan Approval',
                'bias': 'Race and Gender',
                'impact': 'Lower approval rates for certain groups',
                'severity': 0.6,
                'year': 2019
            },
            {
                'system': 'Healthcare AI',
                'bias': 'Race and Gender',
                'impact': 'Unequal treatment recommendations',
                'severity': 0.8,
                'year': 2019
            }
        ]
        
        # Create timeline
        years = [ex['year'] for ex in examples]
        severities = [ex['severity'] for ex in examples]
        systems = [ex['system'] for ex in examples]
        
        # Create scatter plot
        scatter = ax.scatter(years, severities, s=[200] * len(years), 
                           c=severities, cmap='Reds', alpha=0.7, edgecolors='black')
        
        # Add labels
        for i, (year, severity, system) in enumerate(zip(years, severities, systems)):
            ax.annotate(system, (year, severity), xytext=(5, 5), 
                       textcoords='offset points', fontsize=9, fontweight='bold')
        
        ax.set_xlabel('Year', fontsize=12)
        ax.set_ylabel('Bias Severity Score', fontsize=12)
        ax.set_title('Real-World Examples of AI Bias\n(Size represents impact)', 
                    fontsize=14, fontweight='bold')
        
        # Add colorbar
        cbar = plt.colorbar(scatter)
        cbar.set_label('Bias Severity', fontsize=10)
        
        # Add grid
        ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig(output_dir / 'real_world_bias_examples.png', dpi=300, bbox_inches='tight')
        plt.close()
    
    def _create_dataset_bias_analysis(self, df: pd.DataFrame, output_dir: Path):
        """Create analysis of bias in the dataset."""
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
        
        # 1. Barking rate by race
        race_bias = df.groupby('human_race')['barks'].mean().sort_values(ascending=False)
        bars1 = ax1.bar(range(len(race_bias)), race_bias.values, 
                       color=plt.cm.Reds(np.linspace(0.3, 1, len(race_bias))))
        ax1.set_title('Barking Rate by Race\n(Showing bias in dataset)', fontweight='bold')
        ax1.set_ylabel('Barking Rate')
        ax1.set_xticks(range(len(race_bias)))
        ax1.set_xticklabels(race_bias.index, rotation=45, ha='right')
        
        # Add value labels
        for i, (bar, value) in enumerate(zip(bars1, race_bias.values)):
            ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01, 
                    f'{value:.2%}', ha='center', va='bottom')
        
        # 2. Barking rate by gender
        gender_bias = df.groupby('human_gender')['barks'].mean().sort_values(ascending=False)
        bars2 = ax2.bar(range(len(gender_bias)), gender_bias.values,
                       color=plt.cm.Blues(np.linspace(0.3, 1, len(gender_bias))))
        ax2.set_title('Barking Rate by Gender\n(Showing bias in dataset)', fontweight='bold')
        ax2.set_ylabel('Barking Rate')
        ax2.set_xticks(range(len(gender_bias)))
        ax2.set_xticklabels(gender_bias.index, rotation=45, ha='right')
        
        # Add value labels
        for i, (bar, value) in enumerate(zip(bars2, gender_bias.values)):
            ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01, 
                    f'{value:.2%}', ha='center', va='bottom')
        
        # 3. Age group analysis
        age_bias = df.groupby('human_age_group')['barks'].mean().sort_values(ascending=False)
        bars3 = ax3.bar(range(len(age_bias)), age_bias.values,
                       color=plt.cm.Greens(np.linspace(0.3, 1, len(age_bias))))
        ax3.set_title('Barking Rate by Age Group\n(Showing bias in dataset)', fontweight='bold')
        ax3.set_ylabel('Barking Rate')
        ax3.set_xticks(range(len(age_bias)))
        ax3.set_xticklabels(age_bias.index, rotation=45, ha='right')
        
        # Add value labels
        for i, (bar, value) in enumerate(zip(bars3, age_bias.values)):
            ax3.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01, 
                    f'{value:.2%}', ha='center', va='bottom')
        
        # 4. Bias summary
        bias_summary = {
            'Race': race_bias.max() - race_bias.min(),
            'Gender': gender_bias.max() - gender_bias.min(),
            'Age': age_bias.max() - age_bias.min()
        }
        
        bars4 = ax4.bar(bias_summary.keys(), bias_summary.values(),
                       color=['#FF6B6B', '#4ECDC4', '#45B7D1'])
        ax4.set_title('Bias Magnitude by Attribute\n(Max - Min rates)', fontweight='bold')
        ax4.set_ylabel('Bias Magnitude')
        
        # Add value labels
        for bar, value in zip(bars4, bias_summary.values()):
            ax4.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.005, 
                    f'{value:.2%}', ha='center', va='bottom')
        
        plt.tight_layout()
        plt.savefig(output_dir / 'dataset_bias_analysis.png', dpi=300, bbox_inches='tight')
        plt.close()
    
    def generate_awareness_report(self, df: pd.DataFrame, output_dir: Path):
        """Generate comprehensive awareness report."""
        print("📋 Generating awareness report...")
        
        # Create educational content
        content = self.create_bias_education_content()
        
        # Create visualizations
        self.create_bias_visualizations(df, output_dir)
        
        # Generate markdown report
        report_content = f"""# {content['title']}

## Introduction

{content['introduction']['problem']}

**Impact:** {content['introduction']['impact']}

**Solution:** {content['introduction']['solution']}

## Types of Bias in AI

"""
        
        for bias_type, details in content['types_of_bias'].items():
            report_content += f"""### {details['name']}

**Description:** {details['description']}

**Example:** {details['example']}

**Impact:** {details['impact']}

---

"""
        
        report_content += """## Fairness Principles

### Demographic Parity
The probability of a positive outcome should be the same across all groups.

**Formula:** P(Ŷ=1|A=a) = P(Ŷ=1|A=b) for all groups a, b

**Use Case:** When we want equal opportunity regardless of group membership.

### Equalized Odds
True positive and false positive rates should be equal across groups.

**Formula:** P(Ŷ=1|Y=y, A=a) = P(Ŷ=1|Y=y, A=b) for all groups a, b and outcomes y

**Use Case:** When we want equal accuracy for all groups.

### Equal Opportunity
True positive rates should be equal across groups.

**Formula:** P(Ŷ=1|Y=1, A=a) = P(Ŷ=1|Y=1, A=b) for all groups a, b

**Use Case:** When we want equal treatment for positive cases across groups.

## Mitigation Strategies

### Pre-processing
Modify training data to reduce bias before model training.

**Techniques:**
- Data augmentation for underrepresented groups
- Synthetic data generation
- Reweighting samples
- Feature selection to remove biased features

### In-processing
Modify the training process to incorporate fairness constraints.

**Techniques:**
- Fairness-aware loss functions
- Adversarial debiasing
- Multi-objective optimization
- Regularization for fairness

### Post-processing
Modify model predictions to ensure fairness.

**Techniques:**
- Threshold optimization
- Calibration for different groups
- Rejection sampling
- Outcome modification

## Key Takeaways

1. **Bias is everywhere:** AI systems can perpetuate and amplify human biases.

2. **Measurement matters:** We need to measure bias to understand and address it.

3. **Fairness is complex:** Different fairness metrics may conflict with each other.

4. **Intervention is possible:** There are many techniques to reduce bias in AI systems.

5. **Continuous monitoring:** Bias detection and mitigation is an ongoing process.

## Resources for Further Learning

- [Fairness in Machine Learning](https://fairmlbook.org/)
- [AI Fairness 360 Toolkit](https://aif360.mybluemix.net/)
- [Google's Responsible AI Practices](https://ai.google/responsibilities/responsible-ai-practices/)
- [Microsoft's Responsible AI](https://www.microsoft.com/en-us/ai/responsible-ai)

## About This Project

This project demonstrates how bias can manifest in AI systems using a fun, synthetic example of dog behavior. While the scenario is fictional, the underlying principles of bias detection, measurement, and mitigation are real and applicable to serious AI applications.

The goal is to raise awareness about the importance of fairness in AI and provide tools and techniques for building more equitable systems.

---

*Remember: Fair AI is not just a technical challenge—it's a moral imperative.*
"""
        
        # Save report
        with open(output_dir / 'bias_awareness_report.md', 'w') as f:
            f.write(report_content)
        
        # Save structured content as JSON
        with open(output_dir / 'bias_education_content.json', 'w') as f:
            json.dump(content, f, indent=2)
        
        print(f"✅ Awareness report saved to {output_dir}/bias_awareness_report.md")
        print(f"✅ Education content saved to {output_dir}/bias_education_content.json")


def main():
    """Main awareness function."""
    # Check if dataset exists
    data_path = Path("data/dog_behavior_dataset.csv")
    df = None
    if data_path.exists():
        print("📊 Loading dataset for bias analysis...")
        df = pd.read_csv(data_path)
        print(f"Dataset shape: {df.shape}")
    else:
        print("⚠️  Dataset not found. Creating awareness content without data analysis.")
    
    # Initialize awareness raiser
    raiser = BiasAwarenessRaiser()
    
    # Create output directory
    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)
    
    # Generate awareness report
    raiser.generate_awareness_report(df, reports_dir)
    
    print(f"\n✅ Awareness content generated!")
    print(f"Report saved to: reports/bias_awareness_report.md")
    print(f"Education content saved to: reports/bias_education_content.json")
    print(f"Visualizations saved to: reports/")


if __name__ == "__main__":
    main()
