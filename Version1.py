class Temperature:
    def __init__(self, initial)
	self.celsius = initial
            
    @property
    def celsius(self):
        return self._celsius
    @celsius.setter
    def celsius(self, value):
        self._celsius = value
    @property
    def fahrenheit(self):
        return 32+(self.celsius/5)*9
    @fahrenheit.setter
    def farhenheit(self, value):
        self.celsius = 5*(value-32)/9
