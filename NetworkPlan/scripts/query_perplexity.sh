#!/bin/bash
# Query Perplexity API for network equipment research
# Usage: ./query_perplexity.sh <topic> <output_file>

set -euo pipefail

# Load API key from .env
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"
ENV_FILE="$ROOT_DIR/.env"

if [ ! -f "$ENV_FILE" ]; then
    echo "Error: .env file not found at $ENV_FILE"
    exit 1
fi

# Extract API key
API_KEY=$(grep PERPLEXITY_API_KEY "$ENV_FILE" | cut -d'=' -f2)

if [ -z "$API_KEY" ]; then
    echo "Error: PERPLEXITY_API_KEY not found in .env"
    exit 1
fi

TOPIC="$1"
OUTPUT_FILE="$2"
PROMPT="$3"

# Create research directory
mkdir -p "$ROOT_DIR/research"

echo "Querying Perplexity API for: $TOPIC"

# Build JSON payload
JSON_PAYLOAD=$(cat <<EOF
{
  "model": "sonar-pro",
  "messages": [
    {
      "role": "system",
      "content": "You are a helpful research assistant specializing in UK technology procurement. Provide detailed, accurate information with current pricing and purchase links. Today's date is November 14, 2025."
    },
    {
      "role": "user",
      "content": $(echo "$PROMPT" | jq -Rs .)
    }
  ],
  "temperature": 0.2,
  "max_tokens": 4000
}
EOF
)

# Query API
RESPONSE=$(curl -s -X POST "https://api.perplexity.ai/chat/completions" \
    -H "Authorization: Bearer $API_KEY" \
    -H "Content-Type: application/json" \
    -d "$JSON_PAYLOAD")

# Check for errors
if echo "$RESPONSE" | jq -e '.error' > /dev/null 2>&1; then
    echo "API Error:"
    echo "$RESPONSE" | jq '.error'
    exit 1
fi

# Extract content
CONTENT=$(echo "$RESPONSE" | jq -r '.choices[0].message.content')

# Save to markdown file
cat > "$OUTPUT_FILE" <<EOF
# ${TOPIC//_/ }

*Research conducted: $(date -u +"%Y-%m-%d %H:%M UTC")*

$CONTENT
EOF

echo "✓ Saved research to $OUTPUT_FILE"
