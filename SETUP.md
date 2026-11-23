# Setup — zero-hosting mode

This workspace runs FreeLLMAPI and Hermes together inside each GitHub Actions job. Both are temporary: the gateway starts for the job and is discarded when it ends. No VPS, paid hosting, local model, or permanent public endpoint is required.

## One required secret

Open **Repository → Settings → Secrets and variables → Actions → New repository secret**.

Create `FREEAPI_CONFIG_JSON`. Its value must be valid JSON in FreeLLMAPI's declarative startup format, containing your dashboard admin and at least one provider API key. Example shape (replace every placeholder; never paste this example unchanged):

```json
{
  "admin": {
    "email": "your-email@example.com",
    "password": "a-unique-password-at-least-8-characters"
  },
  "keys": [
    {
      "platform": "google",
      "key": "YOUR_PROVIDER_API_KEY",
      "label": "primary-free-key",
      "enabled": true
    }
  ],
  "routing": {
    "strategy": "balanced"
  }
}
```

Use a provider that offers a free API quota in your region. Provider signup and quota policies are separate from FreeLLMAPI; no unlimited free inference is promised. Do not send API keys in chat or commit them to files.

## How the workflow runs

1. GitHub Actions starts a temporary Ubuntu runner.
2. Docker starts the official FreeLLMAPI container with a temporary database and encryption key.
3. The workflow reads the newly generated unified API key from the temporary SQLite settings database.
4. Hermes is installed and configured with the local gateway using the official `freellmapi setup-hermes` command.
5. Hermes generates the requested task output; the output is uploaded as a workflow artifact.
6. The runner, gateway, and temporary database are discarded when the job ends. Provider keys remain only in the GitHub Actions secret.

## Run a YouTube pack

Open **Actions → YouTube Documentary Pack → Run workflow**. Select Hindi or English, then enter the topic and angle. Download the `youtube-production-pack` artifact.

The output is a written production pack, not a rendered video. Human review and editing are still required; publishing is never automatic.

## Free-first limits

GitHub Actions usage and provider free quotas are subject to account/provider limits. If the provider quota is exhausted, the run may fail. No paid fallback is configured.
