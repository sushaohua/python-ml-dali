from .. import mldali
import asyncio
import logging

shade = mldali.MLDaliShade(42)

async def main():
  logging.basicConfig(level=logging.INFO)
  await shade.close()
  await asyncio.sleep(10)
  await shade.stop()
  await asyncio.sleep(3)
  await shade.close()
  await shade.close(50)
  await shade.open()

asyncio.run(main())