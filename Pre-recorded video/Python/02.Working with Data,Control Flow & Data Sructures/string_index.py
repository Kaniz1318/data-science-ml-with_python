a = "this is a string"
   #=0123456789101112131415  - index
   
# 1 -Karim
    #01234 -index
# 2 -Rahim
    #01234 -index
    
print(a[0])
print(a[15])
print(a[4])
print(len(a))  # len method

# maximum index = total length - 1 = 16-1 =15
#print(a[16])- output ashbena


#Last character printing(long method)
print(a[len(a)-1])

#Last character printing(short method)
print(a[-1])  #sudhu python e -(minus) diye ber kora jai

b = "Rahim"
#   -5 =R = 0
#   -4 =A = 1
#   -3 =H = 2
#   -2 =I = 3
#   -1 =M = 4

print(b[-2])
print(b[0])
print(b[-5])


#immutable data type

print(b[1])
b[1] = 'o'
print(b[1]) #error ase, karon string immutable ,vitorer kono character direct change korte parbona

    