# CoastalCodeBook

Tutorial notebooks for Delft University of Technology Coastal Systems course. 

## Usage

For the tuturial sessions we will use an interactive computing environment, that is built
upon [Jupyter]() and mostly uses software packages endorsed by the [Pangeo
community](https://pangeo.io/quickstart.html). 

### Git

If you are not familiar with using Git, please have a look at [this excellent introduction](https://earth-env-data-science.github.io/lectures/environment/intro_to_git.html)
first. 

1. Please refer to the [GitHub Client documentation](https://desktop.github.com/) to install the
   GitHub client, or see [these
   instructions](https://github.com/git-guides/install-git) to install git using the
   command line.
2. Clone [the repository](https://github.com/FlorisCalkoen/CoastalCodebook) to your local
   computer. 
   
   - **GitHub client**: Browse to the [webpage](https://github.com/FlorisCalkoen/CoastalCodebook), click on the green "Code" button and
   select "Open with GitHub Desktop".
   - **Bash shell**: If you have a bash terminal available, provided that git [is
     configured](https://docs.github.com/en/get-started/getting-started-with-git), you can simply run: `
   git clone https://github.com/FlorisCalkoen/CoastalCodebook.git`. 
### Mamba/Conda

If you're not familiar with managing Python environments, please have a look at this
[excellent
introduction](https://earth-env-data-science.github.io/lectures/environment/python_environments.html?highlight=conda)
first. The bottom line is that it is good practice to manage your software environments
to avoid dependency conflicts. 
We recommend to use the lightweight package manager [miniconda](https://conda.io/miniconda.html), or, even better, its
faster successor [mamba](https://mamba.readthedocs.io/en/latest/installation.html).  

1. Please refer to [Conda
   documentation](https://docs.conda.io/projects/conda/en/latest/user-guide/install/windows.html)
   to install Miniconda. Make sure to follow the instructions for your OS.  
2. Activate your base environment by `mamba activate base` and install the packages
   listed in `environment-jupyterlab.yml` into this base environment. You can verify this by running `jupyter lab`. You should be able
   to run a Juypter server. Please refer to [this
   introduction](https://earth-env-data-science.github.io/lectures/environment/intro_to_jupyterlab.html)
   for more information about Jupyterlab. 
3. Create a new environment with the software packages that we will need for the tutorial
   sessions. 
    1. Open a conda or bash terminal
    2. Change to the directory where you cloned the repository `cd </path/to/local/repo>`
    3. In the bash shell or conda prompt run the following command: 
   ```bash
    mamba env create -n coastal -f environment.yml
   ```
4. Now we can open a interactive computing environment and run the code in the notebooks. 
   1. Open a conda or bash terminal
   2. Change to the directory where you cloned the repository `cd </path/to/local/repo>`
   3. In the root directory run `jupyter lab` to launch a jupyter server. 
   4. In the jupyterlab you browse to the `coastalcodebook/assignments` directoy and open
      one of the notebooks, for instance,
      [01_introduction.ipynb](coastalcodebook/assignments/01_introduction.ipynb).
   5. Once the notebook is open you can activate the `coastal` environment in the
      upper-right corner; change `Python 3 (ipykernel)` to `Python [conda env:coastal]`.  




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

## Contributors

We welcome and recognize all contributions. You can see a list of current contributors in the [contributors tab](https://github.com/floriscalkoen/coastalcodebook/graphs/contributors).

## Credits

This project is created using the excellent open source [Jupyter Book
project](https://jupyterbook.org/) and the [executablebooks/cookiecutter-jupyter-book
template](https://github.com/executablebooks/cookiecutter-jupyter-book). We would also
like to acknowledge the [Introduction to Earth and Environmental Data
Science](https://earth-env-data-science.github.io/intro.html) for their excellent
tutorials and inspiration. 
