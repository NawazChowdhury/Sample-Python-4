height=int(input("Enter height in cm"))
weight=float(input("Enter weight"))
last_weight=float(input("Last weight"))
overall_assesment=int(input("Overall Assesment"))


bmi=((weight/ (height**2)) * 10000)

bmi=round(bmi,1)

print("BMI=",bmi)


if(bmi>30):
    intermediate_helath_score=0
elif(bmi>25 and bmi<29.9):
    intermediate_helath_score=3
elif(bmi>18.5 and bmi<24.9):
    intermediate_helath_score=5
elif(bmi<18.5):
    intermediate_helath_score=3

print("Intermediate Score=",intermediate_helath_score)


weight_chnage= weight-last_weight

if(weight_chnage==1):
    intermediate_helath_score=intermediate_helath_score-1

if(weight_chnage>1):

   
    if(bmi<17):
        intermediate_helath_score=intermediate_helath_score+5
    elif(bmi<18.5):
        intermediate_helath_score=intermediate_helath_score+2
    elif(bmi>30):
        intermediate_helath_score=intermediate_helath_score-5
    elif(bmi>25):
        intermediate_helath_score=intermediate_helath_score-3

elif(weight_chnage<1):
    if(bmi<17):
        intermediate_helath_score=intermediate_helath_score-5
    elif(bmi<18.5):
        intermediate_helath_score=intermediate_helath_score-3
    elif(bmi>30):
        intermediate_helath_score=intermediate_helath_score+5
    elif(bmi>25):
        intermediate_helath_score=intermediate_helath_score+2


final=intermediate_helath_score+overall_assesment

if(final==5):
    print("good")
elif(final>3 and final<5):
    print("Need a little work")
elif(final>1 and final<3):
    print("Need a lot work")
elif(final<1):
    print("At Risk")