import os
import markdown
import shutil
import re

def convert_md_to_html(md_content, title):
    html_content = markdown.markdown(md_content)
    template = f"""<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>{title}</title>
    <link rel="stylesheet" href="styles.css">
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
                html_content = convert_md_to_html(md_content, title)
                # URL regex pattern
                url_pattern = r'(https?://[^\s<>"]+|www\.[^\s<>"]+)'
                # Replace URLs with hyperlinks
                html_content = re.sub(url_pattern, r'<a href="\1" target="_blank">\1</a>', html_content)
                # Add dir="auto" to relevant tags
                for tag in ['p', 'a', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                    html_content = html_content.replace(f'<{tag}>', f'<{tag} dir="auto">')
                    html_content = html_content.replace(f'<{tag} ', f'<{tag} dir="auto" ')
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