import os

import setuptools
from distutils.core import Extension
from setuptools.command.test import test as TestCommand
from Maindock.version import CURRENT_VERSION

class NoseTestCommand(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import nose

        nose.run_exit(argv=["nosetests"])


with open("README.md", "r") as fh:
    long_description = fh.read()


# MDAnalysis NumPy delay on setup.py
def abspath(file):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), file)


class DExtension(Extension, object):
    """Derived class for handling setup-time (numpy) dependencies."""

    def __init__(self, name, sources, *args, **kwargs):
        self._ld_include_dirs = []
        super(DExtension, self).__init__(name, sources, *args, **kwargs)

    @property
    def include_dirs(self):
        if not self._ld_include_dirs:
            for item in self._ld_include_dir_args:
                try:
                    self._ld_include_dirs.append(item())
                except TypeError:
                    item = abspath(item)
                    self._ld_include_dirs.append((item))
        return self._ld_include_dirs

    @include_dirs.setter
    def include_dirs(self, val):
        self._ld_include_dir_args = val


def get_numpy_include():
    import builtins

    builtins.__NUMPY_SETUP__ = False
    try:
        import numpy as np
    except ImportError:
        raise SystemExit("Dock requires NumPy for setup")
    return np.get_include()


exts = [
    DExtension(
        name="Main.Math.cython.cutil",
        sources=["Main/Math/cython/cutil.c"],
        include_dirs=[get_numpy_include],
    ),
    DExtension(
        name="Main.Math.cython.quaternion",
        sources=["Main/Math/cython/quaternion.c"],
        include_dirs=[get_numpy_include],
    ),
    DExtension(
        name="Main.gso.searchspace.cython.j1",
        sources=["Main/gso/searchspace/cython/j1.c"],
        include_dirs=[get_numpy_include],
    ),
    DExtension(
        name="Main.gso.searchspace.cython.j2",
        sources=["Main/gso/searchspace/cython/j2.c"],
        include_dirs=[get_numpy_include],
    ),
    DExtension(
        name="Main.gso.searchspace.cython.j3",
        sources=["Main/gso/searchspace/cython/j3.c"],
        include_dirs=[get_numpy_include],
    ),
    DExtension(
        name="Main.gso.searchspace.cython.j4",
        sources=["Main/gso/searchspace/cython/j4.c"],
        include_dirs=[get_numpy_include],
    ),
    DExtension(
        name="Main.gso.searchspace.cython.j5",
        sources=["Main/gso/searchspace/cython/j5.c"],
        include_dirs=[get_numpy_include],
    ),
    DExtension(
        name="Main.scoring.pisa.cython.cpisa",
        sources=["Main/scoring/pisa/cython/cpisa.c"],
        include_dirs=[get_numpy_include],
    ),
    DExtension(
        name="Main.scoring.dfire.cython.cdfire",
        sources=["Main/scoring/dfire/cython/cdfire.c"],
        include_dirs=[get_numpy_include],
    ),
    DExtension(
        name="Main.scoring.ddna.cython.cddna",
        sources=["Main/scoring/ddna/cython/cddna.c"],
        include_dirs=[get_numpy_include],
    ),
    DExtension(
        name="Main.scoring.dfire2.c.cdfire2",
        sources=["Main/scoring/dfire2/c/cdfire2.c"],
        include_dirs=[get_numpy_include],
    ),
    DExtension(
        name="Main.scoring.sd.energy.c.sd",
        sources=["Main/scoring/sd/energy/c/sd.c"],
        include_dirs=[get_numpy_include],
    ),
    DExtension(
        name="Main.scoring.fastdfire.c.cdfire",
        sources=["Main/scoring/fastdfire/c/cdfire.c"],
        include_dirs=[get_numpy_include],
    ),
    DExtension(
        name="Main.scoring.cpydock.energy.c.cpydock",
        sources=["Main/scoring/cpydock/energy/c/cpydock.c"],
        include_dirs=[get_numpy_include],
    ),
    DExtension(
        name="Main.scoring.vdw.energy.c.cvdw",
        sources=["Main/scoring/vdw/energy/c/cvdw.c"],
        include_dirs=[get_numpy_include],
    ),
    DExtension(
        name="Main.scoring.dna.energy.c.cdna",
        sources=["Main/scoring/dna/energy/c/cdna.c"],
        include_dirs=[get_numpy_include],
    ),
    DExtension(
        name="Main.scoring.sipper.c.sipper",
        sources=["Main/scoring/sipper/c/sipper.c"],
        include_dirs=[get_numpy_include],
    ),
]

setuptools.setup(
    name="Docker",
    version=CURRENT_VERSION,
    description="A macromolecular docking framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://lightdock.org/",
    packages=setuptools.find_namespace_packages(),
    include_package_data=True,
    license="GPLv3 License",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Scientific/Engineering :: Chemistry",
    ],
    python_requires=">=3.6",
    setup_requires=["numpy>=1.17.1", "nose"],
    install_requires=[
        "numpy>=1.17.1",
        "scipy>=1.7.0",
        "cython>=0.29.13",
        "prody>=2.0.1",
        "freesasa>=2.0.3",
    ],
    scripts=[
        "bin/ant_thony.py",
        "bin/lgd_calculate_diameter.py",
        "bin/lgd_calculate_reference_points.py",
        "bin/lgd_calculate_scoring.py",
        "bin/lgd_cluster_bsas.py",
        "bin/lgd_copy_structures.py",
        "bin/lgd_create_membrane.py",
        "bin/lgd_dummify.py",
        "bin/lgd_filter_membrane.py",
        "bin/lgd_filter_restraints.py",
        "bin/lgd_flatten.py",
        "bin/lgd_generate_conformations.py",
        "bin/lgd_generate_glowworm_positions.py",
        "bin/lgd_generate_trajectory.py",
        "bin/lgd_gso_to_csv.py",
        "bin/lgd_map_contacts.py",
        "bin/lgd_move_anm.py",
        "bin/lgd_rank.py",
        "bin/lgd_rank_swarm.py",
        "bin/lgd_top.py",
        "bin/dock3.py",
        "bin/dock3_setup.py",
    ],
    cmdclass={"test": NoseTestCommand},
    ext_modules=exts,
    zip_safe=False,
)
