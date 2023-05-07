"""Tests for GSOBuilder class using J1 function"""


import os
import shutil
import filecmp
from pathlib import Path
from Maindock.gso.Parameters import GSOParameters
from Maindock.gso.algorithm import GSOBuilder
from Maindock.gso.Boundaries import Boundary, BoundingBox
from Maindock.Math.lrandom import MTGenerator
from Maindock.Param import MAX_TRANSLATION, MAX_ROTATION
from Maindock.structure.complex import Complex
from Maindock.pdbutil.PDBIO import parse_complex_from_file
from Maindock.scoring.mj3h.driver import MJ3h, MJ3hAdapter


class TestGSOBuilder:
    def __init__(self):
        self.path = Path(__file__).absolute().parent
        self.test_path = self.path / "scratch_dockbuilder"
        self.golden_data_path = self.path / "golden_data"
        self.gso_parameters = GSOParameters()

        self.bounding_box = BoundingBox(
            [
                Boundary(-MAX_TRANSLATION, MAX_TRANSLATION),
                Boundary(-MAX_TRANSLATION, MAX_TRANSLATION),
                Boundary(-MAX_TRANSLATION, MAX_TRANSLATION),
                Boundary(-MAX_ROTATION, MAX_ROTATION),
                Boundary(-MAX_ROTATION, MAX_ROTATION),
                Boundary(-MAX_ROTATION, MAX_ROTATION),
                Boundary(-MAX_ROTATION, MAX_ROTATION),
            ]
        )
        self.random_number_generator = MTGenerator(324324)

    def setup(self):
        try:
            shutil.rmtree(self.test_path)
        except OSError:
            pass
        os.mkdir(self.test_path)

    def teardown(self):
        try:
            shutil.rmtree(self.test_path)
        except OSError:
            pass

    def test_GSOBuilder_using_FromFileInitializer(self):
        builder = GSOBuilder()
        number_of_glowworms = 5
        atoms, _, chains = parse_complex_from_file(
            self.golden_data_path / "1PPErec.pdb"
        )
        receptor = Complex(chains, atoms)
        atoms, _, chains = parse_complex_from_file(
            self.golden_data_path / "1PPElig.pdb"
        )
        ligand = Complex(chains, atoms)
        adapter = MJ3hAdapter(receptor, ligand)
        scoring_function = MJ3h()
        gso = builder.create_from_file(
            number_of_glowworms,
            self.random_number_generator,
            self.gso_parameters,
            [adapter],
            [scoring_function],
            self.bounding_box,
            self.golden_data_path / "initial_positions_1PPE.txt",
            0.5,
            0.5,
            0.5,
            False,
            10,
            10,
        )

        assert gso.swarm.get_size() == 5

        gso.report(self.test_path / "report.out")
        assert filecmp.cmp(
            self.golden_data_path / "report_dockbuilder.out",
            self.test_path / "report.out",
        )
