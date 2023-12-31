"""LightDock protein-protein docking framework library"""

import os

__author__ = "Brian Jimenez-Garcia"
__email__ = "br.jimenezgarcia@gmail.com"
__credits__ = ["Brian Jimenez-Garcia", "Jorge Roel", "Miquel Vidal"]
__license__ = "GPL"
__version__ = "3.0"


# Set global path variables
lightdock_path = os.path.normpath(os.path.dirname(os.path.realpath(__file__)))
configuration_path = "%s%s%s%s" % (lightdock_path, os.sep, "etc", os.sep)

os.environ["LIGHTDOCK_PATH"] = lightdock_path
os.environ["LIGHTDOCK_CONF_PATH"] = configuration_path
