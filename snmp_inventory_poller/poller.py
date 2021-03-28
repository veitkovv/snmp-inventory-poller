from aiosnmp import Snmp


class Poller:
    SYSNAME = '.1.3.6.1.2.1.1.5.0'
    MAC = '.1.3.6.1.2.1.17.1.1.0'
    PLATFORM = '.1.3.6.1.2.1.47.1.1.1.1.13.1'
    IFNAME = '.1.3.6.1.2.1.31.1.1.1.1'
    IFOPERSTATUS = '.1.3.6.1.2.1.2.2.1.8'

    def __init__(self, snmp: Snmp):
        self.snmp = snmp

    async def poll_sysname(self):
        sysname, = await self.snmp.get(self.SYSNAME)
        return sysname.value.decode()

    async def poll_platform(self):
        platform, = await self.snmp.get(self.PLATFORM)
        return platform.value.decode()

    async def poll_mac(self):
        mac, = await self.snmp.get(self.MAC)
        return mac.value.hex()

    async def poll_interfaces(self):
        def get_status(v: int) -> str:
            return {1: "up", 2: "down", 3: "testing"}.get(v, "not detected")

        names = await self.snmp.walk(self.IFNAME)
        statuses = await self.snmp.walk(self.IFOPERSTATUS)
        return {name.value.decode(): get_status(status.value) for name, status
                in zip(names, statuses)}
