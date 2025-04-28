import asyncio
import logging
from bleak import BleakClient, BleakScanner

class LEDController:
    def __init__(self, device_address="61C008D6-5838-2D1B-F300-86F1AAFB172B"):
        self.device_address = device_address
        self.client = None
        self.notification_characteristic = "0000fff4-0000-1000-8000-00805f9b34fb"
        self.write_characteristic = "0000fff3-0000-1000-8000-00805f9b34fb"
        
        # ELK-BLEDOB specific commands
        self.TURN_ON_CMD = bytearray.fromhex("7e 07 04 ff 00 01 02 01 ef")
        self.TURN_OFF_CMD = bytearray.fromhex("7e 07 04 00 00 00 02 01 ef")

    async def connect(self):
        """Connects to the LED device"""
        try:
            self.client = BleakClient(self.device_address)
            await self.client.connect()
            logging.info(f"Connected to LED device: {self.device_address}")
            return True
        except Exception as e:
            logging.error(f"Connection error: {str(e)}")
            return False

    async def disconnect(self):
        """Disconnects from the LED device"""
        if self.client and self.client.is_connected:
            await self.client.disconnect()
            logging.info("Disconnected from LED device")

    async def turn_on(self):
        """Turns on the LED strip"""
        if not self.client or not self.client.is_connected:
            logging.warning("Not connected to device")
            return False
        
        try:
            await self.client.write_gatt_char(self.write_characteristic, self.TURN_ON_CMD)
            logging.info("LED strip turned on")
            return True
        except Exception as e:
            logging.error(f"Error turning on: {str(e)}")
            return False

    async def turn_off(self):
        """Turns off the LED strip"""
        if not self.client or not self.client.is_connected:
            logging.warning("Not connected to device")
            return False
        
        try:
            await self.client.write_gatt_char(self.write_characteristic, self.TURN_OFF_CMD)
            logging.info("LED strip turned off")
            return True
        except Exception as e:
            logging.error(f"Error turning off: {str(e)}")
            return False

    async def set_color(self, r, g, b):
        """
        Sets the color of the LED strip
        :param r: Red value (0-255)
        :param g: Green value (0-255)
        :param b: Blue value (0-255)
        """
        if not self.client or not self.client.is_connected:
            logging.warning("Not connected to device")
            return False
        
        try:
            color_data = bytearray.fromhex("7e 07 05 03 ff 00 00 10 ef")
            color_data[4] = r
            color_data[5] = g
            color_data[6] = b
            
            await self.client.write_gatt_char(self.write_characteristic, color_data)
            logging.info(f"Color set: RGB({r}, {g}, {b})")
            await asyncio.sleep(0.1)
            return True
        except Exception as e:
            logging.error(f"Error setting color: {str(e)}")
            return False

async def main():
    controller = LEDController()
    if await controller.connect():
        try:
            await controller.set_color(255, 0, 0)
            await asyncio.sleep(2)
        finally:
            await controller.disconnect()

if __name__ == "__main__":
    asyncio.run(main())

