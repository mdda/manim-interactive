import pyperclip


# This is used in the iPython interactive session!
def checkpoint_paste():
  code_string = pyperclip.paste()
  #print(f"Received:\n{code_string.replace(' ','#')}")
  get_ipython().ex('''bogo=Text("BOGO");self.play(Write(bogo))''')
  # When this gets executed, `bogo` appears in interactive session
  # locals() (along with `title` and `self`)

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



# get_ipython().ev()
# get_ipython().ex()
# get_ipython().run_code()
# eval('''bogo=Text("BOGO");self.play(Write(bogo))''')

# Scene state copying:
#   https://github.com/3b1b/manim/blob/master/manimlib/scene/scene.py#L882
# Restore scene state:
#   https://github.com/3b1b/manim/blob/master/manimlib/scene/scene.py#L917
