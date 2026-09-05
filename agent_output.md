Adding your contributing guide — mapping the real setup first.
Your guide already exists — I'll verify it matches the plan.
No code changes were needed — `CONTRIBUTING.md` already exists at repo root and fully implements the approved plan, so I left the tree untouched (no commit/push, per instructions).

What I verified:
- `CONTRIBUTING.md` (56 lines) covers all four required sections: Prerequisites, Install dependencies, Run tests, Workflow.
- Install: `venv` + `pip install -r requirements.txt` guarded with "if present", fallback `pip install pytest requests boto3`, plus `cd frontend && npm install` guarded with "if present" — matches plan §3 and avoids the known risk of documenting a non-existent `requirements.txt`.
- Tests: primary `python -m pytest tests/ -v`, with honest notes that `tests/` currently holds only `__pycache__/test_aggregate_agent.*.pyc` (source missing) and that `mail_test.py` / `test_upload.py` are manual scripts, not pytest.
- Includes the 1-line snapshot-mismatch note (`backend/`, `frontend/`, `agent_flow/`, `requirements.txt` absent) and links to `README.md` for full AWS/frontend setup (kept out of scope per plan).
- Sanity checks: `python --version` → 3.12.3, `tests/` contains only `__pycache__`, section/assert script passes. `pytest` isn't installed here, consistent with the file's note that collection may report no tests.
- `git status --short` shows only a pre-existing `M agent_output.md` (not mine); no new diff from my side.

Deviation: none from the plan's content. Minor note: file is 56 lines vs the plan's "~30–50" target — still short, and trimming would remove required guard wording, so I kept it.
