import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

key = os.getenv("GROQ_API_KEY")
print(f"Loaded key starting with: {key[:7] if key else 'NONE'}")

client = Groq(api_key=key)

try:
    # 1. Fetch available models for your exact key
    models = [m.id for m in client.models.list().data]
    print("\n✅ Key authenticated successfully!")
    print(f"Models available on your account: {models}\n")

    # 2. Test completion on llama-3.1-8b-instant
    res = client.chat.completions.create(
        model="llama-3.1-8b-instant", messages=[{"role": "user", "content": "Hello"}]
    )
    print("✅ Model call succeeded!")
    print(f"Response: {res.choices[0].message.content}")

except Exception as e:
    print(f"\n❌ API Error: {e}")
