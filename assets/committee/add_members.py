import re

members_data = """Sourav Kumar Mukhopadhyay	Augusta University, Georgia, USA
Sesha Srinivasan	Florida Polytechnic University, Lakeland, Florida, USA
Lakshman S. Tamil	University of Texas at Dallas, USA
M. Shamim Kaiser	Jahangirnagar University, Savar, Dhaka
Ramani Kannan	Universiti Teknologi PETRONAS, Malaysia
Fumio Kodama	University of Tokyo, Japan
Bettina Von Stamm	London Business School, UK
Hari Reehal	London South Bank University, UK
Vasudevan Lakshminarayanan	University of Waterloo, Canada
Otani Yukitoshi	Utsunomiya University, Japan
Brian Culshaw	Southampton University, UK
Rainer Tutsch	Institute of Production Measurement Technology, Germany
Hyuang suck Cho	Korea Advance Institute of Science & Technology, Korea
Yu-Lung Lo	National Cheng Kung University, Taiwan
Dipak C. Jain	Chulalongkorn University, Bangkok, Thailand
Lalit Kumar Goel	Nanyang Technological University, Singapore
Anandarup Mukherjee	University of Cambridge, U.K"""

def get_initials(name):
    parts = name.strip().split()
    if len(parts) >= 2:
        return (parts[0][0] + parts[-1][0]).upper()
    elif len(parts) == 1:
        return parts[0][:2].upper()
    return "NA"

html_cards = []
for line in members_data.split('\n'):
    if not line.strip(): continue
    parts = line.split('\t')
    if len(parts) == 2:
        name, affiliation = parts
    else:
        name = line
        affiliation = ""
        
    initials = get_initials(name)
    card = f"""                <div class="member-card">
                    <div class="member-photo advisor-avatar"><span>{initials}</span></div>
                    <h3 class="member-name">{name.strip()}</h3>
                    <p class="member-org">{affiliation.strip()}</p>
                </div>"""
    html_cards.append(card)

cards_html = '\n'.join(html_cards)

file_path = "/home/shreyas/Projects/IEMECON_2027-main/assets/committee/advisory_committee.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

target = """            <h2>International Advisory Committee</h2>
            <div class="member-grid">"""

replacement = target + "\n" + cards_html

new_content = content.replace(target, replacement)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Added members successfully!")
