# Coastal Systems Open Codebook

Tutorial notebooks for Delft University of Technology Coastal Systems course. The book is
available [online](https://floriscalkoen.github.io/CoastalCodebook/intro.html) in both
PDF and markdown. 

## Usage

For the tuturial sessions we will use an interactive computing environment, that is built
on the [Jupyter]() ecosystem and use software packages that are by the [Pangeo
community](https://pangeo.io/quickstart.html). 

### Git

If you are not familiar with using Git, please have a look this short but excellent
[introduction](https://earth-env-data-science.github.io/lectures/environment/intro_to_git.html)
first. 

1. Please refer to the [GitHub Client documentation](https://desktop.github.com/) to
   install the GitHub client, or see [these
   instructions](https://github.com/git-guides/install-git) to install git using the
   command line.
2. Clone [the repository](https://github.com/FlorisCalkoen/CoastalCodebook) to your local
   computer using either of the following options. 
   
   1. **GitHub client**: Browse to the
   [webpage](https://github.com/FlorisCalkoen/CoastalCodebook), click on the green "Code"
   button and select "Open with GitHub Desktop".

   2. **Bash shell**: If you have a bash terminal available, provided that git [is
     configured](https://docs.github.com/en/get-started/getting-started-with-git), you
   can simply run: ` git clone https://github.com/FlorisCalkoen/CoastalCodebook.git`. 
### Mamba/Conda

If you're not familiar with managing Python environments, please have a look at this
[introduction](https://earth-env-data-science.github.io/lectures/environment/python_environments.html?highlight=conda)
first. The bottom line is that it is good practice to manage your software environments
to avoid dependency conflicts. For the tutorial notebooks,  we recommend to use the
lightweight package manager
[mambaforge](https://mamba.readthedocs.io/en/latest/installation.html). The instructions
to install this package manager can be found in their documentation, where they refer to
the [Conda Forge GitHub](https://github.com/conda-forge/miniforge#mambaforge) page to
download the software. 

### Windows

1. Download the mambaforge executable file for Windows from [Miniforge GitHub
page](https://github.com/conda-forge/miniforge#mambaforge). On that page there are also
binaries for Mac and Linux; and for `conda` package managers, so make sure you download
the `mambaforge` executable file for Windows. Install the executable by clicking on it;
you can stay with the default settings by just clicking next through the installation
client. 
2. Now that mambaforge is installed, you can open a `Miniforge Prompt`. You can open this
   shell by opening the start window and search for "Miniforge". 
### Unix like - Mac and Linux
1. We recommend to install Mambaforge on Linux and Mac using a terminal. The commands to
   install the package manager are found in their documentation and are: 
   ```bash


   ```
2. Accept the user agreements, and allow the installation script to edit your profile
   file. The profile file (`~/.bashrc` on Linux or possibly `~/.zshrc` on Mac) is the
   first script which is being executed when you open a new terminal. The installation
   script will add a few lines to that file to make the `mamba` command available every
   time open a new terminal. 

### Software environments 
To run the tutorial notebooks we need several packages. To avoid dependency conflicts it
is good practice to seperate your environments; that was the reason for installing a
package manager. Now that we have our package manager we will create the software
environments. We will create one environment that runs the JupyterLab IDE, including
several extensions; and another one that contains the packages that we need for the
tutorials. 

1. Now that mambaforge is available on your machine, open a terminal. On windows you
   should open the Miniforge prompt, which you can find by searching for it in the Start
   window. On Linux and Mac you can open your terminal of choice. If this is your first
   time, just search for terminal or iterm in Spotlight search.  
2. You can check if mamba was installed by running the following command in the terminal: 
   ```bash 
   mamba --version
   ```` 
   It should output something like: 

   ```console
   ~ base ❯ mamba --version
   mamba 1.1.0
   conda 22.9.0
   ```
3. Now that mambaforge is installed, navigate in the Miniforge prompt to the directory
   where you cloned the GitHub CoastalCodeBook repository. **Windows**: if you are on
   Windows and you installed the GitHub client using their default settings you can
   simply run `cd %userprofile\Documents\GitHub\CoastalCodeBook%` **Linux/Mac**: change
   to the directory where you cloned the GitHub repository. This will be something like
   `cd ~/path/to/github/repository`. 
4. The CoastalCodeBook root directory contains two yaml files, that describe the software
   dependencies. The first one, [environment-jupyterlab.yml](environment-coastal.yml)
   contains some packages and several extensions to built an interactive Jupyter
   environment. The other one, [environment-coastal.yml](environment-coastal.yml), is a
   specification for required software that we will use in the tutorial notebooks. First
   create a Jupyterlab environment by running: 
   
   ```bash
   mamba env create -f environment-jupyterlab.yml
   ```

   And then create the coastal environment by running: 
   ``` 
   mamba env create -f environment-coastal.yml
   ``` 
   Depending on whether this is the first time to install this kind of software on your
   machine, this might take a few minutes to complete. 

## Running the tutorial notebooks 
Now that you have access to the code (cloning this Github repository), installed a
package manager and created your environments we can start running the notebooks in
Jupyterlab. If you are new to JupyterLab we encourage you to have a look at [this
introduction](https://earth-env-data-science.github.io/lectures/environment/intro_to_jupyterlab.html). 

1. Open a terminal or Miniforge prompt. 
2. Change to the directory where you cloned the repository `cd </path/to/local/repo>`.
   Note, on Windows you should use backslashes. 
3. Activate your Jupyterlab environment by running: 
   ```bash
   mamba activate lab
   ```
4. Open Jupyterlab by running the following command: 
   ```bash
   jupyter lab 
   ```
   This will open a Jupyterlab client in your browser. 
5. In the jupyterlab you browse to the `coastalcodebook/assignments` directory and open
      one of the notebooks, for instance,
      [01_introduction.ipynb](coastalcodebook/assignments/01_introduction.ipynb).
6. Once the notebook is open you can activate the `coastal` environment in the
      upper-right corner; change `Python 3 (ipykernel)` to `Python [conda env:coastal]`.  


5. Please refer to [Conda
   documentation](https://docs.conda.io/projects/conda/en/latest/user-guide/install/windows.html)
   to install Miniconda. Optionally you can also just install
   [mamba](https://mamba.readthedocs.io/en/latest/installation.). Make sure to follow the
   instructions for your OS.  
6. Change to the directory where you cloned the repository `cd </path/to/local/repo>`.
   Note, depending on your OS you have to user either forward or backward slashes.  
7. Install Juypter software in your base environment. If you're unfamiliar with Jupyter,
   please refer to [this
   introduction](https://earth-env-data-science.github.io/lectures/environment/intro_to_jupyterlab.html).
   The Jupyter software can be installed using the following few steps: 
   1. Open a bash shell or conda prompt Optionally you can also install the Jupyterlab
   packages in your `base` environment. It really doens't make a big difference, but then
  you don't have to activate your environment upon opening a fresh terminal. To update
  your base environment with the packages listed in
  [environment-jupyterlab.yml](environment-jupyterlab.yml) run :  
      ```bash
      conda env update --name base --file environment-jupyterlab.yml --prune
      ```
  

<!-- ### Building the book

If you'd like to develop and/or build the CoastalCodeBook book, you should:

1. Clone this repository
2. Run `pip install -r requirements.txt` (it is recommended you do this within a virtual environment)
3. (Optional) Edit the books source files located in the `coastalcodebook/` directory
4. Run `jupyter-book clean coastalcodebook/` to remove any existing builds
5. Run `jupyter-book build coastalcodebook/`

A fully-rendered HTML version of the book will be built in `coastalcodebook/_build/html/`.

### Hosting the book

Please see the [Jupyter Book documentation](https://jupyterbook.org/publish/web.html) to discover options for deploying a book online using services such as GitHub, GitLab, or Netlify.

For GitHub and GitLab deployment specifically, the [cookiecutter-jupyter-book](https://github.com/executablebooks/cookiecutter-jupyter-book) includes templates for, and information about, optional continuous integration (CI) workflow files to help easily and automatically deploy books online with GitHub or GitLab. For example, if you chose `github` for the `include_ci` cookiecutter option, your book template was created with a GitHub actions workflow file that, once pushed to GitHub, automatically renders and pushes your book to the `gh-pages` branch of your repo and hosts it on GitHub Pages when a push or pull request is made to the main branch. -->

## Questions

If you have a question about the installation process or notebooks, feel free to open an
issue in the [GitHub repository](https://github.com/FlorisCalkoen/CoastalCodebook). If
that's your first time, have a look at [these
instructions](https://docs.github.com/en/issues/tracking-your-work-with-issues/creating-an-issue).
We choose to use the GitHub issue-tracker because your fellow students probably have
similar problems. We will not troubleshoot the tutorial notebooks by email. 


## Contributors

We welcome and recognize all contributions. You can see a list of current contributors in
the [contributors
tab](https://github.com/floriscalkoen/coastalcodebook/graphs/contributors).

## Credits

This project is created using the excellent open source [Jupyter Book
project](https://jupyterbook.org/) and the [executablebooks/cookiecutter-jupyter-book
template](https://github.com/executablebooks/cookiecutter-jupyter-book). We would also
like to acknowledge the [Introduction to Earth and Environmental Data
Science](https://earth-env-data-science.github.io/intro.html) for their excellent
tutorials and inspiration. 
