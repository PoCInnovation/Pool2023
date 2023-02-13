# Setup - Foundry

## Download foundry

- Open your terminal and type
```bash
curl -L https://foundry.paradigm.xyz | bash
```
. This will download foundryup.
- Then, you can download foundry by running `foundryup`
- If everything went fine you should be able to use `forge`, `anvil`, `chisel` and `cast`.
- If you are on macos you will need to install `libusb` with
```zsh
brew install libusb
```

## Create a foundry project

Once everything is done, you can create a new project using
```bash
forge init new_project
cd new_project
```
This should create a new directory with a brand new foundry project

If you already have a repôsitory, you might need to add
```bash
--no-commit
```

The first thing you wants to do is set the solidity version of this project in the `foundry.toml` file wich is the configuration file of foundry.

You can do this by adding in the "[profile.default]" section:
```toml
solc_version = "0.8.17"
```

## VSCode Integration

To be able to use this [solidity vscode extension](https://github.com/juanfranblanco/vscode-solidity) natively with foundry, you are going to do a few steps:

- Generate the remappings.txt using this command
```bash
forge remappings > remappings.txt
```
- Create a `.vscode/settings.json` file with this content
```json
{
  "editor.formatOnSave": true,
  "solidity.packageDefaultDependenciesContractsDirectory": "src",
  "solidity.packageDefaultDependenciesDirectory": "lib",
  "solidity.compileUsingRemoteVersion": "v0.8.17",
  "[solidity]": {
    "editor.defaultFormatter": "JuanBlanco.vscode-solidity" 
  },
  "solidity.formatter": "forge",
}
```
