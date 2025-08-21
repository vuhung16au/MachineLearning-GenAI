#!/usr/bin/env python3

from mlx_lm.utils import load
from mlx_lm.generate import generate
from mlx_lm.sample_utils import make_sampler, make_repetition_penalty

def main():
    print("🤖 MLX-LM Chat Assistant")
    print("=" * 40)
    print("Loading model...")
    
    # Load the model
    model, tokenizer = load("mlx-community/Qwen2.5-0.5B-Instruct-4bit")
    
    print("✅ Model loaded successfully!")
    print("You can start chatting now. Type '/exit' or '/quit' to end the conversation.")
    print("=" * 40)
    
    # Chat loop
    while True:
        # Get user input
        user_input = input("\n💬 You: ").strip()
        
        # Check for exit commands
        if user_input.lower() in ['/exit', '/quit']:
            print("\n👋 Goodbye! Thanks for chatting!")
            break
        
        # Skip empty inputs
        if not user_input:
            continue
        
        # Generate response
        print("\n🤖 Assistant: ", end="", flush=True)
        
        try:
            # Create a sampler with temperature to prevent repetition
            sampler = make_sampler(temp=0.7, top_p=0.9)
            
            # Create repetition penalty processor
            repetition_penalty = make_repetition_penalty(penalty=1.1, context_size=20)
            
            response = generate(
                model, 
                tokenizer, 
                prompt=user_input, 
                max_tokens=550,  # Increased for better responses
                sampler=sampler,
                logits_processors=[repetition_penalty],
                verbose=False
            )
            # Clean up the response by removing all backticks and extra formatting
            cleaned_response = response.strip()
            # Remove all backticks (both single and triple)
            cleaned_response = cleaned_response.replace('```', '').replace('`', '')
            # Remove excessive newlines
            while '\n\n\n' in cleaned_response:
                cleaned_response = cleaned_response.replace('\n\n\n', '\n\n')
            # Strip again to remove any leading/trailing whitespace
            cleaned_response = cleaned_response.strip()
            
            print(cleaned_response)
        except Exception as e:
            print(f"❌ Error generating response: {e}")
            print("Please try again with a different question.")

if __name__ == "__main__":
    main()