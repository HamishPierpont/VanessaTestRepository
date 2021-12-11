# Vanessa's Test Repository

Hi Vanessa! This repo should acclimate you to working with a shared code repository using Git. It'll take you through getting the repository on your computer,
getting a virtual environment set up, installing packages, running unit tests on your code, making a separate branch of your repo, adding your own tests,
pushing your local branch up to GitHub, and then merging your code back into the `main` branch using a pull request.


## How did you write this introduction anyway?
GitHub automatically scans each repository for a `README` file; if it finds one, it'll display its contents on the landing page for the repository.
Traditionally this file contains an introduction to the repository, installation and usage instructions, links to documentation, and anything else
that a new user of/contributor to the repository might need to get started.

`README` files can be written in plain text and stored as `README` or `README.txt`, or written using [reStructuredText](https://docutils.sourceforge.io/rst.html)
and stored as `README.rst`, but the vast majority of GitHub `README`s are written in [Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
and stored as `README.md`.


## What do I need to have installed ahead of time?
You'll need to have Python 3 installed on your system; check to make sure the `python3` and `pip` commands work ahead of time. You'll also need a POSIX-compliant
terminal - either `bash` or `zsh` will do - and the `git` terminal client.


## Cloning this repository
1. Click the green "Code" button and copy either of the HTTPS or SSH links to this repository.
2. Open a terminal and navigate to the directory in which you want to put this repository.
3. Run `git clone <link-to-repo>` to clone this repository.

If you run this command in the directory `~/source`, the repo will end up in `~/source/VanessaTestRepository`.


## Setting up your environment
In computing, the *environment* refers to the software and hardware system in which a computer program runs. If you're executing a computer program using a `zsh` terminal
on a 2017 MacBook Pro running macOS Catalina 10.15.7, all of this information is included in our definition of our program's environment. However, in practice, our working
definition of the environment primarily involves
- what programs (and program versions) we have access to,
- what libraries (and library versions) we have access to, and
- what environment variables are set in the terminal we use to run the program.

This is a confusing definition, and you won't get a great feel for what we mean by "environment" until you've worked on an app that takes config information from the 
environment. The only environment setup we'll do here is initializing a virtual environment, which is just a fancy box that stores Python libraries just for this application.

### Virtual environment
Python projects often rely heavily on external software libraries downloaded through `pip`. For example, as of 10 December 2021, running `pip install sqlalchemy` will download
version `1.4.28` of the popular SQLAlchemy database library. After this, any Python source file on your computer can use this library by just adding `import sqlalchemy` at the
beginning of the file. Great!

But wait. What if I also have an old project on my computer that relies on version `0.9.2` of SQLAlchemy? This old version had a completely different API, so if I update to
version `1.4.28` I'll break my old code. Running `pip install <library>` will install `<current-version-of-library>` into
`/usr/bin/WhateverVersionOfPythonYouCurrentlyHave/site-packages/<library>`. How am I supposed to manage different versions of the same library on the same system?

The answer is the *virtual environment*. A virtual environment is basically a fancy box that you create for each of your Python projects. From inside your application folder,
create a new virtual environment by running `python3 -m venv .venv`. Then run `source .venv/bin/activate`. Now whenever you `pip install` a Python library, it'll live in
`<your-application-folder>/.venv/Lib/site-packages` (the fancy box) instead of globally in `/usr/bin/WhateverVersionOfPythonYouCurrentlyHave/site-packages/`, and when your code 
imports a pip library, it will do so from `<your-application-folder>/.venv/Lib/site-packages` instead of `/usr/bin/WhateverVersionOfPythonYouCurrentlyHave/site-packages/`. Doing 
this with every project lets them all live happy and separate lives, like neighbors with fences. When it's time to stop working on this project, just type `deactivate` and 
Python will go back to pulling its libraries from the global install location.

![Important meme](https://i.redd.it/lqy92av2z2521.jpg)

Just to recap:
- Create a virtual environment by:
  - Opening a terminal in your `VanessaTestRepository` directory
  - Creating a virtual environment folder with `python3 -m venv .venv`
- Every time you work on this project, boot up the virtual environment by running `source .venv/bin/activate`
- When you're done working on this project, deactivate the virtual environment by running `deactivate` 

## Running the tests

## Adding your own test

## Merging your code into `main`
