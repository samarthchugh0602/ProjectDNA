from scanner import scan_project
from analyzer import analyze_project
from report import generate_report

print("=" * 50)
print("ProjectDNA")
print("=" * 50)

path = input("Enter project path: ").strip()

print("\nScanning project...")

files = scan_project(path)

if not files:
    print("No files found.")
    quit()

results = analyze_project(files)

generate_report(results)