from brownie import network, config, accounts, DavidHasAnxietyToken

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]
OPENSEA_URL = "https://testnets.opensea.io/assets/{}/{}"
SAMPLE_OPENSEA_URL = "https://testnets.opensea.io/assets/0xf1b51ab503d2d8cb8b9dcc91968a65c5b5b3e4de/0"

token_uri = "https://ipfs.io/ipfs/Qma4djMdHqTvhhFXcapMDMMRHXBDVittCphMKFrZumdZgD?filename=covid.json"

def get_account(index=None, id=None):
    if index: 
        return accounts[index]
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS: 
        return accounts[0]
    if id:
        return accounts.load(id)
    return accounts.add(config["wallets"]["from_key"])

def main():
    print(network.show_active())
    account = get_account()
    print(account)
    smart_contract = DavidHasAnxietyToken.deploy({"from": account})
    tx = smart_contract.createCollectible(token_uri, {"from": account})
    tx.wait(1)



