def Result():
    name = input(" Enter you name =")
    eng= int(input(" enter you english marks"))
    math = int(input(" enter you math marks"))
    science = int(input(" enter you science marks"))

    if eng<40 or math<40 or science<40:
        print("fail")
    else:
        marks = (eng+math+science)/3
        


        if marks>=90:
            print("A+")
        elif marks>=80:
            print("A")
        elif marks>=70:
            print("B")
        elif marks>=60:
            print("c")
        elif marks>=40:
            print("d")
        
Result()