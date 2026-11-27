# Raj AI Workspace

Zero-budget, GitHub-first workspace with one shared Hermes orchestrator and FreeLLMAPI gateway, plus separate YouTube and Instagram modules.

## Architecture
- Hermes: shared task orchestrator.
- FreeLLMAPI: shared OpenAI-compatible model gateway.
- GitHub Actions: on-demand temporary runners, not permanent hosting.
- Publishing: manual approval only.

## Projects
- YouTube Hindi + English: original 10–15 minute illustrated history documentaries; initial pilot is everyday life in Ancient Rome.
- Instagram: separate faceless psychology, heartbreak, and long-distance-relationship content.

## Start

For the native Hermes Agent in GitHub Codespaces (official Hermes CLI + Gateway + Telegram + Webapp), follow [CODESPACES.md](CODESPACES.md). Codespaces is temporary compute, not 24/7 VPS hosting.

Read [SETUP.md](SETUP.md), add the three Actions secrets, then open **Actions → YouTube Documentary Pack → Run workflow**.

The workflow produces a research/script/visual/SEO production pack, not a finished rendered video. It never auto-publishes. Free quotas and service limits may change; no paid fallback is configured.
