#!/bin/bash

# Get the directory where the script is located
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Check if PID file exists
if [ -f "$DIR/meet_monitor.pid" ]; then
    PID=$(cat "$DIR/meet_monitor.pid")
    if ps -p $PID > /dev/null; then
        kill $PID
        echo "Meet monitor stopped (PID: $PID)"
    else
        echo "Meet monitor is not running"
    fi
    rm "$DIR/meet_monitor.pid"
else
    echo "Meet monitor is not running"
fi 