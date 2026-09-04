# HomeLoanAgent — test utilities

This repository currently contains a small set of **standalone manual test
scripts** written against a larger HomeLoanAgent system (an agentic
home-loan underwriting pipeline with a FastAPI backend and React frontend).
The application code for that system is **not** part of this checkout — only
these test scripts, a deployment PDF, and a compiled test artifact are
tracked here.

If you were expecting the full application (agent pipeline, backend,
frontend), it lives elsewhere; this repo does not include it.

## What's in this repo

| File | What it does |
| --- | --- |
| [`mail_test.py`](mail_test.py) | Sends a test email via AWS SES (raw MIME message with a small PDF attachment) from a hardcoded sender to a hardcoded recipient. Used to confirm SES sandbox sending works end to end. |
| [`test_upload.py`](test_upload.py) | POSTs a sample image to `http://localhost:8000/api/upload` on a locally running backend, to exercise the document-upload endpoint. |
| [`aws-deployment.pdf`](aws-deployment.pdf) | A 9-page PDF documenting the AWS deployment for the (external) HomeLoanAgent system. |
| [`tests/__pycache__/`](tests/__pycache__) | Stale compiled bytecode (`.pyc`) for a `test_aggregate_agent` test module. The corresponding source file is not present in this repo. |

These are manual/ad-hoc scripts, not an installable package or test suite —
there's no `requirements.txt`, `pytest.ini`, or CI config here.

## Running `mail_test.py`

Sends a raw email with a tiny generated PDF attachment via AWS SES.

**Prerequisites:**
- `pip install boto3`
- AWS credentials configured (`~/.aws` or environment variables) with SES
  access in the target region.
- Because the sending AWS account is in the **SES sandbox**, both the sender
  and recipient addresses must be **verified identities in the same region**.

**Before running**, edit the hardcoded values at the top of the script:

```python
SENDER    = "..."   # must be a verified SES identity
RECIPIENT = "..."   # must also be verified, while in the SES sandbox
REGION    = os.environ.get("AWS_REGION", "us-east-1")
```

**Run:**

```bash
export AWS_REGION=us-east-1
python mail_test.py
```

On success it prints the SES `MessageId`. On failure it prints the AWS error
code/message, with extra guidance for the common "recipient not verified" and
region/credentials cases.

> Note: the script's own docstring refers to it as `test_ses_send.py`, but
> the file is named `mail_test.py` — use the actual filename when running it.

## Running `test_upload.py`

Uploads a sample image to a document-upload endpoint on a locally running
backend service.

**Prerequisites:**
- `pip install requests`
- A backend server implementing `POST /api/upload` running locally on port
  `8000`. That backend is not part of this repo.
- An image file at `agent_flow/mock_documents/mock_adhaar.png` relative to
  the working directory. **This path does not exist anywhere in this repo**
  — you'll need to supply your own image at that path (or edit the script)
  before it will run.

**Run:**

```bash
python test_upload.py
```

It prints the HTTP status code and JSON response from the upload endpoint,
or an error if the request fails.

## Known gaps

- `test_upload.py` references a fixture file (`agent_flow/mock_documents/mock_adhaar.png`) that isn't checked into this repo.
- `tests/__pycache__/` contains compiled bytecode with no corresponding source file (`test_aggregate_agent.py` is missing).
- Neither script has a `requirements.txt`; install `boto3` and `requests` manually as needed.
