# github-aibom-scan-test

Test fixture for the GitHub AIBOM / DevOps scanner. Contains AI SDKs, model references,
vulnerable dependency pins and GitHub Actions workflows that pull, serve and use models. Do not deploy.

Test fixture for the AIBOM **DevOps (code) scan** on Bitbucket. Deliberately contains:

| What | Where | Expected finding |
|---|---|---|
| Old, vulnerable Python AI/web libs | `requirements.txt` | Grype CVEs (library components) |
| Old, vulnerable npm libs incl. AI SDKs | `web/package.json` | Grype CVEs (npm) |
| LLM provider calls (OpenAI, Anthropic, HF, Ollama) | `app/*.py`, `web/index.js` | AI endpoints / models |
| Hugging Face models | `app/inference.py`, `config/models.yaml` | machine-learning-model components |
| Unpinned AI images / model pulls | `bitbucket-pipelines.yml`, `Dockerfile` | AI-*-UNPINNED findings |
| Training data | `data/` | data components |
| Hardcoded credential (AWS documented example key, not real) | `config/settings.py` | CWE-798 secret |

**Do not deploy.** Nothing here is meant to run in production.
