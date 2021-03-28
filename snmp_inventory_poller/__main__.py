import argparse
import asyncio
import csv

import aiosnmp

from .poller import Poller

parser = argparse.ArgumentParser(description='SNMP inventory poller')

host_group = parser.add_mutually_exclusive_group()
host_group.add_argument('--host', help="host to poll")
host_group.add_argument('--file', help="CSV file with hosts")
parser.add_argument('--community', help='SNMP v2 community', default='public')
args = vars(parser.parse_args())


async def poll_v2(host: str, community: str, port=161):
    async with aiosnmp.Snmp(host=host, port=port, community=community) as snmp:
        p = Poller(snmp)
        try:
            sysname = await p.poll_sysname()
            platform = await p.poll_platform()
            mac = await p.poll_mac()
            interfaces = await p.poll_interfaces()
        except Exception as e:
            print(f'{host} error: {e}')
        else:
            up_ports = [v for v in interfaces.values() if v.lower() == 'up']
            print(f'{sysname};{host};{platform};{mac};{len(up_ports)}')


async def run_poller():
    host = args['host']
    file = args['file']
    if host is not None:
        await poll_v2(host, args['community'])
    if file is not None:
        with open(file, newline='') as f:
            reader = csv.reader(f)
            tasks = [poll_v2(*row[0].split(';')) for row in reader]
            await asyncio.gather(*tasks)


def main():
    asyncio.run(run_poller())
