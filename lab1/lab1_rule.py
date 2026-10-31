def scholarship(marks, docs_verified, attendance_percentage, payment_status):
    if marks >= 70 and docs_verified == True and attendance_percentage >= 70 and payment_status == True:
        return "Review"
    else:
        return "Hold"


# Four case tests
cases = [
    ("Pass", 90, True, 79, True),
    ("Documents Failure", 75, False, 74, False),
    ("Attendance", 86, True, 65, True),
    ("Fee Payment", 76, True, 67, False),
]

for name, marks, docs_verified, attendance_percentage, payment_status in cases:
    result = scholarship(marks, docs_verified, attendance_percentage, payment_status)

    print(
        "Case:", name,
        "Marks:", marks,
        "Documents:", docs_verified,
        "Attendance:", attendance_percentage,
        "Fee Paid:", payment_status,
        "Result:", result
    )