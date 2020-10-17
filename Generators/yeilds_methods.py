# # -------------------------Yield Function
# def sample():
#     for i in range(10):
#         if (i % 2 == 0):
#             yield i
#
# print(sample())
# # ------------------------Next
# # list = [1,2,3,4,5,6,7,8]
# # z = (x**3 for x in list)
# # print(next(z))
# # print(next(z))
# # ------------------------Memory Management
# import sys
# num = [i*2 for i in range(1000)]
# print(sys.getsizeof(num))
# num_gen = (i**2 for i in range(1000))
# print(sys.getsizeof(num_gen))
# print(type(num_gen), type(num))
#
#
#
# # class Mynumber:
# #     def __iter__(self):
# #         self.number = 1
# #         return self
# #     def __next__(self):
# #         x = self.number
# #         self.number+=1
# #         return x
# #
# # mynum = Mynumber()
# # it = iter(mynum)
# # print(next(it))
# # print(next(it))
#
# #----------------------------------
# # from itertools import permutations
# # print(list(permutations("ABC")))
# #
# #
# import itertools
# lt = [1,2,3,4,5]
# print(list(itertools.accumulate(lt)))
# #--------------------------------
# # import itertools
# # l1 = [1,2,3]
# # l2 = [1,2,3,4,5]
# # l3 = [4,5,6,6]
# # print(list(itertools.chain(l1,l2,l3)))
# #
# # for i in itertools.count(10,5):
# #     if i == 45:
# #         print("Ravi")
# #         break
# #
# #     else:
# #         print(i,end=" ")
#
#
# #------------------------------------
# # import itertools
# # l = [1,2,3,4,5,6,7,8,66,777,888]
# # print(list(itertools.islice(l,2,8,2)))
#
# import itertools
# print(list(itertools.zip_longest('Raviprasad','LaxmiKalyani',fillvalue='love')))


# l=[1,2,3,4]
# l1 = [4,5,9]
# d = list(zip(l,l))
# print(d)
