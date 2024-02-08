# Installation Guide

Welcome to the installation guide for the CoastalCodebook. This document provides the
steps to set up the interactive computing environment built on the Jupyter ecosystem,
mostly using software that is maintained by [NumFOCUS](https://numfocus.org). Follow these steps to
ensure a smooth start with the tutorial sessions.

## 1. Setting up Git

Git is a version control system that we use for managing the course materials. If you're
new to Git, we recommend you to start with [this
introduction](https://earth-env-data-science.github.io/lectures/environment/intro_to_git.html)
to Git.

1. **Install Git software**: 

   <details>
   <summary><strong>By GitHub Desktop</strong></summary>
   
   1. Follow the [GitHub Client documentation](https://desktop.github.com/) to
   install the GitHub client. 
   
   2. GitHub client does not install the underlying git software on your machine. Follow [these
   instructions](https://learn.microsoft.com/en-us/devops/develop/git/install-and-set-up-git)
   to install git on your machine.
   </details>


   <details>
   <summary><strong>By command line</strong></summary>

   
   Follow [these instructions](https://github.com/git-guides/install-git) to install git using the
   command line.
   </details>

2. **Fork the repository** 
   <details>
   <summary><strong>By GitHub Desktop</strong></summary>
   
   Browse to the
   [webpage](https://github.com/FlorisCalkoen/CoastalCodebook), click on the green "Code"
   button and select "Open with GitHub Desktop"; or simply paste the URL into the GitHub
   client "fork repository" menu.
   </details>

   <details>
   <summary><strong>By command line</strong></summary>
   In a terminal, run: `git fork https://github.com/FlorisCalkoen/CoastalCodebook.git`. For more info, see [this introduction](https://docs.github.com/en/get-started/getting-started-with-git). 

Following these steps, the repository's files from GitHub are cloned to your machine.
Verify this by navigating to the cloned directory's path using a file explorer; the
contents should mirror [those found on GitHub](https://github.com/floriscalkoen/coastalcodebook). However, to interact with and execute the
code, we need appropriate software, which we will cover during the installation of a package manager.


## 2. Installing Mamba Package Manager

Mamba is a lightweight efficient package manager that we recommend to manage Python
environments. If you're not familiar with managing Python environments, please have a
look at this
[introduction](https://earth-env-data-science.github.io/lectures/environment/python_environments.html?highlight=conda)
first. Detailed installation instructions are available in [the Mamba
documentation](https://mamba.readthedocs.io/en/latest/installation.html). In those docs,
they refer to the to the [Conda Forge GitHub](https://github.com/conda-forge/miniforge#mambaforge)
page to download the software.

<details>
<summary><strong>Windows Users</strong></summary>

1. Download and install Mambaforge from the [Miniforge GitHub page](https://github.com/conda-forge/miniforge#mambaforge). Make sure you download the Windows binaries.
2. You may install miniforge by double-clicking and just using its default settings.
3. Access and verify Mamba by opening a Miniforge Prompt from the Start menu. You can
   test if Mamba was installed by running `mamba --version`

**Known issue**: Some users have their firewalls configured in such way that the
mambaforge installation is blocked. If you have trouble installing mambaforge, please make
sure to temporarily disable your firewall.

</details>

<details>

<summary><strong>Unix-like Systems (Mac and Linux)</strong></summary>

1. Open a terminal. On Mac, search for terminal or iterm in Spotlight. On linux, the
   hotkey to open a terminal is "cntrl + shift + t". 
2. The commands to install the package manager are copied from their documentation -
   double check to see if they are still the corect!  
   ```bash
   curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-$(uname)-$(uname -m).sh"
   bash Mambaforge-$(uname)-$(uname -m).sh
   ```
3. Accept the user agreements, and allow the installation script to edit your profile
   file because it ensures that the mamba command becomes available in your profile. 

</details>

## 3. Creating the software environment

The tutorial notebooks require specific packages, which we have bundled in a coastal
environment to avoid conflicts with other coding projects you may have. In the next steps
we will create this environment. 

1. **Open a terminal** On windows, open a Miniforge Prompt by searching for that in the
   task bar. On Mac/Linux you can search for the terminal in Spotlight.
2. **Navigate to the CoastalCodeBook repository**: You can navigate the terminal using `cd`, which stands for "change directory".
 
   <details> 
   <summary><strong>Windows</strong></summary>
   
      If you are on Windows and you installed the GitHub client using their default settings you can
      simply run `cd %userprofile%\Documents\GitHub\CoastalCodeBook`.
   </details>
 
   <details>
   <summary><strong>Unix-like Systems (Mac and Linux)</strong></summary>
   Change to the directory where you cloned the GitHub repository. This will be something like `cd ~/path/to/github/repository`.
   </details>

3. **Create the environment**: The repository contains
    [environment.yml](https://github.com/floriscalkoen/coastalcodebook/environment.yml),
    which is a file that describes the software
   dependencies. Now create the software environment by running the following command in the
   terminal/Miniforge prompt:
   
```bash
   mamba env create -f environment.yml -y
```