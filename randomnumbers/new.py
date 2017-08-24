import random
def playlist():
 nums1 = []
 for nums in range(10):
       
        my_nums = random.randint(1,9)
        nums1.append(my_nums)
        print my_nums

 for i in nums1:
  if nums1[i]+nums1[i+1]==10 :
   print("The first numbers whose sum is 10 are:", nums1[i],nums1[i+1])
   break
  else :
    i=i+1
 
playlist()