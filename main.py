import os
import markdown

def convert_md_to_html(md_content, title):
    html_content = markdown.markdown(md_content)
    template = f"""<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>{title}</title>
    <style>
        body {{ font-family: Arial, sans-serif; max-width: 700px; margin: 40px auto; padding: 20px; line-height: 1.6; }}
        h1, h2, h3 {{ color: #333; }}
        a {{ color: #0066cc; }}
        pre {{ background: #f4f4f4; padding: 10px; }}
        code {{ font-family: monospace; }}
    </style>
</head>
<body>
    {html_content}
</body>
</html>"""
    return template

def generate_blog(input_folder='posts', output_folder='public'):
    os.makedirs(output_folder, exist_ok=True)
    for filename in os.listdir(input_folder):
        if filename.endswith('.md'):
            with open(os.path.join(input_folder, filename), 'r', encoding='utf-8') as f:
                md_content = f.read()
                title = filename.replace('.md', '').replace('-', ' ')
                html_content = convert_md_to_html(md_content, title)
                # Add dir="auto" to relevant tags
                for tag in ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                    html_content = html_content.replace(f'<{tag}>', f'<{tag} dir="auto">')
                    html_content = html_content.replace(f'<{tag} ', f'<{tag} dir="auto" ')
            output_file = os.path.join(output_folder, filename.replace('.md', '.html'))
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(html_content)
    print(f'Generated {len(os.listdir(output_folder))} HTML files.')

if __name__ == '__main__':
    generate_blog()
