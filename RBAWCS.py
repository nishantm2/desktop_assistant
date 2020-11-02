import sys
   9 
  10 try:
  11     import Tkinter as tk
  12 except ImportError:
  13     import tkinter as tk
  14 
  15 try:
  16     import ttk
  17     py3 = False
  18 except ImportError:
  19     import tkinter.ttk as ttk
  20     py3 = True
  21 
  22 def init(top, gui, *args, **kwargs):
  23     global w, top_level, root
  24     w = gui
  25     top_level = top
  26     root = top
  27 
  28 def destroy_window():
  29     # Function which closes the window.
  30     global top_level
  31     top_level.destroy()
  32     top_level = None
  33 
  34 if __name__ == '__main__':
  35     import nis
  36     nis.vp_start_gui()