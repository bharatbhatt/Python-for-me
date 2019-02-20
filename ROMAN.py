class ROMAN:

    def chan_to_rom (self,dec_num):
        roman =''
        while dec_num > 0:
            for k , v in dict1:
                print (k)
                print (v)
                while dec_num >= k:
                    print (k)
                    roman = roman + v
                    dec_num =dec_num - k
        return roman


dec= input("Enter the decimal")
print (len(dec))
dec2=int(dec)
obj = ROMAN()
print(dec2)
print (type(dec2))
dict1= [(1000, "M"), (900 , "CM"), (500, "D") , (400 , "CD") , (100 , "C ") , (90 , "XC") ,(50 ,"L"), (40 , "XL"), (10 ,"X"),(9 ,"IX"), (5 ,"V") , (4 , "IV") ,(1 , "I")]
print ("ROMAN NUMBER : " ,obj.chan_to_rom (dec2))

''' dict1[ value) in dict1(itmes):
print (dict1[5])
five = 'V'
print (5)
check = int (str(200)[0])
print (type(check))
print (check)
'''

'''def chan_to_rom (dec_num):
    roman =''
    while dec_num > 0:
        for k , v in dict1.items():
            dec_num >= k
            roman = roman + v
            dec_num =dec_num - k
    return roman
            
'''        
