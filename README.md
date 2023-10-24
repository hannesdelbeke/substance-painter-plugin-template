
# Substance Painter plugin template

A Substance Painter plugin template.


### What is included on this template?
![image](https://github.com/hannesdelbeke/substance-painter-plugin-template/assets/3758308/f0d6ee12-4c59-4862-b965-038ee3bd8b48)

- a dockable Substance Painter widget
- 📦 A [pyproject.toml](pyproject.toml) so you can pip install this plugin.  
- 🤖 A [Makefile](Makefile) with the most useful commands to install, test, lint, format and release your project.
- 📃 Documentation structure using [mkdocs](http://www.mkdocs.org)
- 🔄 Continuous integration using [Github Actions](.github/workflows/) with jobs to lint, test and release your project on Linux, Mac and Windows environments.
   - 💬 Auto generation of change log using **gitchangelog** to keep a HISTORY.md file automatically based on your commit history on every release.
   - 🧪 Testing structure using [pytest](https://docs.pytest.org/en/latest/)
   - ✅ Code linting using [flake8](https://flake8.pycqa.org/en/latest/)
   - 📊 Code coverage reports using [codecov](https://about.codecov.io/sign-up/)
   - 🛳️ Automatic release to [PyPI](https://pypi.org)


### HOW TO USE THIS TEMPLATE

1. Click on **[Use this template](https://github.com/hannesdelbeke/substance-painter-plugin-template/generate)**
3. Give a name to your project (e.g. `my_awesome_project`, use all lowercase and underscores separation <!-- TODO see if we can swap to my-awesome-project for package & project name, but my_awesome_project for python module --> 
3. Wait until the first run of CI finishes
4. For [codecov](https://about.codecov.io/sign-up/) Reports & Automatic Release to [PyPI](https://pypi.org)  
   go to `settings->secrets` add your `PYPI_API_TOKEN` and `CODECOV_TOKEN`
4. Read the file [CONTRIBUTING.md](CONTRIBUTING.md)
> ⚠️ **WAIT** until first CI run on github actions before cloning your new project.
5. Then clone your new project and happy coding!
6. delete all text above this, and complete the README template below for your project
7. This template is in the public domain. Choose a LICENSE for your repo

---
# project_name

[![codecov](https://codecov.io/gh/author_name/project_urlname/branch/main/graph/badge.svg?token=project_urlname_token_here)](https://codecov.io/gh/author_name/project_urlname)
[![CI](https://github.com/author_name/project_urlname/actions/workflows/main.yml/badge.svg)](https://github.com/author_name/project_urlname/actions/workflows/main.yml)

project_description

## Install 
#### install plugin
- Manually copy `project_name.py` to your plugin folder,  
  e.g. `C:\Users\USER\OneDrive\Documents\Adobe\Adobe Substance 3D Painter\python\plugins`
- or pip install from this repo
```bash
pip install --no-dependencies https://github.com/author_name/project_urlname/archive/refs/heads/main.zip --target "C:\Users\USER\OneDrive\Documents\Adobe\Adobe Substance 3D Painter\python\plugins"
```
#### install dependencies
download the repo, browse to the folder with the `requirements.txt`
```bash
pip install -r requirements.txt --target "C:\Users\USER\OneDrive\Documents\Adobe\Adobe Substance 3D Painter\python\modules"
```

## Usage
1. enable the plugin in Substance from the Menu `Python/project_name`

## Development
Read the [CONTRIBUTING.md](CONTRIBUTING.md) file.
