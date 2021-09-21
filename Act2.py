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

if ave>=99 and ave<=100:
    print("A")
elif ave>=90 and ave<=98:
    print("B")
elif ave>=80 and ave<=89:
    print("C")
elif ave>=71 and ave<=79:
    print("D")
elif ave>=61 and ave<=70:
    print("E")
else:
    print("F")   