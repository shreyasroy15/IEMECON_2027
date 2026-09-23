import glob
import os

target_img = '<img src="https://lh3.googleusercontent.com/pw/AP1GczNjy2upmBvXuMtpEDItIe1GVmwYo2Galz4lXj2_FFDy6F45opy9qLOit_yxdoWpGLyCFgfu6I1MJScA2fqwRhwhYGFUflMTDm66xAP75blPSdXq1Ng0sOcYjSCpuWLsBmT3D3zYMIVtbQzgeeC1bkEu=w1024-h1024-s-no-gm?authuser=0" alt="Third logo" class="site-logo">'

html_files = glob.glob('/home/shreyas/Projects/IEMECON_2027-main/**/*.html', recursive=True)

modified_files = 0
for filepath in html_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if target_img in content:
            content = content.replace(target_img, '')
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            modified_files += 1
            print(f"Modified {filepath}")
    except Exception as e:
        print(f"Error on {filepath}: {e}")

print(f"Total files modified: {modified_files}")
