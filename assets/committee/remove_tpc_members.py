import re
import sys

raw_list = """Aaditeshwar Seth	IIT Delhi, India
3	Abdul Gafur Shaik	IIT Jodhpur, India
4	Abhay Sharma	Central University of Rajasthan, India
5	Afaq Ahmed	Sultan Qaboos University, Muscat, Oman
6	Akash Gupta	LNMIIT, India
7	Akash Tayal	IG Technical University for Women, India
8	Alberto Macii	Politecnico di Torino, Italy
9	Al-Sakib Khan Pathan	Southeast University, Bangladesh
10	Ambrish Kumar	Bennett University, India
11	Amer Al-Hinai	Sultan Qaboos University, Oman
12	Anh V. Dinh	University of Saskatchewan, Canada
13	Anjali Priya	University of Hyderabad, India
14	Ashish Mathur	IIT Jodhpur, India
15	Ashok Kaushal	Concordia University, Canada
16	Asish Kumar Mukhopadhyay	Kingston Educational Institution, India
17	Ayaz Chowdhury	Monash University, Malaysia
18	Bardella Paolo	Politecnico di Torino, Italy
19	Behrad Khamesee	University of Waterloo, Canada
20	C.K. Seth	University of Delhi, India
21	Chi-Guhn Lee	University of Toronto, Canada
22	D. Mondal	National Institute of Technology Durgapur, India
23	Detlef Streitferdt	Ilmenau University of Technology, Germany
24	Dipta Mukherjee	University of Engineering & Management, India
25	Erjong Manee	Kasetsart University, Thailand
26	Evangelos Yfantis	University of Nevada, Las Vegas, USA
27	Fabrizio Amarilli	Fondazione Politecnico di Milano, Italy
28	Faical Mnif	Sultan Qaboos University, Oman
29	G.S. Taki	Institute of Engineering and Management, India
30	Ganapati Panda	IIT Bhubaneswar, Orissa, India
31	Gunasekaran Thangavel	Higher College of Technology, Oman
32	Hassan Abdel Halem Hassan Yousef	Sultan Qaboos University, Oman
33	Huma Shankar S TM	Higher College of Technology, Oman
34	Huzur Saran	IIT Delhi, India
35	Ian Yellowley	University of British Columbia, Canada
36	Ichikawa Norimitsu	Kogakuin University, Japan
37	Indranath Sarkar	JIS College of Engineering, Kalyani, India
38	Indraneel Basu	Institute of Engineering and Management, India
39	Jalal Ahamed	University of Windsor, Canada
40	James Yu	University of British Columbia Okanagan, Canada
41	Jan Huissoon	University of Waterloo, Canada
42	K. Kannan	Nagaland University, Zunheboto, Nagaland, India
43	Kamran Behdinan	University of Toronto, Canada
44	Krerk Piromsopa	Chulalongkorn University, Thailand
45	Kyriakos G. Vamvoudakis	Virginia Tech, USA
46	Lipo Wang	Nanyang Technological University, Singapore
47	Lunchakorn Wuttisittikulkij	Chulalongkorn University, Thailand
48	Mahmoud Ibrahim Masoud	Sultan Qaboos University, Oman
49	Mainak Saha	Institute of Engineering and Management, India
50	Malay Gangopadhyay	Institute of Engineering and Management, India
51	Malleswara Talla	Concordia University, Canada
52	Manu Gupta	Arya College, Jaipur, India
53	Manu Pratap Singh	B R Ambedkar University, Agra, India
54	María de los Ángeles Martín	Universidad Nacional de La Pampa, Argentina
55	Marjit Singh	NERIST, AP, India
56	Mark Ng	Monash University, Canada
57	Martin Marciszack	UTN Córdoba, Argentina
58	Maya Ramanath	IIT Delhi, India
59	Md. Rabiul Islam	Rajshahi University of Engineering and Technology (RUET), Bangladesh
60	Mehrdad Radji Kermani	Western University, Canada
61	MELLAL Mohamed Arezki	M'Hamed Bougara University, Algeria
62	Michele Bonnin	Politecnico di Torino, Italy
63	Miriam Capretz	Western University, Canada
64	Mohamed Hisham Jaward	Monash University, Malaysia
65	Mohamed Wahab Mohamed Ismail	Ryerson University, Canada
66	Mohammad Shamim Akhter	Rajshahi University of Engineering and Technology (RUET), Bangladesh
67	Mohammed Albadi	Sultan Qaboos University, Oman
68	Mohammed Beit-Suwailam	Sultan Qaboos University, Oman
69	Nand Kishore	HBT University, Kanpur, India
70	Natawut Nupairoj	Chulalongkorn University, Thailand
71	Nico F. Declercq	Georgia Institute of Technology, U.S.A
72	Nilotpal Halder	JIS College of Engineering, Kalyani, India
73	Nityananda Sarma	Tezpur University, Assam, India
74	P S Rathore	AIR, Indore, India
75	P. M. Khiller	NIT, Rourkela, Orissa, India
76	Parul Agrawal	Jamia Hamdard University, Delhi, India
77	Parveen Kumar	ASET, AUUP, India
78	Pasumpon Panidan	Vaigai College of Engineering, Madurai, India
79	Patha P. Bhattacharya	Mody University, Sikar, India
80	Pawan K. Sharma	Kurukshetra University, India
81	Pawan Kumar Jha	Purbanchal University, Biratnagar, Nepal
82	Phumin Kirawanich	Mahidol University, Thailand
83	Pooja Gupta	LPU, Punjab, India
84	Pornchai Chanyagorn	Mahidol University, Thailand
85	Prabhat Kumar	Galgotias University, Greater Noida, India
86	Pradeep Bedi	Swami Himalayam University, India
87	Prasanna Venkatesan	SNS College of Engineering, Coimbatore, India
88	Prashant Lakkadwala	Acropolis Technical Campus, Indore, India
89	Prem Kumar Singh	AIIT, AUUP, Noida, India
90	Prerna Mahajan	IITM Janak Puri, New Delhi, India
91	Priti Narwal	MRIU, Faridabad, India
92	Prof. Bansibadan Maji	National Institute of Technology, Durgapur, India
93	Qiao Sun	University of Calgary, Canada
94	Ram S. Sharma	IIT-BHU, India
95	Raman Singh	Monash University, Australia
96	Ratna Chakrabarti	Institute of Engineering and Management, India
97	Ravi Goyal	Bharatiya Skill Development University, Jaipur, India
98	Rohit Singh	MIET, India
99	Sagarika Ghosh	University of Engineering & Management, India
100	Saman Hassan Zadeh Amin	Ryerson University, Canada
101	Sandip Kumar Chaurasiya	University of Petroleum and Energy Studies, Dehradun, India
102	Sanjay Sharma	Thapar University, India
103	Santosh Kumar	Kumaun University, India
104	Saradindu Panda	Narula Institute of Technology Kolkata, India
105	Satyendra Sharma	Modern Institute of Technology, India
106	Sergio Bittanti	Politecnico di Torino, Italy
107	Shashikant Sheoran	Thapar Institute of Engineering and Technology, Patiala, India
108	Sheng-Hui Wang	National Research Council Canada
109	Shyam Akashe	ITM University, Gwalior, India
110	Soumava Mukherjee	IIT Jodhpur, India
111	Sourav Saha	Institute of Engineering and Management, India
112	Souvik Pal	Elitte College of Engineering, West Bengal, India
113	Srinivasa Rao	K L University, Andhra Pradesh, India
114	Steven Y. Liang	Georgia Institute of Technology, U.S.A
115	Subhajit Ghosh	Galgotias University, Greater Noida, India
116	Subhash Chand Gupta	AUUP, Noida, India
117	Sudan Jha	KIIT, Bhubaneswar, India
118	Sudarshon Nandi	BITM, WB, India
119	Suman Katiyal	Devi Ahilya Viswavidyalay, Indore, India
120	Suman Mann	MSI Janakpuri, India
121	Sumanta Chatterjee	JISCE WB, India
122	Sumathy Eswaran	Dr. MGR University, Chennai, India
123	Sunita Adhikari	Jadavpur University, Kolkata, WB, India
124	Sunita Chauhan	Monash University, Canada
125	Supavadee Aramvith	Chulalongkorn University, Thailand
126	Supriya Chakroborty	Amity University Kolkata, West Bengal, India
127	Surachoke Thanapitak	Mahidol University, Thailand
128	Surbhi Jain	MDU, Rohtak, India
129	Sushil Kumar	Galgotia University, Noida, India
130	Sushila Madan	LASR, University of Delhi, India
131	Syed Zakir Ali	Middle East College, Oman
132	Tanupriya Choudhury	University of Petroleum and Energy Studies, Dehradun, India
133	Tapas Kumar	Lingaya's University, Faridabad, India
134	Tariq Jamil	Sultan Qaboos University, Oman
135	Tarun Kumar	IITM, Delhi, India
136	Thanaphong Thanasaksiri	Chiang Mai University, Thailand
137	Uday Pratap	Madhav Institute of Technology & Science, Gwalior, India
138	Urmila Bhanja	IGIT Sarang, Orissa, India
139	V Srikanth	KL University, Green Fields, Vaddeswaram, India
140	Valentina Emilia Balas	Aurel Vlaicu University, Romania
141	Varun Kumar Ojha	VSB Technical University of Ostrava, Ostrava, Czech Republic
142	Velmani Ramasamy	Woldia University, Ethiopia
143	Vijay Kr. Khurana	MAIMS, Delhi, India
144	Vinay Joseph Ribeiro	IIT Delhi, India
145	Vipin Tyagi	Jaypee University of Engg. & Technology, India
146	Vipul A. Shah	Dharmsingh Desai University, Gujarat, India
147	Vishal Dattana	Middle East College, Muscat, Oman
148	Vishal Jain	Bharatiya Vidyapeeth, New Delhi, India
149	Vishal Naranje	BITS Pilani, India
150	Vivek Kumar	DCTM Palwal, Haryana, India
151	Vivek Kumar Singh	Banaras Hindu University, India
152	Vivek Rajput	VIT Vellore, India
153	Wang Xin	Monash University, Canada
154	Watchara Pong Khovidhungij	Chulalongkorn University, Thailand
155	Xudong Zhao	Dalian University of Technology, China"""

names_to_remove = []
for line in raw_list.split('\n'):
    if not line.strip(): continue
    parts = line.split('\t')
    if len(parts) >= 2:
        # Check if the first part is a number and a name
        first_part = parts[0].strip()
        match = re.match(r'^(\d+)\s+(.+)$', first_part)
        if match:
            names_to_remove.append(match.group(2).strip())
        else:
            names_to_remove.append(first_part)

# Also handle case-insensitive or slight spacing differences
names_to_remove = [n.lower() for n in names_to_remove]

file_path = "/home/shreyas/Projects/IEMECON_2027-main/assets/committee/technical_program_committee.html"

try:
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    new_lines = []
    removed = 0
    for line in lines:
        if '<td class="s-no">' in line and '<td class="member-name">' in line:
            # Extract the name from the line to check
            match = re.search(r'<td class="member-name">(.*?)</td>', line)
            if match:
                member_name = match.group(1).strip().lower()
                should_remove = False
                for n in names_to_remove:
                    if n in member_name or member_name in n:
                        should_remove = True
                        break
                if should_remove:
                    removed += 1
                    continue
        new_lines.append(line)
        
    with open(file_path, "w", encoding="utf-8") as f:
        f.writelines(new_lines)
    print(f"Removed {removed} rows.")
except Exception as e:
    print(f"Error: {e}")

