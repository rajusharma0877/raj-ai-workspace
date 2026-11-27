# Run the native Hermes Agent in GitHub Codespaces

This uses the official Hermes Agent CLI, Gateway, Telegram adapter, memory, sessions, and native Webapp. It does not add a separate chatbot frontend or duplicate memory service.

## 1. Create the Codespace

1. Open this repository on GitHub.
2. Select **Code → Codespaces → Create codespace on main**.
3. Choose the **2-core** machine to conserve the free Codespaces allowance.
4. Wait for the devcontainer to finish creating. It installs Hermes using the official Nous Research installer.

Codespaces is an on-demand development VM, not an always-on VPS. When the Codespace is stopped, Hermes and Telegram polling stop too. Files in the Codespace persist while the Codespace exists, but deleting the Codespace deletes its local data unless you back it up.

## 2. Configure the model provider

In the Codespaces terminal, run:

```bash
hermes model
```

Choose **Custom endpoint (self-hosted / VLLM / etc.)** and enter the Numes AI OpenAI-compatible settings:

- Base URL: `https://api.numes.ai/api/v1`
- API key: enter your Numes key in the interactive prompt; do not paste it into a repository file.
- Model: choose an exact model ID available to your Numes account.

Do not configure a paid fallback provider. If the selected Numes model is unavailable, let the request fail rather than silently routing to a paid service.

## 3. Configure Telegram on the same native Gateway

Run:

```bash
hermes gateway setup
```

Choose Telegram and enter the bot token from BotFather when prompted. Keep the token private. The Telegram adapter and Webapp will use the same Hermes Gateway and agent home.

## 4. Enable the native Hermes Webapp securely

Create a dashboard password first. Use a strong, unique password when prompted:

```bash
hermes dashboard password
hermes config set webapp.enabled true
hermes config set webapp.host 0.0.0.0
hermes config set webapp.port 9120
```

The Codespaces port 9120 is configured as **Private**. Do not change it to Public.

## 5. Start Hermes

Run the Gateway in the foreground:

```bash
hermes gateway run
```

Wait for the Gateway to start. In the Codespaces **Ports** tab, open the private forwarded port labelled **Hermes Webapp**. Sign in with the dashboard username/password you created.

Telegram and the Webapp now talk to the same Gateway. Keep the Codespace running while you want Telegram and the Webapp available.

## 6. Stop and resume

- To stop: use **Codespaces → Stop codespace**. This stops the Gateway and Telegram bot.
- To resume: reopen the same Codespace, then run `hermes gateway run` again.
- Do not delete the Codespace if you want to retain its Hermes home, sessions, and memory.
- Export regular backups with Hermes' backup command before deleting or recreating the Codespace.

## Limits

- GitHub's free Codespaces allowance is limited and can change. A 2-core Codespace consumes quota while running; check **GitHub → Settings → Billing and licensing → Codespaces** before leaving it on.
- This is not 24/7 free hosting. The Codespace can stop due to inactivity, quota, or manual stop.
- GitHub Actions workflows in this repository are separate, temporary runners; they are not the persistent Hermes Gateway.
- Never commit API keys, Telegram bot tokens, passwords, or Hermes `.env` files.
