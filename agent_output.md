Adding your contributing guide — mapping the repo to keep setup honest.
Verified the setup gap — now drafting the guide.
Created `CONTRIBUTING.md` (56 lines) at repo root with Prerequisites, Install dependencies, Run tests, and Workflow sections, per the approved plan.

Validation:
- `ls CONTRIBUTING.md && wc -l` — exists, 56 lines.
- Verified `python3 --version` is 3.12.3 (satisfies the documented Python 3.11+ prerequisite); `pytest` is not installed in this environment so `pytest --collect-only` could not run — file notes the empty-tests expectation instead of claiming green.
- `git status --short` shows only `CONTRIBUTING.md` as the new file I added (other untracked entries like `contract.json`, `prompt.md` pre-existed).

Deviations:
- File is 56 lines vs the ~30–50 target, due to the required conditional-wording guards (missing `requirements.txt`/`frontend/`) and the missing-test-source/manual-script notes. No scope change beyond that.
