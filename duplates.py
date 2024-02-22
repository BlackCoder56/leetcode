def Containsduplicate():
    nums = [1,2,3]
    
    if len(set(nums)) != len(nums):
        print("True")
    elif len(set(nums)) == len(nums):
        print("False")
         
Containsduplicate()