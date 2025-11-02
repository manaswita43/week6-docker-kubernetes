# Iris Prediction API – GKE Deployment with CI/CD

This project demonstrates building, containerizing, and deploying a **FastAPI-based ML model (Iris classifier)** on **Google Kubernetes Engine (GKE)** using **Google Cloud Build & GitHub Actions (CI/CD)**.

---

## Project Overview

- **Model**: Pre-trained Random Forest classifier on the Iris dataset  
- **API Framework**: FastAPI  
- **Containerization**: Docker  
- **Container Registry**: Google Artifact Registry (GAR)  
- **Orchestration**: Kubernetes (GKE)  
- **Automation**: GitHub Actions for CI/CD  

---

## Project Structure

```
week6-docker-kubernetes/
│
├── models/
│ └── model.joblib # Trained Iris model
│
├── main.py # FastAPI application
├── requirements.txt # Python dependencies
├── Dockerfile # Container image definition
│
├── k8s/
│ ├── deployment.yml # Kubernetes Deployment definition
│ └── service.yml # Kubernetes Service (exposes app)
│
├── .github/
│ └── workflows/
│ └── cd.yml # CI/CD pipeline (build & deploy)
│
└── README.md
```

---

## Implementation

- Fast API application code
- Docker Setup
  Run these to build Docker, after creating the Dockerfile
  ```bash
    docker build -t iris-api-test .
    docker run -p 8200:8200 iris-api-test
  ```
- Google Cloud Setup
  ### Prerequisites
  - Enable Artifact Registry and GKE API.
  - Create:
    - Artifact Registry Repository
    - GKE Cluster
  - Connect:
    ```bash
    gcloud container clusters get-credentials iris-cluster --region us-central1 --project <PROJECT_ID>
    ```
- Kubernetes Deployment
  - deployment.yml
  - service.yml
  - Deploy
    ```bash
    kubectl apply -f k8s/deployment.yaml
    kubectl apply -f k8s/service.yaml
    kubectl get pods
    kubectl get services
    ```
- CI/CD Pipeline (GitHub Actions)
  ```.github/workflows/cd.yml```
  - Triggers: On push to main
  - Builds Docker image
  - Pushes to Artifact Registry
  - Deploys to GKE
    
  ### Required Github secrets
  - GCP_PROJECT_ID
  - GCP_SA_KEY - JSON key of GCP
  - GAR_LOCATION - Google artifact registry location
  - GAR_REPOSITORY - Google artifact registry repository
  - GKE_CLUSTER
  - GKE_ZONE

  ### Port Forwarding & Testing
  ```bash
  kubectl get pods
  kubectl port-forward <pod-name> 8080:8200
  ```
  Visit
  [https://ssh.cloud.google.com/devshell/proxy?port=8080]()
  
  Test API:
  ```bash
  curl -X POST "http://127.0.0.1:8080/predict/" -H "Content-Type: application/json" -d "[5.1, 3.5, 1.4, 0.2]"
  ```

