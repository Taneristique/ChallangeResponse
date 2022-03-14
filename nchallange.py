"answer of a new challange"
def bitmasker(x:int,n:int=0)->list:
    """Function masks the integer list,and produces bit lenght output as list by default,but if n is given it returns a list with
       n elementh.In both cases the elements of output are boolean."""
    return [bool(x>> i and 1) for i in range(n or x.bit_length())]
print(bitmasker(127,5))
print(bitmasker(1,5))
print(bitmasker(280))
print(bitmasker(280,7))
