"""Tests for GSOBuilder class using J1 function"""


import os
from pathlib import Path
from Maindock.gso.Parameters import GSOParameters
from Maindock.gso.searchspace.benchmark_ofunctions import J1
from Maindock.gso.algorithm import GSOBuilder
from Maindock.gso.Boundaries import Boundary, BoundingBox
from Maindock.Math.lrandom import MTGenerator


class TestGSOBuilderInJ1:
    def __init__(self):
        self.golden_data_path = Path(__file__).absolute().parent / "golden_data"
        self.gso_parameters = GSOParameters()
        self.objective_function = J1()
        self.bounding_box = BoundingBox([Boundary(1, 2), Boundary(10, 15)])
        self.number_of_glowworms = 50
        self.random_number_generator = MTGenerator(324324)

    def test_GSOBuilder_using_FromFileInitializer(self):
        builder = GSOBuilder()
        gso = builder.create_from_file(
            self.number_of_glowworms,
            self.random_number_generator,
            self.gso_parameters,
            self.objective_function,
            self.bounding_box,
            self.golden_data_path / "initial_positions.txt",
        )
        population_lines = str(gso.swarm).split(os.linesep)
        expected_lines = open(
            self.golden_data_path / "initial_population_from_file.txt"
        ).readlines()

        assert len(expected_lines) == len(population_lines)
        for line1, line2 in zip(expected_lines, population_lines):
            assert line1.rstrip() == line2.rstrip()

    def test_GSOBuilder_using_RandomInitializer(self):
        builder = GSOBuilder()
        gso = builder.create(
            self.number_of_glowworms,
            self.random_number_generator,
            self.gso_parameters,
            self.objective_function,
            self.bounding_box,
        )
        population_lines = str(gso.swarm).split(os.linesep)
        expected_lines = open(
            self.golden_data_path / "initial_population_random.txt"
        ).readlines()

        assert len(expected_lines) == len(population_lines)
        for line1, line2 in zip(expected_lines, population_lines):
            assert line1.rstrip() == line2.rstrip()
