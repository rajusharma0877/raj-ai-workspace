#!/usr/bin/env bash
set -euo pipefail

if ! command -v hermes >/dev/null 2>&1; then
  curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash -s -- --non-interactive
fi

echo
echo "Hermes Agent installation finished."
echo "Next: follow CODESPACES.md to configure Numes, Telegram, and the native Webapp."
