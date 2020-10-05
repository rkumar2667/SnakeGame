import cx_Freeze

executables = [cx_Freeze.Executable("game.py")]

cx_Freeze.setup(
    name = "SnakeXenzia",
    options = {"build_exe":{"packages":["pygame"],"include_files":["apple.png","head.jpg","icon.png"]}},
    description = "SnakeXenzia Game 2.0",
    executables = executables
)
