class Temperature:
    _units = {'C':'celsius','F':'fahrenheit'}
    def __init__(self, initial):
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
        return 32+(self._celsius/5)*9
    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = 5*(value-32)/9
        
    def __format__(self, format_spec):
        attribute = Temperature._units.get(format_spec[-1],None)
        if not attribute:
            return format(self.celsius,format_spec)
        else:
            return format(getattr(self, attribute),format_spec[:-1]+'f')+'\u00B0'+format_spec[-1]
        
freezing = Temperature('0C')
boiling = Temperature(100)
print(freezing.fahrenheit, boiling.fahrenheit)
print('f{freezing:0.1C}, {freezing:0.1F}')
print('f{boiling:0.1C}, {boiling:0.1F}')
invalid = Temperature('fredF')
