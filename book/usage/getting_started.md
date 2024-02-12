# Getting Started

This guide will help you get up and running with the course notebooks using JupyterLab, assuming you've already installed the necessary software as per our [installation instructions](installation.md).

## Launching the Notebooks

Follow these steps to start exploring the course content through interactive Jupyter notebooks:

1. **Access the code**: Ensure you've forked the [GitHub repository](https://github.com/floriscalkoen/coastalcodebook) to your local
   machine.

2. **Navigate to the repository**: 
   
   <details>
   <summary><strong>Windows Users</strong></summary>

   1. On Windows, open a Miniforge Prompt by searching for "miniforge" in the task bar. 
   2. Change to the directory where you cloned the repository by using `cd
      <drive:\path\to\dir>`. If you installed the GitHub client using their default
      settings you may run
      `cd%userprofile%\Documents\GitHub\CoastalCodeBook`.

   </details>

   <details>
   <summary><strong>Unix-like Systems (Mac and Linux)</strong></summary>

   1. On Mac, search for terminal or iterm in Spotlight (command + space). On linux, the
      hotkey to open a terminal is "cntrl + shift + t". 
   2. You can navigate the terminal using `cd`, which stands for "change directory". So you
      would do something like `cd ~/path/to/cloned/repository`

   </details>


3. **Activate Your Environment**: Activate your coastal environment with the command below. This environment contains all the packages you'll need.

   ```bash
   mamba activate coastal
   ```

4. **Start JupyterLab**: JupyterLab is an interactive development environment that allows you to work with
   notebooks and other files. Run the following command to open JupyterLab in your web browser:

   ```bash
   jupyter lab
   ```


5. **Open a Notebook**: Within JupyterLab, navigate to the notebooks directory, and open a notebook, such as [1_coastal_classification.ipynb](../notebooks/1_coastal_classification.ipynb).

6. **Select the Right Kernel**: Before running the notebook, ensure the coastal environment is selected as the kernel. You can change this in the upper-right corner by selecting Python [conda env:coastal] from the kernel dropdown menu.

6. **Interact with the Notebook**: You're now ready to execute the notebook cells and
   engage with the interactive coastal computational notebooks!

## New to JupyterLab?
If JupyterLab is new to you, or you'd like a refresher, consider browsing through [this
introductory guide](https://earth-env-data-science.github.io/lectures/environment/intro_to_jupyterlab.html). It provides a comprehensive overview of the JupyterLab interface and features.
