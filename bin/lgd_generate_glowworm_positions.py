#!/usr/bin/env python3

"""Creates a PDB with atom points representing the position for each of the glowworms of a swarm"""

import argparse
import os
from Maindock.pdbutil.PDBIO import create_pdb_from_points
from Maindock.util.logger import LoggingManager


log = LoggingManager.get_logger("generate_glowworm_positions")


def valid_file(file_name):
    """Checks if it is a valid file"""
    if not os.path.exists(file_name):
        raise argparse.ArgumentTypeError("The file does not exist")
    return file_name


def parse_output_file(dock_output):
    glowworm_translations = []

    data_file = open(dock_output)
    lines = data_file.readlines()
    data_file.close()

    counter = 0
    for line in lines:
        if line[0] == "(":
            counter += 1
            last = line.index(")")
            coord = line[1:last].split(",")
            glowworm_translations.append(
                [float(coord[0]), float(coord[1]), float(coord[2])]
            )
    log.info("Read %s coordinate lines" % counter)
    return glowworm_translations


if __name__ == "__main__":

    parser = argparse.ArgumentParser(prog="generate_glowworm_positions")
    # output file
    parser.add_argument(
        "dock_output",
        help="dock output file",
        type=valid_file,
        metavar="dock_output",
    )
    args = parser.parse_args()

    # Output file
    translations = parse_output_file(args.dock_output)

    # Destination path is the same as the output
    destination_path = os.path.dirname(args.dock_output)
    pdb_file_name = os.path.splitext(args.dock_output)[0] + ".pdb"

    create_pdb_from_points(os.path.join(destination_path, pdb_file_name), translations, res_name="GLW")
    log.info("PDB %s file created." % os.path.join(destination_path, pdb_file_name))
