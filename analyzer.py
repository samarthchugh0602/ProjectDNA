import os


def count_lines(filepath):

    try:

        with open(
            filepath,
            "r",
            encoding="utf-8",
            errors="ignore"
        ) as file:

            return len(file.readlines())

    except:

        return 0


def analyze_project(files):

    total_lines = 0

    file_data = []

    language_counts = {}

    extension_map = {
        ".py": "Python",
        ".html": "HTML",
        ".css": "CSS",
        ".js": "JavaScript",
        ".cpp": "C++",
        ".c": "C",
        ".java": "Java",
        ".txt": "Text",
        ".md": "Markdown"
    }

    for file in files:

        lines = count_lines(file)

        total_lines += lines

        extension = os.path.splitext(file)[1]

        language = extension_map.get(
            extension,
            "Other"
        )

        language_counts[language] = (
            language_counts.get(language, 0) + lines
        )

        file_data.append(
            {
                "path": file,
                "lines": lines
            }
        )

    file_data.sort(
        key=lambda x: x["lines"],
        reverse=True
    )

    health_score = calculate_health_score(
        total_lines,
        len(files)
    )

    return {
        "files": len(files),
        "lines": total_lines,
        "languages": language_counts,
        "largest_files": file_data[:10],
        "health": health_score
    }


def calculate_health_score(
    total_lines,
    total_files
):

    score = 100

    if total_lines > 5000:
        score -= 10

    if total_lines > 10000:
        score -= 10

    if total_files < 3:
        score -= 15

    if total_files > 100:
        score -= 10

    return max(score, 0)