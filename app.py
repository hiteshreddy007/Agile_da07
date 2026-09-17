students = [
    {"name": "Alice Johnson", "id": "STU001", "gpa": 3.8, "status": "Pass"},
    {"name": "Bob Smith", "id": "STU002", "gpa": 2.9, "status": "Pass"},
    {"name": "Charlie Brown", "id": "STU003", "gpa": 1.7, "status": "Probation"},
    {"name": "Diana Prince", "id": "STU004", "gpa": 3.9, "status": "Pass"}
]

# Calculate metrics
total_students = len(students)
avg_gpa = sum(s["gpa"] for s in students) / total_students
probation_count = sum(1 for s in students if s["status"] == "Probation")

# Write the build artifact report
with open("report.txt", "w") as f:
    f.write("=== STUDENT ACADEMIC PERFORMANCE REPORT (CHANGED Report)===\n")
    f.write(f"Total Records Processed: {total_students}\n")
    f.write(f"Average Institutional GPA: {avg_gpa:.2f}\n")
    f.write(f"Students on Academic Probation: {probation_count}\n\n")
    
    f.write("Detailed Roster:\n")
    for s in students:
        f.write(f"- {s['id']} | {s['name']} | GPA: {s['gpa']} | Status: {s['status']}\n")

print("Report generated.")
