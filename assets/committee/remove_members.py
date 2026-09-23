import re
import sys

names_to_remove = [
    "Abdulla Al-Badi", "Anoop Chawla", "Anshul Kumar", "Abheek Gupta", 
    "Bahni Ray", "Debabrata Dasgupta", "G.S.Taki", "H. R. Vishwakarma", 
    "Hari Krishna Kuruva", "Indrasen Singh", "K. P. Ghatak", "Malay Gangopadhyaya", 
    "M. Ravi Shankar", "M. S. Prasad Babu", "Madan Gupta", "Mahesh Kumar", 
    "Prabhat Singh", "Ratna Chakrabarty", "S. K. Ghorai", "S. Pandey", 
    "Samrat Saha", "Sangjukta Das", "Soumya Sen", "Tahir I. Khan", 
    "Vinod Shukla", "Yang Jiaqiang"
]

files_to_check = [
    "/home/shreyas/Projects/IEMECON_2027-main/assets/committee/organizing_committee.html",
    "/home/shreyas/Projects/IEMECON_2027-main/assets/committee/advisory_committee.html",
    "/home/shreyas/Projects/IEMECON_2027-main/assets/committee/technical_program_committee.html"
]

for file_path in files_to_check:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        
        new_lines = []
        removed = 0
        for line in lines:
            should_remove = False
            for name in names_to_remove:
                if name in line:
                    should_remove = True
                    removed += 1
                    break
            
            if not should_remove:
                new_lines.append(line)
        
        if removed > 0:
            with open(file_path, "w", encoding="utf-8") as f:
                f.writelines(new_lines)
            print(f"Removed {removed} lines from {file_path}")
        else:
            print(f"No matches found in {file_path}")
            
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
