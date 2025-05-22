# 🌸 Scent Hunter

**Scent Hunter** is a full-stack web application that matches users with personalized perfume recommendations based on their preferences. 
Built with a Python Flask backend and a HTML/CSS frontend, this project also incorporates key DevOps practices, including Dockerization, CI/CD pipelines, and cloud deployment.

---

## 🚀 Features

- 🧠 Dynamic quiz that captures user scent preferences
- 💎 AI-style perfume matching logic
- 👤 User profile system with optional profile pictures
- 📦 Store and retrieve users' personal perfume collections
- 🌐 Fully containerized using Docker
- 🔁 CI/CD pipeline with GitHub Actions
- ☁️ Cloud deployment (Render/AWS/GCP)

---

## 🛠️ Tech Stack

| Category       | Tools / Technologies                  |
|----------------|----------------------------------------|
| Frontend  | HTML, CSS, Bootstrap                        |
| Backend   | Python, Flask, Jinja2                       |
| Database  | SQLite (local) / PostgreSQL (cloud)         |
| DevOps    | GitHub Actions, Docker, Git                 |
|Deployment | Render / AWS / Google Cloud Run             |

---

## 📦 Installation

```bash
git clone https://github.com/your-username/scent-hunter.git
cd scent-hunter
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt
python app.py
