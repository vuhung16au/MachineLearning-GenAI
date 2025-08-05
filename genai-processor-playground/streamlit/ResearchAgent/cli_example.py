#!/usr/bin/env python3
"""
Research Agent Example - Command Line Version

This script demonstrates how to use the Research Agent programmatically
without the Streamlit interface. Useful for automation, testing, or
integration into other applications.
"""

import asyncio
import os
import sys
from typing import List

# Add the research module to the path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

try:
    from genai_processors import content_api
    from genai_processors import processor
    from genai_processors import streams
    from genai_processors.examples import research
except ImportError as e:
    print(f"Import error: {e}")
    print("Please ensure the genai-processors library is properly installed.")
    sys.exit(1)

ProcessorPart = processor.ProcessorPart


async def run_research_cli(api_key: str, query: str, num_topics: int = 5):
    """Run the research agent from command line."""
    print(f"🔬 Research Agent CLI")
    print(f"Query: {query}")
    print(f"Topics: {num_topics}")
    print("=" * 50)
    
    # Create configuration
    config = research.interfaces.Config(
        num_topics=num_topics,
        topic_generator_model_name="gemini-2.5-flash",
        topic_researcher_model_name="gemini-2.5-flash",
        research_synthesizer_model_name="gemini-2.5-flash"
    )
    
    # Initialize the research agent
    agent = research.ResearchAgent(api_key=api_key, config=config)
    input_stream = streams.stream_content([ProcessorPart(query)])
    
    # Collect output
    output_parts = content_api.ProcessorContent()
    
    print("📋 Research Process:")
    async for content_part in agent(input_stream):
        if content_part.substream_name == 'status':
            print(f"  • {content_part.text}")
        else:
            output_parts += content_part
    
    # Get final research
    final_research = content_api.as_text(output_parts, substream_name='')
    
    print("\n" + "=" * 50)
    print("📊 RESEARCH RESULTS")
    print("=" * 50)
    print(final_research)
    
    return final_research


def main():
    """Main CLI function."""
    # Check for API key
    api_key = os.getenv('GOOGLE_API_KEY')
    if not api_key:
        print("❌ Error: GOOGLE_API_KEY environment variable not set.")
        print("Please set your API key:")
        print("export GOOGLE_API_KEY='your-api-key-here'")
        sys.exit(1)
    
    # Get query from command line or use default
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
    else:
        query = "Research the best things about Vietnam's military power!"
        print(f"ℹ️  No query provided, using default: {query}")
    
    # Get number of topics
    num_topics = int(os.getenv('NUM_TOPICS', 5))
    
    try:
        # Run the research
        result = asyncio.run(run_research_cli(api_key, query, num_topics))
        
        # Optionally save to file
        output_file = os.getenv('OUTPUT_FILE')
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(f"# Research Results\n\n**Query:** {query}\n\n{result}")
            print(f"\n💾 Results saved to: {output_file}")
        
        print("\n✅ Research completed successfully!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
