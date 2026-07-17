"""Create a dictionary containing:

name
age
country

Print the dictionary."""

data ={
    "name":"Aryan chaudhary",
    "college":"koshi st james",
    "addresss":"itahari",
    "isNepali":True,
    "age":20,
}
print(data)


#create student dict and print only name
student ={
    "name":"Anjan chaudhary",
    "college":"koshi st james",
    "addresss":"dharan",
    "class":12,
}
print(student["name"])

#create a car dict and add color : white

car={
    "cc":1000,
    "model":2025,
    "cmpny":"mahindra"
}
car.update({"color":"white"})
print(car)

#change the page number
book={
    "author":"Aryan chuadhary",
    "pages":187,
}
book.update({"pages":190})
print(book)

#print math marks
marks = {
    "Math": 90,
    "English": 85,
    "Science": 80
}
print(marks["Math"])

#adding computer marks in marks dict
marks.update({"Coumpter":96})
print(marks)
#remove science from dict

marks.pop("Science")
print(marks)

student = {
    "name": "Aryan",
    "age": 20,
    "country": "Nepal",
    "college": "ABC College",
    "semester": 2
}

print(student.keys())      # Print all keys
print(student.values())    # Print all values
print(student.items())     # Print all key-value pairs

#len of key value

fav={
    "college":"koshi",
    "fruit":"mango",
    "fav_place":"home",

}
print(len(fav.items()))

#salay in dic or not with in method

employee = {
    "name": "Aryan",
    "age": 20,
    "salary": 50000,
    "department": "IT"
}

print("salary" in employee)