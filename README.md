# upgrade-proxy-factory-mix

A simple implementation of various proxy and factory patterns. To provide a quick overview of current methods and some deployment scripts to get anyone started quickly. This repo is not optimized and meant for direct production, rather as a demonstration and documentation of possible proxy patterns and how to implement them in code.

## Installation

1. [Install Brownie](https://eth-brownie.readthedocs.io/en/stable/install.html), if you haven't already.

2. Download the needed OpenZeppelin modules

   ```bash
   brownie pm install OpenZeppelin/openzeppelin-contracts@4.8.3
   ```

## Basic Use

This mix provides 3 proxy patterns with Objects defined as deployers.

The 3 Patterns are :

- Transparent Proxy Pattern
  The contracts are located in contracts/transparent_upgradeable_proxy/
  The scripts are located in scripts/transparent_upgradeable_proxy/

  To run :

  ```bash
  brownie run scripts/transparent_upgradeable_proxy/deploy.py
  ```

- UUPS Proxy Pattern
  The contracts are located in contracts/uups_proxy/
  The scripts are located in scripts/uups_proxy/

  To run :

  ```bash
  brownie run scripts/uups_proxy/deploy.py
  ```

- Factory Beacon Proxy Pattern
  The contracts are located in contracts/beacon_proxy/
  The scripts are located in scripts/beacon_proxy/

  To run :

  ```bash
  brownie run scripts/beacon_proxy/deploy.py
  ```

## License

This project is licensed under the [MIT license](LICENSE).
