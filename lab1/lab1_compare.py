def symbolic(marks, documents_verified):
    return "Review" if documents_verified and marks >= 70 else "Hold"


def threshold(confidence_level):
    return "Review" if confidence_level >= 0.70 else "Hold"


test_cases = [
    ("complete_high", 82, True, 0.81),
    ("complete_low", 68, True, 0.74),
    ("incomplete_high", 91, False, 0.88),
    ("boundary", 70, True, 0.70)
]

print("Case | Symbolic | Threshold | Disagreement")

for case_name, student_marks, docs_status, probability_score in test_cases:
    symbolic_result = symbolic(student_marks, docs_status)
    threshold_result = threshold(probability_score)

    print(case_name, symbolic_result, threshold_result,
          symbolic_result != threshold_result, sep=" | ")