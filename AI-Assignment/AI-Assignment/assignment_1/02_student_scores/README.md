# 2. Student Score Processing and Visualization

This program fetches a student-score dataset from a public JSON endpoint,
calculates each student's average across the available subjects, prints
the overall average, and creates a Matplotlib bar chart.

The public dataset contains fields such as math, history, physics,
chemistry, biology, English and geography scores.

## Run

```bash
pip install -r requirements.txt
python assignment_1/02_student_scores/student_scores.py
```

The chart is saved as `student_average_scores.png`.
