# Setup — zero-hosting mode

This workspace runs FreeLLMAPI and Hermes together inside each GitHub Actions job. Both are temporary: the gateway starts for the job and is discarded when it ends. No VPS, paid hosting, local model, or permanent public endpoint is required.

## Step 1 — Create a free provider key

Recommended first provider: Google Gemini through Google AI Studio.

1. Open [Google AI Studio API keys](https://aistudio.google.com/app/apikey).
2. Sign in and create/copy an API key.
3. Check the current [Gemini API pricing and free-tier limits](https://ai.google.dev/gemini-api/docs/pricing). Select a model that is currently available in the free tier. Do not enable paid billing for this zero-budget setup.

Google's free tier has model and rate limits, and its pricing page states that free-tier content may be used to improve Google's products. Review Google's terms before sending private material.

## Step 2 — Add one GitHub secret

Open **Repository → Settings → Secrets and variables → Actions → New repository secret**.

Name:
`FREEAPI_CONFIG_JSON`

Value (replace the email, password and API key; keep valid JSON):

```json
{
  "admin": {
    "email": "your-email@example.com",
    "password": "choose-a-unique-password"
  },
  "keys": [
    {
      "platform": "google",
      "key": "PASTE_YOUR_GOOGLE_AI_STUDIO_KEY_HERE",
      "label": "google-free-tier",
      "enabled": true
    }
  ],
  "routing": {
    "strategy": "balanced"
  }
}
```

Use a unique dashboard password of at least 8 characters. Never send the provider key in ChatGPT, commit it to a file, or put it in a workflow input. Store it only as this GitHub Actions secret.

## Step 3 — What happens when a workflow runs

1. GitHub Actions starts a temporary Ubuntu runner.
2. Docker starts the official FreeLLMAPI container with a temporary database and encryption key.
3. The workflow reads the generated unified API key from the temporary SQLite settings database.
4. Hermes is installed and configured with the local gateway using the official `freellmapi setup-hermes` command.
5. Hermes generates the requested output; the output is uploaded as a workflow artifact.
6. The runner, gateway, and temporary database are discarded when the job ends. Provider keys remain only in the GitHub Actions secret.

## Step 4 — Run a YouTube pack

Open **Actions → YouTube Documentary Pack → Run workflow**. Select Hindi or English, enter the topic and angle, and leave model as `auto` initially. Download the `youtube-production-pack` artifact after a successful run.

The output is a written production pack, not a rendered video. Human review and editing are still required; publishing is never automatic.

## Free-first limits

GitHub Actions usage and provider free quotas are subject to account/provider limits. If the provider quota is exhausted or a model is unavailable in the free tier, the run may fail. No paid fallback is configured.
