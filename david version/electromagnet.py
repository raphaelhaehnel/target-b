


class Electromagnet:
    def __init__(self, n, R, relative_permeability_max):
        # Coil parmeters :
        self.n = n
        self.R = R
        # https://en.wikipedia.org/wiki/Permeability_(electromagnetism)
        self.relative_permeability_max = relative_permeability_max
    
    def get_n(self):
        return self.n
    
    def set_n(self, n):
        self.n = n
        
    def get_R(self):
        return self.R
    
    def set_R(self, R):
        self.R = R
        
    def get_relative_permeability_max(self):
        return self.relative_permeability_max
    
    def set_relative_permeability_max(self, relative_permeability_max):
        self.relative_permeability_max = relative_permeability_max
