# Contributing (Advanced)

## Building the book

If you'd like to build the book yourself you should:

1. Fork this repository
2. Run `mamba env create -f ci/envs/311-book.yml`
3. Run `mamba activate 311-book`
4. Run `jupyter-book build book`

A fully-rendered HTML version of the book will be built in
`book/_build/html/`.

**Known issue**: If you use `nb_conda_kernels` to expose your environments, you might run
into kernelspec errors when building the book. Until [this
issue](https://github.com/executablebooks/jupyter-book/issues/1348) is fixed, a
workaround is to add the environments manually to the kernselspec:

1. Run `mamba activate 311-book`
2. Run `python -m ipykernel install --user --name conda-env-311-book-py --display-name
   "conda-env-311-book-py"`

## Propose changes

We welcome pull requests!