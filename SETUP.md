# Setup — FreeLLMAPI + Hermes (mobile-friendly)

The repository now includes a temporary FreeLLMAPI host workflow. It starts the official FreeLLMAPI Docker image on a GitHub Actions runner and exposes it through a temporary HTTPS tunnel. You can start and stop it from the GitHub mobile app.

The default model is `auto`. You do not need a provider/model key just to create the gateway account or obtain its unified API key. Real chat generation will work after a provider is enabled later.

## 1. Add admin login secrets once

Open **Repository → Settings → Secrets and variables → Actions → New repository secret** and add:

- `FREELLMAPI_ADMIN_EMAIL` — the email you want to use for the FreeLLMAPI dashboard.
- `FREELLMAPI_ADMIN_PASSWORD` — a strong password of at least 8 characters.

These are used to provision the first dashboard account. They are not provider keys and are not printed in workflow logs.

## 2. Start the FreeLLMAPI host

In GitHub mobile:

1. Open this repository → **Actions**.
2. Select **FreeLLMAPI Temporary Host**.
3. Tap **Run workflow** and keep model as `auto`.
4. Open the completed/running workflow run and expand **Summary**.
5. Copy the HTTPS Dashboard / API address shown there.

The host stays online while that workflow run is active. Stop the run when finished. This is a temporary session, not persistent hosting; a new run creates a fresh instance.

## 3. Get the unified API key

Open the HTTPS address from the workflow Summary and sign in with the admin email/password you saved in Step 1. On the FreeLLMAPI Keys page, copy the unified API key from the page header.

The unified key is the gateway credential. It is separate from any provider/model key.

## 4. Connect the repository workflows

Add these two more repository Actions secrets:

- `FREELLMAPI_BASE_URL` — the HTTPS address from the workflow Summary, without a trailing slash and without `/v1`.
- `FREELLMAPI_API_KEY` — the unified API key from the FreeLLMAPI dashboard.

Then run **Actions → FreeLLMAPI Connection Check** with model `auto`. After it passes, run **Hermes Task** or **YouTube Documentary Pack**.

## 5. Add a model later

When ready, add a provider key/model inside the FreeLLMAPI dashboard. The unified API key remains the gateway key; it is not a replacement for a provider key.

## Free-first notes

- Official image: `ghcr.io/tashfeenahmed/freellmapi:latest`.
- Data is held in the runner's Docker volume for that session; this temporary host does not provide durable storage between runs.
- No paid provider fallback is configured.
