
# GitHealth: Open Source Project Health Analyzer

## Project Overview

GitHealth is a Python-based tool that evaluates the health of open-source GitHub repositories.

Many people judge open-source projects only by the number of stars. However, project quality and sustainability also depend on factors such as development activity, contributor participation, issue management, and community engagement.

GitHealth collects repository information through the GitHub API and calculates a health score to help users better understand the status of an open-source project.

---

## Project Purpose

The purpose of this project is to analyze GitHub repositories and provide an easy-to-understand evaluation of project health.

This tool helps users:

* Identify actively maintained projects
* Evaluate community engagement
* Find beginner-friendly open-source projects
* Compare project sustainability using objective criteria

---

## Main Features

### 1. Repository Information Analysis

The program retrieves:

* Repository name
* Owner
* Number of stars
* Number of forks
* Number of open issues
* Primary programming language

### 2. Health Score Calculation

The project health score is calculated based on:

| Category               | Maximum Score |
| ---------------------- | ------------- |
| Recent Commit Activity | 30            |
| Contributors           | 20            |
| Stars                  | 20            |
| Forks                  | 10            |
| Issue Management       | 20            |
| Total                  | 100           |

### 3. Grade Classification

Based on the calculated score:

| Score    | Grade |
| -------- | ----- |
| 90 - 100 | A     |
| 80 - 89  | B     |
| 70 - 79  | C     |
| 60 - 69  | D     |
| Below 60 | F     |

### 4. Beginner-Friendly Detection

The program determines whether a project is suitable for beginner contributors based on:

* Number of contributors
* Number of open issues

### 5. Visualization

The health score is displayed using a bar chart generated with Matplotlib.

### 6. Report Generation

The analysis result is automatically saved as a text report.

---

## Workflow

1. User enters a GitHub repository URL.
2. GitHub API retrieves repository information.
3. Project metrics are collected.
4. Health score is calculated.
5. Grade is assigned.
6. Beginner-friendly status is determined.
7. Results are displayed and saved to a report file.

---

## Input Example

```text
https://github.com/pallets/flask
```

---

## Output Example

```text
===== Repository Info =====

Name: flask
Owner: pallets
Stars: 70000
Forks: 16000
Open Issues: 20
Language: Python

===== Health Analysis =====

Health Score: 95/100
Grade: A

Beginner Friendly: YES
```

---

## Technologies Used

* Python
* PyGithub
* Matplotlib

---

## Installation

Install required packages:

```bash
pip install -r requirements.txt
```

---

## Running the Program

```bash
python main.py
```

Then enter a GitHub repository URL when prompted.

---

## Project Structure

```text
GitHealth/

├── main.py
├── scoring.py
├── visualization.py
├── requirements.txt
├── README.md
├── LICENSE
└── results/
```

---

## License

This project is released under the MIT License.

See the LICENSE file for more details.

---

## Future Improvements

* More advanced repository analysis
* Additional health indicators
* Web-based interface
* Historical trend visualization
* Support for repository comparison

```
```
