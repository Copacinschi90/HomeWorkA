xs =[12, 10, 32, 3, 66, 17, 42, 99, 20]
#1
for num in xs:
    print(num)
#2
    for num in xs:
        square= num**2
        print(num, 'square is', square)

#3

    total=0
    for num in xs:
        total += num
    print('Total is', total)


#4
    product=1
    for num in xs:
        product *= num
        print(product)


