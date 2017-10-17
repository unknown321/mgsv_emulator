mgsv_emulator
==========================

This is boilerplate code for your project, generated using the `python_boilerplate` paster template. It provides simple starting points for using some of the popular best-practices:

  * Proper [setuptools](https://pypi.python.org/pypi/setuptools)-compatible package layout.
  * [py.test](http://pytest.org/)-based tests.
  * [buildout](http://www.buildout.org/) for managing development tools or developing multiple-package projects
  * Usage of the [Travis-CI](https://travis-ci.org/) continuous integration service.

Preparation
-----------

The next thing to do after having created the project layout is to add the code to a version control repository. There are two common options for you to choose from:

  1. For smaller single-package projects you might want to keep only the Python's package code (i.e. `src/mgsv_emulator`) under version control, and consider the rest (the `buildout.cfg` and all that comes with it) to be your local development environment.
  2. For larger projects you should consider keeping the whole development environment (including `buildout.cfg`, perhaps several eggs under `src`, docs in `doc`, etc) under version control.

**If you decided in favor of Option 1**:

  - Create a version control repository under `src/mgsv_emulator`. Here is an example with Git:

        > cd src/mgsv_emulator
        > git init
        > git add .
        > git commit -m "Initial package structure"
    
    If you are using Github, proceed by creating a `<your-project>` repository on the Github website, and then doing:

        > git remote add origin https://github.com/<username>/<your-project>.git
        > git push origin master

  - You can safely delete the `.travis.yml` file in the root of the project (but leave the one within the `src/mgsv_emulator` directory).

**If you decided in favor of Option 2**:

  - Create a version control repository under the project root (i.e. in this directory). The Git/Github example above applies, except for the first `cd` line.
  - Drop `.travis.yml` from the `src/mgsv_emulator` directory (leave the one in the project root).

Before you begin developing your code, you may wish to tune the `src/mgsv_emulator/README.rst` file. This file should contain a detailed description of what your package is supposed to do. In particular, when you submit your package to PyPI, the contents of this file will be shown on the package index page. 

In addition, the `LICENSE.txt` included with the boilerplate code is a copy of the `MIT` license. If you project uses a different license, replace this file to match.

Eventually, you will also want to edit this `README.md` to reflect the actual development instructions that apply to your project. Note that if you decided to keep the whole project layout in Github, this `README.md` will be shown as the index page of your project on Github.

Finally, review the settings in `src/mgsv_emulator/setup.py` (e.g., the `classifiers` parameter might require tuning).

Once you are done with the preparation, you can start developing by running `python bootstrap.py` and `buildout`. See next section.

Common development tasks
------------------------

  * **Setting up the development environment before first use**
  
        > python bootstrap.py
        > export PATH=$PWD/bin:$PATH  
            (in Windows: set PATH=%CD%\bin;%PATH%)
        > buildout
       
  * **Running tests**  
    Tests are kept in the `tests` directory and are run using

        > py.test
    
  * **Creating Sphinx documentation**
  
        sphinx-quickstart
        (Fill in the values, edit documentation, add it to version control)
        (Generate documentation by something like "cd docs; make html")
        
    (See [this guide](http://sphinx-doc.org/tutorial.html) for more details)
    
  * **Specifying dependencies for your package**  
    Edit the `install_requires` line in `src/mgsv_emulator/setup.py` by listing all the dependent packages.

  * **Producing executable scripts**  
    Edit the `console_scripts` section of `entry_points` in `src/mgsv_emulator/setup.py`. Then run `buildout`. The corresponding scripts will be created in the `bin/` subdirectory. Note that the boilerplate project already contains one dummy script as an example.

  * **Debugging the code manually**      
    Simply run `bin/python`. This generated interpreter script has the project package included in the path.
    
  * **Publishing the package on Pypi**
  
         > cd src/mgsv_emulator
         > python setup.py register sdist upload
       
  * **Creating an egg or a windows installer for the package**
  
         > cd src/mgsv_emulator
         > python setup.py bdist_egg
          or
         > python setup.py bdist_wininst
       
  * **Travis-CI integration**  
    To use the [Travis-CI](https://travis-ci.org/) continuous integration service, follow the instructions at the [Travis-CI website](https://travis-ci.org/) to register an account and connect your Github repository to Travis. The boilerplate code contains a minimal `.travis.yml` configuration file that might help you get started.

  * **Other tools**  
    The initial `buildout.cfg` includes several useful code-checking tools under the `[tools]` section. Adapt this list to your needs (remember to run `buildout` each time you change `buildout.cfg`).

  * **Working with setup.py**  
    If you are working on a small project you might prefer to drop the whole `buildout` business completely and only work from within the package directory (i.e. make `src\mgsv_emulator` your project root). In this case you should know that you can use
    
         > python setup.py develop
         
    to include the package into the system-wide Python path. Once this is done, you can run tests via
    
         > python setup.py test
         
    Finally, to remove the package from the system-wide Python path, run:
    
         > python setup.py develop -u

  * **Developing multi-package projects**  
    Sometimes you might need to split your project into several packages, or use a customized version of some package in your project. In this case, put additional packages as subdirectories of `src/` alongside the original `src/mgsv_emulator`, and register them in `buildout.cfg`. For example, if you want to add a new package to your project, do:
    
         > cd src/
         > cookiecutter https://github.com/audreyr/cookiecutter-pypackage.git
           or
         > paster create <new_package_name>
         
    Then add `src/<new_package_name>` to version control and add the directory `src/<new_package_name>` to the `develop` list in `buildout.cfg`. Also, if necessary, add `<new_package_name>` to the `[main]` part of `buildout.cfg` and mention it in the `[pytest]` configuration section of `setup.cfg`.

Copyright & License
-------------------

  * Copyright 2017, unknown
  * License: MIT
