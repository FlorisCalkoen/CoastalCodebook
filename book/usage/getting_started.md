# Getting started


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
