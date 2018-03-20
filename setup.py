from cx_Freeze import setup, Executable

setup(
    name = "trubs",
    version = "1.0",
    description = "Freelance Parser",
    executables = [Executable("login.py")]
)
