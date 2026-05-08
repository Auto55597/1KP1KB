import csv
import os

# โครงสร้างหน้าเว็บแบบบทความยาว (SEO Friendly)
template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} Salary Guide in {location} - 1KP1KB</title>
    <style>
        body {{ font-family: 'Segoe UI', sans-serif; line-height: 1.7; max-width: 800px; margin: 0 auto; padding: 20px; color: #333; background: #f9f9f9; }}
        .container {{ background: white; padding: 40px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); }}
        .ad-space {{ background: #f0f0f0; padding: 25px; margin: 25px 0; text-align: center; border: 2px dashed #ddd; color: #999; font-weight: bold; }}
        h1 {{ color: #2c3e50; border-bottom: 3px solid #10b981; padding-bottom: 10px; }}
        h2 {{ color: #2980b9; margin-top: 30px; }}
        .salary-tag {{ font-size: 24px; color: #e67e22; font-weight: bold; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="ad-space">TOP BANNER AD</div>

        <h1>{title} Career and Salary Insights in {location} (2026)</h1>
        
        <p>The role of a <strong>{title}</strong> in the <strong>{industry}</strong> industry has seen significant growth. As companies in {location} continue to evolve, the demand for high-skilled professionals is at an all-time high.</p>

        <h2>Detailed Salary Breakdown</h2>
        <p>Current data indicates that the average annual compensation for a {title} with an experience level of <strong>{exp}</strong> is approximately:</p>
        <div class="salary-tag">{salary} USD per Year</div>

        <div class="ad-space">MID-CONTENT AD 1</div>

        <h2>Essential Skills & Qualifications</h2>
        <p>To succeed as a {title} in {location}, candidates are typically expected to master the following skill set:</p>
        <ul>
            <li>Core Skills: <strong>{skills}</strong></li>
        </ul>
        <p>Holding these certifications or expertise can significantly increase your bargaining power in the {industry} sector.</p>

        <div class="ad-space">MID-CONTENT AD 2</div>

        <h2>Industry Outlook</h2>
        <p>In 2026, the <strong>{industry}</strong> field is expected to integrate more automation and AI-driven processes. This shift makes the role of {title} more critical than ever before. Professionals who can bridge the gap between technical execution and business strategy will command the highest premiums in the market.</p>

        <div class="ad-space">FOOTER AD</div>
    </div>
</body>
</html>
"""

# ส่วนการสร้างโฟลเดอร์และไฟล์เหมือนเดิม...
if not os.path.exists('jobs'):
    os.makedirs('jobs')

with open('data.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        filename = f"jobs/{row['job_id']}.html"
        content = template.format(
            title=row['job_title'],
            location=row['company_location'],
            industry=row['industry'],
            salary=row['salary_usd'],
            exp=row['experience_level'],
            skills=row['required_skills']
        )
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
print("Successfully upgraded to article version!")

# ส่วนท้ายของไฟล์ generate.py (เพิ่มต่อจากเดิม)

# สร้างหน้าสารบัญ (Index of Jobs)
index_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>AI Job Directory - 1KP1KB</title>
    <style>
        body {{ font-family: sans-serif; padding: 40px; max-width: 800px; margin: 0 auto; }}
        h1 {{ color: #10b981; }}
        .job-link {{ display: block; padding: 10px; border-bottom: 1px solid #eee; text-decoration: none; color: #333; }}
        .job-link:hover {{ background: #f0f0f0; }}
    </style>
</head>
<body>
    <h1>AI Job Salary Directory (Batch 1)</h1>
    <div id="links">
        {links}
    </div>
</body>
</html>
"""

all_links = ""
# อ่านข้อมูลอีกรอบเพื่อสร้างลิงก์
with open('data.csv', mode='r', encoding='utf-8') as file:
    file.seek(0) # กลับไปเริ่มอ่านใหม่
    reader = csv.DictReader(file)
    for row in reader:
        # สร้างแท็ก <a> สำหรับแต่ละงาน
        all_links += f'<a class="job-link" href="jobs/{row["job_id"]}.html">{row["job_title"]} in {row["company_location"]}</a>\n'

# บันทึกเป็นไฟล์ list.html
with open('list.html', 'w', encoding='utf-8') as f:
    f.write(index_template.format(links=all_links))

print("Directory list.html created!")
