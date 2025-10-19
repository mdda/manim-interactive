# manim community 'interactive' plugin

## Getting Started
### Installation

First you will want to [install manim](https://docs.manim.community/en/stable/installation.html). Make sure it is the Manim Community edition, and not the original 3Blue1Brown Manim version. 

Then install the package from source or `pip install manim_interactive` 
(you can also use `uv pip install manim_interactive`).

Also install the `manimvs` extension in `vscode`.  
I chose to base this plugin on that that extension, since it does not depend on `3b1t manim` to run.



### Debugging

This is only required if you want to debug this `manim` plugin : Normal usage should just require the installation steps above.

Install `poetry` module, to manage the development environment in a way that is compatible with the `manim` ecosystem.

For me, using Fedora (during development), I needed to do (as root):

```bash
dnf install poetry
```

Then use the Python environment defined through `poetry` (as user):
```bash
poetry shell
poetry install
```
The `manim` file I used during development was the simple `testbed.py` file included here.


### Usage / Setting Up a Scene  

In the file that you want to interactively edit, please insert:

```py
from manim_interactive import *
```

after the initial `from manim import *`.  This will simply give you the `checkpoint_paste()` command in the interactive session.

