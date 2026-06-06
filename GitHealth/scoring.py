from datetime import datetime, timezone


def calculate_health_score(repo):
    score = 0
    strengths = []
    weaknesses = []
    # 1. recent commit (score: 30)
    last_commit = repo.get_commits()[0]
    commit_date = last_commit.commit.author.date

    now = datetime.now(timezone.utc)
    days = (now - commit_date).days

    if days <= 30:
        score += 30
        strengths.append("Active development (commit within 30 days)")
    elif days <= 90:
        score += 20
    elif days <= 180:
        score += 10
        weaknesses.append("Development activity slowing down (commit within 180 days)")
    else:
        weaknesses.append("Inactive development (no commit in 180 days)")

    # 2. Contributors (score: 20)
    contributors = repo.get_contributors().totalCount

    if contributors >= 100:
        score += 20
        strengths.append("Many contributors (>= 100)")
    elif contributors >= 50:
        score += 15
    elif contributors >= 10:
        score += 10
        weaknesses.append("Few contributors (>= 10)")
    else:
        score += 5
        weaknesses.append("Limited contributors (< 10)")

    # 3. Stars (score: 20)
    stars = repo.stargazers_count

    if stars >= 10000:
        score += 20
        strengths.append("Strong community interest (>= 10000)")
    elif stars >= 1000:
        score += 15
    elif stars >= 100:
        score += 10
        weaknesses.append("Few community members (>= 100)")
    else:
        score += 5
        weaknesses.append("Low community interest (< 100)")

    # 4. Forks (score: 10)
    forks = repo.forks_count

    if forks >= 1000:
        score += 10
        strengths.append("Highly forked project (>= 1000)")
    elif forks >= 100:
        score += 7
    else:
        score += 3
        weaknesses.append("Low fork count (< 100)")

    # 5. Issues (score: 20)
    issues = repo.open_issues_count

    if issues <= 50:
        score += 20
        strengths.append("Few issues (<= 50)")
    elif issues <= 200:
        score += 15
    else:
        score += 5
        weaknesses.append("Many issues (> 200)")

    return score, strengths, weaknesses

def beginner_friendly(repo):
    contributors = repo.get_contributors().totalCount
    issues = repo.open_issues_count
    
    if contributors >= 10 and issues <= 100:
        return True
    
    return False