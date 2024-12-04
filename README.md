<h1 align="center" style="border-bottom: none">
    <img height="200" width="1000" alt="HDWallet" src="data/hdlogo.png">
</h1>

<p align="center">
    <a href="https://github.com/talonlab/hdwallet-desktop/releases" target="_blank">Releases</a> · <a href="https://talonlab.gitbook.io/hdwallet/manual" target="_blank">Manual</a> ·  <a href="#donations">Donation</a>
</p>

<div align="center">

![GitHub Created At](https://img.shields.io/github/created-at/talonlab/hdwallet-desktop)
![GitHub License](https://img.shields.io/github/license/talonlab/hdwallet-desktop?color=black)
![Platforms](https://img.shields.io/badge/platforms-Windows%20%7C%20Linux%20%7C%20Mac-blue)
![GitHub Release](https://img.shields.io/github/v/release/talonlab/hdwallet-desktop)
![GitHub Release Date](https://img.shields.io/github/release-date/talonlab/hdwallet-desktop)


</div>

A cross-platform client desktop application built on the [Hierarchical Deterministic (HD) Wallet Library](https://github.com/talonlab/python-hdwallet). This application leverages the Python-based library for the implementation of a hierarchical deterministic wallet generator for more than 200 multiple cryptocurrencies. 

![Desktop Application](data/hdwallet.gif)


## Installation

### For Windows (64-bit)

To install on Windows, download one of the following from the Releases page:

- MSI Installer– Recommended for a guided installation process.

- Executable (.exe) – A standalone version that runs without installation.

Once downloaded, double-click the .msi or .exe file and follow the on-screen instructions to complete the installation.

### For Linux

To install on Linux, download one of the following from the Releases page:

- Debian Package (.deb) – Recommended for Debian-based systems like Ubuntu and Debian.

    Installation: Open a terminal, navigate to the download location, and run:
    ```
    sudo dpkg -i hdwallet-desktop-x.x.x-amd64.deb
    ```

- AppImage– A portable format compatible with most Linux distributions.

    Installation: Make the file executable and run:
    ```
    chmod +x hdwallet-desktop-x.x.x-x86_64.AppImage
    ```
    ```
    ./hdwallet-desktop-x.x.x-x86_64.AppImage
    ```

### For Mac

To install on Mac, download one of the following from the Releases page:

- MacOS App Bundle (.app):
   - Available as a `.zip` file.
   - Two versions:
     - **ARM64**: For Apple Silicon `M` series devices.
     - **x64**: For Intel-based Macs.

- MacOS Disk Image (.dmg):
   - A convenient format for installation on macOS.
   - Two versions:
     - **ARM64**: For Apple Silicon `M` series devices.
     - **x64**: For Intel-based Macs.


## Development

Fork the Repository: Fork this repository to your GitHub account.

Clone Locally: Clone the repository to your local machine. You can also clone the latest development version directly from GitHub:

```
git clone https://github.com/talonlab/hdwallet-desktop.git
```

Install Requirements: Navigate to the project directory and install the required dependencies:

```
pip install -r requirements.txt
```


## Contributing

Feel free to open an [issue](https://github.com/talonlab/hdwallet-desktop/issues) if you find a problem,
or a pull request if you've solved an issue. And also any help in testing, development,
documentation and other tasks is highly appreciated and useful to the project.
There are tasks for contributors of all experience levels.


## Donations

Your contributions help us maintain and improve this tool for the community. 
If you find our work helpful, consider supporting the project:

- **Bitcoin** - 16c7ajUwHEMaafrceuYSrd35SDjmfVdjoS
- **Ethereum / ERC20** - 0xD3cbCB0B6F82A03C715D665b72dC44CEf54e6D9B

Thank you very much for your support.

## License

Distributed under the [MIT](https://github.com/talonlab/hdwallet-desktop/blob/master/LICENSE) license. See ``LICENSE`` for more information.

## Terms and Conditions

By using this project, you agree to the [Terms and Conditions](https://talonlab.gitbook.io/hdwallet/terms-and-conditions).

## Privacy Policy

To understand how your data is used, please review our [Privacy Policy](https://talonlab.gitbook.io/hdwallet/privacy-policy).