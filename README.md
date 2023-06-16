# upgrade-proxy-factory-mix

A simple implementation of various proxy and factory patterns. To provide a quick overview of current methods and some deployment scripts to get anyone started quickly. This repo is not optimized and meant for direct production, rather as a demonstration and documentation of possible proxy patterns and how to implement them in code.

![image](https://github.com/Harsh-Gill/brownie-proxy-factory-mix/assets/70016426/1181f7af-5694-4b91-b753-d40d7d570a8d)

I've written an article for a quick overview of this repo and concepts at : https://medium.com/@harshgill2954/upgradeable-and-clonable-blockchain-smart-contracts-f3df36bbba6c

## Installation

1. [Install Brownie](https://eth-brownie.readthedocs.io/en/stable/install.html), if you haven't already.

2. Download the needed OpenZeppelin modules

   ```bash
   brownie pm install OpenZeppelin/openzeppelin-contracts@4.8.3
   ```

3. Compile the contracts

   ```bash
   brownie compile
   ```

## Basic Use

This mix provides 3 proxy patterns with Objects defined as deployers.

The 3 Patterns are :

- Transparent Proxy Pattern
  The contracts are located in contracts/transparent_upgradeable_proxy/
  The scripts are located in scripts/transparent_upgradeable_proxy/
![image](https://github.com/Harsh-Gill/brownie-proxy-factory-mix/assets/70016426/c193789c-bca6-451b-b07c-f4629bf62d0c)

  To run :

  ```bash
  brownie run scripts/transparent_upgradeable_proxy/deploy.py
  ```

- UUPS Proxy Pattern
  The contracts are located in contracts/uups_proxy/
  The scripts are located in scripts/uups_proxy/
![image](https://github.com/Harsh-Gill/brownie-proxy-factory-mix/assets/70016426/abf24858-e1d5-4673-a7c5-c8d944733ce2)

  To run :

  ```bash
  brownie run scripts/uups_proxy/deploy.py
  ```

- Factory Beacon Proxy Pattern
  The contracts are located in contracts/beacon_proxy/
  The scripts are located in scripts/beacon_proxy/
![image](https://github.com/Harsh-Gill/brownie-proxy-factory-mix/assets/70016426/c01bdcdf-c05f-46be-b3f0-d9e376dd9656)

  To run :

  ```bash
  brownie run scripts/beacon_proxy/deploy.py
  ```

## License

This project is licensed under the [MIT license](LICENSE).
