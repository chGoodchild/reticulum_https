
identitypath = configdir + "/identity/lxmfserver"
if os.path.exists(identitypath):
    self.ID = RNS.Identity.from_file(identitypath)
else:
    self.ID = RNS.Identity()
    self.ID.to_file(identitypath)
    print(f"Created new identity and saved key to {identitypath}...")


destination_url = "https://logodownload.org/wp-content/uploads/2017/06/bitcoin-logo-1-1.png"
# python3 lxmf_proxy_server.py destination_url <identity_name> [<announce_delay_time>]

