# Self-Learning Python Process

A documentation of my journey learning Python, specifically focused on **Test Automation Engineering**. Below is the roadmap I follow:

---

### Stage 1: Python Foundational Infrastructure
**Status: Completed**

Skills Learned:
* In-depth Lists/Dictionaries & Data Structures
* File Handling (I/O)
* Error Handling (try/except)

**Practical Goal:** Built a "Number Guessing Game" with robust error handling & score persistence.

---

### Stage 2: Python Intermediate & Developer Tools
**Status: Completed**

Skills Learned:
* Object-Oriented Programming (OOP)
* Virtual Environments (venv) & Package Management (pip)
* Git Basics (Personal Version Control & GitHub)

**Practical Goal:** Refactored the "Number Guessing Game" using OOP principles, managed dependencies with venv, and pushed the project to GitHub.

---

### Stage 3: Introduction to Android Automation (Mobly)
**Status: In Progress**

Skills to Learn:
* **Google Mobly Framework:** Understanding the lifecycle (`setup_class`, `teardown_class`, `test_*`).
* **ADB (Android Debug Bridge):** Controlling devices via command line and Python `subprocess`.
* **YAML Configuration:** Managing testbeds and user parameters externally.

**Practical Goal:** Write a basic Mobly script to automatically toggle Wi-Fi on an Android emulator and verify the state via ADB.

---

### Stage 4: Modularization & Logic Encapsulation
**Status: In Progress**

Skills to Learn:
* **Controller Pattern:** Separating test logic (Script) from device operations (Lib).
* **Snippet Interaction:** Using Mobly Bundled Snippets (`mbs`) for stable RPC calls.
* **Defensive Programming:** Using `hasattr` and error handling for robust device control.

**Practical Goal:** Refactor the Wi-Fi test to use a `WifiController` class, decoupling the ADB/Snippet commands from the test case.

---

### Stage 5: Enterprise Mobly Architecture (Current Focus)
**Status: Active Practice**

Skills to Learn:
* **Layered Architecture:** Designing `config`, `common`, `libs`, `datamodels`, and `tests` layers.
* **Data Models (Proto-style):** Using Python `dataclasses` to create strict contracts between Config and Controllers.
* **Dependency Injection (DI):** Injecting device objects into Controllers via `BaseTest` to improve testability.
* **Robust Data Mapping:** Safely parsing external YAML data into internal Type-safe objects.

**Practical Goal:** Build a scalable **Wi-Fi & Bluetooth Automation Framework** featuring:
- [x] **Datamodels:** `WifiConfig` & `BluetoothConfig` for strict type checking.
- [x] **Dependency Injection:** Injecting controllers in `EnterpriseBaseTest`.
- [x] **Abstraction:** High-level test scripts that read like English instructions.

---

### Stage 6: CI/CD & Pipeline Integration
**Status: Planned**

Skills to Learn:
* Git for Teams (Branching & Merging)
* CI/CD Concepts (GitLab CI / GitHub Actions)
* Automated Reporting (Generating Test Summaries)

**Practical Goal:** Set up a GitHub Actions pipeline to automatically run the Mobly test suite (using Emulators) on every code push.

---

### Stage 7: Containerization & Advanced Analysis
**Status: Planned**

Skills to Learn:
* Docker Core Concepts (Running tests in isolated containers)
* Log Analysis (Parsing Mobly logs with Pandas)
* Visualization (Matplotlib for pass/fail trends)

**Practical Goal:** Dockerize the test environment and create a dashboard to visualize test stability over time.
