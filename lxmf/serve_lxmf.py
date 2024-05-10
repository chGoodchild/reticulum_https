import asyncio
import RNS
import os
import sys
import time
from lxmf_proxy_server import LXMFWrapperProxy

async def main_event_loop(destination_url, identity_name, announce_delay_time=1800):
    print("Initializing proxy...")
    proxy = LXMFWrapperProxy(destination_url, identity_name)
    print("Listening for requests...")

    while True:
        proxy.send_announce()
        print("Sent announce to the network...")
        await asyncio.sleep(announce_delay_time)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 serve_lxmf.py <destination_url> <identity_name> [<announce_delay_time>]")
        sys.exit(1)

    announce_delay_time = 1800  # default to 30 minutes
    if len(sys.argv) > 3:
        announce_delay_time = int(sys.argv[3])

    loop = asyncio.get_event_loop()
    loop.set_debug(True)
    loop.run_until_complete(main_event_loop(sys.argv[1], sys.argv[2], announce_delay_time))
    loop.close()
