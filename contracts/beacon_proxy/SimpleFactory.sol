// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.8.0;

import "./BeaconProxy.sol";
import "./UpgradeableBeacon.sol";
import "../shared_contracts/Proxy.sol";
import "../shared_contracts/SimpleContract.sol";

contract SimpleFactory {
    address[] public simpleContractAddresses;
    UpgradeableBeacon public beacon;

    // constructor to define the UpgradeableBeacon address
    constructor(address _beacon) {
        beacon = UpgradeableBeacon(_beacon);
    }

    // create a new BeaconProxy and use SimpleContract to build initialize function with value as length of simpleContractAddresses then add as argument to BeaconProxy constructor
    function createSimpleContractProxy(uint256 initialValue) public {
        address simpleContractAddress = address(
            new BeaconProxy(
                address(beacon),
                abi.encodeWithSignature("initialize(uint256)", initialValue)
            )
        );
        simpleContractAddresses.push(simpleContractAddress);
    }
}
