#!/bin/bash
# Pre-pull security tool images to eliminate MCP execution latency

IMAGES=(
    "instrumentisto/nmap"
    "projectdiscovery/nuclei"
    "sqlmap/sqlmap"
)

echo "--- Warming up security tool containers ---"
for img in "${IMAGES[@]}"; do
    echo "Processing: $img"
    docker pull $img > /dev/null 2>&1
done
echo "--- Warmup complete. Tools are ready for low-latency invocation. ---"
