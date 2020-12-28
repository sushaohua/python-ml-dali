import asyncio
from MLDali import MLDaliLight

async def turnOnOff(address):
    light_fixture = MLDaliLight(address)
    await asyncio.sleep(1)
    await light_fixture.turn_on()
    await asyncio.sleep(3)
    await light_fixture.turn_off()

async def turnOnOffDelayed(address):
    await asyncio.sleep(2)
    light_fixture = MLDaliLight(address)
    await asyncio.sleep(1)
    await light_fixture.turn_on()
    await asyncio.sleep(1)
    await light_fixture.turn_off()


async def main():
    await asyncio.gather(turnOnOff(12), turnOnOffDelayed(13), asyncio.sleep(20))


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
