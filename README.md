# py_led_controller

A Python application that monitors Google Meet tabs in Safari and controls an LED strip via Bluetooth. The LED turns red when a Meet tab is active, providing a visual indicator of meeting status. Perfect for home office setups to avoid interruptions during meetings.

## Features

- Monitors Safari tabs for Google Meet
- Controls LED strip via Bluetooth
- Non-intrusive monitoring (doesn't force Safari to open)
- Background operation with proper logging
- Easy start/stop scripts

## Open Source

This project is open source and released under the MIT License. Being open source means:

- 🆓 Free to use for any purpose
- 🔧 Free to modify and adapt
- 📦 Free to distribute
- 🔍 Free to inspect the code
- 🤝 Free to contribute

We welcome contributions from the community! Whether it's:
- Bug fixes
- New features
- Documentation improvements
- Code optimizations
- Or any other enhancements

## Requirements

- Python 3.9+
- macOS (for Safari monitoring)
- Bluetooth-enabled LED strip (ELK-BLEDOB compatible)
- Required Python packages:
  - bleak
  - asyncio

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/py_led_controller.git
cd py_led_controller
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## Configuration

The default configuration uses the following settings:
- LED device address: "61C008D6-5838-2D1B-F300-86F1AAFB172B"
- Check interval: 1 second
- Pleasant color: Soft blue (0, 100, 255)
- Meet detection color: Red (255, 0, 0)

To modify these settings, edit the respective values in `meet_led_monitor.py`.

## Usage

### Starting the Monitor

To start the monitor in the background:
```bash
./start_meet_monitor.sh
```

This will:
- Start the monitor in the background
- Create a log file (meet_monitor.log)
- Save the process ID for later stopping

### Stopping the Monitor

To stop the monitor:
```bash
./stop_meet_monitor.sh
```

### Checking Status

The monitor's status and all events are logged in `meet_monitor.log`. You can check the current status with:
```bash
tail -f meet_monitor.log
```

## Project Structure

- `meet_led_monitor.py`: Main application file
- `led_controller.py`: LED strip control module
- `safari_controller.py`: Safari monitoring module
- `start_meet_monitor.sh`: Script to start the monitor
- `stop_meet_monitor.sh`: Script to stop the monitor
- `meet_monitor.log`: Log file (created when running)
- `meet_monitor.pid`: Process ID file (created when running)

## How It Works

1. The monitor checks Safari tabs every second
2. If a Google Meet tab is found:
   - LED turns red
   - Status is logged
3. If no Meet tabs are found:
   - LED returns to pleasant blue
   - Status is logged
4. All events are logged with timestamps

## Troubleshooting

### Common Issues

1. LED not connecting:
   - Check if the device address is correct
   - Ensure Bluetooth is enabled
   - Verify the LED strip is powered on

2. Safari monitoring not working:
   - Ensure Safari is running
   - Check if you have permission to control Safari
   - Verify the script has necessary permissions

3. Script not starting:
   - Make sure the scripts are executable:
     ```bash
     chmod +x start_meet_monitor.sh
     chmod +x stop_meet_monitor.sh
     ```

### Logs

Check `meet_monitor.log` for detailed information about:
- Connection status
- Meet detection
- LED color changes
- Any errors or warnings

## Contributing

We love your input! We want to make contributing to this project as easy and transparent as possible, whether it's:

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features
- Becoming a maintainer

### How to Contribute

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

The MIT License is a permissive license that is short and to the point. It lets people do anything they want with your code as long as they provide attribution back to you and don't hold you liable.

## Acknowledgments

- Thanks to all contributors who have helped this project grow
- Inspired by the need for better meeting awareness
- Built with open source tools and libraries
 
