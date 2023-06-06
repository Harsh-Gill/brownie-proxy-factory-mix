// SPDX-License-Identifier: MIT
// OpenZeppelin Contracts (last updated v4.7.0) (proxy/transparent/TransparentUpgradeableProxy.sol)

pragma solidity ^0.8.0;

import "@openzeppelin/contracts/proxy/ERC1967/ERC1967Proxy.sol";
import "@openzeppelin/contracts/proxy/utils/UUPSUpgradeable.sol";
import "../shared_contracts/SimpleContractV2.sol";

contract SimpleContractUUPSV2 is UUPSUpgradeable, SimpleContractV2 {
    function _authorizeUpgrade(address) internal override {}

    function upgradeTo(
        address newImplementation
    ) public virtual override onlyProxy {
        _authorizeUpgrade(newImplementation);
        _upgradeToAndCallUUPS(newImplementation, new bytes(0), false);
    }
}
