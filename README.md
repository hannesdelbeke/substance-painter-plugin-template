
# Substance Painter plugin template

A Substance Painter plugin template.

### HOW TO USE THIS TEMPLATE

1. Click on **[Use this template](https://github.com/rochacbruno/python-project-template/generate)**
3. Give a name to your project  
   (e.g. `my_awesome_project` recommendation is to use all lowercase and underscores separation for repo names.)
3. Wait until the first run of CI finishes  
   (Github Actions will process the template and commit to your new repo)
4. If you want [codecov](https://about.codecov.io/sign-up/) Reports and Automatic Release to [PyPI](https://pypi.org)  
  On the new repository `settings->secrets` add your `PYPI_API_TOKEN` and `CODECOV_TOKEN` (get the tokens on respective websites)
4. Read the file [CONTRIBUTING.md](CONTRIBUTING.md)
> ⚠️ **WAIT** until first CI run on github actions before cloning your new project.
5. Then clone your new project and happy coding!


### What is included on this template?

- 📦 A [pyproject.toml](pyproject.toml) so you can pip install this plugin.  
  Template uses setuptools because it's the de-facto standard for Python packages, you can run `make switch-to-poetry` later if you want.
- 🤖 A [Makefile](Makefile) with the most useful commands to install, test, lint, format and release your project.
- 📃 Documentation structure using [mkdocs](http://www.mkdocs.org)
- 💬 Auto generation of change log using **gitchangelog** to keep a HISTORY.md file automatically based on your commit history on every release.
- 🧪 Testing structure using [pytest](https://docs.pytest.org/en/latest/)
- ✅ Code linting using [flake8](https://flake8.pycqa.org/en/latest/)
- 📊 Code coverage reports using [codecov](https://about.codecov.io/sign-up/)
- 🛳️ Automatic release to [PyPI](https://pypi.org) using [twine](https://twine.readthedocs.io/en/latest/) and github actions.
- 🎯 Entry points to execute your program using `python -m <project_name>` or `$ project_name` with basic CLI argument parsing.
- 🔄 Continuous integration using [Github Actions](.github/workflows/) with jobs to lint, test and release your project on Linux, Mac and Windows environments.

> Curious about architectural decisions on this template? read [ABOUT_THIS_TEMPLATE.md](ABOUT_THIS_TEMPLATE.md)  
> If you want to contribute to this template please open an [issue](https://github.com/rochacbruno/python-project-template/issues) or fork and send a PULL REQUEST.

[❤️ Sponsor this project](https://github.com/sponsors/rochacbruno/)

<!--  DELETE THE LINES ABOVE THIS AND WRITE YOUR PROJECT README BELOW -->

---
# project_name

[![codecov](https://codecov.io/gh/author_name/project_urlname/branch/main/graph/badge.svg?token=project_urlname_token_here)](https://codecov.io/gh/author_name/project_urlname)
[![CI](https://github.com/author_name/project_urlname/actions/workflows/main.yml/badge.svg)](https://github.com/author_name/project_urlname/actions/workflows/main.yml)

project_description

## Install it from PyPI

```bash
pip install project_name
```

## Usage

```py
from project_name import BaseClass
from project_name import base_function

BaseClass().base_method()
base_function()
```

```bash
$ python -m project_name
#or
$ project_name
```

## Development

Read the [CONTRIBUTING.md](CONTRIBUTING.md) file.
