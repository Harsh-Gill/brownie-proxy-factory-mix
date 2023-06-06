# import needed libraries
from brownie import TransparentUpgradeableProxy,ProxyAdmin, Contract, accounts, network, config,SimpleContract, SimpleContractV2,UpgradeableBeacon,SimpleFactory
import time

# all contracts will be deployed by accounts[0] by default

# Object to manage the entire work flow
class FacotryBeaconProxyDeployer:
    def __init__(self, implementation_contract_code, implementation_initialize_args):
        self.implementation_contract_code = implementation_contract_code
        self.implementation_initialize_args = implementation_initialize_args
        self.implementation_contract_object = None
        self.implementation_contract_name = "SimpleContract"

        self.factory_contract_object = None
        self.upgradeable_beacon_contract_object= None
        self.deployed_beacon_proxy_object_list = []

    def deploy(self):
        self.deploy_implementation_contract()
        self.deploy_upgradeable_beacon_contract()
        self.deploy_factory_contract()
        self.deploy_beacon_proxy_contract()

    def deploy_implementation_contract(self):
        print("Deploying Implementation")
        self.implementation_contract_object = self.implementation_contract_code.deploy( 
            {'from': accounts[0]}
            )
        return self.implementation_contract_object

    def deploy_upgradeable_beacon_contract(self):
        print("Deploying Upgradeable Beacon")
        self.upgradeable_beacon_contract_object = UpgradeableBeacon.deploy(
            self.implementation_contract_object.address,
            {'from': accounts[0]}
            )
        return self.upgradeable_beacon_contract_object

    def deploy_factory_contract(self):
        print("Deploying Factory")
        self.factory_contract_object = SimpleFactory.deploy(
            self.upgradeable_beacon_contract_object.address,
            {'from': accounts[0]}
            )

    def deploy_beacon_proxy_contract(self,num_of_proxy_to_deploy = 3):
        for i in range(num_of_proxy_to_deploy):
            latest_beacon_proxy_index = len(self.deployed_beacon_proxy_object_list)
            print("Deploying Beacon Proxy: ",i)
            deploy_beacon_proxy_contract = self.factory_contract_object.createSimpleContractProxy(
                latest_beacon_proxy_index,
                {'from': accounts[0]}
                )
            # from factory contract get simpleContractAddresses variable
            beacon_proxy_address = self.factory_contract_object.simpleContractAddresses.call(latest_beacon_proxy_index)
            # load BeaconProxy contract from abi
            beacon_proxy_contract = Contract.from_abi("SimpleContract", beacon_proxy_address, SimpleContract.abi)
            self.deployed_beacon_proxy_object_list.append(beacon_proxy_contract)

            time.sleep(1)
            
    def upgrade_upgradeable_beacon_proxy_contract(self,new_implementation_code, new_implementation_address,new_contract_name):
        print("Upgrading Proxy")
        self.implementation_contract_code = new_implementation_code
        self.implementation_contract_object = new_implementation_code.at(new_implementation_address)
        self.implementation_contract_name = new_contract_name
        upgrade_txn = self.upgradeable_beacon_contract_object.upgradeTo(new_implementation_address, {'from': accounts[0]})
        time.sleep(1)
        return upgrade_txn

    def interact_with_proxy_contract(self,call_function,proxy_index = 0):
        print("Interacting With Proxy of index: ",proxy_index)

        # get address of proxy_index from list self.deployed_beacon_proxy_object_list
        selected_proxy_contract = self.deployed_beacon_proxy_object_list[proxy_index]
        print("Proxy has address: ",selected_proxy_contract.address)

        # load from implementation_contract_object abi
        current_proxy_logic = Contract.from_abi(self.implementation_contract_name , selected_proxy_contract.address, self.implementation_contract_object.abi)

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
    deployer_object = FacotryBeaconProxyDeployer(SimpleContract, 123)
    deployer_object.deploy()

    # Interact with original function of all deployed proxies
    for i in range(len(deployer_object.deployed_beacon_proxy_object_list)):
        deployer_object.interact_with_proxy_contract("getValue",i)
        time.sleep(1)
        
        # try and check that setValue function is not available
        try:
            deployer_object.interact_with_proxy_contract("setValue",i)
        except:
            print("As expected setValue function is not available")

    # DEPLOY SimpleContractV2
    simple_contract_v2 = SimpleContractV2.deploy({'from': accounts[0]})
    time.sleep(1)

    # UPGRADE UPGRADABLE BEACON PROXY CONTRACT
    deployer_object.upgrade_upgradeable_beacon_proxy_contract(SimpleContractV2,simple_contract_v2.address,"SimpleContractV2")

    # Interact with new function of all deployed proxies
    for i in range(len(deployer_object.deployed_beacon_proxy_object_list)):
        deployer_object.interact_with_proxy_contract("setValue",i)
        time.sleep(1)


