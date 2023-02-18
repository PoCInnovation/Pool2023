## Create your web application with react
```sh
npx create-react-app my-dapp
```
### This installation will take a while, do not worry.

```sh
cd my-app
npm install --save-dev hardhat # Install hardhat in your project
npx hardhat # Press enter and accept everything, this will create your hardhat project
npm install @openzeppelin/contracts # OpenZeppelin is a great tool and a standard for blockchain development. It makes creating smart contracts very easy with their blueprints smart contracts
```

```sh
npm install react-router-dom # This will be helpful to build multiple pages in your app
npm install @chakra-ui/react @emotion/react @emotion/styled framer-motion #For the style of your website
```

## Infura

Infura is a powerful tool that helps you interact with blockchain. In our case, it will make it easy to call functions on the ethereum blockchain.

## Installation

Go on [Infura](https://www.infura.io/), login and create a project

Create new key

Select network : Web3 API

Give it a name and you're ready to go !

You're on the dashboard

Under Ethereum, click on mainnet and select Görli

Copy the link and paste it in the hardhat.config.js



hardhat.config.js:
```js
require("@nomicfoundation/hardhat-toolbox");

/** @type import('hardhat/config').HardhatUserConfig */
module.exports = {
  solidity: "0.8.9",
  defaultNetwork: "goerli",
  etherscan: {
    apiKey: "FILL-IN-ETHERSCAN-API-KEY"
  },
  networks: {
    goerli: {
      url: "https://goerli.infura.io/v3/FILL-IN-INFURA-PROJECT-URL",
      accounts: ["FILL-IN-INFURA-API-KEY"]
    }
  }
};
```


## Metamask

Download [Metamask extension](https://metamask.io/)

Copy your private key under the 3 dots menu > account details > export private key

Paste it in the hardhat.config.js file.


## Faucets

### What are faucets ?

Faucets let you earn fake money that can be used on testnet networks. They will be very useful since you need money to pay the transaction fees on the blockchain.

Get some ether on [Goerli Faucet](https://goerlifaucet.com/). They will appear shortly on your account (on the goerli test network) <!-- markdown-link-check-disable-line -->

