questions =[[ " which is the capital city of India? ", "Delhi","Bengaluru","Mumbai","Belagavi",1],
            [ " which is the capital city of India? ", "Delhi","Bengaluru","Mumbai","Belagavi",1],
            [ " which is the capital city of India? ", "Delhi","Bengaluru","Mumbai","Belagavi",1],
            [ " which is the capital city of India? ", "Delhi","Bengaluru","Mumbai","Belagavi",1],
            [ " which is the capital city of India? ", "Delhi","Bengaluru","Mumbai","Belagavi",1],
            [ " which is the capital city of India? ", "Delhi","Bengaluru","Mumbai","Belagavi",1],
            [ " which is the capital city of India? ", "Delhi","Bengaluru","Mumbai","Belagavi",1],
            [ " which is the capital city of India? ", "Delhi","Bengaluru","Mumbai","Belagavi",1]]

levels = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]

money = 0

for i in range(0, len(questions)):
    question = questions[i]
    print(f"\n\nQuestion for Rs. {levels[i]}\n{question[0]}: ")
    print(f"a.{question[1]}         b.{question[2]}")
    print(f"a.{question[3]}         b.{question[4]}")
    reply = int(input("Enter your choice(1-4): "))
    if (reply == question[-1]):
        print(f"Correct answer. you won Rs.  {levels[i]}")
        if (i==5):
            money = 5000
        elif(i==7):
            money=7000
    else:
        print("Wrong answer!!")
        break
print(f"\n your take home money is {money}")
