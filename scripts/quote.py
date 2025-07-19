import requests
import re

with open("README.md", "r", encoding="utf-8") as file:
    readme = file.read()

response = requests.get("https://zenquotes.io/api/random")
quote_data = response.json()
quote = f"{quote_data[0]['q']} — {quote_data[0]['a']}"

# Replace between the tags
updated_readme = re.sub(
    r"<!--QUOTE-START-->[\s\S]*?<!--QUOTE-END-->",
    f"<!--QUOTE-START-->\n{quote}\n<!--QUOTE-END-->",
    readme
)

with open("README.md", "w", encoding="utf-8") as file:
    file.write(updated_readme)
