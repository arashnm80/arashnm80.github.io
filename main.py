import os
import markdown2
import shutil
import re
from weeks import generate_weeks_md

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
    # Trouver le premier H1 Markdown
    match = re.search(r'^# (.+)', md_content, re.MULTILINE)
    title = match.group(1).strip() if match else title

    html_content = markdown2.markdown(md_content, extras=[
        "fenced-code-blocks",
        "break-on-newline",
        "tables",
        "strike",
        "header-ids"
    ])

    # Extraire la première image <img src="...">
    match_img = re.search(r'<img[^>]+src="([^">]+)"', html_content)
    image_url = match_img.group(1) if match_img else '../assets/arashnm80.jpg'

    template = f"""<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>{title}</title>
    
    <!-- seo -->
    <meta property="og:site_name" content="Arash Nemat Zadeh">
    <meta property="og:title" content="{title}">
    <meta property="og:image" content="{image_url}">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:image" content="{image_url}">

    <link rel="stylesheet" href="styles.css">
    {{{{{{google_anylitics}}}}}}
</head>
<body>
    {html_content}
</body>
</html>"""
    return template


def read_markdown_files(input_folder):
    """Read markdown files from the specified folder."""
    md_files = [f for f in os.listdir(input_folder) if f.endswith('.md')]
    md_files.sort()
    return md_files


def convert_raw_urls(html):
    """Convert raw URLs in the HTML content to clickable links, ignoring those within iframe, meta, and img tags."""
    parts = []
    last_end = 0
    # Regex to find iframe, anchor, meta, and img tags
    for match in re.finditer(r'<a\b[^>]*>.*?</a>|<iframe\b[^>]*>.*?</iframe>|<meta\b[^>]*>|<img\b[^>]*>', html, re.DOTALL):
        parts.append(html[last_end:match.start()])
        parts.append(match.group(0))
        last_end = match.end()
    parts.append(html[last_end:])
    url_pattern = r'(https?://[^\s<>"]+|www\.[^\s<>"]+)'
    for j in range(len(parts)):
        if not parts[j].startswith('<a') and not parts[j].startswith('<iframe') and not parts[j].startswith('<meta') and not parts[j].startswith('<img'):
            parts[j] = re.sub(
                url_pattern,
                lambda m: f'<a href="{m.group(0)}" target="_blank">{m.group(0)}</a>',
                parts[j]
            )
    return ''.join(parts)


def add_dir_auto(html_content):
    """Add dir="auto" to specific HTML tags."""
    for tag in ['p', 'a', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
        html_content = html_content.replace(f'<{tag}>', f'<{tag} dir="auto">')
        html_content = html_content.replace(f'<{tag} ', f'<{tag} dir="auto" ')
    return html_content


def add_navigation_links(html_content, md_files, i):
    """Add previous and next navigation links for weekly posts."""
    prev_link = ""
    next_link = ""

    if i > 0:
        prev_file = md_files[i - 1].replace('.md', '')
        prev_link = f'<button onclick="window.location.href=\'{prev_file}\'">← previous</button>'

    if i < len(md_files) - 1:
        next_file = md_files[i + 1].replace('.md', '')
        next_link = f'<button onclick="window.location.href=\'{next_file}\'">next →</button>'

    nav_html = f'''
    <div style="display: flex; justify-content: space-between;">
        <div>{prev_link}</div>
        <div>{next_link}</div>
    </div>
    '''
    return html_content.replace('</body>', f'{nav_html}\n</body>')


def add_anchor_links(html_content):
    """Add anchor link icon to the left of each h2 and h3 header with id, outside the header text."""
    # Minimal SVG icon for anchor
    anchor_svg = '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" style="vertical-align:middle;fill:gray;"><path d="M13.2218 3.32234C15.3697 1.17445 18.8521 1.17445 21 3.32234C23.1479 5.47022 23.1479 8.95263 21 11.1005L17.4645 14.636C15.3166 16.7839 11.8342 16.7839 9.6863 14.636C9.48752 14.4373 9.30713 14.2271 9.14514 14.0075C8.90318 13.6796 8.97098 13.2301 9.25914 12.9419C9.73221 12.4688 10.5662 12.6561 11.0245 13.1435C11.0494 13.1699 11.0747 13.196 11.1005 13.2218C12.4673 14.5887 14.6834 14.5887 16.0503 13.2218L19.5858 9.6863C20.9526 8.31947 20.9526 6.10339 19.5858 4.73655C18.219 3.36972 16.0029 3.36972 14.636 4.73655L13.5754 5.79721C13.1849 6.18774 12.5517 6.18774 12.1612 5.79721C11.7706 5.40669 11.7706 4.77352 12.1612 4.383L13.2218 3.32234Z"/><path d="M6.85787 9.6863C8.90184 7.64233 12.2261 7.60094 14.3494 9.42268C14.7319 9.75083 14.7008 10.3287 14.3444 10.685C13.9253 11.1041 13.2317 11.0404 12.7416 10.707C11.398 9.79292 9.48593 9.88667 8.27209 11.1005L4.73655 14.636C3.36972 16.0029 3.36972 18.219 4.73655 19.5858C6.10339 20.9526 8.31947 20.9526 9.6863 19.5858L10.747 18.5251C11.1375 18.1346 11.7706 18.1346 12.1612 18.5251C12.5517 18.9157 12.5517 19.5488 12.1612 19.9394L11.1005 21C8.95263 23.1479 5.47022 23.1479 3.32234 21C1.17445 18.8521 1.17445 15.3697 3.32234 13.2218L6.85787 9.6863Z"/></svg>'
    import re
    def repl(match):
        tag, id_val, rest = match.group(1), match.group(2), match.group(3)
        anchor = f'<a href="#{id_val}" class="anchor-link" aria-label="Anchor link">{anchor_svg}</a>'
        return f'<{tag} dir="auto" id="{id_val}"{rest}>{anchor}'
    # Only add to h2 and h3 with id
    pattern = r'<(h[23]) dir="auto" id="([^"]+)"([^>]*)>'
    return re.sub(pattern, repl, html_content)

def add_copy_anchor_script(html_content):
    """Ajoute un script JS minimaliste pour copier le lien de l'ancre au clic sur l'icône."""
    script = '''<script>
    document.addEventListener('DOMContentLoaded', function() {
        document.querySelectorAll('.anchor-link').forEach(function(anchor) {
            anchor.addEventListener('click', function(e) {
                e.preventDefault();
                var url = window.location.origin + window.location.pathname + anchor.getAttribute('href');
                if (navigator.clipboard) {
                    navigator.clipboard.writeText(url);
                }
            });
        });
    });
    </script>'''
    return html_content.replace('</body>', f'{script}\n</body>')

def save_html_file(output_folder, filename, html_content):
    """Save the HTML content to a file."""
    output_file = os.path.join(output_folder, filename.replace('.md', '.html'))
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)


def generate_blog(input_folder='posts', output_folder='public'):
    os.makedirs(output_folder, exist_ok=True)
    md_files = read_markdown_files(input_folder)

    for i, filename in enumerate(md_files):
        with open(os.path.join(input_folder, filename), 'r', encoding='utf-8') as f:
            md_content = f.read()
            title = filename.replace('.md', '').replace('-', ' ')
            html_content = convert_md_to_html(md_content, title)

            html_content = convert_raw_urls(html_content)
            html_content = add_dir_auto(html_content)
            html_content = add_anchor_links(html_content)

            if input_folder == "weeks":
                html_content = add_navigation_links(html_content, md_files, i)

            html_content = html_content.replace("{{{google_anylitics}}}", google_anylitics)
            html_content = add_copy_anchor_script(html_content)

            save_html_file(output_folder, filename, html_content)

    print(f'Generated {len(md_files)} HTML files from {input_folder}.')

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

def generate_sitemap(pages_list_file="pages_list.txt", sitemap_file="sitemap.xml"):
    """Generate a sitemap.xml file based on the pages listed in pages_list.txt."""
    try:
        with open(pages_list_file, "r") as f:
            pages = f.readlines()
    except FileNotFoundError:
        print(f"Error: File '{pages_list_file}' not found.")
        return

    # Base URL for the sitemap
    base_url = "https://www.arashnm80.com/"

    # Start the XML structure
    sitemap_content = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
"""

    # Add each page to the sitemap
    for page in pages:
        page = page.strip()
        # Remove .html extension
        if page.endswith('.html'):
            page = page[:-5]
        sitemap_content += f"  <url>\n    <loc>{base_url}{page}</loc>\n  </url>\n"

    # Close the XML structure
    sitemap_content += "</urlset>"

    # Write the sitemap to a file
    with open(sitemap_file, "w") as f:
        f.write(sitemap_content)

    print(f"Sitemap generated and saved to {sitemap_file}.")

if __name__ == '__main__':
    # Delete the output folder if it exists
    if os.path.exists('public'):
        shutil.rmtree('public')  # Removes folder and all contents

    # generate weeks.md
    generate_weeks_md()

    # generate pages
    generate_blog("posts", "public")
    generate_blog("weeks", "public")
    generate_blog("custom-pages", "public")

    # for shuffle
    generate_pages_list()

    # Call the function to generate the sitemap
    generate_sitemap()