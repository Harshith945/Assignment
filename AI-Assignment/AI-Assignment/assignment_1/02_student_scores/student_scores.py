import requests
import matplotlib.pyplot as plt


API_URL = (
    "https://api.slingacademy.com/v1/sample-data/files/"
    "student-scores.json"
)

SUBJECTS = [
    "math_score",
    "history_score",
    "physics_score",
    "chemistry_score",
    "biology_score",
    "english_score",
    "geography_score",
]


def fetch_student_data() -> list[dict]:
    """Fetch student score data from a public JSON endpoint."""
    response = requests.get(API_URL, timeout=30)
    response.raise_for_status()
    data = response.json()

    # The endpoint is expected to return a JSON list.
    # This also handles a common wrapper such as {"data": [...]}.
    if isinstance(data, list):
        return data

    if isinstance(data, dict):
        if isinstance(data.get("data"), list):
            return data["data"]
        if isinstance(data.get("students"), list):
            return data["students"]

    raise ValueError("Unexpected API response format.")


def calculate_averages(students: list[dict]) -> list[dict]:
    """Calculate the average score across available subjects per student."""
    results = []

    for student in students:
        scores = [
            float(student[field])
            for field in SUBJECTS
            if field in student and student[field] is not None
        ]

        if not scores:
            continue

        name = (
            f"{student.get('first_name', '')} "
            f"{student.get('last_name', '')}"
        ).strip()

        results.append(
            {
                "name": name or f"Student {student.get('id', '')}",
                "average": sum(scores) / len(scores),
            }
        )

    return results


def plot_averages(results: list[dict], max_students: int = 15) -> None:
    """Create a bar chart for the first max_students records."""
    selected = results[:max_students]

    names = [item["name"] for item in selected]
    averages = [item["average"] for item in selected]

    plt.figure(figsize=(12, 6))
    plt.bar(names, averages)
    plt.xlabel("Students")
    plt.ylabel("Average Score")
    plt.title("Average Student Scores")
    plt.xticks(rotation=45, ha="right")
    plt.ylim(0, 100)
    plt.tight_layout()

    output_file = "student_average_scores.png"
    plt.savefig(output_file, dpi=150)
    print(f"Chart saved as: {output_file}")
    plt.show()


def main() -> None:
    try:
        students = fetch_student_data()
        results = calculate_averages(students)

        if not results:
            print("No valid student score records were found.")
            return

        overall_average = sum(
            item["average"] for item in results
        ) / len(results)

        print(f"Number of students processed: {len(results)}")
        print(f"Overall average student score: {overall_average:.2f}")

        for item in results[:10]:
            print(f"{item['name']}: {item['average']:.2f}")

        plot_averages(results)

    except requests.RequestException as exc:
        print(f"API request failed: {exc}")
    except (ValueError, TypeError, KeyError) as exc:
        print(f"Data processing error: {exc}")


if __name__ == "__main__":
    main()
