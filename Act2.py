print("PRINTING THE AVERAGE OF THE STUDENT")
pre=int(input("Enter Prelim: "))
mid=int(input("Enter Midterm: "))
sem=int(input("Enter SemiFinal: "))
fin=int(input("Enter Final: "))

tot=(pre+mid+sem+fin)
ave=tot/4

print(ave, "The average ")

if ave>=75:
    print("Passed")
else:
    print("Failed")