import os
import yaml

# Load redirects from _redirects.yml
with open('_redirects.yml', 'r') as file:
    redirects = yaml.safe_load(file)['redirects']

# Ensure the _redirects directory exists
os.makedirs('_redirects', exist_ok=True)

# Generate markdown files for each redirect
for redirect in redirects:
    from_path = redirect['from'].strip('/')
    to_url = redirect['to']
    filename = f'_redirects/{from_path}.md'
    
    # Create markdown content
    content = f"""---
layout: null
permalink: {redirect['from']}
redirect_to: {to_url}
---"""
    
    # Write the content to the markdown file
    with open(filename, 'w') as file:
        file.write(content)

print('Redirect markdown files generated successfully.')
