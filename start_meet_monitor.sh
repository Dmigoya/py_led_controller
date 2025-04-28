#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

nohup python3 "$DIR/meet_led_monitor.py" > "$DIR/meet_monitor.log" 2>&1 &

echo $! > "$DIR/meet_monitor.pid"
echo "Meet monitor started in background. PID: $(cat $DIR/meet_monitor.pid)"
echo "Logs will be written to: $DIR/meet_monitor.log" 