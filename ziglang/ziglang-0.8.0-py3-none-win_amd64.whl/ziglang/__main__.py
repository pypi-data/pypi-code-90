import os, sys, subprocess
sys.exit(subprocess.call([
    os.path.join(os.path.dirname(__file__), "zig.exe"),
    *sys.argv[1:]
]))
