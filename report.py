from colorama import init

init()


def generate_report(data):

    print("\n")

    print("=" * 50)
    print("PROJECT DNA REPORT")
    print("=" * 50)

    print(f"Files Analysed : {data['files']}")
    print(f"Total Lines    : {data['lines']}")
    print(f"Health Score   : {data['health']}%")

    print("\nLanguages")

    total = sum(
        data["languages"].values()
    )

    for lang, count in data["languages"].items():

        percentage = (
            count / total
        ) * 100

        print(
            f"{lang:<12}"
            f"{percentage:.1f}%"
        )

    print("\nLargest Files")

    for item in data["largest_files"]:

        print(
            f"{item['lines']:>6} lines"
            f"  {item['path']}"
        )

    print("\nProject Status")

    score = data["health"]

    if score >= 90:
        print("Excellent")

    elif score >= 75:
        print("Good")

    elif score >= 50:
        print("Needs Improvement")

    else:
        print("Critical")