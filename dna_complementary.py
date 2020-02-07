

### START FUNCTION
def dna_complementary(dna):
    # define how key and values will be maped 
    maping = {'ins':'0'} 

    # A dictinary of links
    dict_links = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'} 

    #We assume other letters or characters may exist
    # other than 'ATGC' and we map them to single letters     
     
    for k,v in maping.items():
        dna = dna.replace(k,v)

    # store as a list
    dna_letters = list(dna)

    #reversing the list 
    dna_letters= reversed([dict_links.get(letter,letter) for letter in dna_letters])
    dna_letters = ''.join(dna_letters)
    for k,v in maping.items():
        dna_letters = dna_letters.replace(v,k)

    # returning the reversed string        
    return dna_letters[::-1]
    
### END FUNCTION 
dna = "ATCTTATAATTACCGAGTCGATCGG"
print("Reverse Complement:")
print(dna_complementary(dna))