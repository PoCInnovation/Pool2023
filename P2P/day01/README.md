# P2P Pool 2023 - Day 01 - Solidity

✔️ You'll learn how to create a smart contract and how to use variables and visibilities.

✔️ You'll learn how to create and use functions and modifiers.

✔️ You'll learn what gas, ethers and gwei are and how to use it.

✔️ You'll learn how to create and use hashes, events & errors.

## Introduction

Solidity is a programming language for writing smart contracts.\
It is used for implementing smart contracts on various blockchain platforms, most notably, Ethereum.

A smart contract is a program that is stored and executed on a blockchain.\
It's written in Solidity and compiled to bytecode.\
This bytecode is then deployed on the blockchain and it's possible to interact with it by sending transactions.

## Step 0 - Setup

Please refer to the [SETUP.md](./SETUP.md) file.

## Step 1 - Smart Contract

### :bookmark_tabs: **Description**:

In this first step, you will learn how to create a smart contract.
A Solidity smart contract is formed like this :

```solidity
pragma solidity ^0.8.4;             // Solidity compiler version

contract SmartContracts {           // Smart contract declaration
    // ...
}
```

### :pushpin: **Tasks**:

- Create a new file `SmartContracts.sol`.


- In this file, create a new smart contract.

### :books: **Documentation**:

- [Smart Contract Introduction](https://docs.soliditylang.org/en/v0.8.17/introduction-to-smart-contracts.html)


## Step 2 - Variables types

### :bookmark_tabs: **Description**:

With Solidity, you have access to different types of variables :

- Signed integers
- Unsigned integers
- Strings
- Booleans
- Addresses
- And many more...

You will have to create variables.\
For this, take your smart contract from the previous step.

### :pushpin: **Tasks**:

- Create a variable `halfAnswerOfLife` with value `21`


- Create a variable `youAreACheater` with value `-42`


- Create a variable `PoCIsWhat` with value `PoC is good, PoC is life.`


- Create a variable `areYouABadPerson` with value `false`


- Create a variable `myEthereumContractAddress` with value the current contract address


- Create a variable `myEthereumAddress` with value the current user address


### :books: **Documentation**:

- [Variables types](https://docs.soliditylang.org/en/v0.8.17/types.html#value-types)


## Step 3 - Visibility

### :bookmark_tabs: **Description**:

In Solidity, you can define the visibility of your variables and functions.\

There are 4 types of visibility :
- `public` : The variable or function is accessible from everywhere
- `private` : The variable or function is accessible only from the current contract
- `internal` : The variable or function is accessible only from the current contract and from contracts that inherit it
- `external` : The variable or function is only accessible outside the contract

You will have to modify the visibility of your variables created in the previous step.
For this, take your smart contract from the previous step.

### :pushpin: **Tasks**:

- Modify the visibility to `public` for:
  - `halfAnswerOfLife`
  - `myEthereumContractAddress`
  - `myEthereumAddress`
  - `PoCIsWhat`


- Modify the visibility to `private` for:
  - `youAreACheater`
  - `areYouABadPerson`

### :books: **Documentation**:

- [Visibility documentation](https://docs.soliditylang.org/en/v0.8.17/contracts.html#function-visibility)
- [Visibility example](https://solidity-by-example.org/visibility/)


## Step 4 - Variables types #2

### :bookmark_tabs: **Description**:

There are other types of variables that you can use in Solidity :
- `bytes` : Store a sequence of bytes
- `mapping` : Store data in a key-value format
- `array` : Store data in a list format
- `struct` : Store data in a structure format
- `enum` : Store data in a list format with a name for each value

You will have to create variables.\
For this, take your smart contract from the previous step.

### :pushpin: **Tasks**:

- Create a variable `whoIsTheBest` with value `0x4c75636173206327657374206c65206265737400000000000000000000000000`


- Create a variable `myGrades`
  - This variable is a mapping with key `string` and value `uint`


- Create a variable `myPhoneNumber` with value `06`, `65`, `70`, `67`, `61`
  - This variable is an array of `string`
  - This variable has a length of `6`


- Create an enum `roleEnum` with values `STUDENT`, `TEACHER`


- Create a structure `informations` with values `name`, `firstname`, `age`, `city`, `role`
  - `name` is a `string`
  - `firstname` is a `string`
  - `age` is a `uint`
  - `city` is a `string`
  - `role` is a `roleEnum`


- Create a variable `myInformations` with your personal informations

### :books: **Documentation**:

- [Variables types](https://docs.soliditylang.org/en/v0.8.17/types.html#value-types)


## Step 5 - Functions

### :bookmark_tabs: **Description**:

Create variables is cool, but you can also create functions.\

A function is a block of code that is executed when it is called.\
You can pass data to a function, and the function will return data as a result.\
A function can also modify your contract (its variables/balance) or the balance of the user that interacts with it.

There are 3 types of functions :
- `view` : The function is read-only
- `pure` : The function is read-only and does not even read the state or the environment
- `payable` : The function can receive ethers
- `public` or no type: The function can modify the state

You will have to create functions.\
For this, take your smart contract from the previous step.

### :pushpin: **Tasks**:

- Create a function `getHalfAnswerOfLife` that returns `halfAnswerOfLife` + 21
  - This function is `public`


- Create a function `getMyEthereumContractAddress` that returns `myEthereumContractAddress`
  - This function is `internal`


- Create a function `getPoCIsWhat` that returns `PoCIsWhat`
  - This function is `external`


- Create a function `setAreYouABadPerson` that returns `areYouABadPerson`
  - This function is `private`
  - This function takes a `bool` as parameter
  - This function modifies `areYouABadPerson` with the parameter

:warning: Don't forget to define the type of your functions

### :books: **Documentation**:

- [Functions documentation](https://docs.soliditylang.org/en/v0.8.17/contracts.html#functions)


## Step 6 - Modifier

### :bookmark_tabs: **Description**:

A modifier is a function that is executed before a function.\
You can use a modifier to check if the user is allowed to execute a function.

You will have to create a modifier.\
For this, take your smart contract from the previous step.

### :pushpin: **Tasks**:

- Create a function `completeHalfAnswerOfLife`
  - This function is `public`
  - This function takes a `uint256` as parameter
  - This function modifies `halfAnswerOfLife` by adding `21`


- Create a modifier `verifyHalfAnswerOfLife`
  - This modifier checks if the parameters is equal to `21`


- Add the modifier `verifyHalfAnswerOfLife` to the function `completeHalfAnswerOfLife`

### :books: **Documentation**:

- [Modifiers documentation](https://docs.soliditylang.org/en/v0.8.17/contracts.html#function-modifiers)


## Step 7 - Hashes

### :bookmark_tabs: **Description**:

Hashes are used to encrypt data in order to make it unreadable.\
Hashes are very useful to secure data.

Take your smart contract from the previous step.

### :pushpin: **Tasks**:

- Create a function `hashMyMessage` that returns a `bytes32`
  - This function is `public`
  - This function takes a `bytes memory` as parameter
  - This function hashes the parameter with `keccak256` and returns the result

### :books: **Documentation**:

- [Keccak256 example](https://solidity-by-example.org/hashing/)


## Step 8 - Gas, ethers & gwei

### :bookmark_tabs: **Description**:

Gas, ethers and gwei are units used in Ethereum.

Gas is the unit used to measure the cost of a transaction.\
It is used to pay the miners for the execution of the transaction. The more there is gas, the more the transaction will be executed quickly.\
The gas was introduced to prevent spamming the network. The more the network is used, the more the gas will be expensive.

Ethers/ gwei are the unit used to measure the value of a transaction.\
There are used to pay the transaction fees.

Take your smart contract from the previous step.

### :pushpin: **Tasks**:

- Add a variable `balances`
  - This variable is `public`
  - This variable is a mapping with key `address` and value `uint`
  - This mapping will store the balances of each address


- Create a function `getBalance` that returns a `uint`
  - This function is `public`
  - This function returns the balance of the user who calls the function


- Create a function `addToBalance`
  - This function is `public`
  - This function takes no parameter
  - This function adds the value send with the transaction to the balance of the user who calls the function


- Create a function `withdrawFromBalance`
  - This function is `public`
  - This function takes a `uint` as parameter
  - This function withdraws the value of the parameter from the balance of the user who calls the function

:warning: Don't forget to define the type of your functions (`addToBalance` :wink:)
:warning: Don't forget to update the balance of the user who calls the function

### :books: **Documentation**:

- [Ether units documentation](https://docs.soliditylang.org/en/v0.8.17/units-and-global-variables.html#ether-units)
- [Ether function documentation](https://docs.soliditylang.org/en/v0.8.17/contracts.html#receive-ether-function)


## Step 9 - Events

### :bookmark_tabs: **Description**:

Events are used to log data.\
They are useful to know what happened in the smart contract.

Take your smart contract from the previous step.

### :pushpin: **Tasks**:

- Create an event `BalanceUpdated`
  - This event takes a `address indexed` as parameter
  - This event takes a `uint` as parameter


- Add the event `BalanceUpdated` to the function `addToBalance` and `withdrawFromBalance`

The `indexed` keyword is used to filter the event.\
It is used to filter the event by the parameter.

### :books: **Documentation**:

- [Events documentation](https://docs.soliditylang.org/en/v0.8.17/contracts.html#events)


## Step 10 - Errors

### :bookmark_tabs: **Description**:

Errors are used to return an error message.\
They are useful to know what happened in the smart contract.

There is two ways to throw an error :
- With the usage of `require`, `assert` or `revert`
- With the usage of `error`

Take your smart contract from the previous step.

### :pushpin: **Tasks**:

- Create an error `InsufficientBalance`
  - This error takes a `uint` as parameter of the quantity of ethers available in the balance of the user
  - This error takes a `uint` as parameter of the quantity of ethers requested by the user


- Add the error `InsufficientBalance` to the function `withdrawFromBalance`
  - This error is thrown if the balance of the user is inferior to the value requested

### :books: **Documentation**:

- [Errors documentation](https://docs.soliditylang.org/en/v0.8.17/contracts.html#errors-and-the-revert-statement)


## Conclusion

Well done ! You've accomplished a lot with this first day of P2P pool, and there is so much more to discover.
Refer to the [official documentation](https://docs.soliditylang.org/en/v0.8.17/) to deep-dive into it.

Hope you enjoyed this day !

## Authors

| [<img src="https://github.com/lucas-louis.png?size=85" width=85><br><sub>!LUK</sub>](https://github.com/lucas-louis) | 
|:----------------------------------------------------------------------------------------------------------------:|
<h2 align=center>
Organization
</h2>
<br/>
<p align='center'>
    <a href="https://www.linkedin.com/company/pocinnovation/mycompany/">
        <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white">
    </a>
    <a href="https://www.instagram.com/pocinnovation/">
        <img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white">
    </a>
    <a href="https://twitter.com/PoCInnovation">
        <img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white">
    </a>
    <a href="https://discord.com/invite/Yqq2ADGDS7">
        <img src="https://img.shields.io/badge/Discord-7289DA?style=for-the-badge&logo=discord&logoColor=white">
    </a>
</p>
<p align=center>
    <a href="https://www.poc-innovation.fr/">
        <img src="https://img.shields.io/badge/WebSite-1a2b6d?style=for-the-badge&logo=GitHub Sponsors&logoColor=white">
    </a>
</p>

> :rocket: Follow us on our different social networks, and put a star 🌟 on `PoC's` repositories.
