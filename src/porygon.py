"""
File:
    porygon.py

Description:
    DJ/Mixxx interface and note-taking companion.

Authors:
    nubby

Date:
    11 Jul 2026

Version:
    0.0.1
"""
import argparse
import os

import cue


def _find_cues_and_mixes(path_base: str) -> tuple[str, str]:
    """
    _find_cues_and_mixes(path_base) -> paths_cues, paths_mixes
    """
    paths_cues = []
    paths_mixes = []

    # Identify all desired files by extensions.
    with os.scandir(path) as bp:
        for path in bp:
            if path.is_file():
                if path.name.endswith("cue"):
                    paths_cues.append(path)
                elif path.name.endswith("wav"):
                    # TODO: Make this more type-agnostic.
                    paths_mixes.append(path)
    return (paths_cues, paths_mixes)

def load_mixes(path_base: str) -> dict:
    """
    load_mixes(path) -> mixes
    """
    # First find all file paths.
    paths_cues, paths_mixes = _find_cues_and_mixes(path_base=path_base)

    # Now generate new Mixes based on info from each cue.
    # TODO: Mix objects.
    mixes = {}
    for path_cue in paths_cues:
        mix_cue = cue.load_file(path=path_cue)

    return {}

def porygon(path_mixes: str):
    """
    porygon(path_mixes)
    """
    # Load information about any newly-added mixes.
    mixes = load_mixes(path_base=path_mixes)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
            description=("A Pokemon that consists entirely of programming code."
                         " Capable of moving freely in cyberspace."
                         "\n\tAlso, DJ/Mixxx interface and note-taking"
                         " companion.")
        )
    parser.add_argument(
            "--mix-path",
            default="~/Music/Mixxx/Recordings/",
            type=str,
            help=("Path to directory containing both recorded mixes and their"
                  " respective .cue files.")
        )

    args = parser.parse_args()

    porygon(path_mixes=args.path_mixes)
