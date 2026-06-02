from github import Github

TOKEN = "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"

g = Github(TOKEN)

repo_url = input("GitHub Repository URL: ")

parts = repo_url.rstrip("/").split("/")

owner = parts[-2]
repo_name = parts[-1]

repo = g.get_repo(f"{owner}/{repo_name}")

print("\n===== Repository Info =====")
print("Name:", repo.name)
print("Owner:", repo.owner.login)
print("Stars:", repo.stargazers_count)
print("Forks:", repo.forks_count)
print("Open Issues:", repo.open_issues_count)
print("Language:", repo.language)