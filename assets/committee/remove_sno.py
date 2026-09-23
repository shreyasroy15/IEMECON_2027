import re

file_path = "/home/shreyas/Projects/IEMECON_2027-main/assets/committee/technical_program_committee.html"

try:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Remove the table header for S.No (case insensitive just in case, but usually S.No)
    content = re.sub(r'<th>S\.No</th>\s*', '', content, flags=re.IGNORECASE)
    
    # Remove the table data cells for s-no
    content = re.sub(r'<td class="s-no">\d+</td>\s*', '', content)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    print("S.NO column removed successfully.")
except Exception as e:
    print(f"Error: {e}")
