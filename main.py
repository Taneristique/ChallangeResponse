def fct(word,shift):
    """This function gets two parameter 
        word : string and shift : integer.
        Then it will automatically create an empty list called elist and empty word called eword.
        It will create new words as shifting your word via shift parameter and an eword which is string type variable.
        Then it will add each string to the elist via second for loop.
        This way maximum shift times world will be created by function.
    """
    eword=""
    elist=[]
    for i in range(0,shift): #main loop the length of list will be equal to shift parameter 
        for w in range(i,len(word),shift):  #create new words and add them to empty list as shifting words
            if(len(word)-1>=w+shift):
                eword+=word[w]
            else:
                eword+=word[w]
                elist.append(eword)
                eword=""
                break
    return(print(elist))
fct('fboaor',2)