import os
import markdown2
import shutil
import re

google_anylitics = \
'''
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-C32LDMX65L"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){{dataLayer.push(arguments);}}
        gtag('js', new Date());

        gtag('config', 'G-C32LDMX65L');
    </script>
'''

def convert_md_to_html(md_content, title):
    html_content = markdown2.markdown(md_content, extras=[
        "fenced-code-blocks",
        "break-on-newline",
        "tables",
        "strike",
        "header-ids"
    ])
    template = f"""<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>{title}</title>
    <link rel="stylesheet" href="styles.css">
    {{{{{{google_anylitics}}}}}}
</head>
<body>
    {html_content}
</body>
</html>"""
    return template


def generate_blog(input_folder='posts', output_folder='public'):
    # Recreate the folder
    os.makedirs(output_folder, exist_ok=True)
    for filename in os.listdir(input_folder):
        if filename.endswith('.md'):
            with open(os.path.join(input_folder, filename), 'r', encoding='utf-8') as f:
                md_content = f.read()
                title = filename.replace('.md', '').replace('-', ' ')

                # First convert to HTML (let markdown2 handle markdown links)
                html_content = convert_md_to_html(md_content, title)
                
                # Now convert only raw URLs that aren't already in <a> tags
                def convert_raw_urls(html):
                    # Split HTML into parts that are inside <a> tags and parts that aren't
                    parts = []
                    last_end = 0
                    for match in re.finditer(r'<a\b[^>]*>.*?</a>', html, re.DOTALL):
                        # Add text before the <a> tag
                        parts.append(html[last_end:match.start()])
                        # Add the <a> tag itself (unchanged)
                        parts.append(match.group(0))
                        last_end = match.end()
                    # Add remaining text after last <a> tag
                    parts.append(html[last_end:])
                    
                    # Only convert URLs in non-<a> parts
                    url_pattern = r'(https?://[^\s<>"]+|www\.[^\s<>"]+)'
                    for i in range(len(parts)):
                        if not parts[i].startswith('<a'):
                            parts[i] = re.sub(
                                url_pattern,
                                lambda m: f'<a href="{m.group(0)}" target="_blank">{m.group(0)}</a>',
                                parts[i]
                            )
                    return ''.join(parts)
                
                html_content = convert_raw_urls(html_content)

                
                # Add dir="auto" to relevant tags
                for tag in ['p', 'a', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                    html_content = html_content.replace(f'<{tag}>', f'<{tag} dir="auto">')
                    html_content = html_content.replace(f'<{tag} ', f'<{tag} dir="auto" ')
                # put google analytics in the head
                html_content = html_content.replace("{{{google_anylitics}}}", google_anylitics)
            output_file = os.path.join(output_folder, filename.replace('.md', '.html'))
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(html_content)
    print(f'Generated {len(os.listdir(output_folder))} HTML files.')

def generate_pages_list(output_file="pages_list.txt"):
    # Specify the folder path
    folder_path = "public"
    # Get all files in the folder
    try:
        files = os.listdir(folder_path)
    except FileNotFoundError:
        print(f"Error: Folder '{folder_path}' not found.")
        return
    except PermissionError:
        print(f"Error: Permission denied when accessing '{folder_path}'.")
        return
    
    # Filter out directories (optional, remove if you want directories too)
    files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]
    
    # Write to output file
    with open(output_file, "w") as f:
        for file_name in files:
            f.write(file_name + "\n")
    
    print(f"Successfully saved {len(files)} file names to {output_file}")

if __name__ == '__main__':
    # Delete the output folder if it exists
    if os.path.exists('public'):
        shutil.rmtree('public')  # Removes folder and all contents

    # generate pages
    generate_blog("posts", "public")
    generate_blog("weeks", "public")

    # for shuffle
    generate_pages_list()