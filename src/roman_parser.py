class RomanParser:
    def parse(self,number):
        romanNumber = 'I'
        if number == 2 :
            romanNumber+=romanNumber
        return romanNumber