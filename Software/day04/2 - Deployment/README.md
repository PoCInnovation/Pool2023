# PoC Software Pool 2023 - Day 04 - Deployment

**Day purposes**

✔️ Deploy an entire application

✔️ Use a cloud instance

✔️ Discover GitHub Actions

✔️ Setup a CI/CD pipeline


## Introduction

[This morning](../1%20-%20Docker/) you discovered Docker, a very useful and popular tool to package your application into containers. That's great, but you still need to start these containers *somewhere* reachable by someone who wants to access your app.

This can be quite complicated if you want to do it by yourself on your computer:
- It should be up and running 24/7
- You should make sure it's secured and up to date in case of vulnerabilities
- It can impact the performances of your other apps
- Dozens of other problems...

That's where cloud providers like [AWS](https://aws.amazon.com/) or [Scaleway](https://www.scaleway.com/) 🇫🇷 come into play: they offer cloud-based services like data storage or computing power.

They handle the hardware, maintenance and security concerns to let you focus on what's really important for you as a developer: shipping your application to users 🚀

> 💡 If you are curious, check [this link](https://www.bmc.com/blogs/saas-vs-paas-vs-iaas-whats-the-difference-and-how-to-choose/) to learn about the different types of services.

Today you will use [Scaleway Instances](https://www.scaleway.com/en/virtual-instances/) which are computing units installed with an OS of your choice, on which you can then connect via SSH and use as you want 🚀

Then you will discover [GitHub Actions](https://github.com/features/actions) to run tests and update your deployed application whenever you make change to your code 🔥


## Step 0 - Setup

### 📑 **Description**:

The first thing you would normally do is to [create an instance](https://www.youtube.com/watch?v=1ulVecpL6QE) with all the settings you want, like the OS, computing power, storage space...\
We've already done this for you today, so you only have to connect to it 🔥

### 📌 **Tasks**:

- Check your email address, you've received some information related to your dedicated instance
    - An IP address
    - A private SSH key
- Connect to the instance through SSH using the above information

### 📚 **Documentation**:

- [Scaleway Instances Quickstart](https://www.scaleway.com/en/docs/compute/instances/quickstart/)
- [What is SSH and how to use it](https://www.ucl.ac.uk/isd/what-ssh-and-how-do-i-use-it)

### ✔️ **Validation**:

Once you are connected to the instance, you can check the machine information with the following command:
```sh
hostnamectl
# Operating System: Ubuntu 22.04.1 LTS       
# Kernel: Linux 5.15.0-53-generic
# Architecture: x86-64
# Hardware Vendor: Scaleway
# Hardware Model: SCW-DEV1-S
```

You can then `exit` to go back to your terminal 😄


# Step 1 - Copy app files & run it