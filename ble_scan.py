import asyncio
from bleak import BleakScanner

async def scan_devices():
    print("Escaneando dispositivos BLE...")
    devices = await BleakScanner.discover()
    for d in devices:
        print(f"\nDispositivo encontrado:")
        print(f"Nombre: {d.name}")
        print(f"Dirección MAC: {d.address}")
        print(f"RSSI: {d.rssi} dBm")
        print(f"Metadata: {d.metadata}")
        print("-" * 50)


