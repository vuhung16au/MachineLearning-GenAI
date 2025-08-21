#!/usr/bin/env python3

from mlx_lm import load, generate

def main():
    print("Loading model...")
    
    # Load a small, fast model for demo purposes
    model, tokenizer = load("mlx-community/Qwen2.5-0.5B-Instruct-4bit")
    
    print("Model loaded successfully!")
    print("Generating 'Hello World' response...\n")
    
    # Simple prompt
    prompt = "why sky is blue?"
    
    # Generate response
    response = generate(
        model, 
        tokenizer, 
        prompt=prompt, 
        max_tokens=50,
        verbose=False
    )
    
    print(f"Prompt: {prompt}")
    print(f"Response: {response}")
    print("\n🎉 Hello World with MLX-LM complete!")

if __name__ == "__main__":
    main()