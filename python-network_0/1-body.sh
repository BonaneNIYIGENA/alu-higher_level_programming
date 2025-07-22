#!/bin/bash
# Sends GET request and displays body only for status 200
curl -s -o /tmp/body -w "%{http_code}" "$1" | { read status; [ "$status" -eq 200 ] && cat /tmp/body; }
