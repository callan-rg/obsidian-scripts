import os
import re

# Function to extract the numerical part of the filename for sorting
def extract_number(filename):
    match = re.search(r'!(\d+)', filename)
    return int(match.group(1)) if match else 0

# Get the absolute path of the current working directory
current_dir = os.path.abspath('.')

# Get the name of the current working directory
folder_name = os.path.basename(current_dir)

# Prepend the folder name to the output filename
output_file = f"{folder_name} Index.md"

# Gather all markdown files in the directory, excluding the output file
markdown_files = [f for f in os.listdir(current_dir) if f.endswith('.md') and not f.startswith(folder_name)]

# Sort files based on the number extracted from the filename
sorted_files = sorted(markdown_files, key=extract_number)

# Create or clear the output file
with open(output_file, 'w') as file_out:
    # Write a header or title for the index file if desired
    file_out.write(f"# Index of {folder_name}\n\n")

    # Write the sorted markdown links as an ordered list
    for fname in sorted_files:
        # Extract the class title from the filename
        title = fname[4:-3]  # Assumes the title starts at 4th character and ends before '.md'
        
        # Construct the markdown link
        markdown_link = f"1. [[{fname}|{title}]]\n"
        
        # Write the markdown link to the output file
        file_out.write(markdown_link)

print(f"Index file '{output_file}' has been created with links to markdown files in sorted order.")
