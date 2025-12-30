import json
import random
import re
from datetime import datetime

# Read quotes
with open('quotes.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    quotes = data['quotes']

# Select random quote
quote = random.choice(quotes)

# Read current README
with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

# Replace quote section
quote_pattern = r'<div align="center">\s*<h3>.*?</h3>\s*<p><i>.*?</i></p>\s*</div>'

new_quote_section = f'''<div align="center">
  <h3>{quote['sanskrit']}</h3>
  <p><i>"{quote['english']}"</i></p>
</div>'''

# Update README
updated_readme = re.sub(quote_pattern, new_quote_section, readme, flags=re.DOTALL)

# Write back
with open('README.md', 'w', encoding='utf-8') as f:
    f.write(updated_readme)

print(f"Updated quote to: {quote['english']}")
