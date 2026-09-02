# internal-jira-test

This repository does **not** contain the HomeLoanAgent application source (no
`agent_flow/`, `backend/`, or `frontend/` directories exist here). It currently
holds a small set of standalone scripts and reference material related to
that project, plus this README.

## Table of contents

- [What's in this repo](#whats-in-this-repo)
- [`mail_test.py`](#mail_testpy)
- [`test_upload.py`](#test_uploadpy)
- [`aws-deployment.pdf`](#aws-deploymentpdf)

## What's in this repo

| Path | Purpose |
| --- | --- |
| `mail_test.py` | Standalone AWS SES sandbox send test. |
| `test_upload.py` | Smoke test for a local `/api/upload` endpoint. |
| `aws-deployment.pdf` | Deployment reference document. |

## `mail_test.py`

A standalone script that sends a test email (with a small PDF attachment)
through AWS SES, to verify sandbox sending works end to end.

**Requires:**
- AWS credentials configured (`~/.aws` or environment variables).
- A sender and recipient email, each a **verified identity** in the same SES
  region (SES sandbox requirement).

**Run:**

```bash
export AWS_REGION=us-east-1
export SES_SENDER=you@example.com        # must be a verified identity
export SES_RECIPIENT=someone@example.com # in sandbox, must ALSO be verified
python mail_test.py
```

Expected output: a printed `MessageId` and the mail arriving in the
recipient's inbox.

## `test_upload.py`

POSTs a sample file to `http://localhost:8000/api/upload`. This depends on a
`backend/` server and an `agent_flow/mock_documents/` directory, **neither of
which exist in this repo** — it's meant to be run against the full
HomeLoanAgent checkout, not standalone here.

## `aws-deployment.pdf`

Reference document describing the AWS deployment setup for the HomeLoanAgent
project. Consult it when provisioning or reviewing the AWS infrastructure
(Bedrock, S3, DynamoDB, SES) that the full application depends on.

> A `tests/` directory previously tracked only compiled `__pycache__/*.pyc`
> artifacts for a `test_aggregate_agent.py` that doesn't exist in this repo.
> Those artifacts have been removed (see `.gitignore`); re-add `tests/` with
> real source if/when a test suite is brought into this repo.
