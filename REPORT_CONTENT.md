# CCA 2 Short Report – BloodLink

## 1. Title Page

**Project:** BloodLink – Smart Blood Donor Directory  
**Course:** Cloud Computing and DevOps (CSE30040)  
**Student Name:** <YOUR NAME>  
**PRN:** <YOUR PRN>  
**Roll No. / Panel:** <YOUR ROLL/PANEL>  
**GitHub Repository:** <ADD LINK>  
**Live Application:** <ADD LINK>

## 2. Problem Statement and Features

Finding an available blood donor can be difficult when donor information is scattered. BloodLink provides a simple web directory where demo donors can register with a blood group, city, contact field, last donation date and availability status. Users can filter the directory and access donor data through a JSON API.

Features:
- Donor registration
- Input validation
- Blood group and city filtering
- Availability filtering on the web page
- Dashboard statistics
- JSON API
- Health endpoint
- Automated tests
- Linting
- Docker containerisation
- GitHub Actions CI/CD
- Render deployment

## 3. Architecture and Pipeline

Browser → Flask application → In-memory donor data

CI/CD:
Git push → GitHub Actions → flake8 → pytest → Docker build → Docker smoke test → Render deploy → live site

## 4. Pipeline Stages

### Lint
flake8 checks the Python source for style and common errors.

### Test
pytest verifies the health route, valid donor registration, invalid input handling and API filtering.

### Docker Build
The Dockerfile packages the Flask application and dependencies into a reproducible container image.

### Smoke Test
The container is started and `/health` is requested. A failed response causes the build job to fail.

### Deploy
Only a successful build on the main branch triggers the Render deploy hook.

### Verification
The live application is opened and the footer commit ID is compared with the successful GitHub Actions run.

## 5. Failure Demonstration

For the required failure demo, intentionally change one test so that it fails. Push the branch and capture the red GitHub Actions run. The deploy job must be skipped because it depends on the build job.

Then restore the test, push/merge the fix to main and capture the green run. Open the live application and capture the commit ID shown in the footer.

## 6. Challenges and Learning

Possible points:
- Configuring Flask for the Render PORT environment variable
- Creating automated tests
- Writing a GitHub Actions workflow
- Building and testing the Docker image
- Connecting GitHub Actions to Render through a secret
- Understanding how `needs` controls pipeline order
- Demonstrating that a failed test prevents deployment

## 7. Links

GitHub Repository: <ADD LINK>  
Live Site: <ADD LINK>  
GitHub Actions: <ADD LINK>
