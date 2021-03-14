#CV application
#Each dictionary represents a CV
#cv={name, age, jobtitle}
cv1= {"Name":"Aslı", 
      "Age":23, 
      "Jobtitle":"Interior Architect"}
cv2= {"Name":"Eda", 
      "Age":22, 
      "Jobtitle":"Translator"}
cv3= {"Name":"Güliz", 
      "Age":24, 
      "Jobtitle":"Geomatic Engineer"}
cv4= {"Name":"Nisa", 
      "Age":21, 
      "Jobtitle":"Lawyer"}
cv5= {"Name":"Melisa", 
      "Age":28, 
      "Jobtitle":"Journalist"}

print("CV1")
for i,j in cv1.items():
  print(str(i) + " : " + str(j))
print("\n")

print("CV2")
for i,j in cv2.items():
  print(str(i) + " : " + str(j))
print("\n")

print("CV3")
for i,j in cv3.items():
  print(str(i) + " : " + str(j))
print("\n")

print("CV4")
for i,j in cv4.items():
  print(str(i) + " : " + str(j))
print("\n")

print("CV5")
for i,j in cv5.items():
  print(str(i) + " : " + str(j))
print("\n")