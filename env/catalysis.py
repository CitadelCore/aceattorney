#!/usr/bin/env python3
import argparse
import subprocess
from pathlib import Path

parser = argparse.ArgumentParser("catalysis", description="Wrapper script to start Catalysis")
parser.add_argument("-c", "--case", type=Path, default=Path.cwd(), help="Path to the case to use")

args = parser.parse_args()
base = Path.resolve(args.case)

if not base.exists():
    print("the specified case dir does not exist")
    exit(1)

selector = base.joinpath("selector.txt")
if not selector.exists():
    print("selector.txt must be present in the case folder")
    exit(1)

subprocess.run(["docker", "run", "-it", "--rm"
    "-v", ""
])
