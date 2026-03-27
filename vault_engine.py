import random
import string

def generate_secure_key(phrase):
    # Mapping "weak" characters to "strong" symbols
    transformations = {
        'a': '@', 's': '$', 'i': '!', 'o': '0', 'e': '3', 't': '7'
    }
    
    # Apply transformations
    secure_phrase = "".join(transformations.get(c.lower(), c) for c in phrase)
    
    # Add a "Salt" (random complexity)
    salt = "".join(random.choices(string.ascii_uppercase + string.punctuation, k=4))
    
    return f"{secure_phrase}_{salt}"

def main():
    print("🔐 THE VAULT: SECURITY ENGINE v1.0")
    print("-" * 35)
    
    user_input = input("Enter a memorable phrase: ")
    if user_input:
        key = generate_secure_key(user_input)
        print(f"\n[ORIGINAL]: {user_input}")
        print(f"[SECURE KEY]: {key}")
        print("\nStructure: [Transformed Phrase] + [Random Salt]")

if __name__ == "__main__":
    main()
