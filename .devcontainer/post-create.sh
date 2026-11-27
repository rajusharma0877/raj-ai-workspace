#!/usr/bin/env bash
set -euo pipefail

if ! command -v hermes >/dev/null 2>&1; then
  curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
fi

echo
echo "Hermes installation step finished."
echo "Next: run 'hermes setup' and configure your model provider."
echo "Then configure messaging with 'hermes gateway setup'."
