"""
File:
    cue.py

Description:
    Interfaces and tools related to .cue files.

Authors:
    nubby

Date:
    11 Jul 2026

Version:
    0.0.1
"""
import os


def _read_file(path: str) -> tuple:
    """
    _read_file(path) -> lines 
    """
    lines = []
    with open(path, "r") as cfp:
        lines.append(cfp.readline())
    return lines

def _convert_first_line(line: str) -> tuple[str]:
    """
    _convert_first_line(line) -> contents

    First line format:
        FILE "<NAME>" <FORMAT>
    """
    contents = line.split("\"")
    if len(contents) < 3:
        raise IndexError

    return (contents[1], contents[2].lower())

def _convert_lines(lines: tuple[str]) -> dict:
    """
    _convert_lines(lines) -> contents
    """
    cue = {}

    # The first line of the file has the name and mix filetype. 
    cue["filename"], cue["filetype"] = _convert_first_line(line=lines[0])

    print(cue)
    exit()

def read(path: str) -> dict:
    """
    read(path) -> contents

    Read the contents of a .cue file and return a dict with info on its
    contents.
    """
    # Confirm file exists.
    if not os.path.isfile(path):
        raise FileNotFoundError

    # Format .cue file into dict in two steps.
    cue_lines = _read_file(path=path)
    cue = _convert_lines(lines=cue_lines)
    
    return cue
