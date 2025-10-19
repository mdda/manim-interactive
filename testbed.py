# Community edition default renderer (uses mp4 as display : SLOW)
# NOPE: manim -pql your_script_name.py TransformerDecoderScene

# Community edition GL renderer (can render dynamically : FAST)
# manim transformer.py TransformerDecoderScene --renderer=opengl -p
# '-p' = autoplay when done rendering
# Open up by doing : 
#   Create Terminal New Window = Ctrl-Shift-Alt-`
#     manim testbed.py SimpleTest --renderer=opengl -p
#   Manimgl: Select terminal (Python3)


# self.embed defined : https://github.com/ManimCommunity/manim/blob/main/manim/scene/scene.py#L1559
#   = specific to OpenGLRenderer

from manim import *
from manim_interactive import *


class SimpleTest(MovingCameraScene):
  def construct(self):
    # --- 1. One checkpoint ---
    title = Text("Transformer Decoder").to_edge(UP)
    self.play(Write(title))

    self.embed()  # Can now work on stuff *after this call*

    # --- 2. Next checkpoint ---
    other = Text("Autoregressive").to_edge(LEFT)
    self.play(Write(other))

    after = Text("Generation").to_edge(DOWN)
    self.play(Write(after))

# on fedora (during development)
#   # dnf install poetry
# poetry new --src manim-interactive

