# Setup

## Runtime model
GitHub Actions runners are temporary. They cannot host a permanent FreeLLMAPI service. This workspace therefore needs a reachable FreeLLMAPI HTTPS endpoint while a workflow runs.

## Repository secrets
Open **Settings → Secrets and variables → Actions → New repository secret** and add:
- `FREELLMAPI_BASE_URL`: HTTPS origin/base URL of your running FreeLLMAPI instance.
- `FREELLMAPI_API_KEY`: unified API key created by that instance.
- `FREELLMAPI_MODEL`: model ID enabled on that instance.

Never commit provider keys, admin passwords, or API keys.

## FreeLLMAPI and Hermes
Deploy FreeLLMAPI using its official documentation, configure at least one provider key, then create its unified API key. The workflow installs Hermes in its temporary runner and uses the official `freellmapi setup-hermes` command to connect it.

A free provider quota does not mean unlimited inference. No paid fallback is configured.

## Run a YouTube pack
Go to **Actions → YouTube Documentary Pack → Run workflow**. Select Hindi or English, enter a topic and angle. Download the `youtube-production-pack` artifact after a successful run.

The workflow produces a written production pack; it does not render a finished video or publish automatically. Human review is required.
