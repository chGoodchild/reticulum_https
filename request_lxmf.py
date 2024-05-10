from lxmf_wrapper_client import LXMFWrapperClient, LXMFProxy

# Initialize the client
client = LXMFWrapperClient()

identitypath = configdir + "/identity/lxmfclient"
if os.path.exists(identitypath):
    self.ID = RNS.Identity.from_file(identitypath)
else:
    self.ID = RNS.Identity()
    self.ID.to_file(identitypath)
    print(f"Created new identity and saved key to {identitypath}...")


# Send a message
await client.send_lxmf_message(
    destination="destination_hex",
    content="Your message or HTTP request details",
    fields={"method": "GET", "headers": {"User-Agent": "MyApp"}},
    delivery_callback=my_delivery_callback,
    failed_callback=my_failed_callback,
    reply_callback=my_reply_callback
)



# Assuming `client` is an instance of `LXMFWrapperClient`
proxy = LXMFProxy(lxmf_wrapper_client=client, mappings={
    'http://example.com/api': 'destination_hex'
})


response = await proxy.get('http://example.com/api/resource')
print(response.text())

