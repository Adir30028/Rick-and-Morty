# Rick and Morty Filter API 🧪

A DevOps-oriented Python project that queries the Rick and Morty API for all characters who are:
- 👽 Species: Human
- ✅ Status: Alive
- 🌍 Origin: Earth

It then exposes these results via a Flask REST API and deploys it with Docker, Kubernetes, Helm, and GitHub Actions.

---

## 🧰 Features

- [x] Fetch filtered character data from public API
- [x] Serve data via `/characters` endpoint
- [x] Healthcheck via `/healthcheck`
- [x] Save results to CSV
- [x] Dockerized Flask service
- [x] Kubernetes manifests (`yamls/`)
- [x] Helm Chart (`helm/`)
- [x] Full CI/CD pipeline with GitHub Actions

---

## 🧪 Endpoints

| Method | Endpoint         | Description                       |
|--------|------------------|-----------------------------------|
| GET    | `/characters`    | Returns filtered characters (JSON)|
| GET    | `/healthcheck`   | Returns `{ "status": "ok" }`      |

Example:

```bash
curl http://localhost:5000/characters
```

---

## 🐳 Docker

### 🔧 Build

```bash
docker build -t rick-api .
```

### ▶️ Run

```bash
docker run -p 5000:5000 rick-api
```

---

## ☸️ Kubernetes (manifests)

```bash
kubectl apply -f yamls/
```

Make sure to port-forward the service or expose it via ingress.

---

## 🪖 Helm Chart

```bash
helm upgrade --install rick-api ./helm \
  --set image.username=<your-dockerhub-user> \
  --set image.tag=latest
```

---

## 🤖 GitHub Actions Workflow

This repo contains a CI/CD pipeline that performs the following:

- ✅ Builds and pushes Docker image to Docker Hub
- ✅ Creates a **temporary Kubernetes cluster using KinD** inside GitHub Actions
- ✅ Deploys the app using Helm
- ✅ Runs a curl test to verify `/healthcheck` works

To trigger it, simply push to the `main` branch.

> 🧠 **Note**: The application does **not** run persistently on AWS or any cloud provider.  
> It is deployed temporarily **inside GitHub Actions** for validation purposes only.

---

## 📝 CSV Output Example

```csv
Name,Location,Image
Rick Sanchez,Earth,https://rickandmortyapi.com/api/character/avatar/1.jpeg
```

---

## 🔐 Secrets Required for CI/CD

| Secret Name         | Purpose                   |
|---------------------|---------------------------|
| `DOCKER_USERNAME`   | Docker Hub username       |
| `DOCKER_PASSWORD`   | Docker Hub password/token |

---

## 👋 Author

Built with ❤️ by Adir Mizrahi for the DevOps Engineer Home Exercise.
