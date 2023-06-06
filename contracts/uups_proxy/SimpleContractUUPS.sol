// SPDX-License-Identifier: MIT
// OpenZeppelin Contracts (last updated v4.7.0) (proxy/transparent/TransparentUpgradeableProxy.sol)

pragma solidity ^0.8.0;

import "@openzeppelin/contracts/proxy/utils/UUPSUpgradeable.sol";
import "../shared_contracts/SimpleContract.sol";

contract SimpleContractUUPS is UUPSUpgradeable, SimpleContract {
    function _authorizeUpgrade(address) internal override {}

    function upgradeTo(
        address newImplementation
    ) public virtual override onlyProxy {
        _authorizeUpgrade(newImplementation);
        _upgradeToAndCallUUPS(newImplementation, new bytes(0), false);
    }
}
