class Converter():
    def __init__(self):
        self.conversion_table = {
     'mm': .001,
     'cm': .01,
     'm': 1,
     'km': 1000,
     'in': 0.0254 , 
     'inch': 0.0254, 
     'inches': 0.0254, 
     'ft': 0.3048, 
     'feet': 0.3048,
     'miles': 1609.34,
     'mi':  1609.34,
     }

    def convert(self, input_units, num_of_units, output_unit):
        output = float(num_of_units) * self.conversion_table[input_units] / self.conversion_table[output_unit]
        return output