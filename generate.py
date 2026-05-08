import csv
import os

# โครงสร้างหน้าเว็บ (Template)
template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{title} Salary in {location} 2026</title>
    <style>
        body {{ font-family: sans-serif; line-height: 1.6; max-width: 800px; margin: 0 auto; padding: 20px; background: #f4f4f4; }}
        .container {{ background: white; padding: 30px; border-radius: 10px; }}
        .ad-space {{ background: #eee; padding: 20px; margin: 20px 0; text-align: center; border: 1px dashed #ccc; }}
        h1 {{ color: #2c3e50; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="ad-space">AD SPACE 1</div>
        <h1>{title} Salary in {location}</h1>
        <p>Industry: {industry}</p>
        <p>Salary: <strong>{salary} USD</strong></p>
        <p>Experience: {exp}</p>
        <div class="ad-space">AD SPACE 2</div>
        <p>Required Skills: {skills}</p>
        <div class="ad-space">AD SPACE 3</div>
    </div>
</body>
</html>
"""

# สร้างโฟลเดอร์สำหรับเก็บหน้าเว็บ
if not os.path.exists('jobs'):
    os.makedirs('jobs')

# อ่านไฟล์ข้อมูลและสร้างหน้าเว็บ
with open('data.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # สร้างชื่อไฟล์จาก job_id
        filename = f"jobs/{row['job_id']}.html"
        
        # ใส่ข้อมูลลงใน Template
        content = template.format(
            title=row['job_title'],
            location=row['company_location'],
            industry=row['industry'],
            salary=row['salary_usd'],
            exp=row['experience_level'],
            skills=row['required_skills']
        )
        
        # บันทึกไฟล์
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

print("Successfully generated batch 1!")
