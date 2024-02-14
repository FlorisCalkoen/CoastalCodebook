# Installation Guide

Welcome to the installation guide for the CoastalCodebook! This document provides a
step-by-step guide to set up your coastal computing environment; that will mostly use the Jupyter
ecosystem combined with other packages maintained by the [NumFOCUS](https://numfocus.org)
project to
provide you with an interactive learning experience. Please follow these steps to
ensure a smooth start with the tutorial sessions.

## 1. Setting up Git

Git is a version control system that we use for managing the course materials. If you're
new to Git, we recommend you to start with [this
introduction](https://earth-env-data-science.github.io/lectures/environment/intro_to_git.html).

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
2. **Fork the repository**: 

   Before you can start working on the project, you'll need to create a fork of the repository. This will give you a copy of the project in your GitHub account, allowing you to make changes without affecting the original project.

   <details>
   <summary><strong>By GitHub Desktop</strong></summary>

   1. Go to the [CoastalCodebook repository ](https://github.com/floriscalkoen/coastalcodebook.git) on GitHub.
   2. Click on the "Fork" button at the top right corner of the page to create a copy of the repository in your account.
   3. Once the fork is created, open GitHub Desktop.
   4. Go to File > Clone Repository.
   Switch to the "URL" tab and paste the URL of your fork of the repository. It will look
   something like `https://github.com/<yourusername>/CoastalCodebook.git.`, replacing yourusername with your GitHub username. 
   5. Choose where to clone the repository on your computer and click "Clone".
   </details>


   <details>
   <summary><strong>By command line</strong></summary>

   1. Go to the [CoastalCodebook repository ](https://github.com/floriscalkoen/coastalcodebook.git) on GitHub.
   2. Click on the "Fork" button at the top right corner of the page to create a copy of the repository in your account.
   3. Once the fork is created, open a terminal on your computer.
   4. Clone your fork of the repository by running: `git clone https://github.com/<YOURUSERNAME>/CoastalCodebook.git`, replacing yourusername with your GitHub username.
   5. Navigate into the cloned directory: `cd ~/path/to/CoastalCodebook`

   </details>


Following these steps, the repository's files from GitHub are cloned to your machine.
Verify this by navigating to the cloned directory's path using a file explorer; the
contents should mirror those found in the [CoastalCodebook repository](https://github.com/floriscalkoen/coastalcodebook). However, to interact with and execute the
code, we need appropriate software, which we will cover during the installation of a package manager.


## 2. Installing Mamba Package Manager

Mamba is a lightweight efficient package manager that we recommend to manage Python
environments --- if you're not familiar with managing Python environments, please have a
look at this
[introduction](https://earth-env-data-science.github.io/lectures/environment/python_environments.html?highlight=conda)
first. Detailed installation instructions for Mamba are available in [the Mamba
documentation](https://mamba.readthedocs.io/en/latest/installation.html), but here we
will share the most important links. In their docs,
they refer to the [Conda Forge GitHub](https://github.com/conda-forge/miniforge#mambaforge)
page to download the software, so that's where we will download the software as well. 

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
2. The commands to install the package manager are copied from their documentation ---
   double check to see if they are still the correct!  
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


<details>
<summary><strong>Windows Users</strong></summary>

1. On Windows, open a Miniforge Prompt by searching for "miniforge" in the task bar. 
2. Change to the directory where you cloned the repository. If you installed the GitHub client using their default settings you run
   `cd%userprofile%\Documents\GitHub\CoastalCodeBook`. By running `DIR` you can see a
   list of all files and directories. You can also see this in the file explorer by
   navigating to this directory. 
3. The directory contains
   [environment.yml](https://github.com/floriscalkoen/coastalcodebook/environment.yml),
   which is a file that describes the software dependencies. Now create the software
   environment by running the following command in the terminal/Miniforge prompt:
   
   ```bash
      mamba env create -f environment.yml
   ```

</details>

<details>
<summary><strong>Unix-like Systems (Mac and Linux)</strong></summary>

1. On Mac, search for terminal or iterm in Spotlight (command + space). On linux, the
   hotkey to open a terminal is "cntrl + shift + t". 

2. You can navigate the terminal using `cd`, which stands for "change directory". So you
   would do something like `cd ~/path/to/cloned/repository`
3. The repository contains
   [environment.yml](https://github.com/floriscalkoen/coastalcodebook/environment.yml),
   which is a file that describes the software dependencies. Now create the software environment by running the following command in the terminal/Miniforge prompt:
   
   ```bash
      mamba env create -f environment.yml
   ```

</details>
   

## 4. Running the notebooks

Having successfully installed all necessary content and software on your computer, you're
ready to move forward. The [following section](getting_started.md) will guide you through
running thenotebooks!
