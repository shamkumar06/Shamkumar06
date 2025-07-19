import requests
import re
import sys

def get_quote():
    try:
        response = requests.get("https://zenquotes.io/api/random", timeout=10)
        response.raise_for_status()
        data = response.json()
        quote = f"**{data[0]['q']}** — *{data[0]['a']}*"
        return quote
    except Exception as e:
        print(f"[❌ ERROR] Failed to fetch quote: {e}")
        sys.exit(1)

def replace_quote_in_readme(new_quote):
    try:
        with open("README.md", "r", encoding="utf-8") as file:
            content = file.read()

        updated_content = re.sub(
            r"<!--QUOTE-START-->.*?<!--QUOTE-END-->",
            f"<!--QUOTE-START-->\n{new_quote}\n<!--QUOTE-END-->",
            content,
            flags=re.DOTALL,
        )

        with open("README.md", "w", encoding="utf-8") as file:
            file.write(updated_content)

        print("[✅ SUCCESS] README.md updated with new quote.")

    except Exception as e:
        print(f"[❌ ERROR] Failed to update README.md: {e}")
        sys.exit(1)

if __name__ == "__main__":
    quote = get_quote()
    replace_quote_in_readme(quote)

