# Setup 

## Node npm and yarn

For this day you need to install:

- [NodeJs](https://github.com/nodejs/node) and [Npm](https://www.npmjs.com/) (node package manager):

```bash
# For Fedora
sudo dnf install nodejs -y

# For Ubuntu
sudo apt install nodejs npm -y
```

You need to use at least the version **v18.12.1** of **NodeJs** for this project. To install the good version of node I recommend you install the [node version manager](https://github.com/nvm-sh/nvm) (nvm)


- [Yarn](https://yarnpkg.com/): a faster alternative of npm (recommended).

```bash
# For any Linux distribution
npm install --global yarn
```

⚠️ *Be carfull, if you uses yarn for the project it's important to install packages with it.*


## Nestjs

Nestjs provide you a cli with the framwork, I invite you to install it:

```bash
# To install it with npm
npm i -g @nestjs/cli

# To install it with yarn
yarn global add @nestjs/cli
```

After install the cli you can use it to start a new Nestjs project in the respository of the day.

```bash
# For creating a new nestjs project
nest new Software-Day03-Project

# This prompt will appear, chooses npm or yarn (recommended)
⚡ We will scaffold your app in a few seconds..

? Which package manager would you ❤️ to use ? (Use arrow keys)
❯ npm
  yarn
  pnpm

# Type this command to remove the .git folder in the nestjs project and copy the project's files 
rm -rf ./software-day03-project/.git && mv software-day03-project/* ./ && rm -rf software-day03-project

# Run the command
npm run start

# Or
yarn start
```
If the application starts, congratulations you have completed the setup you can begin the day ! 🎉