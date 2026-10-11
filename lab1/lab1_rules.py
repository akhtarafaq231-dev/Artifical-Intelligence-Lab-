"""Lab 1 - Task 2: Modified Rule-Based Scholarship Evaluation.

All thresholds and rules are synthetic lab assumptions.
"""


def scholarship_evaluation(score, document_complete,
                           experience_years, background_check):
    if not document_complete:
        return "Hold", "Documents are incomplete."
    elif score < 70:
        return "Hold", "Score is below 70."
    elif experience_years < 2:
        return "Hold", "Experience is less than 2 years."
    elif not background_check:
        return "Hold", "Background check failed."
    else:
        return "Review", "All conditions passed."


test_cases = [
    ("Case 1 - Pass", 85, True, 3, True, "Review"),
    ("Case 2 - Experience Failure", 80, True, 1, True, "Hold"),
    ("Case 3 - Background Failure", 90, True, 4, False, "Hold"),
    ("Case 4 - Threshold Boundary", 70, True, 2, True, "Review"),
]

print("CASE | INPUT | EXPECTED | ACTUAL | TEST | REASON")
print("-" * 90)
for name, score, complete, exp, bg, expected in test_cases:
    actual, reason = scholarship_evaluation(score, complete, exp, bg)
    print(
        f"{name} | "
        f"Score={score}, Documents={complete}, "
        f"Experience={exp}, Background={bg} | "
        f"{expected} | {actual} | "
        f"{'PASS' if actual == expected else 'FAIL'} | "
        f"{reason}"
    )
