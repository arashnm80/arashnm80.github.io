import os

def generate_weeks_md(output_file="custom-pages/weeks.md"):
    """Generate a weeks.md file with week files in descending order."""
    folder_path = "weeks"
    try:
        files = os.listdir(folder_path)
    except FileNotFoundError:
        print(f"Error: Folder '{folder_path}' not found.")
        return
    except PermissionError:
        print(f"Error: Permission denied when accessing '{folder_path}'.")
        return
    
    # Filter week files and extract week numbers for sorting
    week_files = []
    for f in files:
        if f.startswith("week-") and f.endswith(".md"):
            # Extract week number for sorting
            week_num = f.replace("week-", "").replace(".md", "")
            try:
                week_files.append((int(week_num), f))
            except ValueError:
                continue
    
    # Sort by week number in descending order
    week_files.sort(key=lambda x: x[0], reverse=True)
    
    # Write to markdown file
    with open(output_file, "w") as f:
        f.write("# weeks\n")
        for week_num, filename in week_files:
            page_name = filename.replace(".md", "")
            f.write(f"- [{page_name}]({page_name})\n")
    
    print(f"Successfully saved {len(week_files)} week files to {output_file}")