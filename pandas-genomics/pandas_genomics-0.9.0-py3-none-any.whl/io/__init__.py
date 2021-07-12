"""
Input/Output
------------
The `io` module provides functions for loading and saving GenotypeArrays to common variant formats

.. autosummary::
     :toctree: io

     from_plink
     to_plink
     from_vcf
"""

from .plink import from_plink, to_plink
from .vcf import from_vcf

__all__ = ["from_plink", "to_plink", "from_vcf"]
