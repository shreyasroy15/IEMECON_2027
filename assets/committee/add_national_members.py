import re

members_data = """Ashwini Kumar Arya	Jawaharlal Nehru University, New Delhi
Taimoor Khan	NIT Silchar, India
Arvind Kumar	Motilal Nehru National Institute of Technology Allahabad, Prayagraj
Manjeet Kumar	DTU Delhi
Chandra Prakash	NIT, Kurukshetra, India
Utpal Garain	Indian Statistical Institute, Kolkata
Shyam Lal	National Institute of Technology Surathkal, India
Nand Kishore	HBTU, Kanpur, Uttar Pradesh
Vinay Kumar	MNNIT Allahabad
Sandeep Kumar Singh	MNNIT Allahabad
Rowdro Ghatak	National Institute of Technology Durgapur, India
Subrata Chattopadhyay	National Institute of Technical Teachers' Training and Research, Kolkata, India
Jitendra Bahadur Maurya	NIT Patna, India
Soumitra Kumar Mandal	National Institute of Technical Teachers' Training & Research, Kolkata, India
Vijay Janyani	Malaviya National Institute of Technology, Rajasthan, India
Seemanti Saha	NIT Patna"""

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

section_html = f"""        </div>
        <div class="committee-group">
            <h2>National Advisory Committee</h2>
            <div class="member-grid">
{cards_html}
            </div>
        </div>"""

file_path = "/home/shreyas/Projects/IEMECON_2027-main/assets/committee/advisory_committee.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

target = "        </div>\n    </section>"
replacement = section_html + "\n    </section>"

new_content = content.replace(target, replacement)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Added National Advisory Committee members successfully!")
