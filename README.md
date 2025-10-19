# Manim Community Edition 'interactive' plugin

## Getting Started

### Installation

There are several components that require installation:
* `manim` (Community edition) - obviously
* OpenGL for your machine (we use `--renderer=opengl`)
* `manim_interactive` - this plugin
* `manimvs` VScode extension

#### Further details

First you will want to [install manim](https://docs.manim.community/en/stable/installation.html). Make sure it is the Manim Community edition, and not the original 3Blue1Brown Manim version. 

In addition, we will be using the OpenGL renderer 
(which is not exactly the same as the regular Cairo renderer).  The reason is that the Cairo one renders to video files fine, 
but isn't really intended for 'realtime/interactive' usage 
(unless you are prepared to wait for lots of video regeneration).

To install the essentials required for OpenGL (on Fedora), I needed to run (as root):
```bash
# For manim (base)
dnf install pango-devel texlive-dvisvgm texlive-standalone
# For manim OpenGL backend
dnf install mesa-libGL libglvnd-devel

# The latter of these packages was discovered by running:
dnf provides '*/libGL.so'
```

Then install this plugin `pip install manim_interactive` 
(you can also use `uv pip install manim_interactive`) - or install from source (for debugging, see below).

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

Running this interactive session requires a few steps:
* import this plugin
* add a `self.embed()` breakpoint to your scene
* run `manim` in a VScode terminal window
* connect `manimvs` extension to the terminal window
* select the appropriate line(s) in vscode, and press the magic hotkeys

#### Further details

In the file that you want to interactively edit, please make sure you've included `manim_interactive`:

```py
from manim import * # Already there
# ... other stuff
from manim_interactive import *
# ... etc
```

This will simply give you the `checkpoint_paste()` command in the interactive session.

Then, in that scene, before a comment starting a segment that you are building out (or refining), insert the following:

```py
self.embed()
```

(See the `testbed.py` file here to see how it looks in practice).

Then, you can create a terminal in a separate window in VScode 
("Create Terminal New Window = Ctrl-Shift-Alt-`"), and run there (updated for your file/scene):
```bash
manim testbed.py SimpleTest --renderer=opengl -p
```
to get an interactive scene.

Then, connect that terminal using the `manimvs` extension command `Manimgl: Select terminal (Python3)`.

Then, go to the line(s) that you want to debug and use the manimvs extension command `Manimgl: On Cursor Checkpoint Paste` (it'll likely be helpful to bind this to a key combo, like `Ctrl-m-Ctrl-p`).

There are several modes of 'Checkpoint Paste' in the editor:
* *editor cursor is on a line of code* : This line is executed immediately
* *editor has lines of code selected* : These lines are executed immediately
* *editor cursor in on a commented line* : Saves a checkpoint (corresponding to the contents of the line), which you can reset the scene to by redoing this commented-line CheckpointPaste : **This is the key time-saving feature!** and then runs the block up until the next commented line


