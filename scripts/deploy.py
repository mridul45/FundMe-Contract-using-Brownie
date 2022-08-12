from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helpful_scripts import get_account
from web3 import Web3


def deploy_fund_me():

    account = get_account()

    if network.show_active() != "development":
        price_feed_address = config["networks"][network.show_active()][
            "eth-usd-price-feed"
        ]

    else:
        print(f"Active netork is {network.show_active()}")
        print("Deploying Mock...")

		if len(MockV3Aggregator)<=0:
			mock_aggregator = MockV3Aggregator.deploy(
				2000, Web3.toWei("ether"), {"from": account}
			)

        price_feed_address = mock_aggregator.address
        print("Mocks Deployed")

    fund_me = FundMe.deploy(
        "0x8A753747A1Fa494EC906cE90E9f37563A8AF630e",
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract deployed to {fund_me.address}")


def main():
    deploy_fund_me()
