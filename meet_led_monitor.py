import asyncio
import logging
from safari_controller import SafariController
from led_controller import LEDController

# Configure logging
logging.basicConfig(
    filename='meet_monitor.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class MeetLEDMonitor:
    def __init__(self):
        self.safari = SafariController()
        self.led = LEDController()
        self.is_meet_active = False
        self.pleasant_color = (0, 100, 255)  # Soft blue

    async def check_meet_status(self):
        """
        Checks if there's a Meet tab open in Safari
        :return: True if Meet is active, False otherwise
        """
        tabs = self.safari.get_tabs()
        return any("Meet" in tab for tab in tabs)

    async def update_led_color(self):
        """
        Updates LED color based on Meet status
        """
        meet_active = await self.check_meet_status()
        
        if meet_active != self.is_meet_active:
            self.is_meet_active = meet_active
            if meet_active:
                await self.led.set_color(255, 0, 0)
                logging.info("Meet detected - LED set to red")
            else:
                await self.led.set_color(*self.pleasant_color)
                logging.info("Meet not detected - LED set to pleasant color")

    async def run(self, check_interval=1.0):
        """
        Main monitoring loop
        :param check_interval: Time between checks in seconds
        """
        if await self.led.connect():
            try:
                logging.info("Starting Meet LED monitor...")
                while True:
                    await self.update_led_color()
                    await asyncio.sleep(check_interval)
            except KeyboardInterrupt:
                logging.info("Stopping monitor...")
            finally:
                await self.led.disconnect()

async def main():
    monitor = MeetLEDMonitor()
    await monitor.run()

if __name__ == "__main__":
    asyncio.run(main()) 