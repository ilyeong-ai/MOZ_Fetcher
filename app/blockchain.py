from web3 import Web3
from app.config import EVM_RPC_URL, TETHER_CONTRACT_ADDRESS
from app.error_handler import CustomException

w3 = Web3(Web3.HTTPProvider(EVM_RPC_URL))

TETHER_ABI = [
    {
        "anonymous": False,
        "inputs": [
            {"indexed": True, "name": "from", "type": "address"},
            {"indexed": True, "name": "to", "type": "address"},
            {"indexed": False, "name": "value", "type": "uint256"}
        ],
        "name": "Transfer",
        "type": "event"
    }
]

tether_contract = w3.eth.contract(address=TETHER_CONTRACT_ADDRESS, abi=TETHER_ABI)

def get_transfer_events(from_block, to_block):
    try:
        transfer_filter = tether_contract.events.Transfer.create_filter(fromBlock=from_block, toBlock=to_block)
        return transfer_filter.get_all_entries()
    except Exception as e:
        raise CustomException(status_code=500, detail=f"Failed to fetch transfer events: {str(e)}")