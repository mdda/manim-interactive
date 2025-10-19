from collections import OrderedDict
import pyperclip
import textwrap

from manim import Scene, Mobject


# Cleans up interface when uncommented
__all__ = 'checkpoint_paste'.split()


# This is a heavily modified version of the code in 3b3t manim:
#   https://github.com/3b1b/manim/blob/master/manimlib/scene/scene.py#L882
class SceneState():
  def __init__(self, scene: Scene, ignore: list[Mobject] | None = None):
    self.time = scene.time
    #self.num_plays = scene.num_plays
    self.mobjects_to_copies = OrderedDict.fromkeys(scene.mobjects)
    if ignore:
      for mob in ignore:
        self.mobjects_to_copies.pop(mob, None)

    #last_m2c = scene.undo_stack[-1].mobjects_to_copies if scene.undo_stack else dict()
    last_m2c = dict()  # Makes some of the below redundant...
    for mob in self.mobjects_to_copies:
      # If it hasn't changed since the last state, just point to the
      # same copy as before
      if mob in last_m2c and last_m2c[mob].looks_identical(mob):
        self.mobjects_to_copies[mob] = last_m2c[mob]
      else:
        self.mobjects_to_copies[mob] = mob.copy()

  #def __eq__(self, state: SceneState):
  #  return all((
  #    self.time == state.time,
  #    self.num_plays == state.num_plays,
  #    self.mobjects_to_copies == state.mobjects_to_copies
  #  ))

  #def mobjects_match(self, state: SceneState):
  #  return self.mobjects_to_copies == state.mobjects_to_copies

  #def n_changes(self, state: SceneState):
  #  m2c = state.mobjects_to_copies
  #  return sum(
  #      1 - int(mob in m2c and mob.looks_identical(m2c[mob]))
  #      for mob in self.mobjects_to_copies
  #  )

  def restore_scene(self, scene: Scene):
    #scene.time = self.time
    scene.renderer.time = self.time
    #scene.num_plays = self.num_plays
    scene.mobjects = [
      mob.become(mob_copy)
      for mob, mob_copy in self.mobjects_to_copies.items()
    ]

# This is a heavily modified version of the code in 3b3t manim:
#   https://github.com/3b1b/manim/blob/master/manimlib/scene/scene_embed.py#L195
class CheckpointManager:
  def __init__(self):
    self.checkpoint_states: dict[str, list[tuple[Mobject, Mobject]]] = dict()

  def checkpoint_paste(self, ipy, scene_showing):
    """
    Used during interactive development to run (or re-run)
    a block of scene code.

    If the copied selection starts with a comment, this will
    revert to the state of the scene the first time this function
    was called on a block of code starting with that comment.
    """
    code_string = pyperclip.paste()
    checkpoint_key = self.get_leading_comment(code_string)
    if len(checkpoint_key)>0:
      #print(f"Checkpointing : {checkpoint_key=}")
      self.handle_checkpoint_key(scene_showing, checkpoint_key)

    code_deindent = textwrap.dedent(code_string)
    if True:
      print("Code to run:\n")
      print(code_deindent)

    ##shell.run_cell(code_string)
    ipy.ex(code_deindent)
    #ipy.run_code(code_deindent) # alternative?

  @staticmethod
  def get_leading_comment(code_string: str) -> str:
    leading_line = code_string.partition("\n")[0].lstrip()
    if leading_line.startswith("#"):
      return leading_line
    return ""

  def handle_checkpoint_key(self, scene_showing, key: str):
    if not key:
      return
    elif key in self.checkpoint_states:
      # Revert to checkpoint
      #scene.restore_state(self.checkpoint_states[key])
      self.checkpoint_states[key].restore_scene(scene_showing)
      print(f"Restored SceneState: {key}")

      # Clear out any saved states that show up later (i.e invalidate them)
      all_keys = list(self.checkpoint_states.keys())
      index = all_keys.index(key)
      for later_key in all_keys[index+1:]:
        self.checkpoint_states.pop(later_key)
        print(f"Killed Checkpoint key : {later_key}")
    else:
      #self.checkpoint_states[key] = scene.get_state()
      self.checkpoint_states[key] = SceneState(scene_showing)
      print(f"Saved SceneState: {key}")

  #def clear_checkpoints(self):
  #  self.checkpoint_states = dict()


checkpoint_manager = CheckpointManager()

# This is used in the iPython interactive session!
def checkpoint_paste():
  #code_string = pyperclip.paste()
  #print(code_string)
  ipy = get_ipython()
  scene_showing = ipy.ev('self')
  checkpoint_manager.checkpoint_paste(ipy, scene_showing)


# --- below here was just for initial development/experimentation ---


def interactive_write_bogo():
  #print(f"Received:\n{code_string.replace(' ','#')}")
  get_ipython().ex('''bogo=Text("BOGO");self.play(Write(bogo))''')
  # When this gets executed, `bogo` appears in interactive session
  # locals() (along with `title` and `self`)

def interactive_show_variables():
  # However, 'locals()' here only refers to function interior
  #vars = sorted(locals())
  # And 'globals()' refers to stuff outside the module, somehow
  #vars = sorted(globals())
  #vars = sorted(get_ipython().globals())  NOPE
  # These 'locals()' have the interactive session 'locals'
  #   which include the new variables, and self :-)
  # Perhaps these are defined in 
  #   https://github.com/ManimCommunity/manim/blob/main/manim/scene/scene.py#L1588
  vars = sorted(get_ipython().ev('locals()'))
  #print([v for v in vars if 't' in v or 'b' in v or 'f' in v])
  print([v for v in vars])
  """  Here are the get_ipython().ev('locals()')
    'In', 'Out', 
    '_dh', '_i', '_i1', '_ih', '_ii', '_iii', '_oh', 
    'exit', 'quit', 'get_ipython', 'open', 
    'play', 'wait', 'add', 'remove', 'interact', 
    'self', 
    'bogo', 'title', 
  """
  # mobject save_state / restore_state :
  #   https://github.com/ManimCommunity/manim/blob/main/manim/mobject/opengl/opengl_mobject.py#L1491
  print(get_ipython().ev('self'))


## Oddments
# get_ipython().ev()
# get_ipython().ex()
# get_ipython().run_code()
# eval('''bogo=Text("BOGO");self.play(Write(bogo))''')

