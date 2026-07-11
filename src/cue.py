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
import logging
import os

logger = logging.getLogger(name="porygon")


def _read_file(path: str) -> tuple:
    """
    _read_file(path) -> lines 
    """
    lines = []
    with open(path, "r") as cfp:
        lines.append(cfp.readline())
    return lines

def _convert_first_line(line: str) -> [dict, str, str]:
    """
    _convert_first_line(line) -> contents

    First line format:
        FILE "<NAME>" <FORMAT>
    """
    contents = line.strip().split("\"")
    if len(contents) < 3:
        raise IndexError

    # Extract date and time.
    try:
        mix_date_str, mix_time_str = contents[1].split("_")
    except:
        raise IndexError
    # Saving on compute, hurting on prettiness today.
    mix_date_parts = mix_date_str.split("-")
    mix_time_raw = mix_time_str.split(".")[0]
    mix_datetime = {
            "year": mix_date_parts[0],
            "month": mix_date_parts[1],
            "day": mix_date_parts[2]
        }
    mix_name = contents[1]
    mix_filetype = contents[2].lower()

    return (mix_datetime, mix_name, mix_filetype)

def _convert_lines(lines: tuple[str]) -> dict:
    """
    _convert_lines(lines) -> contents
    """
    cue = {}

    # The first line of the file has the name and mix filetype. 
    try:
        (cue["datetime"],
         cue["filename"],
         cue["filetype"]) = _convert_first_line(line=lines[0])
    except IndexError:
        logger.error(f"Cue has invalid first line format: {lines[0]}")

    logger.info(cue)

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
