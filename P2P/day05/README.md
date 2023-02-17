# Day 5 - IPFS : INTER PLANETARY FILE SYSTEM

✔️ Create Node

✔️ Mesh Network

✔️ Bitswap

✔️ Distributed Hash Table (DHT)

## Notions
* Node
* Filesystem
* Mesh Network
* Bitswap
* Distributed Hash Table (DHT)

## Introduction

For this matinee we will use an implementation of IPFS in Go.
This implementation is the most used today and the most complete.
There are also many Iroh implementations in Rust, Js and many others.

It is not necessary to have done Go, the goal is to understand the technology and for this we will use the CLI.

## Step 0 - Setup

Please refer to the [SETUP.md](./SETUP.md) file.

## Step 1 - Create CID

### :bookmark_tabs: **Description**:

### :pushpin: **Tasks**:

- We will create a file called `Hello_World.txt` in which we will write `Hello World !`.
  The goal is to create a CID from this file.
- Find the command to create a CID from a file content.


### books: **Documentation**:

- [IPFS Documentation](https://docs.ipfs.tech/)

### ✔️ **Validation**:

- Run the validation script `./scripts/scripts/validate -1` then enter your CID to validate your work.

And that's it, we have created our first CID!
It is now available on our machine and you can find it in `$HOME/.ipfs/blocks`.

One of the features of your CID is that it always starts with Qm. This is called a version 0 CID.

```
### Bonus - Version 1 CID
Our goal now is to create a v1 CID with the same file.

We now have a new CID with the same content?

The question is: What do we have in our `$HOME/.ipfs/blocks`? Two identical files?
```

## Step 2 - Custom CID

### :bookmark_tabs: **Description**:

It's good to use SHA-2 but SHA-1 is better!
Let's go a little further. In the file `./utils`, you can find two pdf named `infographic-1.pdf` and `infographic-2.pdf`.
In groups of two, you will each choose a different pdf and create a CID with the SHA-1 hash.

What is the difference between SHA-1 and SHA-2?

The hash of a content is a mathematical function allowing to have always the same output with a given input.
The reverse is unfortunately not possible. This practice is used to store passwords for example.
We will check the equality between our password that we will hash and the password already hashed in database.
If it is identical, it means that the password given in input is correct.
Moreover, if our database leaks, the crook will only have hashes that he won't be able to reverse.

But we can ask ourselves the question: What is the use of several hash algorithms?
It is possible to obtain two identical hashes with different contents, which is called a hash collision.
If we go back to our database example, it would be possible to get the same hash without having an identical password.
As you may have guessed, with SHA-1 we are able to make hash collisions.

### pushpin: **Tasks**:

- Now it's time to create CID using SHA-1 and compare the two CIDs.

### books: **Documentation**:

- [CLI Kubo](https://docs.ipfs.tech/reference/kubo/cli/)
- CID](https://docs.ipfs.io/concepts/content-addressing/#cid-conversion)
- [Google Shattered](https://www.numerama.com/tech/235436-shattered-google-a-casse-la-methode-de-chiffrement-sha-1.html)

### ✔️ **Validation**:

- Run the validation script `./scripts/scripts/validate -2` then enter your CID to validate your work.

Congratulations! We got the same CID with two visibly different contents.
Actually the first pdf you will chunk will be stored on your machine and not overwritten by the second one.

You can change the size of your block and other more exciting things but we'll move on very quickly!

You will notice that the CID does not start with Qm anymore but with bafy. This is what we call a version 1 CID.
It is customizable and allows to do more interesting things (block size, encoding, hash, ...).

## Step 3 - My name is Daemon

### :bookmark_tabs: **Description**:

As you can see, it is possible to create CIDs but nobody can actually communicate with you.
Nobody? Not for long. It's time to open up to the p2p world.

### pushpin: **Tasks**:

- Run your ipfs daemon.

### ✔️ **Validation**:

- Run the validation script `./scripts/scripts/validate -3` to validate your work.

YES ! Let's do it !
You can now exchange and retrieve content anywhere in the world. How to do it ?

## Step 4 - Get my content

### :bookmark_tabs: **Description**:

By default a content is not replicated on the network.
When we add a content, it is accessible but for it to be replicated the content must be requested.
The requested content is stored in the cache of your daemon but is not permanent.
For it to be permanent you must pin it.


Here is the CID that will be used: `QmeVUSb9cFAzKFMQNBqzUCoa4jFCTGaRJVQ8SYWYvXmdQj`
We have seen that a CID points to a content. By performing a GET command we should be able to find the desired content.

### :pushpin: **Tasks**:

- Retrieve this content, it is possible that this content will take some time to be retrieved. Your daemon will ask everyone you know on the network.

### ✔️ **Validation**:

Open the content once received!
If your content is identical to `./utils/POC_01_black.png` you have succeeded!

It goes much faster than expected!

## Step 5 - One, Two, Three ... Replication



### :bookmark_tabs: **Description**:

It is useful to retrieve content, but the best is to replicate it also known as pinner.
This will allow you to write some metadata and express that you don't want to delete the content.

REPLICATIONNNNNN! Now we have several nodes with our content.
The more nodes you have with your pinned content, the faster the retrieval and exchange of content will be.

There are pinning services that allow you to use machines to pin content.

EXAMPLE : Pinata, Scaleway. You even have blockchains dedicated to rewarding with tokens the people who put their machines at
their machines (Filecoin).

### pushpin: **Tasks**:

- Using the CID from step 4, make a pin of the content.

### ✔️ **Validation**:

Verify with the `ipfs pin ls` command that your content is pinned.

## Step 6 - Garbage Collector

### :bookmark_tabs: **Description**:

Now that our content is pinner. We will remove all the useless blocks,
There are several types of garbage collector in computer science.
The garbage collector in programming that allows you to free your memory automatically like python or JS.
And the one that allows you to delete blocks on filesystems.

### pushpin: **Tasks**:

- Guess which one we are going to use :eyes:

This command is a bit more complicated to find but you'll get there!
The `gc`, by default is not enabled on your nodes, you can check your ~/.ipfs/config file for that.

### ✔️ **Validation**:

Enter the command you found with `./scripts/validate -6` to validate your work.

## Step 7 - Turn Off

### :bookmark_tabs: **Description**:

We'll make sure we always have our content, but before we do that so we don't get biased, we'll turn off our daemon.
Otherwise, it is possible without knowing it to get the content of another node.

### pushpin: **Tasks**:

- Disconnect your node from the network.
- No need to cut your internet connection for this :sink:

### ✔️ **Validation**:

You can run the script `./scripts/validate -7` to validate your work.

## Step 8 - Unpin content

### :bookmark_tabs: **Description**:

Remember, earlier we pinned a content. That is to say that it is permanent on our machine.
It would be nice to update our metadata so that at the next gc, it can be deleted.

### :pushpin: **Tasks**:

- The goal is to unpin our CID.

### ✔️ **Validation**:

Check with `ipfs pin ls` that your cid does not exist

## Step 9 - Back to the past

### :bookmark_tabs: **Description**:

If all the steps went well, we should only be able to pass the GC and see our blocks disappear forever.

### pushpin: **Tasks**:

- Pass the GC again

### ✔️ **Validation**:

Your CID should be displayed on your shell after the command.

## Step 10 - Node automatic

### :bookmark_tabs: **Description**:

We have observed a lot of problems with our node.

Why our GC doesn't default?

### :pushpin: **Tasks**:

Our node is set up so that the gc passes every 1 hour.
So why doesn't it do that?

You will have to find the command that enables the GC.
Be careful your daemon must be running.

### ✔️ **Validation**:

Enter the complete command with `./scripts/validate -10` to validate your work.

## Conclusion

Well done ! You've accomplished a lot with IPFS, and there is so much more to discover.
Refer to the [official documentation](https://link.com) to deep-dive into it.

Hope you enjoyed the workshop !

## Authors

| [<img src="https://github.com/OnsagerHe.png?size=85" width=85><br><sub>Onsager</sub>](https://github.com/OnsagerHe) | 
|:---------------------------------------------------------------------------------------------------------------:|
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
