# import needed libraries
from brownie import TransparentUpgradeableProxy,ProxyAdmin, Contract, accounts, network, config,SimpleContract, SimpleContractV2
import time

# all contracts will be deployed by accounts[0] by default

# Object to manage the entire work flow
class TransparentUpgradeableProxyDeployer:
    def __init__(self, implementation_cotract_code, implementation_initialize_args):
        self.implementation_contract_code = implementation_cotract_code
        self.implementation_initialize_args = implementation_initialize_args
        self.implementation_contract_object = None
        self.implementation_contract_name = "SimpleContract"
        self.admin_contract_object = None
        self.proxy_contract_object= None

    def deploy(self):
        self.deploy_admin_contract()
        self.deploy_implementation_contract()
        self.deploy_proxy_contract()

    def deploy_admin_contract(self):
        print("Deploying Admin")
        self.admin_contract_object = ProxyAdmin.deploy( {'from': accounts[0]})
        return self.admin_contract_object

    def deploy_implementation_contract(self):
        print("Deploying Implementation")
        self.implementation_contract_object = self.implementation_contract_code.deploy( 
            {'from': accounts[0]}
            )
        return self.implementation_contract_object

    def deploy_proxy_contract(self):
        print("Deploying Proxy")
        self.proxy_contract_object = TransparentUpgradeableProxy.deploy(
            self.implementation_contract_object.address,
            self.admin_contract_object.address,
            self.implementation_contract_object.initialize.encode_input(self.implementation_initialize_args),
            {'from': accounts[0]}
            )
        return self.proxy_contract_object

    def upgrade_proxy_contract(self,new_implementation_code, new_implementation_address,new_contract_name):
        print("Upgrading Proxy")
        self.implementation_contract_code = new_implementation_code
        self.implementation_contract_object = new_implementation_code.at(new_implementation_address)
        self.implementation_contract_name = new_contract_name
        upgrade_txn = self.admin_contract_object.upgrade(self.proxy_contract_object, new_implementation_address, {'from': accounts[0]})
        time.sleep(1)
        return upgrade_txn
 
    def interact_with_proxy_contract(self,call_function):
        print("Interacting With Proxy")
        # load from implementation_contract_object abi
        current_proxy_logic = Contract.from_abi(self.implementation_contract_name , self.proxy_contract_object.address, self.implementation_contract_object.abi)
        
        if call_function == "setValue":
            txn_receipt = current_proxy_logic.setValue(456, {'from': accounts[0]})
        elif call_function == "getValue":
            txn_receipt = current_proxy_logic.getValue({'from': accounts[0]})
        else:
            print("Undefined Function Call!")
            return
        time.sleep(1)
        return txn_receipt

def main():
    deployer_object = TransparentUpgradeableProxyDeployer(SimpleContract, 123)
    deployer_object.deploy()

    # Interact with original function
    deployer_object.interact_with_proxy_contract("getValue")
    time.sleep(1)

    # try and check that setValue function is not available
    try:
        deployer_object.interact_with_proxy_contract("setValue")
    except:
        print("As expected setValue function is not available")

    # DEPLOY SimpleContractV2
    simple_contract_v2 = SimpleContractV2.deploy({'from': accounts[0]})
    time.sleep(1)

    # UPGRADE PROXY CONTRACT
    deployer_object.upgrade_proxy_contract(SimpleContractV2,simple_contract_v2.address,"SimpleContractV2")
    time.sleep(1)

    # Interact with new function
    deployer_object.interact_with_proxy_contract("setValue")
    time.sleep(1)


