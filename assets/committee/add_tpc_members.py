import re

new_members_data = """A. P. Singh	Central University of Rajasthan, India
Aaditeshwar Seth	IIT Delhi, India
Alok Kumar Baranwal	NIT Manipur
Abdul Gafur Shaik	IIT Jodhpur, India
Abhay Sharma	GEHU, Dehradun, India
Ashish Mathur	IIT Jodhpur, India
Ashok Kaushal	Concordia University, Canada
Bardella Paolo	Politecnico di Torino, Italy
D. Mondal	National Institute of Technology Durgapur, India
Erjong manee	Kasetsart University, Thailand
Ganapati Panda	IIT, Bhubaneswar, Orissa, India
Jan Huissoon	University of Waterloo, Canada
Kamran Behdinan	University of Toronto, Canada
Lipo Wang	Nanyang Technological University, Singapore
Nico F. Declercq	Georgia Institute of Technology, U.S.A
P. M.Khiller	NIT, Rourkela, Orissa, India
Ram S. Sharma	IIT-BHU, India
Sandeep Vyas	JECRC Jaipur, India
Suman Samui	NIT Durgapur
Sumit Kundu	NIT Durgapur, Higher Administrative Grade, HAG
Vinay Joseph Ribeiro	IIT Delhi, India
Wang Xin	Monash University, Canada
Xudong Zhao	Dalian University of Technology, China
Yanxia Sun	University of Johannesburg, South Africa
Zhe Zhang	Technical University of Denmark, Denmark"""

html_rows = []
counter = 1
for line in new_members_data.split('\n'):
    if not line.strip(): continue
    parts = line.split('\t')
    if len(parts) == 2:
        name, affiliation = parts
    else:
        name = line
        affiliation = ""
        
    row = f'                    <tr><td class="s-no">{counter}</td><td class="member-name">{name.strip()}</td><td>{affiliation.strip()}</td></tr>'
    html_rows.append(row)
    counter += 1

rows_html = '\n'.join(html_rows)

file_path = "/home/shreyas/Projects/IEMECON_2027-main/assets/committee/technical_program_committee.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Find the empty tbody or the end of the existing tbody and inject it
# The previous script might have left <tbody>\n</tbody> or <tbody></tbody>
if "<tbody>" in content and "</tbody>" in content:
    # Just insert right after <tbody>
    target = "<tbody>"
    replacement = "<tbody>\n" + rows_html
    new_content = content.replace(target, replacement)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Added TPC members successfully!")
else:
    print("Could not find tbody in the file.")
