#table od 5

def table(num):
    for x in range(1,10+1):
        print(f"{num} * {x} = ",num*x)
    

def even_number():
    for x in range(1,20+1):
        if x%2==0:
            print(x)


def count_down():
    for xd in range(10,0,-1):
        print(xd)

def sum1tosum10():
    s=0
    for x in range(1,10+1):
        s+=x
        print(s)

def starts():
    for xd in range(5):
        print("*",end="")

def info(name,age,college):
    print(f" name = {name}\n age ={age}\n college = {college}")







info("Aryan chaudhary",20,"koshi st james")
#starts()

#count_down()
# even_number()
# table(5)



#lambda arguments: expression



# lambda → creates the function
# arguments → inputs
# expression → what to return

# Important: A lambda can only contain one expression. You cannot write loops or multiple statements inside it.