"""Configuration parameters.
"""


class Config:
    """ Encapsulates configuration parameters.
    """

    def __init__(self):

        self.working_dir_out = None
        self.run_start = None
        self.run_end = None
        self.time_total = None
        self.logfreq = None
        self.savefreq = None
        self.edge_length = None
        self.mtmassini = None
        self.segmassini = None
        self.use_fission = None
        self.rate_fission = None
        self.use_11_fusion = None
        self.fusion_rate_11 = None
        self.use_12_fusion = None
        self.fusion_rate_12 = None
        self.use_1c_fusion = None
        self.fusion_rate_1c = None

    def readin(self, f):

        """ Read the configuration data from the log file 'f'
        """

        def skip_lines(n):
            for _ in range(n):
                f.readline()

        skip_lines(2)            # Run started, empty
        self.working_dir_out = f.readline().split()[2]
        self.run_start = int(f.readline().split()[2])
        self.run_end = int(f.readline().split()[2])
        skip_lines(2)            # empty, reading...
        self.time_total = float(f.readline().split()[2])
        self.logfreq = int(f.readline().split()[2])
        self.savefreq = int(f.readline().split()[2])
        self.edge_length = float(f.readline().split()[2])
        self.mtmassini = int(f.readline().split()[2])
        self.segmassini = int(f.readline().split()[2])
        self.use_fission = bool(f.readline().split()[2])
        self.rate_fission = float(f.readline().split()[2])
        self.use_11_fusion = bool(f.readline().split()[2])
        self.fusion_rate_11 = float(f.readline().split()[2])
        self.use_12_fusion = bool(f.readline().split()[2])
        self.fusion_rate_12 = float(f.readline().split()[2])
        self.use_1c_fusion = bool(f.readline().split()[2])
        self.fusion_rate_1c = float(f.readline().split()[2])

    def __eq__(self, c):

        """ Equality operator.
        """

        for a in list(vars(self).keys()):
            if getattr(self, a) != getattr(c, a):
                return False

        return True
