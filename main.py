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
    image_url = match_img.group(1) if match_img else '/assets/arashnm80.png'

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


def generate_blog(input_folder='posts', output_folder='public'):
    os.makedirs(output_folder, exist_ok=True)

    # Liste des fichiers .md uniquement
    md_files = [f for f in os.listdir(input_folder) if f.endswith('.md')]
    md_files.sort()  # Assure un ordre croissant (week-1254 -> week-1258)

    for i, filename in enumerate(md_files):
        with open(os.path.join(input_folder, filename), 'r', encoding='utf-8') as f:
            md_content = f.read()
            title = filename.replace('.md', '').replace('-', ' ')
            html_content = convert_md_to_html(md_content, title)

            # Conversion des URL brutes
            def convert_raw_urls(html):
                parts = []
                last_end = 0
                for match in re.finditer(r'<a\b[^>]*>.*?</a>', html, re.DOTALL):
                    parts.append(html[last_end:match.start()])
                    parts.append(match.group(0))
                    last_end = match.end()
                parts.append(html[last_end:])
                url_pattern = r'(https?://[^\s<>"]+|www\.[^\s<>"]+)'
                for j in range(len(parts)):
                    if not parts[j].startswith('<a'):
                        parts[j] = re.sub(
                            url_pattern,
                            lambda m: f'<a href="{m.group(0)}" target="_blank">{m.group(0)}</a>',
                            parts[j]
                        )
                return ''.join(parts)

            html_content = convert_raw_urls(html_content)

            # Ajout de dir="auto"
            for tag in ['p', 'a', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                html_content = html_content.replace(f'<{tag}>', f'<{tag} dir="auto">')
                html_content = html_content.replace(f'<{tag} ', f'<{tag} dir="auto" ')

            # Lien précédent/suivant pour les semaines
            if input_folder == "weeks":
                prev_link = ""
                next_link = ""

                if i > 0:
                    prev_file = md_files[i - 1].replace('.md', '')
                    prev_link = f'<button onclick="window.location.href=\'{prev_file}\'">← previous week</button>'

                if i < len(md_files) - 1:
                    next_file = md_files[i + 1].replace('.md', '')
                    next_link = f'<button onclick="window.location.href=\'{next_file}\'">next week →</button>'
                    

                nav_html = f'''
                <div style="display: flex; justify-content: space-between;">
                    <div>{prev_link}</div>
                    <div>{next_link}</div>
                </div>
                '''
                html_content = html_content.replace('</body>', f'{nav_html}\n</body>')

            # Intégrer Google Analytics
            html_content = html_content.replace("{{{google_anylitics}}}", google_anylitics)

            # Sauvegarde du fichier
            output_file = os.path.join(output_folder, filename.replace('.md', '.html'))
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(html_content)

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

if __name__ == '__main__':
    # Delete the output folder if it exists
    if os.path.exists('public'):
        shutil.rmtree('public')  # Removes folder and all contents

    # generate pages
    generate_blog("posts", "public")
    generate_blog("weeks", "public")

    # for shuffle
    generate_pages_list()