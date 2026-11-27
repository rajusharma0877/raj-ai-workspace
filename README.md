# Hermes Agent Workspace

A clean, single-purpose workspace for **NousResearch Hermes Agent**.

This repository contains deployment notes and a GitHub Codespaces development environment. It does not fork or vendor Hermes itself; the official installer installs the upstream project.

## Start in GitHub Codespaces

1. Open this repository on GitHub.
2. Select **Code → Codespaces → Create codespace on main**.
3. Wait for the environment setup to finish.
4. In the Codespaces terminal, run:

   ```bash
   hermes setup
   ```

5. Configure the model provider in the setup wizard. Choose **Custom Endpoint** for an OpenAI-compatible provider such as Numes AI, then enter its base URL, model ID, and API key when prompted.
6. Configure Telegram from the native gateway setup:

   ```bash
   hermes gateway setup
   hermes gateway run
   ```

Read [SETUP.md](SETUP.md) before exposing any web interface or adding credentials.

## Important limits

- Codespaces is a development environment, **not an always-on VPS**. It can stop or be reclaimed; a stopped Codespace cannot receive Telegram messages.
- GitHub Actions runners are temporary jobs, not a persistent Hermes host.
- No paid provider or paid fallback is configured by this repository.
- Device-specific work cannot run while that device is offline unless a separate, tested remote-execution connection is configured.
- Hermes' own memory, sessions, subagents, skills, MCP integrations, and cron features remain native Hermes features.

## Upstream

- [Hermes Agent source](https://github.com/NousResearch/hermes-agent)
- [Official documentation](https://hermes-agent.nousresearch.com/docs)
- [Quickstart](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart)
- [Messaging Gateway](https://hermes-agent.nousresearch.com/docs/user-guide/messaging)
