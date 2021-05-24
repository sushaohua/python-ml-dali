import mldali
import asyncio
import logging




async def main():
  logging.basicConfig(level=logging.INFO)
  shade = mldali.MLDaliShade(46)
  await shade.close()
  await asyncio.sleep(10)
  await shade.stop()
  await asyncio.sleep(3)
  await shade.close()
  await asyncio.sleep(50)
  await shade.open()
  await asyncio.sleep(120)

asyncio.run(main())
