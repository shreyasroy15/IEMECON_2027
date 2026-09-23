import re

file_path = "/home/shreyas/Projects/IEMECON_2027-main/assets/gallery.html"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Match the specific image tag for the Third logo across multiple lines
new_content = re.sub(r'<img[^>]+alt="Third logo"[^>]*>', '', content)

if content != new_content:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Modified gallery.html")
else:
    print("No changes made.")
