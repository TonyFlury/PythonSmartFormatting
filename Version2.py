class Temperature:
    _units = {'C':'celsius','F':'fahrenheit'}
    def __init__(self, initial):
        """Temperature in C or F with automatic translation between the two
        
             initial : numeric or str. If numeric is assumed to be initial value in degrees C.
                                       If str is assumed to be formatted with last letter C or F:
                                       e.g. '212F' will be taken to be 212 degrees Farenheit. 
             raises ValueError if str is not formatted correctly (eg. no unit as last letter),
                               or numeric is not valid converted to a float.
        """
        attribute = 'celsius'
        try:
            attribute = Temperature._units[initial[-1].upper()]
            value = initial[:-1]
        except KeyError:
            raise ValueError(f'Invalid initial Temperature given: {initial}') from None
        except TypeError:
            value = initial
            
        try:
            setattr(self, attribute, float(value))
        except (ValueError, TypeError):
                raise ValueError(f'Invalid initial Temperature given: {initial}') from None
            
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
