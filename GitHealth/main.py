from github import Github
from scoring import calculate_health_score
from scoring import beginner_friendly
from visualization import draw_score_chart
import os

TOKEN = "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"

g = Github(TOKEN)

repo_url = input("GitHub Repository URL: ").strip()

repo_path = repo_url.replace("https://github.com/", "")
repo_path = repo_path.replace(".git", "")

print(repo_path)

repo = g.get_repo(repo_path)


print("\n===== Repository Info =====")
print("Name:", repo.name)
print("Owner:", repo.owner.login)
print("Stars:", repo.stargazers_count)
print("Forks:", repo.forks_count)
print("Open Issues:", repo.open_issues_count)
print("Language:", repo.language)

score, strengths, weaknesses, checklist = calculate_health_score(repo)

print("\n===== Health Analysis =====")
print("Health Score:", score, "/100")

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)
draw_score_chart(score)

print("\n===== Checklist =====")
for item, passed in checklist:
    status = "✓" if passed else "✗"
    print(f"{status} {item}")

if beginner_friendly(repo):
    print("\nBeginner Friendly: Yes")
else:    print("\nBeginner Friendly: No")

print("\n===== Strengths =====")
for s in strengths:
    print("✓", s)

print("\n===== Weaknesses =====")
for w in weaknesses:
    print("✗", w)

report_path = os.path.join(os.path.dirname(__file__),
                           f"{repo.name}_report.txt")

with open(report_path, "w", encoding="utf-8") as f:
    f.write(f"Repository: {repo.name}\n")
    f.write(f"Owner: {repo.owner.login}\n")
    f.write(f"Stars: {repo.stargazers_count}\n")
    f.write(f"Forks: {repo.forks_count}\n")
    f.write(f"Health Score: {score}\n")
    f.write(f"Grade: {grade}\n")
    for strength in strengths:
        f.write(f"  O {strength}\n")
    for weakness in weaknesses:
        f.write(f"  X {weakness}\n")
        
    print(f"\nReport saved as {repo.name}_report.txt")