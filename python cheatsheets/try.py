# TODO:-Binary search
# from math import ceil
# numbers = int(input('How many elements you want to add in list'))
# l = []
# for i in range(numbers):
#     no = float(input(f'Enter {i+1} element'))
#     l.append(no)
# l.sort()
# choiceele = float(
#     input('Enter your element, which is you want to find from the list?'))
# legthlist = ceil(len(l)/2)
# if l[legthlist-1] > choiceele and legthlist-1 == 0:
#     print('Element not found')
# elif l[legthlist-1] < choiceele and legthlist-1 == 0:
#     for i in range(len(l)):
#         if l[i] == choiceele:
#             print('Element found successfully')
#             break
#         if i == len(l)-1:
#             print('Element not found')
#             break
# elif l[legthlist-1] == choiceele and legthlist-1 == 0:
#     print('Element found successfully')
# elif l[legthlist-1] == choiceele:
#     print('Element found successfully')
# elif l[legthlist-1] < choiceele:
#     for i in range(legthlist-1, len(l)):
#         if l[i] == choiceele:
#             print('Element found successfully')
#             break
#         if i == len(l)-1:
#             print('Element not found')
#             break
# elif l[legthlist-1] > choiceele:
#     for i in range(legthlist):
#         if l[i] == choiceele:
#             print('Element found successfully')
#             break
#         if i == legthlist:
#             print('Element not found')
#             break
# TODO:-Selecction sort
# for i in range(0, legthlist):
#     for j in range(0, legthlist):
#         if j == len(l)-1:
#             pass
#         elif l[j] > l[j+1]:
#             l[j], l[j+1] = l[j+1], l[j]
# for i in range(legthlist, len(l)):
#     for j in range(legthlist, len(l)):
#         if j == len(l)-1:
#             pass
#         elif l[j] > l[j+1]:
#             l[j], l[j+1] = l[j+1], l[j]
# for i in range(0, len(l)):
#     for j in range(0, len(l)):
#         if j == len(l)-1:
#             pass
#         elif l[j] > l[j+1]:
#             l[j], l[j+1] = l[j+1], l[j]
# print(l)
a = {'jay'}
a.pop()
a.add(5)
print(a)
