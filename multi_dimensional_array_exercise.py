us_in = input("m,n : eg. 5,3 ").split(",")
# print(us_in)
us_in = list(map(int,us_in))
# print(us_in)
main_array = []

for i in range(us_in[0]):
    main_array.append([])         # this way i can solve it
    for j in range(us_in[1]):
        main_array[i].append(i*j)      


# for i in range(us_in[0]):
#     main_array.append([])
#     for j in range(us_in[1]):
#         main_array[i].append(0)

                                # for better understanding i can write this code like this also
# for row in range(us_in[0]):
#     for col in range(us_in[1]):
#         main_array[row][col] = row*col

print(main_array)







