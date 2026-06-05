# ============================================================
# bias_analyzer.py
# Student Performance Pattern Analyzer
# Modified and personalized by: Mahshid Alam
# Original code generated with assistance from Claude AI
# Date: May 27, 2026
# Course: Software Systems Capstone - CPSC 49200
# ============================================================
# MODIFICATIONS MADE:
# 1. Changed subjects to actual CS courses
# 2. Added GPA converter (4.0 scale)
# 3. Added class ranking system
# 4. Added color-coded pass/fail system
# ============================================================

import numpy as np

# ── ANSI Color Codes for terminal output ───────────────────
GREEN  = "\033[92m"   # Pass / High performer
YELLOW = "\033[93m"   # Warning / Below average
RED    = "\033[91m"   # Fail / At risk
BLUE   = "\033[94m"   # Headers
RESET  = "\033[0m"    # Reset to default color

# ── STEP 1: Define student grade data ──────────────────────
# Each row = one student
# Each column = one subject
student_grades = np.array([
    [95, 92, 88, 90],   # Student 1
    [78, 75, 80, 72],   # Student 2
    [55, 60, 58, 52],   # Student 3
    [90, 88, 85, 91],   # Student 4
    [65, 70, 60, 68],   # Student 5
    [82, 79, 84, 80],   # Student 6
    [45, 50, 48, 42],   # Student 7 - below passing
    [88, 91, 87, 89],   # Student 8
])

# Modified: Changed to actual CS department courses
subjects = [
    "Discrete Math",
    "Linear Algebra",
    "Software System Capstone",
    "Theory of Algorithms"
]

num_students = student_grades.shape[0]
PASSING_GRADE = 60  # Minimum passing grade

# ── GPA Converter Function ──────────────────────────────────
# Modified: Added GPA conversion on 4.0 scale
def convert_to_gpa(average):
    if average >= 94: return 4.0
    elif average >= 90: return 3.7
    elif average >= 87: return 3.3
    elif average >= 84: return 3.0
    elif average >= 80: return 2.7
    elif average >= 77: return 2.3
    elif average >= 74: return 2.0
    elif average >= 70: return 1.7
    elif average >= 67: return 1.3
    elif average >= 64: return 1.0
    elif average >= 60: return 0.7
    else: return 0.0

print(f"{BLUE}{'=' * 58}")
print("     STUDENT PERFORMANCE PATTERN ANALYZER")
print(f"     CS Department — Spring 2026")
print(f"{'=' * 58}{RESET}")

# ── STEP 2: Calculate averages per student ──────────────────
student_averages = np.mean(student_grades, axis=1)

# Modified: Added class ranking (sorted highest to lowest)
ranked_indices = np.argsort(student_averages)[::-1]

print(f"\n{BLUE}📊 CLASS RANKING (Highest to Lowest):{RESET}")
print("-" * 58)
print(f"  {'Rank':<6} {'Student':<12} {'Average':<10} {'GPA':<8} {'Status'}")
print("-" * 58)

for rank, idx in enumerate(ranked_indices):
    avg = student_averages[idx]
    gpa = convert_to_gpa(avg)

    # Modified: Color coded status
    if avg >= 85:
        status = f"{GREEN}✔ High Performer{RESET}"
        color = GREEN
    elif avg >= 70:
        status = f"{GREEN}→ Passing{RESET}"
        color = GREEN
    elif avg >= 60:
        status = f"{YELLOW}⚠ Below Average{RESET}"
        color = YELLOW
    else:
        status = f"{RED}✘ FAILING{RESET}"
        color = RED

    print(f"  {rank+1:<6} {f'Student {idx+1}':<12} "
          f"{color}{avg:<10.1f}{RESET} "
          f"{color}{gpa:<8.1f}{RESET} {status}")

# ── STEP 3: Subject averages ────────────────────────────────
subject_averages = np.mean(student_grades, axis=0)
print(f"\n{BLUE}📚 SUBJECT AVERAGES:{RESET}")
print("-" * 58)
for subject, avg in zip(subjects, subject_averages):
    if avg >= 75:
        color = GREEN
    elif avg >= 65:
        color = YELLOW
    else:
        color = RED
    print(f"  {subject:<30} {color}{avg:.1f}{RESET}")

strongest = subjects[np.argmax(subject_averages)]
weakest   = subjects[np.argmin(subject_averages)]
print(f"\n  {GREEN}✔ Strongest Subject: {strongest}{RESET}")
print(f"  {RED}✘ Weakest Subject:   {weakest}{RESET}")

# ── STEP 4: Pass/Fail Report ────────────────────────────────
# Modified: Color coded pass/fail per student per subject
print(f"\n{BLUE}🚦 PASS/FAIL REPORT (Passing grade: {PASSING_GRADE}):{RESET}")
print("-" * 58)
header = f"  {'Student':<12}"
for s in subjects:
    header += f"{s[:10]:<13}"
print(header)
print("-" * 58)

for i, grades in enumerate(student_grades):
    row = f"  {f'Student {i+1}':<12}"
    for grade in grades:
        if grade >= PASSING_GRADE:
            row += f"{GREEN}{grade:<13}{RESET}"
        else:
            row += f"{RED}{grade:<13}{RESET}"
    print(row)

# ── STEP 5: Eigenvalue analysis ─────────────────────────────
covariance_matrix = np.cov(student_grades.T)
eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)

print(f"\n{BLUE}🔍 EIGENVALUE ANALYSIS (Subject Correlation Patterns):{RESET}")
print("-" * 58)
print("  Eigenvalues show which patterns explain the most")
print("  variation in student performance across subjects.")
print()
for i, val in enumerate(eigenvalues):
    print(f"  Pattern {i+1}: {val:.2f}")

dominant = np.argmax(eigenvalues)
print(f"\n  {GREEN}→ Dominant Pattern: Pattern {dominant+1}{RESET}")
print(f"    This pattern explains the most variation")
print(f"    in student performance across all subjects.")

# ── STEP 6: Bias warning ─────────────────────────────────────
print(f"\n{YELLOW}⚠  BIAS AWARENESS NOTE:{RESET}")
print("-" * 58)
print("  This tool finds patterns in whatever data it receives.")
print("  If the input data reflects historical bias (e.g.")
print("  students from under-resourced schools scoring lower),")
print("  the algorithm will treat that bias as truth and")
print(f"  amplify it -- exactly as described in:")
print(f"  {RED}'Weapons of Math Destruction' by Cathy O'Neil.{RESET}")
print(f"  {RED}Code is not neutral. Data is not neutral.{RESET}")
print(f"  {RED}Whoever designs the model holds the power.{RESET}")
print(f"{BLUE}{'=' * 58}{RESET}")