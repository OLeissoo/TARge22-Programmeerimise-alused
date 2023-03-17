class Error(Exception):
    """Base class for other exceptions"""
    pass
    
class AgeInvalid(Error):
    """Raised when input of age is invalid"""
    pass

class HeightInvalid(Error):
    """Raised when input of age is invalid"""
    pass

class WeightInvalid(Error):
    """Raised when input of age is invalid"""
    pass

def CalculateBMI(height, weight):
    return weight / (height ** 2)

def AskValues():
    age,length,weight = 0,0,0
    try:
        age = int(input("Sisesta oma vanus: "))
    except ValueError:
        raise AgeInvalid
    finally:
        try:
            height = int(input("Sisesta oma pikkus: "))
        except ValueError:
            raise HeightInvalid
        try:
            weight = int(input("Sisesta oma kaal: "))
        except ValueError:
            raise WeightInvalid
        return age, height / 100, weight
    