# Setup and operating notes

## 1. Install

The Codespaces devcontainer runs the official Hermes installer from Nous Research. If you need to install or repair it manually on Linux, use the upstream command:

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
source ~/.bashrc
hermes doctor
```

Official installer and documentation: https://github.com/NousResearch/hermes-agent

## 2. Configure the model

Run:

```bash
hermes setup
```

Use the setup wizard's **Custom Endpoint** option for an OpenAI-compatible API. For the Numes AI endpoint currently selected for this project, use:

```
https://api.numes.ai/api/v1
```

Enter the exact model identifier supplied by the provider and the API key in the interactive prompt. Do not put keys in repository files, shell history, screenshots, or commits. If the provider's model ID or endpoint changes, use `hermes model` to reconfigure.

There is no automatic paid fallback. If the selected provider is unavailable or out of credits, Hermes should report the error rather than silently switching to a paid provider.

## 3. Telegram

Use Hermes' own gateway setup:

```bash
hermes gateway setup
```

Select Telegram and enter the bot token when prompted. Keep the token private. Then run the gateway in the foreground:

```bash
hermes gateway run
```

The foreground process ends when the Codespace stops or the terminal process exits. Do not treat this as a permanent bot host.

## 4. Browser / dashboard access

Use the dashboard/web-app instructions for the exact Hermes version installed:

https://hermes-agent.nousresearch.com/docs

Do not expose an unauthenticated dashboard to the public internet. Prefer private access or a properly authenticated remote connection. Never disable authentication merely to make a public port work.

## 5. Native capabilities

Prefer Hermes' built-in functionality rather than building duplicate systems:

- Native gateway adapters for supported messaging platforms
- Native sessions and memory
- Native subagents and delegation
- Native skills and MCP integrations
- Native cron scheduler
- Native CLI and dashboard/web interface where supported by the installed version

Concurrency depends on the selected model provider's limits and available compute. Do not assume ten concurrent subagents will always be available.

## 6. Runtime and persistence reality

GitHub Codespaces is temporary compute. Files in the repository are versioned, but runtime state, active processes, and uncommitted data should not be assumed to survive deletion or recreation of a Codespace. Keep Hermes state in its supported persistent home/volume when using a host that provides persistent storage.

GitHub Actions are short-lived workflow runners and are not a replacement for an always-on gateway.

A device that is powered off or disconnected cannot execute local commands. A queue-and-resume workflow for Windows/Kali/Android requires a separate authenticated worker/relay that reconnects and drains queued jobs; it is not created by this repository and must be implemented and tested before being promised.

## 7. Secrets checklist

- Never commit `.env`, `.env.*`, Telegram tokens, provider API keys, passwords, or session files.
- Use interactive Hermes setup or the host's encrypted secret store.
- Rotate any credential that is accidentally committed.
- Keep the repository private while configuring it.
