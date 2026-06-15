# cloudrun-app

A simple Python Flask web service deployed on Google Cloud Run.

## Endpoints

| Endpoint  | Description |
|-----------|-------------|
| `/`       | Welcome message with your name |
| `/health` | Health check — returns `{"status": "healthy"}` |
| `/info`   | Container hostname and current UTC timestamp |

---

## Project Structure

```
.
├── app.py
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## Local Development

### Run directly with Python
```bash
pip install -r requirements.txt
python app.py
# Visit http://localhost:8080
```

### Run with Docker locally
```bash
# Build the image
docker build -t pwani-cloudrun-app .

# Run the container
docker run -p 8080:8080 pwani-cloudrun-app

# Test endpoints
curl http://localhost:8080/
curl http://localhost:8080/health
curl http://localhost:8080/info
```

---

## Deployment to Google Cloud Run

### Prerequisites
- [Google Cloud SDK](https://cloud.google.com/sdk/docs/install) installed
- A GCP project created
- Billing enabled on the project

### Step 1 — Authenticate & set your project
```bash
gcloud auth login
gcloud config set project YOUR_PROJECT_ID
```

### Step 2 — Enable required APIs
```bash
gcloud services enable run.googleapis.com
gcloud services enable artifactregistry.googleapis.com
```

### Step 3 — Build & push the image using Cloud Build
```bash
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/pwani-cloudrun-app
```

### Step 4 — Deploy to Cloud Run
```bash
gcloud run deploy pwani-cloudrun-app \
  --image gcr.io/YOUR_PROJECT_ID/pwani-cloudrun-app \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

### Step 5 — Verify the deployment
```bash
# Get the service URL
gcloud run services describe pwani-cloudrun-app \
  --platform managed \
  --region us-central1 \
  --format "value(status.url)"

# Test all endpoints (replace SERVICE_URL with the URL from above)
curl SERVICE_URL/
curl SERVICE_URL/health
curl SERVICE_URL/info
```

---

## Cloud Run Service URL
<!-- TODO: Paste your deployed URL here after deployment -->
`https://pwani-cloudrun-app-XXXXXXXXXX-uc.a.run.app`
