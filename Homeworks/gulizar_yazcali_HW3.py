name1=input("Enter your name:")
vize1=float(input("Enter your midterm grade:"))
proje1=float(input("Enter your project grade:"))
final1=float(input("Enter your final grade:"))
print("\n")
name2=input("Enter your name:")
vize2=float(input("Enter your midterm grade:"))
proje2=float(input("Enter your project grade:"))
final2=float(input("Enter your final grade:"))
print("\n")
name3=input("Enter your name:")
vize3=float(input("Enter your midterm grade:"))
proje3=float(input("Enter your project grade:"))
final3=float(input("Enter your final grade:"))
print("\n")
name4=input("Enter your name:")
vize4=float(input("Enter your midterm grade:"))
proje4=float(input("Enter your project grade:"))
final4=float(input("Enter your final grade:"))
print("\n")
name5=input("Enter your name:")
vize5=float(input("Enter your midterm grade:"))
proje5=float(input("Enter your project grade:"))
final5=float(input("Enter your final grade:"))
print("\n")

ogr1=((vize1*0.3)+(proje1*0.3)+(final1*0.4))
dict1= {"Name:": name1, "Midterm Grade:": vize1, "Project Grade:": proje1, "Final Grade:": final1, "Grade:": ogr1}
print(dict1)

if ogr1 >= 60:
    print(name1 + " GEÇTİ")
elif ogr1 < 60:
    print(name1 + " KALDI")

print("\n")

ogr2=((vize2*0.3)+(proje2*0.3)+(final2*0.4))
dict2= {"Name:": name2, "Midterm Grade:": vize2, "Project Grade:": proje2, "Final Grade:": final2, "Grade:": ogr2}
print(dict2)

if ogr2 >= 60:
    print(name2 + " GEÇTİ")
elif ogr2 < 60:
    print(name2 + " KALDI")

print("\n")

ogr3=((vize3*0.3)+(proje3*0.3)+(final3*0.4))
dict3= {"Name:": name3, "Midterm Grade:": vize3, "Project Grade:": proje3, "Final Grade:": final3, "Grade:": ogr3}
print(dict3)

if ogr3 >= 60:
    print(name3 + " GEÇTİ")
elif ogr3 < 60:
    print(name3 + " KALDI")

print("\n")

ogr4=((vize4*0.3)+(proje4*0.3)+(final4*0.4))
dict4= {"Name:": name4, "Midterm Grade:": vize4, "Project Grade:": proje4, "Final Grade:": final4, "Grade:": ogr4}
print(dict4)

if ogr4 >= 60:
    print(name4 + " GEÇTİ")
elif ogr4 < 60:
    print(name4 + " KALDI")

print("\n")

ogr5=((vize5*0.3)+(proje5*0.3)+(final5*0.4))
dict5= {"Name:": name5, "Midterm Grade:": vize5, "Project Grade:": proje5, "Final Grade:": final5, "Grade:": ogr5}
print(dict5)

if ogr5 >= 60:
    print(name5 + " GEÇTİ")
elif ogr5 < 60:
    print(name5 + " KALDI")

print("\n")

mylist=[ogr1, ogr2, ogr3, ogr4, ogr5]
mylist.sort()
mylist.reverse()
print(mylist)
