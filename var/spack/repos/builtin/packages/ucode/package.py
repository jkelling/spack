# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

#
# Author: Jeffrey Kelling <j.kellingNOSPAM AT hzdr.de>
# Date: June 13, 2019
from spack import *
import os

class Ucode(Package):
    """UCODE_2014 and auxiliary computer codes for universal sensitivity
    analysis, calibration, and uncertainty evaluation.
    """

    homepage = 'https://igwmc.mines.edu/ucode-2/'
    url      = "https://wpfiles.mines.edu/igwmc/UCODE/ucode_2014_1.004.tgz"

    version('2014_1.004', sha256='7db967338499647c53b17703c46f0ca790646dfb0fbeda6cf7f8f85d91d376fd')

    variant('all', default=False,
            description='Builds and installs all targets')

    def install(self, spec, prefix):
        if '+all' in spec:
            make("-C", "bin/", "all", "F90={}".format(spack_fc), parallel=False)
        else:
            make("-C", "bin/", "F90={}".format(spack_fc), parallel=False)
        make("-C", "bin/", "clean")
        mkdirp(prefix.bin)
        for root, dirs, files in os.walk(os.path.join(self.stage.source_path, "bin")):
            for name in files:
                if os.access(os.path.join(self.stage.source_path, "bin", name), os.X_OK):
                    install(os.path.join("bin/", name), prefix.bin)
