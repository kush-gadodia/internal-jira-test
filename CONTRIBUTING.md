# Contributing to HomeLoanAgent

Thanks for contributing! This is a short getting-started guide. For full
system setup (AWS Bedrock/S3/DynamoDB/SES), see `README.md`
(Prerequisites / Setup & installation).

## Prerequisites

- Python 3.11+ (`python3 --version`)
- Node.js 18+ and npm — frontend only, if `frontend/` is present
- AWS credentials — only needed for Bedrock/SES manual scripts, not for unit tests

## Install dependencies

```bash
git clone <repo-url> HomeLoanAgent
cd HomeLoanAgent

python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt    # if requirements.txt is missing: pip install pytest boto3 requests

# Frontend (only if frontend/ exists):
cd frontend && npm install && cp .env.example .env
```

## Run tests

```bash
# all tests
pytest -v

# single file
pytest tests/test_aggregate_agent.py -v
```

Helper scripts (not unit tests, need extra setup):

- `python mail_test.py` — SES sandbox script, needs verified sender/recipient.
- `python test_upload.py` — needs the backend running on `:8000`.

## Quick checks before a PR

- `pytest` passes
- No secrets committed (`users.db`, `jwt_secret.txt`, AWS keys)
