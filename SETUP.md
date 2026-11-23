# Setup — connect FreeLLMAPI first, add models later

This workspace connects Hermes to an already-running FreeLLMAPI instance. You do **not** need to add a provider/model key just to test the connection. The initial model setting is `auto`.

Important distinction: FreeLLMAPI is an API gateway/router, not an inference model itself. Its unified API key authenticates requests to the gateway. Actual chat generation needs at least one provider key/model enabled in that FreeLLMAPI instance. Until then, the workflow can verify the gateway, authentication, and model catalog, but a real chat test may return “no available provider/model”.

## Step 1 — FreeLLMAPI must be running

Start FreeLLMAPI wherever you intend to host it. It must remain reachable from GitHub Actions over HTTPS while a workflow runs. A local-only `localhost` address on your phone/computer will not be reachable from GitHub's cloud runner.

In the FreeLLMAPI dashboard, copy:
- the reachable HTTPS server URL (base URL, without `/v1`)
- the unified API key from the Keys page

The unified key is not a provider key. You can add provider keys/models later in the FreeLLMAPI dashboard.

## Step 2 — Add two GitHub Actions secrets

Open **Repository → Settings → Secrets and variables → Actions → New repository secret**.

1. `FREELLMAPI_BASE_URL` — your reachable HTTPS FreeLLMAPI URL, e.g. `https://your-host.example` (do not use the example literally).
2. `FREELLMAPI_API_KEY` — the unified API key copied from the FreeLLMAPI dashboard.

Never paste the API key into workflow inputs, source files, or chat.

## Step 3 — Test the connection first

Open **Actions → FreeLLMAPI Connection Check → Run workflow**. Leave model as `auto`.

This checks:
- HTTPS endpoint reachability
- unified-key authentication against `/v1/models`
- model catalog response
- optional real chat inference

If no provider/model is configured yet, catalog/auth can pass while the chat probe reports that no model is available. That is expected; add a provider key/model later in FreeLLMAPI and rerun the check.

## Step 4 — Run Hermes

After connection check passes, open **Actions → Hermes Task → Run workflow** or **YouTube Documentary Pack → Run workflow**. Leave model as `auto` to let FreeLLMAPI choose from the enabled pool.

Hermes is installed in the temporary GitHub Actions runner and configured using the official `freellmapi setup-hermes` command. The runner does not host FreeLLMAPI; it connects to your reachable instance.

## Free-first limits
GitHub Actions and upstream provider quotas have limits. No paid fallback is configured. A successful gateway check alone does not prove a model can generate until at least one provider is enabled.
