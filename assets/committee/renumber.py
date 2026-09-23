import re

file_path = "/home/shreyas/Projects/IEMECON_2027-main/assets/committee/technical_program_committee.html"

with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

new_lines = []
counter = 1
for line in lines:
    if '<td class="s-no">' in line:
        line = re.sub(r'<td class="s-no">\d+</td>', f'<td class="s-no">{counter}</td>', line)
        counter += 1
    new_lines.append(line)

with open(file_path, "w", encoding="utf-8") as f:
    f.writelines(new_lines)
print(f"Renumbered {counter - 1} rows.")
