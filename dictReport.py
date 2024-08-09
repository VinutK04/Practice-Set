students = [
    {
        "name": "Alice",
        "age": 20,
        "grades": {
            "math": 90,
            "science": 85,
            "literature": 88
        }
    },
    {
        "name": "Bob",
        "age": 22,
        "grades": {
            "math": 75,
            "science": 80,
            "literature": 78
        }
    }
]

result = {}

for student in students:
    average_grade = sum(student['grades'].values()) / len(student["grades"])
    student_infor = {
        "average_grade": round(average_grade, 2),
        "age": student['age']
    }
    result[student["name"]] = student_infor

for key, value in result.items():
    print(key, value)
