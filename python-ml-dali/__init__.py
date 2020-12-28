import aioserial
import asyncio
import serial
from controller import MLDaliController
from light import MLDaliLight

async def serial_monitor():
    ctr = MLDaliController.get_instance()
    await ctr.monitor()

async def turnOnOff1(address):
    kastenwand = MLDaliLight(address)
    await asyncio.sleep(1)
    await kastenwand.turn_on()
    await asyncio.sleep(1)
    await kastenwand.turn_off()

async def turnOnOffDelayed(address):
    await asyncio.sleep(5)
    kastenwand = MLDaliLight(address)
    await asyncio.sleep(1)
    await kastenwand.turn_on()
    await asyncio.sleep(1)
    await kastenwand.turn_off()


async def main():
    await asyncio.gather(serial_monitor(), turnOnOff1(12), turnOnOffDelayed(13))

asyncio.run(main())
