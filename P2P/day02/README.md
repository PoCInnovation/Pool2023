# PoC p2p Pool 2023 - Day 02 - Solidity

**Day purposes**

✅ Advance solidty notion.

✅ Create a pet which can me minted.

✅ Feed the pet to upgrade it.

✅ Turn the pet into a NFT, and make it tranferable.

## Introduction

Now that you are familiar with solidity, let's build a more complex project such as creating our own NFT. If you need to learn more about NFTs, check out this link [Nft Explanation](https://www.esports.net/crypto/nft-explained/), [Non-fungible token](https://en.wikipedia.org/wiki/Non-fungible_token)

I think that you are familiar with the concept of an NFT (Non-Fungible Token), the ability to own a unique digital asset.

If you are new to smart contract development you may think that an NFT is a complex piece of code but in reality it is a program running on a blockchain. Just as any other contract.

First, you may wonder : what will this NFT do ?

We will create an NFT representing a Pet. It can be minted (created) by any wallet and be fed to upgrade its level. To feed a Pet, you will need to pay a certain price.

Write and test your contracts on Remix Online IDE [Remix Online IDE](https://remix.ethereum.org/)

<br>

## Step 1: Pet Factory Contract

### :bookmark_tabs: **Description**:

Let's start by creating a contract which:

1. Makes every user able to mint (create) a pet
2. Stores the ownership over each user on their pets.

Each pet must have a :

- name
- id
- level
- feed time

### :pushpin: **Tasks**:

- ### **Task 0: Init the contract**

  Let's start by creating a contract called `PetFactory`.

  Add this line at the top of your file:

  ```solidity
  pragma solidity 0.8.17;
  ```

  In this contract create a _struct_ `myPet` which contains a :

  - **name**: _Pet's name_
  - **level**: _Pet's level_
  - **ToFeed**: _when will the pet be able to be fed (timestamp)_

  1. We need a `number` called **cooldownTime** which is set to `1 minutes`.<br>
  2. We need a `array` of Pets called **myPets**.<br>
  3. We need a relation between a `number` (the pet's id) and an `address` called **ntfOwner** to know who is the pet owner.<br>
  4. We need a relation between a `address` and a `number` called **petCount** to keep track of how many pet are owned by a person.<br>

- ### **Task 1: Create Pet**

  Now that we created the contract, we need to add a function to call to mint (create) a pet. This function will be limited to be only called once per wallet (if the wallet already own a pet, they can't get a new pet).

  Here is the expected function's prototype:

  ```solidity
  function createPet(string memory _name) public {}
  ```

  When creating a pet set its **level** to `1`, and its **ToFeed** attribute to the `current timestamp`.

  In the body of this function, you need to use **require**. Check if owner has already pet.

  After this you need to create function **\_pushPet** and call this function.

  ```solidity
  function _pushPet(string memory _name) private {}
  ```

  By convention add **\_** in the beginning **private** function.

  In this function you need to push your pet in your array **myPets**.
  <br>
  Don't forget to update how many pet is owned by the user :grin:

  Calling the `createPet` function should:
    - Only work once per wallet.
<br>
<br>

  ### :books: **Documentation**:

  [Array](https://www.tutorialspoint.com/solidity/solidity_arrays.htm)
  <br>
  [Mapping](https://www.tutorialspoint.com/solidity/solidity_mappings.htm)
  <br>
  [Require](https://docs.soliditylang.org/en/v0.8.17/control-structures.html#error-handling-assert-require-revert-and-exceptions)
  <br>
  [Timestamp](https://docs.soliditylang.org/en/latest/units-and-global-variables.html#block-and-transaction-properties)
  <br>

- ### **Task 2: Get info**

  Now that we are able to create a Pet, we need one method to view who owns which pet and a second one to view which pet we currently own.

  Implement a function called **\_getPetsIndexFromAddress** which returns an array of the indexes of pets owned by a giving adress.

  ```solidity
  function getPetsIndexFromAddress(address _owner) public view returns (uint[] memory) {}
  ```

  Implement a function called **getPetsIndex** which returns an array of the indexes of pets owned by the caller of the function.

  ```solidity
  function getPetsIndex() public view returns (uint[] memory) {}
  ```

  Calling the `getPetsIndex` function should:
    - Return the **id** of your Pet
<br>
<br>

- ### **Task 3: Testing**

  For testing your smart contract you can use: <br>
  **- Remix** [Remix doc](https://remix-ide.readthedocs.io/en/latest/index.html) <br>
  **- Hardhat** [Hardhat doc](https://hardhat.org/docs) <br>
  **- truffle** [truffle doc](https://trufflesuite.com/docs/) <br>

> Try at least two testers ! <br>

<br>
<br>

## Step 2: Feeding Contract

### :bookmark_tabs: **Description**:

Now let's feed our pet. When a user will want to feed his pet, the user will have to pay a certain amount to be able to feed the pet.

### :pushpin: **Tasks**:

- ### **Task 0: Init the contract**

  Let's start by creating a new contract, create a new file called `PetFeeding.sol` and create the contract called `PetFeeding`.

  Add this ligne at the top of your file:

  ```solidity
  pragma solidity 0.8.17;
  ```

  Your contract will have to inherit the contract `PetFactory` to have access to the previous contract [Inheritance](https://www.geeksforgeeks.org/solidity-inheritance/).<br>
  We need a `uint` called **levelFee** which is set to `0.000001 ether`, this fee will be the price each user must pay to upgrade their pet.<br>

- ### **Task 1: Feed a Pet**

  We now need to create a function to feed our pet. As said in the introduction, the user will need to pay a fee to feed his pet.

  Below is the function's prototype:

  ```solidity
  function feedMe(uint _petId) external payable onlyPetOwner(_petId) {}
  ```

  You can see, we use the `external payable` keywords indicating that the calling the function will trigger a payment.<br>
  And we also have **onlyPetOwner(\_petId)** which is a **modifer** that you are going to write.

  ```solidity
  modifier onlyPetOwner(uint _petId) {}
  ```

  **Modifier** is an element that will check if it can execute the function.<br>
  For example: check if the pet belongs to the one who wants the feed. :eyes:

  Don't forget to check if the pet can be fed (by checking its **ToFeed** variable), and if the user has payed the right amount with **require**.

  If the pet can be fed, raise its level by one, and change the **ToFeed** variable to the **current time** + **cooldownTime** (defined in `PetFactory.sol`).

  Your turn :grin:

  The `feedMe` function should:
    - Only be executed if the user pay the level Up fee.
    - Only the owner of the Pet is able to call the function.
    - The level of the pet must increase by 1.
<br>
<br>

  ### :books: **Documentation**:

  [Modifier](https://solidity-by-example.org/function-modifier/)
  </br>
  [Payable](https://cryptomarketpool.com/payable-modifier-in-solidity-smart-contracts/)

- ### **Task 2: Change the feeding price**

  There is an issue with our implementation: that the price to feed a pet is constant. This means that if you want to change the price, you need to upload a new contract with the new value. If your contract needs to last on the long term on the blockchain, you need to be able to change values, such as the price.

  Create a function to set a new value to **levelFee** :

  ```solidity
  function setPrice(uint _levelFee) external {}
  ```

  Take into consideration the wei, gwei, and ether conversation.

  The `setPrice` function should:
    - Only be callable with the wallet which deployed the contract.
<br>
<br>

- ### **Task 3: Role based contract**

  This function works fine but a big problem is that anyone can call this function and they can set the price to zero. This isn't the desired behaviour. Only the contract owner should be able to change the price to feed a pet.

  Create the following modifier, and apply it on **setPrice** :

  ```solidity
  modifier onlyContractOwner() {}
  ```

  ### :books: **Documentation**:

  [Convert Ethereum units](https://eth-converter.com/)

- ### **Task 4: Testing**

  For testing your smart contract you can use: <br>
  **- Remix** [Remix doc](https://remix-ide.readthedocs.io/en/latest/index.html) <br>
  **- Hardhat** [Hardhat doc](https://hardhat.org/docs) <br>
  **- truffle** [truffle doc](https://trufflesuite.com/docs/) <br>

> Try at least two testers ! <br>

<br>
<br>

## Step 3: Pet NFT Contract

### :bookmark_tabs: **Description**:

Until now we haven't really used the word NFT to describe the pet, we could have described it as an NFT because a pet can only be owned by a single wallet, thus it's **non-fungible**. But we aren't able to transfert it, this is a main feature of an NFT, it can be sent and exchange between wallets.

Your next step is to create a contract which makes possible for wallets to transfert pet and to approve a transaction.

Approving a transaction means that you approve a given wallet to transfer your pet to himself at any time, unless if you remove the approval.

### :pushpin: **Tasks**:

- ### **Task 0: Init the contract**

  Let's start by creating a contract called `PetNFT`.

  Add this ligne at the top of your file:

  ```solidity
  pragma solidity 0.8.17;
  ```

  Your contract will have to inherit the contract `PetFeeding`, and `ERC721`

- ### **Task 1: ERC721**

  You may have seen the `ERC721.sol` file from the start of the day. **ERC721** is the technical name for a NFT contract. This contract contains an **abstract contract**. It is the skeleton of a contract, it contains the function prototype which much be implemented in the contract which inherit the **abstract contact**.
  [Learn more about Abstract Contract here](https://www.geeksforgeeks.org/solidity-abstract-contract/)


- ### **Task 2: Complete the contract**

    During this final Task your job will be to complete the `PetNFT` contract. This contract must inherit from `ERC721`.

    This means that you must implement each function located in the `ERC721` **abstract contract**:

    - `balanceOf`(address _owner): This function returns the number of ERC721 tokens owned by the given address.

    - `ownerOf`(uint256 _NftId): This function returns the address that owns the given ERC721 token.

    - `transfer`(address _to, uint256 _NftId): This function transfers the ownership of an ERC721 token from the caller to the given address.

    - `approve`(address _to, uint256 _NftId): This function allows the owner of an ERC721 token to approve another address to transfer the token on their behalf.

    - `takeOwnership`(uint256 _NftId): This function transfers the ownership of an ERC721 token from the current owner to the contract itself. This can be used to implement a "payment" feature, where the contract takes ownership of a token and sends it back to the original owner when a payment is received.
    <!-- This means that your task is be to implement each function located in the ERC721 contract. -->
<!-- Exercice -->

<!-- Code -->

<!-- ### ✔️ **Validation**: -->
<!-- ## Bonus - [NAME] -->
## Conclusion

## Authors

| [<img src="https://github.com/MrSIooth.png?size=85" width=85><br><sub>Victor</sub>](https://github.com/MrSIooth) | [<img src="https://github.com/Alex-Prevot.png?size=85" width=85><br><sub>Alex</sub>](https://github.com/Alex-Prevot) | [<img src="https://github.com/Doozers.png?size=85" width=85><br><sub>Isma</sub>](https://github.com/Doozers) |
| :--------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------: |

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

