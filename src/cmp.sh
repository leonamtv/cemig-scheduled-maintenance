#!/usr/bin/bash

output=$(python main.py --city $1)

python send_to_telegram.py --token $2 --chat-id $3 --message="$output"