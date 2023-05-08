#!/usr/bin/env python3

import os
import pathlib
import shutil
import subprocess


def search_font(name, ext):
    base_path = pathlib.Path("/Library/Application Support/Morisawa")
    for path in base_path.glob(f"**/*.{ext}"):
        with open(path, "rb") as fp:
            bytes = fp.read()
            if bytes.find((name + name[0]).encode()) >= 0:
                return path


texmf_dir = "/usr/local/texlive/texmf-local"
os.makedirs(f"{texmf_dir}/fonts/truetype/cjk-gs-integrate", exist_ok=True)

table = {
    "BIZ-UDReimin-Light": "ttc",
    "BIZ-UDReimin": "ttc",
    "BIZ-UDReimin-Bold": "ttc",
    "BIZ-UDShinGo-Medium": "ttc",
    "BIZ-UDShinGo-Bold": "ttc",
    "BIZ-UDShinGo-Heavy": "ttc",
    "BIZ-UDShinMGo": "ttc",
}

for name, ext in table.items():
    font_path = search_font(name, ext)
    if font_path is None:
        print(f"font not found: {name}")
        exit(1)
    path_from = str(font_path)
    path_to = f"{texmf_dir}/fonts/truetype/cjk-gs-integrate/{name}.{ext}"
    print(f"create symlink: {path_from} -> {path_to}")
    if os.path.islink(path_to):
        os.remove(path_to)
    os.symlink(path_from, path_to)

shutil.copytree(
    "ptex-fontmaps", f"{texmf_dir}/fonts/map/dvipdfmx/ptex-fontmaps", dirs_exist_ok=True
)

subprocess.run(["mktexlsr"])
