# DevOps HTTP Application

## 📌 Project Overview
This project is a simple containerized HTTP application that exposes a health-check endpoint.  
It is designed to demonstrate Dockerization, CI/CD automation, and cloud deployment using managed services.

---

## 🛠️ Tech Stack
- Programming Language: Python
- Web Framework: Flask
- Containerization: Docker
- CI/CD: Google Cloud Build (YAML-based pipeline)
- Cloud Platform: Google Cloud Platform (Cloud Run / Container Registry)
- Version Control: GitHub

---

## 🏗️ Architecture
1. Source code is maintained in a GitHub repository.
2. A Cloud Build trigger runs on every push to the main branch.
3. The CI/CD pipeline:
   - Builds a Docker image
   - Pushes the image to Google Container Registry
4. The container image is deployed to a managed cloud service.
5. The application is exposed via a public HTTP endpoint.

---

## ▶️ Running the Application Locally

### Prerequisites
- Docker installed

### Steps
```bash
git clone <https://github.com/Pushpa1212/HTTP-Project>
cd devops-http-app
docker build -t devops-http-app .
docker run -p 8080:8080 devops-http-app
