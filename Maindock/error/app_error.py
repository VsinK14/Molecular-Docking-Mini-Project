"""Custom error classes"""

class DockError(Exception):
    """Dock exception base class"""

    def __init__(self, cause):
        self.cause = cause

    def __str__(self):
        representation = "[%s] %s" % (self.__class__.__name__, self.cause)
        return representation


class DockWarning(DockError):
    """Custom error class intented only for warnings to be notified, not to fail"""

    pass

class RandomNumberError(DockError):
    """Custom RandomNumber exception"""

    pass

class GSOError(DockError):
    """Custom GSO exception"""

    pass

class GSOParameteresError(GSOError):
    """Custom GSOParameteres exception"""

    pass

class GSOCoordinatesError(GSOError):
    """Custom error for CoordinatesFileReader class"""

    pass

class StructureError(DockError):
    """General structure error"""

    pass

class BackboneError(StructureError):
    """General structure error"""

    pass

class SideChainError(StructureError):
    """General structure error"""

    pass

class ResidueNonStandardError(StructureError):
    """General structure error"""

    pass

class AtomError(StructureError):
    """Atom error exception"""

    pass

class MinimumVolumeEllipsoidError(StructureError):
    """MinimumVolumeEllipsoid exception"""

    pass

class PDBParsingError(DockError):
    """PDB parser error"""

    pass

class PDBParsingWarning(DockWarning):
    """PDB parser warning"""

    pass

class PotentialsParsingError(DockError):
    """Reading potential file error"""

    pass

class ScoringFunctionError(DockError):
    """Error in the scoring function drivers"""

    pass

class NotSupportedInScoringError(DockError):
    """Error to be raised when an atom or residue type is not supported by the scoring function"""
    
    pass

class NormalModesCalculationError(DockError):
    """Error in normal modes calculation"""

    pass

class SetupError(DockError):
    """Error in setup"""

    pass

class SwarmNumError(DockError):
    """Error in number of swarms"""

    pass

class MembraneSetupError(DockError):
    """Error in membrane setup"""

    pass