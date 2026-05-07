# 🍎 Teacher Management API Automation Framework

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Pytest](https://img.shields.io/badge/Tested%20with-Pytest-yellow.svg)](https://docs.pytest.org/)
[![Allure](https://img.shields.io/badge/Report-Allure-brightgreen.svg)](https://docs.qameta.io/allure/)
[![Requests](https://img.shields.io/badge/Library-Requests-orange.svg)](https://requests.readthedocs.io/)

This project is a comprehensive **REST API Automation Framework** designed to validate the **Teacher Management APIs**. It focuses on clean code architecture, reusable helper functions, and detailed reporting.

---

## 📊 Test Execution Summary
Below is the execution result from the latest test run:

| Total Tests | Passed ✅ | Failed ❌ | Pass Rate % |
| :--- | :--- | :--- | :--- |
| 13 | 13 | 0 | 100% |

---
## 📊 Test Execution Dashboards

### Allure Overview
Below is the high-level summary of the test execution results, showcasing the pass/fail ratio and overall test health.
![Allure Dashboard](./assets/allure.png)

### Graphical Analysis
Visual representation of test severity, duration, and status trends.
![Test Graphs](./assets/graphs.png)

### Category & Suite Breakdown
Detailed view of test cases organized by their functional categories and suites.
![Category View](./assets/suites.png)

### Execution Timeline
A visual timeline showing when each test was executed and how long it took.
![Timeline](./assets/timeline.png)
---

## 🚀 Key Features
* **Complete CRUD Validation**: Covers Create, Read, and Delete operations for Teacher profiles.
* **Helper-Driven Design**: Reusable logic for API calls to avoid code duplication.
* **Security Testing**: Validates API behavior with and without Authorization tokens.
* **Negative Scenarios**: Includes tests for invalid emails, missing fields, and non-existent IDs.
* **Environment Management**: Uses `.env` for securing sensitive credentials like `BASE_URL` and `ADMIN_PASS`.

---

## 📂 Project Structure
```text
├── utils/
│   ├── config.py           # Loads environment variables
│   └── helper_functions.py # Core API call wrappers (Post, Get, Delete)
├── test_cases/
│   ├── test_create.py      # Tests for Teacher creation logic
│   └── test_delete.py      # Tests for deletion and edge cases
├── .env                    # Environment variables (BASE_URL, Credentials)
├── .gitignore              # Files to exclude from Git
├── pytest.ini              # Pytest configuration
├── requirements.txt        # Dependencies (pytest, requests, allure-pytest, etc.)
└── README.md               # Project documentation
```
## 👩‍💻 Author
**Israt Jahan Tarifa**
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/israt-tarifa/) 
[![GitHub](https://img.shields.io/badge/GitHub-Profile-lightgrey?style=flat&logo=github)](https://github.com/Israt-Tarifa)
