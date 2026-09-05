# Contributing

Thanks for contributing to HomeLoanAgent! This guide covers the basics:
installing dependencies and running tests. For full system setup
(AWS Bedrock/S3/DynamoDB/SES, frontend dev server, agent pipeline),
see `README.md`.

> Note: `README.md` references `backend/`, `frontend/`, `agent_flow/`,
> and `requirements.txt`, which are absent from this snapshot. Steps below
> are guarded with "if present" accordingly.

## Prerequisites

- Python 3.11+ (`python --version` to check) with `pip` and `venv`
- Node.js 18+ and npm — only needed if `frontend/` is present

## Install dependencies

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate

# If requirements.txt exists:
pip install -r requirements.txt

# Otherwise (this snapshot has no requirements.txt), install the minimum:
pip install pytest requests boto3
```

Frontend (only if `frontend/` is present):

```bash
cd frontend && npm install
```

## Run tests

```bash
python -m pytest tests/ -v
```

Notes:

- `tests/` currently contains only a compiled
  `__pycache__/test_aggregate_agent.*.pyc` (the
  `test_aggregate_agent.py` source is missing), so collection may report
  no tests until the source is restored.
- `mail_test.py` (SES sandbox check, needs `boto3` + AWS credentials) and
  `test_upload.py` (needs a backend on `localhost:8000`) are manual
  scripts, not pytest tests — run them only when those services exist.

## Workflow

1. Create a branch for your change.
2. Make focused commits.
3. Open a pull request describing what changed and how you tested it.
