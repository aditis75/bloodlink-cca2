# BloodLink – Smart Blood Donor Directory

BloodLink is a small dynamic Flask web application created for CSE30040 Cloud Computing and DevOps CCA 2.

## Features

- Donor registration form
- Blood group, city and availability filtering
- Dynamic donor statistics
- JSON API at `/api/donors`
- Health endpoint at `/health`
- Automated pytest tests
- flake8 linting
- Docker container
- GitHub Actions CI/CD
- Render deployment through a deploy hook
- Live commit ID shown in the footer

## Technology

- Python 3.12
- Flask
- Jinja2
- pytest
- flake8
- Docker
- GitHub Actions
- Render

## Run locally

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

macOS/Linux:

```bash
source venv/bin/activate
```

Install:

```bash
pip install -r requirements.txt
```

Run tests:

```bash
pytest -v
```

Run lint:

```bash
flake8 .
```

Start:

```bash
python app.py
```

Open `http://localhost:5000`.

## Docker

Build:

```bash
docker build -t bloodlink .
```

Run:

```bash
docker run -p 5000:5000 bloodlink
```

Open `http://localhost:5000`.

## API

`GET /api/donors`

Optional filters:

`GET /api/donors?blood_group=O%2B`

`GET /api/donors?city=Pune`

## CI/CD flow

Git push → Lint → Test → Docker Build → Health Check → Deploy → Live site

The deployment job uses the GitHub Actions secret `RENDER_DEPLOY_HOOK`.

## Important academic-project note

Use fictional/demo donor records only. Do not put real donor contact or medical information into the public repository or live demo. BloodLink is an academic directory demonstration, not a medical eligibility or emergency-response system.

## CI/CD
BloodLink uses GitHub Actions for linting, testing, Docker build, and Render deployment.