![](https://github.com/FlorisCalkoen/CoastalCodebook/blob/main/coastalcodebook/imgs/waves_angola.jpeg)
# Coastal Systems Open Codebook


Tutorial notebooks for Delft University of Technology Coastal Systems course. The book is
available [online](https://floriscalkoen.github.io/CoastalCodebook/intro.html) in both
PDF and markdown.

## Usage

For the tuturial sessions we will use an interactive computing environment, that is built
on the [Jupyter]() ecosystem and mostly rely on software that is supported by numfocus. We will communicate the tutorial content
using `git` version control and provide instructions on how to do so using the GitHub client. In the subsections
that follow we talk you through the three configurations steps.

### 1. Git

If you are not familiar with using Git, please have a look this short but excellent
[introduction](https://earth-env-data-science.github.io/lectures/environment/intro_to_git.html)
first.

1. Please refer to the [GitHub Client documentation](https://desktop.github.com/) to
   install the GitHub client, or see [these
   instructions](https://github.com/git-guides/install-git) to install git using the
   command line.
2. Clone this repository to your local
   computer using either of the following options.

   1. **GitHub client**: Browse to the
   [webpage](https://github.com/FlorisCalkoen/CoastalCodebook), click on the green "Code"
   button and select "Open with GitHub Desktop"; or simply paste the URL into the GitHub
   client "clone repository" menu.

   2. **Bash shell**: If you have a bash terminal available, assuming that git [is
     configured](https://docs.github.com/en/get-started/getting-started-with-git), you
   can simply run: ` git clone https://github.com/FlorisCalkoen/CoastalCodebook.git`.

3. GitHub client does not install the underlying git software on your machine. Follow [these
   instructions](https://learn.microsoft.com/en-us/devops/develop/git/install-and-set-up-git)
   to install git on your machine.


By these steps, the files that are hosted at GitHub are "pulled" to your machine. You can
check that by opening a file explorer and going to the path where you cloned the
directory. The files that you find there should reflect what's on the GitHub page.
But we can't we do anything with the files yet, as we don't have the software that can
understand the code, so we will continue with installing a package manager.

### 2. Mamba package manager

If you're not familiar with managing Python environments, please have a look at this
[introduction](https://earth-env-data-science.github.io/lectures/environment/python_environments.html?highlight=conda)
first. The bottom line is that it is good practice to manage your software environments
to avoid dependency conflicts. For the tutorial notebooks,  we recommend to use the
lightweight package manager `mambaforge`. The instructions to install this package
manager can be found in [their
documentation](https://mamba.readthedocs.io/en/latest/installation.html), in which they
refer to the [Conda Forge GitHub](https://github.com/conda-forge/miniforge#mambaforge)
page to download the software.

#### Windows

1. Download the mambaforge executable file for Windows from [Miniforge GitHub
page](https://github.com/conda-forge/miniforge#mambaforge). On that page there are also
binaries for Mac and Linux; and for `conda` package managers, so make sure you download
the `mambaforge` executable file for Windows. Install the executable by clicking on it;
you can stay with the default settings by just clicking next through the installation
client.
2. Now that mambaforge is installed, you can open a `Miniforge Prompt`. You can open this
   shell by opening the start window and search for "Miniforge".

**Known issues**: Some users have their firewalls configured in such way that the
mambaforge installation is blocked. If you have trouble installing mambaforge, please make
sure to temporarily disable your firewall.

#### Unix like - Mac and Linux
1. We recommend to install Mambaforge on Linux and Mac using a terminal. On Mac, you can
   open a terminal by searching for "terminal" or "iterm". On Linux the hotkey to open a
   terminal is "cntrl + shift + t". The commands to
   install the package manager are copied from their documentation and can be run by
   copying the commands below over to your terminal and pressing enter:
   ```bash
   curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-$(uname)-$(uname -m).sh"
   bash Mambaforge-$(uname)-$(uname -m).sh

   ```
2. Accept the user agreements, and allow the installation script to edit your profile
   file. The profile file (`~/.bashrc` on Linux or possibly `~/.zshrc` on Mac) is the
   first script which is being executed when you open a new terminal. The installation
   script will add a few lines to that file to make the `mamba` command available every
   time open a new terminal.
3. Close the terminal.

### 3. Software environments
To run the tutorial notebooks we need several packages. To avoid dependency conflicts it
is good practice to seperate your environments; that was the reason for installing a
package manager. Now that we have our package manager we will create the software
environments. We will create one environment that runs the JupyterLab IDE, including
several extensions; and another one that contains the packages that we need for the
tutorials.

1. Now that mambaforge is available on your machine, open a terminal. On Windows you
   should open the Miniforge prompt, which you can find by searching for it in the Start
   window. On Mac you can open a terminal by searching for "terminal" or "iterm". For
   Linux it's "cntrl + shift + t".
2. You can check if mamba was installed by running the following command in the terminal:
   ```bash
   mamba --version

   ```
   It should output something like:

   ```console
   ~ (base) mamba --version
   mamba 1.1.0
   conda 22.9.0
   ```

3. Now that mambaforge is installed, navigate in the terminal to the directory
   where you cloned the GitHub CoastalCodeBook repository. You can navigate the terminal
   using `cd`, which stands for "change directory".
   - **Windows**: if you are on Windows and you installed the GitHub client using their default settings you can
   simply run `cd %userprofile%\Documents\GitHub\CoastalCodeBook`.
   - **Linux/Mac**: change to the directory where you cloned the GitHub repository. This
     will be something like `cd ~/path/to/github/repository`.
4. The CoastalCodeBook root directory contains an [environment.yml](environment.yml) file that describes the software
   dependencies. This environment contains several packages and extension to build an
   interactive Jupyter lab environment that you can use to run the tutorial notebooks.

   You can create the software environment using this command:

   ```bash
   mamba env create -f environment.yml
   ```


### Running the tutorial notebooks
Now that you have access to the code (cloning this Github repository), installed a
package manager and created your environments we can start running the notebooks in
Jupyterlab. If you are new to JupyterLab we encourage you to have a look at [this
introduction](https://earth-env-data-science.github.io/lectures/environment/intro_to_jupyterlab.html).

1. Open a terminal or Miniforge prompt.
2. Change to the directory where you cloned the repository `cd </path/to/local/repo>`.
   Note, on Windows you should use backslashes (see sec 2).
3. Activate your environment by running:
   ```bash
   mamba activate coastal
   ```
4. Open Jupyterlab by running the following command:
   ```bash
   jupyter lab
   ```
   This will open a Jupyterlab client in your browser.
5. In the JupyterLab IDE you can browse to the `notebooks` directory and open
      one of the notebooks, for instance,
      [01_coastal_classification.ipynb](notebooks/01_coastal_classification.ipynb).
6. Once the notebook is open you can activate the `coastal` environment in the
      upper-right corner; change `Python 3 (ipykernel)` to `Python [conda env:coastal]`.
7. Now you can run the cells and do some interactive coastal analysis!

## Questions

If you have a question about the installation process or notebooks, feel free to open an
issue in the [GitHub repository](https://github.com/FlorisCalkoen/CoastalCodebook). If
that's your first time, have a look at [these
instructions](https://docs.github.com/en/issues/tracking-your-work-with-issues/creating-an-issue).
We choose to use the GitHub issue-tracker because your fellow students probably have
similar problems. We will not troubleshoot the tutorial notebooks by email.

### Building the book

If you'd like to develop and/or build the CoastalCodeBook book, you should:

1. Clone this repository
2. Run `mamba env create -f environment-coastal.yml`
3. Run `mamba activate coastal`
5. Run `jupyter-book build book`

A fully-rendered HTML version of the book will be built in
`book/_build/html/`.

**Known issues**: If you use `nb_conda_kernels` to expose your environments, you might run
into kernelspec errors when building the book. Until
https://github.com/executablebooks/jupyter-book/issues/1348 is fixed, a workaround is to
add the environments manually to the kernselspec:
1. Run `mamba activate coastal`
2. Run `python -m ipykernel install --user --name conda-env-coastal-py --display-name "conda-env-coastal-py"`

## Contributors

We welcome and recognize all contributions. You can see a list of current contributors in
the [contributors
tab](https://github.com/floriscalkoen/coastalcodebook/graphs/contributors).

## Credits

This project is created using the excellent open source [Jupyter Book
project](https://jupyterbook.org/) and the [executablebooks/cookiecutter-jupyter-book
template](https://github.com/executablebooks/cookiecutter-jupyter-book).