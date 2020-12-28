import aioserial
import asyncio
import serial

class MLDaliController:
    __instance__ = None

    def __init__(self, port, baudrate, parity, stopbits, bytesize, timeout):
        """ Constructor.
        """

        if MLDaliController.__instance__ is None:
            self._ser = aioserial.AioSerial(
                                        port = port,
                                        baudrate = baudrate,
                                        timeout = timeout,
                                        parity = parity,
                                        stopbits = stopbits,
                                        bytesize = bytesize
                                    )
            self._register = {}
            MLDaliController.__instance__ = self

    
    @staticmethod
    def get_instance(port = "COM4", 
                    baudrate = 9600, 
                    parity = serial.PARITY_NONE, 
                    stopbits = serial.STOPBITS_ONE, 
                    bytesize = serial.EIGHTBITS, 
                    timeout = None) -> 'MLDaliController': #see why this needs to be quoted: https://stackoverflow.com/questions/36286894/name-not-defined-in-type-annotation
        """ Static method to fetch the current instance
        """
        if not MLDaliController.__instance__:
            MLDaliController(port, baudrate, parity, stopbits, bytesize, timeout)
        return MLDaliController.__instance__
    
    def register_component(self, component):
        self._register[(component.address*2)+1] = component

    def open(self):
        self._ser.open()
    
    def close(self):
        self._ser.close()
    
    async def monitor(self):
        print("Start Monitoring")
        cmd = bytes()
        while True:
            rx = await self._ser.read_async(1)
            print(f"Observed: {rx}")
            if rx == b'\x02' or rx == b'\x04':
                cmd = rx
            else:
                cmd += rx
            
            if len(cmd) == 3:
                address = int.from_bytes(cmd[1:2],'big')
                component = self._register.get(address, None)
                if component:
                    component.status_update(cmd[2:3])

    async def read_byte(self):
        rx = await self._ser.read_async(3)
        return rx
    
    async def sendCmd(self, tx):
        await self._ser.write_async(tx)
