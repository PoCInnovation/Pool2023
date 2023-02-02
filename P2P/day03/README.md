# Day 4 - Foudry : Advanced Solidity Project

✔ Testing

✔ Fuzzing

✔ Deploy

✔ ERC20

## Introduction

During this day, you are going to see how to use foundry, an all in one tool to develop solidity projects.

By doing so, you will develop a vesting platform. A way to let your tokens stay in a smart contract for a determined period of time. This is really usefull when you go about tokenomics

Compared to hardhat, foundry allows to develop much faster because of tests and scripts directly written in solidity with built in fuzzing.
It is also written in rust so the runtime is way faster compared to javascript.

## Step 0 - Setup

Please refer to the [SETUP.md](./SETUP.md) file.

## Step 1 - Vesting is simple

### 📑 **Description**:

In this step, you will learn how to create the start of a native vesting platform.

This platform will let users create a new vesting of native tokens (ETH for exemple) by calling the `createVesting` function and once the endTimestamp has been passed, the users should be able to call the `claimVesting` with the index of their vesting to claim back the tokens they vested.

### 📌 **Tasks**:

- Create a `VestingPlatform` contract inside the `VestingPlatform.sol` file in the `src` directory
- It should inherit from the `IVestingPlatform.sol` interface
- Implement every functions from this interface based of the comments
- Create some normal and failing tests to see if everything works as expected

### 📚 **Documentation**:

- [inheritence](https://blog.soliditylang.org/2020/06/18/solidity-0.6-inheritance/)
- [IVestingPlatform](./interfaces/IVestingPlatform1.sol)
- [create tests in foundry](https://book.getfoundry.sh/forge/writing-tests)

### ✔ **Validation**:

## Step 2 - What about events ?

### 📑 **Description**:

Now that you have a working vesting platform, you should try to add some events to it to make it easier to know what's happening inside.

### 📌 **Tasks**:

- Inherit your `VestingPlatform` from the `IVestingPlatformEvents`
- Emit `NewVesting` when a vesting has been created
- Emit `ClaimVesting` when a vesting has been claimed
- Add a section in your tests to be sure these events are being emited with the right arguments

### 📚 **Documentation**:

- [IVestingPlatformEvents](./interfaces/IVestingPlatformEvents.sol)
- [events](https://docs.soliditylang.org/en/v0.8.17/contracts.html?highlight=event#events)
- [test events](https://book.getfoundry.sh/forge/cheatcodes?highlight=testExpectEmit%20event#cheatcodes)

### ✔ **Validation**:


## Step 3 - Fuzzing is great

### 📑 **Description**:

You now have tests to be sure that your contract works as intended. But if you wants to improve them, there is always a way.
And what you will learn is fuzzing. Fuzzing tests means that instead of you manually putting value to tests the contract, you can just let foundry generate x values and test the functions for you.

### 📌 **Tasks**:

- Create a new fuzz test based of the one when creating a successfull vesting with `amount`, `to`, `endTimestamp` as arguments

> ⚠️ vm.assume may be helpfull

### 📚 **Documentation**:

- [fuzz testing](https://book.getfoundry.sh/forge/fuzz-testing?highlight=fuzzing#fuzz-testing)

### ✔ **Validation**:


## Step 4 - What about fees ?

### 📑 **Description**:

In this step, you will learn how to create a fungible token of ERC20 type to pay the fees to use the Vesting service.

This token will be based off `openzeppelin` library

### 📌 **Tasks**:

- Create a `VestingToken` contract inside the `VestingToken.sol` file in the `src` directory
- Add openzeppelin contracts as dependency of the project
- This token should inherit from openzeppelin ERC20
- When deploying this token, you should set a price for users to exchange an amount of native tokens (ETH for exemple) against a token
- Add a `price()` function to returns the price of a token
- Add a `buy()` function that mints a new amount of tokens against a amount sent when calling the function
- Add a `sell(uint256 amount)` function that burns a amount of token and send the equivalant of native tokens to the user
- Create tests to see if the `VestingToken` works 

### 📚 **Documentation**:

- [foundry dependencies](https://book.getfoundry.sh/projects/dependencies)
- [ERC721](https://eips.ethereum.org/EIPS/eip-20)
- [library of open source smart contracts](https://docs.openzeppelin.com/contracts/4.x/)

### ✔ **Validation**:

## Step 5 - Implement the Vesting Fee

### 📑 **Description**:

Now that you have created the fee token, it's time to implement it in the VestingPlatform.

Basically, everytime a user will wants to create a vesting, he will need to pay a price in the FeeToken that will be transfered to the platform.
The price should be set once the platform is deployed and can then be changed by the owner

### 📌 **Tasks**:

- Inherit your `VestingPlatform` from the `IVestingPlatformFee` and `Ownable`
- Add to the constructor the `price` argument
- Implement all the new functions from the `IVestingPlatformFee` Interface
- Change the `createVesting` to take the fee and revert if it's not possible
- Update your tests to check if the fee is working

### 📚 **Documentation**:

- [IVestingPlatformFee](./interfaces/IVestingPlatformFee.sol)
- [Ownable](https://docs.openzeppelin.com/contracts/4.x/api/access#Ownable)

### ✔ **Validation**:


## Step 6 - Deploy

### 📑 **Description**:

Once that everything is working perfectly, you can deploy your contract !!!!

You will see how to deploy it to a local blockchain and a testnet

### 📌 **Tasks**:

- Create a script to deploy VestingToken
- Create a script to deploy VestingPlatform
- Create a Makefile
- Add a rule to launch a local blockchain called `anvil`
- Add a rule into this Makefile to run the tests and the coverage
- Add a rule to deploy to local blockchain
- Add a rule to deploy to a testnet with a given rpc url (can be from alchemy, infura ...)
- Run those scripts to deploy

### 📚 **Documentation**:

- [scripts](https://book.getfoundry.sh/tutorials/solidity-scripting?highlight=scripts#solidity-scripting)

### ✔ **Validation**:


## Conclusion

You achieved to create a fully working and good foundry project, I hope you now know why foundry is good and how it can speed up solidity developemnts.

Just having solidity inside the whole project makes it a lot more reslient and better than typescript.

You can also interact with your contracts directly with one of foundry tools called `cast` if you'd wish

However it is only the beginning of foundry and if you wish to go futher here are some ressources:

- [foundry best practices](https://book.getfoundry.sh/tutorials/best-practices)
- [solidity style guide](https://docs.soliditylang.org/en/v0.8.17/style-guide.html)
- [verify with etherscan](https://book.getfoundry.sh/forge/deploying?highlight=etherscan%20verify#verifying-a-pre-existing-contract)
- [foundrybook](https://book.getfoundry.sh/)
- [awesome foundry](https://github.com/crisgarner/awesome-foundry)
- [solmate](https://github.com/transmissions11/solmate)
- [github-action](https://book.getfoundry.sh/config/continous-integration?highlight=github#github-actions)
- [solidity topics in videos](https://www.youtube.com/@smartcontractprogrammer)

## Authors

| [<img src="https://github.com/0xtekgrinder.png?size=85" width=85><br><sub>Isma</sub>](https://github.com/0xtekgrinder) | 
|:------------------------------------------------------------------------------------------------------------:|
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

> 🚀 Follow us on our different social networks, and put a star 🌟 on `PoC's` repositories.
