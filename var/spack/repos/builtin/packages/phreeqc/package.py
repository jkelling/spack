# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

#
# Author: Matteo Giantomassi <matteo.giantomassiNOSPAM AT uclouvain.be>
# Date: October 11, 2016
from spack import *

class Phreeqc(CMakePackage):
    """PHREEQC Version 3 is a computer program written in the C++ programming
    language that is designed to perform a wide variety of aqueous geochemical
    calculations. PHREEQC implements several types of aqueous models including
    two ion-association aqueous models.
    """

    homepage = 'https://www.usgs.gov/software/phreeqc-version-3'
    url      = 'http://water.usgs.gov/water-resources/software/PHREEQC/phreeqc-3.5.0-14000.tar.gz'

    version('3.5.0-14000', '0e77b2538d61df00212b9f648aae9c75')
