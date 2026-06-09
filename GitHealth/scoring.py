from datetime import datetime, timezone


def calculate_health_score(repo):
    score = 0
    strengths = []
    weaknesses = []
    checklist = []
    
    # 1. recent commit (score: 25)
    last_commit = repo.get_commits()[0]
    commit_date = last_commit.commit.author.date

    now = datetime.now(timezone.utc)
    days = (now - commit_date).days

    if days <= 30:
        score += 25
        strengths.append("Active development (commit within 30 days)")
        checklist.append(("Recent Commit Activity", True))
    elif days <= 90:
        score += 20
        checklist.append(("Recent Commit Activity", False))
    elif days <= 180:
        score += 15
        weaknesses.append("Development activity slowing down (commit within 180 days)")
        checklist.append(("Recent Commit Activity", False))
    else:
        weaknesses.append("Inactive development (no commit in 180 days)")
        checklist.append(("Recent Commit Activity", False))

    # 2. Contributors (score: 15)
    contributors = repo.get_contributors().totalCount

    if contributors >= 100:
        score += 15
        strengths.append("Many contributors (>= 100)")
        checklist.append(("Contributors", True))
    elif contributors >= 50:
        score += 10
        checklist.append(("Contributors", False))
    elif contributors >= 10:
        score += 5
        weaknesses.append("Few contributors (>= 10)")
        checklist.append(("Contributors", False))
    else:
        weaknesses.append("Limited contributors (< 10)")
        checklist.append(("Contributors", False))

    # 3. Stars (score: 15)
    stars = repo.stargazers_count

    if stars >= 10000:
        score += 15
        strengths.append("Strong community interest (>= 10000)")
        checklist.append(("Stars", True))
    elif stars >= 1000:
        score += 10
        checklist.append(("Stars", False))
    elif stars >= 100:
        score += 5
        weaknesses.append("Few community members (>= 100)")
        checklist.append(("Stars", False))
    else:
        weaknesses.append("Low community interest (< 100)")
        checklist.append(("Stars", False))

    # 4. Forks (score: 10)
    forks = repo.forks_count

    if forks >= 1000:
        score += 10
        strengths.append("Highly forked project (>= 1000)")
        checklist.append(("Forks", True))
    elif forks >= 100:
        score += 7
        checklist.append(("Forks", False))
    else:
        score += 3
        weaknesses.append("Low fork count (< 100)")
        checklist.append(("Forks", False))

    # 5. Issues (score: 15)
    issues = repo.open_issues_count

    if issues <= 50:
        score += 15
        strengths.append("Few issues (<= 50)")
        checklist.append(("Issues", True))
    elif issues <= 200:
        score += 10
        checklist.append(("Issues", False))
    else:
        score += 5
        weaknesses.append("Many issues (> 200)")
        checklist.append(("Issues", False))
    
    # 6. README (score: 10)    
    try:
        repo.get_readme()
        score += 10
        strengths.append("README documentation available")
        checklist.append(("Documentation (README)", True))
    except:
        weaknesses.append("README documentation missing")
        checklist.append(("Documentation (README)", False))
    
    # 7. License (score: 10)    
    try:
        repo.get_license()
        score += 10
        strengths.append("License information available")
        checklist.append(("License Information", True))
    except:
        weaknesses.append("License information missing")
        checklist.append(("License Information", False))

    return score, strengths, weaknesses, checklist

def beginner_friendly(repo):
    contributors = repo.get_contributors().totalCount
    issues = repo.open_issues_count
    
    if contributors >= 10 and issues <= 100:
        return True
    
    return False