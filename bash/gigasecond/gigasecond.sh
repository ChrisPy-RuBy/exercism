#!/usr/bin/env bash
echo "$(date -d 1977-06-13 +%s) + 1000000000" | bc -l | xargs -I % date -d @%
