import requests

quote_data = requests.get("https://api.quotable.io/random").json()
quote = f'"{quote_data["content"]}" — *{quote_data["author"]}*'

with open("README.md", "r", encoding="utf-8") as f:
    lines = f.readlines()

start = lines.index("<!--QUOTE-START-->\n")
end = lines.index("<!--QUOTE-END-->\n")

lines[start + 1:end] = [quote + "\n"]

with open("README.md", "w", encoding="utf-8") as f:
    f.writelines(lines)
