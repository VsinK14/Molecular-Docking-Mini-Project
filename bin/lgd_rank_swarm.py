#!/usr/bin/env python3


"""Calculates the ranking file by scoring intra-swarm"""

import os
import argparse
from Maindock.util.logger import LoggingManager
from Maindock.Param import DEFAULT_SWARM_FOLDER, GSO_OUTPUT_FILE
from Maindock.util.analysis import read_output
from Maindock.util.analysis import write_ranking_to_file


log = LoggingManager.get_logger("lgd_rank_swarm")


def parse_command_line():
    parser = argparse.ArgumentParser(prog="lgd_rank_swarm")
    parser.add_argument(
        "num_swarms",
        help="number of swarms to consider",
        type=int,
        metavar="num_swarms",
    )
    parser.add_argument("steps", help="steps to consider", type=int, metavar="steps")
    return parser.parse_args()


if __name__ == "__main__":
    try:
        current_path = os.getcwd()
        args = parse_command_line()

        for swarm_id in range(args.num_swarms):
            os.chdir(f"{DEFAULT_SWARM_FOLDER}{swarm_id}")
            result_file_name = GSO_OUTPUT_FILE % args.steps
            dock_output = read_output(result_file_name)
            for g in dock_output:
                g.id_swarm = swarm_id
                g.pdb_file = f"dock_{g.id_glowworm}.pdb"
            write_ranking_to_file(dock_output, order_by="scoring")
            os.chdir(current_path)
    except IOError:
        log.warning("Either num_clusters or steps not found. Exiting...")
        raise SystemExit()
