import os

SUPPORTED_EXTENSIONS = {
    ".py",
    ".html",
    ".css",
    ".js",
    ".cpp",
    ".c",
    ".java",
    ".txt",
    ".md"
}


def scan_project(folder):

    collected = []

    for root, dirs, files in os.walk(folder):

        dirs[:] = [
            d for d in dirs
            if d not in {
                ".git",
                "__pycache__",
                "venv",
                ".venv",
                "node_modules"
            }
        ]

        for file in files:

            extension = os.path.splitext(file)[1]

            if extension in SUPPORTED_EXTENSIONS:

                full_path = os.path.join(root, file)

                collected.append(full_path)

    return collected