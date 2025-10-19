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

In the file that you want to interactively edit, please make sure you've included `manim_interactive`:

```py
from manim import * # Already there
# ... other stuff
from manim_interactive import *
# ... etc
```

This will simply give you the `checkpoint_paste()` command in the interactive session.

Then, you can create a terminal in a separate window in VScode 
("Create Terminal New Window = Ctrl-Shift-Alt-`"), and run there:
```bash
manim testbed.py SimpleTest --renderer=opengl -p
```
to get an interactive scene.

Then, connect that terminal using the manimvs extension command `Manimgl: Select terminal (Python3)`.

Then, go to the line(s) that you want to debug and use the manimvs extension command `Manimgl: On Cursor Checkpoint Paste` (it'll likely be helpful to bind this to a key combo, like `Ctrl-m-Ctrl-p`).

There are several modes of 'Checkpoint Paste' in the editor:
* editor cursor is on a line of code : This will get executed immediately
* editor has lines of code selected : These will get executed immediately
* editor cursor in on a commented line : This will save a checkpoint (corresponding to the contents of the line), which you can reset the scene to by redoing this commented-line CheckpointPaste : *This is the key time-saving feature!*



