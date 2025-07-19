# scripts/quote.py

import requests

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    data = response.json()
    quote = f"**{data[0]['q']}** — *{data[0]['a']}*"
    return quote

def replace_quote_in_readme(new_quote):
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

if __name__ == "__main__":
    quote = get_quote()
    replace_quote_in_readme(quote)
