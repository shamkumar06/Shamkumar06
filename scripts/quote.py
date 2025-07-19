import requests

README_PATH = "README.md"

def fetch_quote():
    try:
        response = requests.get("https://zenquotes.io/api/random")
        response.raise_for_status()
        data = response.json()
        quote = f"**{data[0]['q']}** — *{data[0]['a']}*"
        return quote
    except Exception as e:
        print(f"Error fetching quote: {e}")
        return "**Be the change that you wish to see in the world.** — *Mahatma Gandhi*"

def replace_quote_in_readme(new_quote):
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    updated_content = re.sub(
        r"(<!--QUOTE-START-->)(.*?)(<!--QUOTE-END-->)",
        f"\\1\n{new_quote}\n\\3",
        content,
        flags=re.DOTALL
    )

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(updated_content)

    print("✅ README updated with new quote.")

if __name__ == "__main__":
    quote = fetch_quote()
    replace_quote_in_readme(quote)
