import asyncio
import sys
import time
from lxmf_wrapper_client import LXMFWrapperClient

async def main_event_loop(identity_path, announce_delay_time=1800):
    print("Initializing LXMF Client...")
    client = LXMFWrapperClient(identity_path)  # Assumes LXMFWrapperClient accepts an identity path in its constructor

    while True:
        client.local_lxmf_destination.announce()
        print("Client announced its presence to the network...")
        await asyncio.sleep(announce_delay_time)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 request_lxmf.py <identity_path> [<announce_delay_time>]")
        sys.exit(1)

    identity_path = sys.argv[1]
    announce_delay_time = 1800  # default to 30 minutes
    if len(sys.argv) > 2:
        announce_delay_time = int(sys.argv[2])

    loop = asyncio.get_event_loop()
    loop.set_debug(True)
    loop.run_until_complete(main_event_loop(identity_path, announce_delay_time))
    loop.close()
