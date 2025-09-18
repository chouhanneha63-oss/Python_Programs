Max_marks= int(input("Enter the maximum marks of a subject:"))

if(Max_marks <= 0 or Max_marks > 100):
    print("Invalid Maximum Marks!!!")
else:
    Total_max_marks = (Max_marks)*5

    Physics = int(input("Enter the marks scored in Physics:"))
    Chemistry = int(input("Enter the marks scored in Chemistry:"))
    Maths = int(input("Enter the marks scored in Maths:"))
    Hindi = int(input("Enter the marks scored in Hindi:"))
    English = int(input("Enter the marks scored in English:"))
    if(Physics < 0 or Physics > Max_marks) or (Chemistry < 0 or Chemistry > Max_marks) or (Maths < 0 or Maths > Max_marks) or (Hindi < 0 or Hindi > Max_marks) or (English < 0 or English > Max_marks):
        print("You have enetered invalid marks in:")
        if(Physics < 0 or Physics > Max_marks):
           print("Physics:",Physics)
        if(Chemistry < 0 or Chemistry > Max_marks):
           print("Chemistry:",Chemistry)
        if(Maths < 0 or Maths > Max_marks):
           print("Maths:",Maths)
        if(Hindi < 0 or Hindi > Max_marks):
           print("Hindi:",Hindi)
        if(English < 0 or English > Max_marks):
           print("English:",English)
        

    elif(Physics >= 36 and Chemistry >= 36 and Maths >= 36 and Hindi >= 36 and English >= 36):
        Total_scored_marks = Physics + Chemistry + Maths + Hindi + English
        Percentage = (Total_scored_marks*100)/Total_max_marks

        if(Percentage >= 90 and Percentage < 100):
            print("You have passed the exam with a grade of A+.")

        elif(Percentage >=80 and Percentage < 90):
            print("You have passed the exam with a grade of A.")

        elif(Percentage >=70 and Percentage < 80):
            print("You have passed the exam with a grade of B+.")

        elif(Percentage >=60 and Percentage < 70):
            print("You have passed the exam with a grade of B.")

        elif(Percentage >=50 and Percentage < 60):
            print("You have passed the exam with a grade of C+.")

        elif(Percentage >=40 and Percentage < 50):
            print("You have passed the exam with a grade of C.")

        elif(Percentage >=36 and Pecentage < 40):
            print("You have passed the exam with a grade of D.")

    elif(Physics <36 and Chemistry < 36 and Maths < 36 and Hindi < 36 and English < 36 ):
        print("You are failed in all the five subjects")
        print("Physics:",Physics)
        print("Chemistry:",Chemistry)
        print("Maths:",Maths)
        print("Hindi:",Hindi)
        print("English:",English)
        
    elif(Physics < 36 and Chemistry < 36 and Maths < 36 and Hindi < 36):
        print("You are failed in four subjects")
        print("Physics:",Physics)
        print("Chemistry:",Chemistry)
        print("Maths:",Maths)
        print("Hindi:",Hindi)

    elif(Physics < 36 and Chemistry < 36 and Maths < 36 and English < 36):
        print("You are failed in four subjects")
        print("Physics:",Physics)
        print("Chemistry:",Chemistry)
        print("Maths:",Maths)
        print("English:",English)

    elif(Physics < 36 and Chemistry < 36 and Hindi < 36 and English < 36):
        print("You are failed in four subjects")
        print("Physics:",Physics)
        print("Chemistry:",Chemistry)
        print("Hindi:",Hindi)
        print("English:",English)

    elif(Physics < 36 and Maths < 36 and Hindi < 36 and English < 36):
        print("You are failed in four subjects")
        print("Physics:",Physics)
        print("Maths:",Maths)
        print("Hindi:",Hindi)
        print("English:",English)

    elif(Chemistry < 36 and Maths < 36 and Hindi < 36 and English < 36):
        print("You are failed in four subjects")
        print("Chemistry:",Chemistry)
        print("Maths:",Maths)
        print("Hindi:",Hindi)
        print("English:",English)

    elif(Physics < 36 and Chemistry < 36 and Maths < 36):
        print("You are failed in three subjects")
        print("Physics:", Physics)
        print("Chemistry:",Chemistry)
        print("Maths:",Maths)

        Physics = int(input("Enter the marks scored in Physics after the reattempt:"))
        Chemistry = int(input("Enter the marks scored in Chemistry after the reattempt:"))
        Maths = int(input("Enter the marks scored in Maths after the reattempt:"))

        if(Physics >= 36 and Chemistry >= 36 and Maths >= 36 and Hindi >= 36 and English >= 36):
            Total_scored_marks = Physics + Chemistry + Maths + Hindi + English

            Percentage = (Total_scored_marks*100)/Total_max_marks

            if(Percentage >= 90 and Percentage < 100):
                print("You have passed the exam with a grade of A+.")

            elif(Percentage >=80 and Percentage < 90):
                print("You have passed the exam with a grade of A.")

            elif(Percentage >=70 and Percentage < 80):
                print("You have passed the exam with a grade of B+.")

            elif(Percentage >=60 and Percentage < 70):
                print("You have passed the exam with a grade of B.")

            elif(Percentage >=50 and Percentage < 60):
                print("You have passed the exam with a grade of C+.")

            elif(Percentage >=40 and Percentage < 50):
                print("You have passed the exam with a grade of C.")

            elif(Percentage >=36 and Pecentage < 40):
                print("You have passed the exam with a grade of D.")

        
    elif(Physics < 36 and Chemistry < 36 and Hindi < 36):
        print("You are failed in three subjects")
        print("Physics:", Physics)
        print("Chemistry:",Chemistry)
        print("Hindi:",Hindi)

        Physics = int(input("Enter the marks scored in Physics after the reattempt:"))
        Chemistry = int(input("Enter the marks scored in Chemistry after the reattempt:"))
        Hindi = int(input("Enter the marks scored in Hindi after the reattempt:"))

        if(Physics >= 36 and Chemistry >= 36 and Maths >= 36 and Hindi >= 36 and English >= 36):
            Total_scored_marks = Physics + Chemistry + Maths + Hindi + English

            Percentage = (Total_scored_marks*100)/Total_max_marks

            if(Percentage >= 90 and Percentage < 100):
                print("You have passed the exam with a grade of A+.")

            elif(Percentage >=80 and Percentage < 90):
                print("You have passed the exam with a grade of A.")

            elif(Percentage >=70 and Percentage < 80):
                print("You have passed the exam with a grade of B+.")

            elif(Percentage >=60 and Percentage < 70):
                print("You have passed the exam with a grade of B.")

            elif(Percentage >=50 and Percentage < 60):
                print("You have passed the exam with a grade of C+.")

            elif(Percentage >=40 and Percentage < 50):
                print("You have passed the exam with a grade of C.")

            elif(Percentage >=36 and Pecentage < 40):
                print("You have passed the exam with a grade of D.")


    elif(Physics < 36 and Chemistry < 36 and English < 36):
        print("You are failed in three subjects")
        print("Physics:", Physics)
        print("Chemistry:",Chemistry)
        print("English:",English)

        Physics = int(input("Enter the marks scored in Physics after the reattempt:"))
        Chemistry = int(input("Enter the marks scored in Chemistry after the reattempt:"))
        English = int(input("Enter the marks scored in English after the reattempt:"))

        if(Physics >= 36 and Chemistry >= 36 and Maths >= 36 and Hindi >= 36 and English >= 36):
            Total_scored_marks = Physics + Chemistry + Maths + Hindi + English

            Percentage = (Total_scored_marks*100)/Total_max_marks

            if(Percentage >= 90 and Percentage < 100):
                print("You have passed the exam with a grade of A+.")

            elif(Percentage >=80 and Percentage < 90):
                print("You have passed the exam with a grade of A.")

            elif(Percentage >=70 and Percentage < 80):
                print("You have passed the exam with a grade of B+.")

            elif(Percentage >=60 and Percentage < 70):
                print("You have passed the exam with a grade of B.")

            elif(Percentage >=50 and Percentage < 60):
                print("You have passed the exam with a grade of C+.")

            elif(Percentage >=40 and Percentage < 50):
                print("You have passed the exam with a grade of C.")

            elif(Percentage >=36 and Pecentage < 40):
                print("You have passed the exam with a grade of D.")

    

    elif(Physics < 36 and Maths < 36 and Hindi):
        print("You are failed in three subjects")
        print("Physics:", Physics)
        print("Maths:",Maths)
        print("Hindi", Hindi)

        Physics = int(input("Enter the marks scored in Physics after the reattempt:"))
        Maths = int(input("Enter the marks scored in Maths after the reattempt:"))
        Hindi = int(input("Enter the marks scored in Hindi after the reattempt:"))

        if(Physics >= 36 and Chemistry >= 36 and Maths >= 36 and Hindi >= 36 and English >= 36):
            Total_scored_marks = Physics + Chemistry + Maths + Hindi + English

            Percentage = (Total_scored_marks*100)/Total_max_marks

            if(Percentage >= 90 and Percentage < 100):
                print("You have passed the exam with a grade of A+.")

            elif(Percentage >=80 and Percentage < 90):
                print("You have passed the exam with a grade of A.")

            elif(Percentage >=70 and Percentage < 80):
                print("You have passed the exam with a grade of B+.")

            elif(Percentage >=60 and Percentage < 70):
                print("You have passed the exam with a grade of B.")

            elif(Percentage >=50 and Percentage < 60):
                print("You have passed the exam with a grade of C+.")

            elif(Percentage >=40 and Percentage < 50):
                print("You have passed the exam with a grade of C.")

            elif(Percentage >=36 and Pecentage < 40):
                print("You have passed the exam with a grade of D.")

    

    elif(Physics < 36 and Maths < 36 and English):
        print("You are failed in three subjects")
        print("Physics:", Physics)
        print("Maths:",Maths)
        print("English", English)

        Physics = int(input("Enter the marks scored in Physics after the reattempt:"))
        Maths = int(input("Enter the marks scored in Maths after the reattempt:"))
        English = int(input("Enter the marks scored in English after the reattempt:"))

        if(Physics >= 36 and Chemistry >= 36 and Maths >= 36 and Hindi >= 36 and English >= 36):
            Total_scored_marks = Physics + Chemistry + Maths + Hindi + English

            Percentage = (Total_scored_marks*100)/Total_max_marks

            if(Percentage >= 90 and Percentage < 100):
                print("You have passed the exam with a grade of A+.")

            elif(Percentage >=80 and Percentage < 90):
                print("You have passed the exam with a grade of A.")

            elif(Percentage >=70 and Percentage < 80):
                print("You have passed the exam with a grade of B+.")

            elif(Percentage >=60 and Percentage < 70):
                print("You have passed the exam with a grade of B.")

            elif(Percentage >=50 and Percentage < 60):
                print("You have passed the exam with a grade of C+.")

            elif(Percentage >=40 and Percentage < 50):
                print("You have passed the exam with a grade of C.")

            elif(Percentage >=36 and Pecentage < 40):
                print("You have passed the exam with a grade of D.")

    

    elif(Physics < 36 and Hindi < 36 and English < 36):
        print("You are failed in three subjects")
        print("Physics:", Physics)
        print("Hindi", Hindi)
        print("English", English)

        Physics = int(input("Enter the marks scored in Physics after the reattempt:"))
        Hindi = int(input("Enter the marks scored in Hindi after the reattempt:"))
        English = int(input("Enter the marks scored in English after the reattempt:"))

        if(Physics >= 36 and Chemistry >= 36 and Maths >= 36 and Hindi >= 36 and English >= 36):
            Total_scored_marks = Physics + Chemistry + Maths + Hindi + English

            Percentage = (Total_scored_marks*100)/Total_max_marks

            if(Percentage >= 90 and Percentage < 100):
                print("You have passed the exam with a grade of A+.")

            elif(Percentage >=80 and Percentage < 90):
                print("You have passed the exam with a grade of A.")

            elif(Percentage >=70 and Percentage < 80):
                print("You have passed the exam with a grade of B+.")

            elif(Percentage >=60 and Percentage < 70):
                print("You have passed the exam with a grade of B.")

            elif(Percentage >=50 and Percentage < 60):
                print("You have passed the exam with a grade of C+.")

            elif(Percentage >=40 and Percentage < 50):
                print("You have passed the exam with a grade of C.")

            elif(Percentage >=36 and Pecentage < 40):
                print("You have passed the exam with a grade of D.")

    

    elif(Chemistry < 36 and Maths < 36 and Hindi < 36):
        print("You are failed in three subjects")
        print("Chemistry:",Chemistry)
        print("Maths:",Maths)
        print("Hindi:",Hindi)

        
        Chemistry = int(input("Enter the marks scored in Chemistry after the reattempt:"))
        Maths = int(input("Enter the marks scored in Maths after the reattempt:"))
        Hindi = int(input("Enter the marks scored in Hindi after the reattempt:"))

        if(Physics >= 36 and Chemistry >= 36 and Maths >= 36 and Hindi >= 36 and English >= 36):
            Total_scored_marks = Physics + Chemistry + Maths + Hindi + English

            Percentage = (Total_scored_marks*100)/Total_max_marks

            if(Percentage >= 90 and Percentage < 100):
                print("You have passed the exam with a grade of A+.")

            elif(Percentage >=80 and Percentage < 90):
                print("You have passed the exam with a grade of A.")

            elif(Percentage >=70 and Percentage < 80):
                print("You have passed the exam with a grade of B+.")

            elif(Percentage >=60 and Percentage < 70):
                print("You have passed the exam with a grade of B.")

            elif(Percentage >=50 and Percentage < 60):
                print("You have passed the exam with a grade of C+.")

            elif(Percentage >=40 and Percentage < 50):
                print("You have passed the exam with a grade of C.")

            elif(Percentage >=36 and Pecentage < 40):
                print("You have passed the exam with a grade of D.")

        
    
    elif(Chemistry < 36 and Maths < 36 and English < 36):
        print("You are failed in three subjects")
        print("Chemistry:",Chemistry)
        print("Maths:",Maths)
        print("English:",English)

    
        Chemistry = int(input("Enter the marks scored in Chemistry after the reattempt:"))
        Maths = int(input("Enter the marks scored in Maths after the reattempt:"))
        English = int(input("Enter the marks scored in English after the reattempt:"))

        if(Physics >= 36 and Chemistry >= 36 and Maths >= 36 and Hindi >= 36 and English >= 36):
            Total_scored_marks = Physics + Chemistry + Maths + Hindi + English

            Percentage = (Total_scored_marks*100)/Total_max_marks

            if(Percentage >= 90 and Percentage < 100):
                print("You have passed the exam with a grade of A+.")

            elif(Percentage >=80 and Percentage < 90):
                print("You have passed the exam with a grade of A.")

            elif(Percentage >=70 and Percentage < 80):
                print("You have passed the exam with a grade of B+.")

            elif(Percentage >=60 and Percentage < 70):
                print("You have passed the exam with a grade of B.")

            elif(Percentage >=50 and Percentage < 60):
                print("You have passed the exam with a grade of C+.")

            elif(Percentage >=40 and Percentage < 50):
                print("You have passed the exam with a grade of C.")

            elif(Percentage >=36 and Pecentage < 40):
                print("You have passed the exam with a grade of D.")

    
    elif(Chemistry < 36 and Hindi < 36 and English < 36):
        print("You are failed in three subjects")
        print("Chemistry:",Chemistry)
        print("Hindi:",Hindi)
        print("English:",English)

        
        Chemistry = int(input("Enter the marks scored in Chemistry after the reattempt:"))
        Hindi = int(input("Enter the marks scored in Hindi after the reattempt:"))
        English = int(input("Enter the marks scored in English after the reattempt:"))

        if(Physics >= 36 and Chemistry >= 36 and Maths >= 36 and Hindi >= 36 and English >= 36):
            Total_scored_marks = Physics + Chemistry + Maths + Hindi + English

            Percentage = (Total_scored_marks*100)/Total_max_marks

            if(Percentage >= 90 and Percentage < 100):
                print("You have passed the exam with a grade of A+.")

            elif(Percentage >=80 and Percentage < 90):
                print("You have passed the exam with a grade of A.")

            elif(Percentage >=70 and Percentage < 80):
                print("You have passed the exam with a grade of B+.")

            elif(Percentage >=60 and Percentage < 70):
                print("You have passed the exam with a grade of B.")

            elif(Percentage >=50 and Percentage < 60):
                print("You have passed the exam with a grade of C+.")

            elif(Percentage >=40 and Percentage < 50):
                print("You have passed the exam with a grade of C.")

            elif(Percentage >=36 and Pecentage < 40):
                print("You have passed the exam with a grade of D.")

    

    elif(Maths < 36 and Hindi < 36 and English < 36):
        print("You are failed in three subjects")
        print("Maths:",Maths)
        print("Hindi:",Hindi)
        print("English:",English)

        
        Maths = int(input("Enter the marks scored in Maths after the reattempt:"))
        Hindi = int(input("Enter the marks scored in Hindi after the reattempt:"))
        English = int(input("Enter the marks scored in English after the reattempt:"))

        if(Physics >= 36 and Chemistry >= 36 and Maths >= 36 and Hindi >= 36 and English >= 36):
            Total_scored_marks = Physics + Chemistry + Maths + Hindi + English

            Percentage = (Total_scored_marks*100)/Total_max_marks

            if(Percentage >= 90 and Percentage < 100):
                print("You have passed the exam with a grade of A+.")

            elif(Percentage >=80 and Percentage < 90):
                print("You have passed the exam with a grade of A.")

            elif(Percentage >=70 and Percentage < 80):
                print("You have passed the exam with a grade of B+.")

            elif(Percentage >=60 and Percentage < 70):
                print("You have passed the exam with a grade of B.")

            elif(Percentage >=50 and Percentage < 60):
                print("You have passed the exam with a grade of C+.")

            elif(Percentage >=40 and Percentage < 50):
                print("You have passed the exam with a grade of C.")

            elif(Percentage >=36 and Pecentage < 40):
                print("You have passed the exam with a grade of D.")



    elif(Physics < 36 and Chemistry < 36):
        print("You are failed in two subjects")
        print("Physics:", Physics)
        print("Chemistry:",Chemistry)

        Physics = int(input("Enter the marks scored in Physics after the reattempt:"))
        Chemistry = int(input("Enter the marks scored in Chemistry after the reattempt:"))

        if(Physics >= 36 and Chemistry >= 36 and Maths >= 36 and Hindi >= 36 and English >= 36):
            Total_scored_marks = Physics + Chemistry + Maths + Hindi + English

            Percentage = (Total_scored_marks*100)/Total_max_marks

            if(Percentage >= 90 and Percentage < 100):
                print("You have passed the exam with a grade of A+.")

            elif(Percentage >=80 and Percentage < 90):
                print("You have passed the exam with a grade of A.")

            elif(Percentage >=70 and Percentage < 80):
                print("You have passed the exam with a grade of B+.")

            elif(Percentage >=60 and Percentage < 70):
                print("You have passed the exam with a grade of B.")

            elif(Percentage >=50 and Percentage < 60):
                print("You have passed the exam with a grade of C+.")

            elif(Percentage >=40 and Percentage < 50):
                print("You have passed the exam with a grade of C.")

            elif(Percentage >=36 and Pecentage < 40):
                print("You have passed the exam with a grade of D.")

        
    
    elif(Physics < 36 and Maths < 36):
        print("You are failed in two subjects")
        print("Physics:", Physics)
        print("Maths:",Maths)

        Physics = int(input("Enter the marks scored in Physics after the reattempt:"))
        Maths = int(input("Enter the marks scored in Maths after the reattempt:"))

        if(Physics >= 36 and Chemistry >= 36 and Maths >= 36 and Hindi >= 36 and English >= 36):
            Total_scored_marks = Physics + Chemistry + Maths + Hindi + English

            Percentage = (Total_scored_marks*100)/Total_max_marks

            if(Percentage >= 90 and Percentage < 100):
                print("You have passed the exam with a grade of A+.")

            elif(Percentage >=80 and Percentage < 90):
                print("You have passed the exam with a grade of A.")

            elif(Percentage >=70 and Percentage < 80):
                print("You have passed the exam with a grade of B+.")

            elif(Percentage >=60 and Percentage < 70):
                print("You have passed the exam with a grade of B.")

            elif(Percentage >=50 and Percentage < 60):
                print("You have passed the exam with a grade of C+.")

            elif(Percentage >=40 and Percentage < 50):
                print("You have passed the exam with a grade of C.")

            elif(Percentage >=36 and Pecentage < 40):
                print("You have passed the exam with a grade of D.")

            

    elif(Physics < 36 and Hindi < 36):
        print("You are failed in two subjects")
        print("Physics:", Physics)
        print("Hindi:",Hindi)

        Physics = int(input("Enter the marks scored in Physics after the reattempt:"))
        Hindi = int(input("Enter the marks scored in Hindi after the reattempt:"))

        if(Physics >= 36 and Chemistry >= 36 and Maths >= 36 and Hindi >= 36 and English >= 36):
            Total_scored_marks = Physics + Chemistry + Maths + Hindi + English

            Percentage = (Total_scored_marks*100)/Total_max_marks

            if(Percentage >= 90 and Percentage < 100):
                print("You have passed the exam with a grade of A+.")

            elif(Percentage >=80 and Percentage < 90):
                print("You have passed the exam with a grade of A.")

            elif(Percentage >=70 and Percentage < 80):
                print("You have passed the exam with a grade of B+.")

            elif(Percentage >=60 and Percentage < 70):
                print("You have passed the exam with a grade of B.")

            elif(Percentage >=50 and Percentage < 60):
                print("You have passed the exam with a grade of C+.")

            elif(Percentage >=40 and Percentage < 50):
                print("You have passed the exam with a grade of C.")

            elif(Percentage >=36 and Pecentage < 40):
                print("You have passed the exam with a grade of D.")

    

    elif(Physics < 36 and English < 36):
        print("You are failed in two subjects")
        print("Physics:", Physics)
        print("English:",English)

        Physics = int(input("Enter the marks scored in Physics after the reattempt:"))
        English = int(input("Enter the marks scored in English after the reattempt:"))

        if(Physics >= 36 and Chemistry >= 36 and Maths >= 36 and Hindi >= 36 and English >= 36):
            Total_scored_marks = Physics + Chemistry + Maths + Hindi + English

            Percentage = (Total_scored_marks*100)/Total_max_marks

            if(Percentage >= 90 and Percentage < 100):
                print("You have passed the exam with a grade of A+.")

            elif(Percentage >=80 and Percentage < 90):
                print("You have passed the exam with a grade of A.")

            elif(Percentage >=70 and Percentage < 80):
                print("You have passed the exam with a grade of B+.")

            elif(Percentage >=60 and Percentage < 70):
                print("You have passed the exam with a grade of B.")

            elif(Percentage >=50 and Percentage < 60):
                print("You have passed the exam with a grade of C+.")

            elif(Percentage >=40 and Percentage < 50):
                print("You have passed the exam with a grade of C.")

            elif(Percentage >=36 and Pecentage < 40):
                print("You have passed the exam with a grade of D.")

    

    elif(Chemistry < 36 and Maths < 36):
        print("You are failed in two subjects")
        print("Chemistry:",Chemistry)
        print("Maths", Maths)

        Chemistry = int(input("Enter the marks scored in Chemistry after the reattempt:"))
        Maths = int(input("Enter the marks scored in Maths after the reattempt:"))

        if(Physics >= 36 and Chemistry >= 36 and Maths >= 36 and Hindi >= 36 and English >= 36):
            Total_scored_marks = Physics + Chemistry + Maths + Hindi + English

            Percentage = (Total_scored_marks*100)/Total_max_marks

            if(Percentage >= 90 and Percentage < 100):
                print("You have passed the exam with a grade of A+.")

            elif(Percentage >=80 and Percentage < 90):
                print("You have passed the exam with a grade of A.")

            elif(Percentage >=70 and Percentage < 80):
                print("You have passed the exam with a grade of B+.")

            elif(Percentage >=60 and Percentage < 70):
                print("You have passed the exam with a grade of B.")

            elif(Percentage >=50 and Percentage < 60):
                print("You have passed the exam with a grade of C+.")

            elif(Percentage >=40 and Percentage < 50):
                print("You have passed the exam with a grade of C.")

            elif(Percentage >=36 and Pecentage < 40):
                print("You have passed the exam with a grade of D.")

    

    elif(Chemistry < 36 and Hindi < 36):
        print("You are failed in two subjects")
        print("Chemistry:",Chemistry)
        print("Hindi:", Hindi)

        Chemistry = int(input("Enter the marks scored in Chemistry after the reattempt:"))
        Hindi = int(input("Enter the marks scored in Hindi after the reattempt:"))

        if(Physics >= 36 and Chemistry >= 36 and Maths >= 36 and Hindi >= 36 and English >= 36):
            Total_scored_marks = Physics + Chemistry + Maths + Hindi + English

            Percentage = (Total_scored_marks*100)/Total_max_marks

            if(Percentage >= 90 and Percentage < 100):
                print("You have passed the exam with a grade of A+.")

            elif(Percentage >=80 and Percentage < 90):
                print("You have passed the exam with a grade of A.")

            elif(Percentage >=70 and Percentage < 80):
                print("You have passed the exam with a grade of B+.")

            elif(Percentage >=60 and Percentage < 70):
                print("You have passed the exam with a grade of B.")

            elif(Percentage >=50 and Percentage < 60):
                print("You have passed the exam with a grade of C+.")

            elif(Percentage >=40 and Percentage < 50):
                print("You have passed the exam with a grade of C.")

            elif(Percentage >=36 and Pecentage < 40):
                print("You have passed the exam with a grade of D.")

    

    elif(Chemistry < 36 and English < 36):
        print("You are failed in two subjects")
        print("Chemistry:",Chemistry)
        print("English:", English)

        Chemistry = int(input("Enter the marks scored in Chemistry after the reattempt:"))
        English = int(input("Enter the marks scored in English after the reattempt:"))

        if(Physics >= 36 and Chemistry >= 36 and Maths >= 36 and Hindi >= 36 and English >= 36):
            Total_scored_marks = Physics + Chemistry + Maths + Hindi + English

            Percentage = (Total_scored_marks*100)/Total_max_marks

            if(Percentage >= 90 and Percentage < 100):
                print("You have passed the exam with a grade of A+.")

            elif(Percentage >=80 and Percentage < 90):
                print("You have passed the exam with a grade of A.")

            elif(Percentage >=70 and Percentage < 80):
                print("You have passed the exam with a grade of B+.")

            elif(Percentage >=60 and Percentage < 70):
                print("You have passed the exam with a grade of B.")

            elif(Percentage >=50 and Percentage < 60):
                print("You have passed the exam with a grade of C+.")

            elif(Percentage >=40 and Percentage < 50):
                print("You have passed the exam with a grade of C.")

            elif(Percentage >=36 and Pecentage < 40):
                print("You have passed the exam with a grade of D.")

        
    elif(Maths < 36 and Hindi < 36):
        print("You are failed in two subjects")
        print("Maths:", Maths)
        print("Hindi:", Hindi)

        Maths = int(input("Enter the marks scored in Maths after the reattempt:"))
        Hindi = int(input("Enter the marks scored in Hindi after the reattempt:"))

        if(Physics >= 36 and Chemistry >= 36 and Maths >= 36 and Hindi >= 36 and English >= 36):
            Total_scored_marks = Physics + Chemistry + Maths + Hindi + English

            Percentage = (Total_scored_marks*100)/Total_max_marks

            if(Percentage >= 90 and Percentage < 100):
                print("You have passed the exam with a grade of A+.")

            elif(Percentage >=80 and Percentage < 90):
                print("You have passed the exam with a grade of A.")

            elif(Percentage >=70 and Percentage < 80):
                print("You have passed the exam with a grade of B+.")

            elif(Percentage >=60 and Percentage < 70):
                print("You have passed the exam with a grade of B.")

            elif(Percentage >=50 and Percentage < 60):
                print("You have passed the exam with a grade of C+.")
    
            elif(Percentage >=40 and Percentage < 50):
                print("You have passed the exam with a grade of C.")

            elif(Percentage >=36 and Pecentage < 40):
                print("You have passed the exam with a grade of D.")

    

    elif(Maths < 36 and English < 36):
        print("You are failed in two subjects")
        print("Maths:", Maths)
        print("Hindi:", English)

        Maths = int(input("Enter the marks scored in Maths after the reattempt:"))
        English = int(input("Enter the marks scored in English after the reattempt:"))

        if(Physics >= 36 and Chemistry >= 36 and Maths >= 36 and Hindi >= 36 and English >= 36):
            Total_scored_marks = Physics + Chemistry + Maths + Hindi + English

            Percentage = (Total_scored_marks*100)/Total_max_marks

            if(Percentage >= 90 and Percentage < 100):
                print("You have passed the exam with a grade of A+.")

            elif(Percentage >=80 and Percentage < 90):
                print("You have passed the exam with a grade of A.")

            elif(Percentage >=70 and Percentage < 80):
                print("You have passed the exam with a grade of B+.")

            elif(Percentage >=60 and Percentage < 70):
                print("You have passed the exam with a grade of B.")

            elif(Percentage >=50 and Percentage < 60):
                print("You have passed the exam with a grade of C+.")

            elif(Percentage >=40 and Percentage < 50):
                print("You have passed the exam with a grade of C.")

            elif(Percentage >=36 and Pecentage < 40):
                print("You have passed the exam with a grade of D.")

    

    elif(Hindi < 36 and English < 36):
        print("You are failed in two subjects")
        print("Hindi:", Hindi)
        print("English:", English)

        Hindi = int(input("Enter the marks scored in Hindi after the reattempt:"))
        English = int(input("Enter the marks scored in English after the reattempt:"))

        if(Physics >= 36 and Chemistry >= 36 and Maths >= 36 and Hindi >= 36 and English >= 36):
            Total_scored_marks = Physics + Chemistry + Maths + Hindi + English

            Percentage = (Total_scored_marks*100)/Total_max_marks

            if(Percentage >= 90 and Percentage < 100):
                print("You have passed the exam with a grade of A+.")

            elif(Percentage >=80 and Percentage < 90):
                print("You have passed the exam with a grade of A.")

            elif(Percentage >=70 and Percentage < 80):
                print("You have passed the exam with a grade of B+.")

            elif(Percentage >=60 and Percentage < 70):
                print("You have passed the exam with a grade of B.")

            elif(Percentage >=50 and Percentage < 60):
                print("You have passed the exam with a grade of C+.")

            elif(Percentage >=40 and Percentage < 50):
                print("You have passed the exam with a grade of C.")

            elif(Percentage >=36 and Pecentage < 40):
                print("You have passed the exam with a grade of D.")

    

    elif(Physics < 36):
        print("You are failed in one subject:")
        print("Physics:",Physics)

        if(Physics >= 30 and Physics <= 35):
            grace= 36-Physics
            Physics=Physics+(36-Physics)
            print("Grace marks",grace,"added.")
            print("Physics:",Physics)

            if(Physics >= 36 and Chemistry >= 36 and Maths >= 36 and Hindi >= 36 and English >= 36):
                Total_scored_marks = Physics + Chemistry + Maths + Hindi + English

                Percentage = (Total_scored_marks*100)/Total_max_marks

                if(Percentage >= 90 and Percentage < 100):
                    print("You have passed the exam with a grade of A+.")

                elif(Percentage >=80 and Percentage < 90):
                    print("You have passed the exam with a grade of A.")

                elif(Percentage >=70 and Percentage < 80):
                    print("You have passed the exam with a grade of B+.")

                elif(Percentage >=60 and Percentage < 70):
                    print("You have passed the exam with a grade of B.")

                elif(Percentage >=50 and Percentage < 60):
                    print("You have passed the exam with a grade of C+.")

                elif(Percentage >=40 and Percentage < 50):
                    print("You have passed the exam with a grade of C.")

                elif(Percentage >=36 and Pecentage < 40):
                    print("You have passed the exam with a grade of D.")


        else:
            Physics = int(input("Enter the marks scored in Physics after the reattempt:"))

            if(Physics >= 36 and Chemistry >= 36 and Maths >= 36 and Hindi >= 36 and English >= 36):
                Total_scored_marks = Physics + Chemistry + Maths + Hindi + English

                Percentage = (Total_scored_marks*100)/Total_max_marks

                if(Percentage >= 90 and Percentage < 100):
                    print("You have passed the exam with a grade of A+.")

                elif(Percentage >=80 and Percentage < 90):
                    print("You have passed the exam with a grade of A.")

                elif(Percentage >=70 and Percentage < 80):
                    print("You have passed the exam with a grade of B+.")

                elif(Percentage >=60 and Percentage < 70):
                    print("You have passed the exam with a grade of B.")

                elif(Percentage >=50 and Percentage < 60):
                    print("You have passed the exam with a grade of C+.")

                elif(Percentage >=40 and Percentage < 50):
                    print("You have passed the exam with a grade of C.")

                elif(Percentage >=36 and Pecentage < 40):
                    print("You have passed the exam with a grade of D.")


            
    elif(Chemistry < 36):
        print("You are failed in one subject:")
        print("Chemistry:",Chemistry)

        if(Chemistry >= 30 and Chemistry <= 35):
            grace= 36-Chemistry
            Chemistry=Chemistry+grace
            print("Grace marks",grace,"added.")
            print("Chemistry:",Chemistry)

            if(Physics >= 36 and Chemistry >= 36 and Maths >= 36 and Hindi >= 36 and English >= 36):
                Total_scored_marks = Physics + Chemistry + Maths + Hindi + English

                Percentage = (Total_scored_marks*100)/Total_max_marks

                if(Percentage >= 90 and Percentage < 100):
                    print("You have passed the exam with a grade of A+.")

                elif(Percentage >=80 and Percentage < 90):
                    print("You have passed the exam with a grade of A.")

                elif(Percentage >=70 and Percentage < 80):
                    print("You have passed the exam with a grade of B+.")

                elif(Percentage >=60 and Percentage < 70):
                    print("You have passed the exam with a grade of B.")

                elif(Percentage >=50 and Percentage < 60):
                    print("You have passed the exam with a grade of C+.")

                elif(Percentage >=40 and Percentage < 50):
                    print("You have passed the exam with a grade of C.")

                elif(Percentage >=36 and Pecentage < 40):
                    print("You have passed the exam with a grade of D.")

        else:
            Chemistry = int(input("Enter the marks scored in Chemistry after the reattempt:"))

            if(Physics >= 36 and Chemistry >= 36 and Maths >= 36 and Hindi >= 36 and English >= 36):
                Total_scored_marks = Physics + Chemistry + Maths + Hindi + English

                Percentage = (Total_scored_marks*100)/Total_max_marks

                if(Percentage >= 90 and Percentage < 100):
                    print("You have passed the exam with a grade of A+.")

                elif(Percentage >=80 and Percentage < 90):
                    print("You have passed the exam with a grade of A.")

                elif(Percentage >=70 and Percentage < 80):
                    print("You have passed the exam with a grade of B+.")

                elif(Percentage >=60 and Percentage < 70):
                    print("You have passed the exam with a grade of B.")

                elif(Percentage >=50 and Percentage < 60):
                    print("You have passed the exam with a grade of C+.")

                elif(Percentage >=40 and Percentage < 50):
                    print("You have passed the exam with a grade of C.")

                elif(Percentage >=36 and Pecentage < 40):
                    print("You have passed the exam with a grade of D.")

        
    elif(Maths < 36):
            print("You are failed in one subject:")
            print("Maths:",Maths)

            if(Maths >= 30 and Maths <= 35):
                grace= 36-Maths
                Maths=Maths+grace
                print("Grace marks",grace,"added.")
                print("Maths:",Maths)

                if(Physics >= 36 and Chemistry >= 36 and Maths >= 36 and Hindi >= 36 and English >= 36):
                    Total_scored_marks = Physics + Chemistry + Maths + Hindi + English

                    Percentage = (Total_scored_marks*100)/Total_max_marks

                    if(Percentage >= 90 and Percentage < 100):
                        print("You have passed the exam with a grade of A+.")

                    elif(Percentage >=80 and Percentage < 90):
                        print("You have passed the exam with a grade of A.")

                    elif(Percentage >=70 and Percentage < 80):
                        print("You have passed the exam with a grade of B+.")

                    elif(Percentage >=60 and Percentage < 70):
                        print("You have passed the exam with a grade of B.")

                    elif(Percentage >=50 and Percentage < 60):
                        print("You have passed the exam with a grade of C+.")

                    elif(Percentage >=40 and Percentage < 50):
                        print("You have passed the exam with a grade of C.")

                    elif(Percentage >=36 and Pecentage < 40):
                        print("You have passed the exam with a grade of D.")

            else:
                Maths = int(input("Enter the marks scored in Maths after the reattempt:"))
                if(Physics >= 36 and Chemistry >= 36 and Maths >= 36 and Hindi >= 36 and English >= 36):
                    Total_scored_marks = Physics + Chemistry + Maths + Hindi + English

                    Percentage = (Total_scored_marks*100)/Total_max_marks

                    if(Percentage >= 90 and Percentage < 100):
                        print("You have passed the exam with a grade of A+.")

                    elif(Percentage >=80 and Percentage < 90):
                        print("You have passed the exam with a grade of A.")

                    elif(Percentage >=70 and Percentage < 80):
                        print("You have passed the exam with a grade of B+.")

                    elif(Percentage >=60 and Percentage < 70):
                        print("You have passed the exam with a grade of B.")

                    elif(Percentage >=50 and Percentage < 60):
                        print("You have passed the exam with a grade of C+.")

                    elif(Percentage >=40 and Percentage < 50):
                        print("You have passed the exam with a grade of C.")

                    elif(Percentage >=36 and Pecentage < 40):
                        print("You have passed the exam with a grade of D.")

        
    elif(Hindi < 36):
        print("You are failed in one subject:")
        print("Hindi:",Hindi)

        if(Hindi >= 30 and Hindi <= 35):
            grace= 36-Hindi
            Hindi=Hindi+grace
            print("Grace marks",grace,"added.")
            print("Hindi:",Hindi)

            if(Physics >= 36 and Chemistry >= 36 and Maths >= 36 and Hindi >= 36 and English >= 36):
                Total_scored_marks = Physics + Chemistry + Maths + Hindi + English

                Percentage = (Total_scored_marks*100)/Total_max_marks

                if(Percentage >= 90 and Percentage < 100):
                    print("You have passed the exam with a grade of A+.")

                elif(Percentage >=80 and Percentage < 90):
                    print("You have passed the exam with a grade of A.")

                elif(Percentage >=70 and Percentage < 80):
                    print("You have passed the exam with a grade of B+.")

                elif(Percentage >=60 and Percentage < 70):
                    print("You have passed the exam with a grade of B.")

                elif(Percentage >=50 and Percentage < 60):
                    print("You have passed the exam with a grade of C+.")

                elif(Percentage >=40 and Percentage < 50):
                    print("You have passed the exam with a grade of C.")

                elif(Percentage >=36 and Pecentage < 40):
                    print("You have passed the exam with a grade of D.")

        else:
            Hindi= int(input("Enter the marks scored in Hindi after the reattempt:"))

            if(Physics >= 36 and Chemistry >= 36 and Maths >= 36 and Hindi >= 36 and English >= 36):
                Total_scored_marks = Physics + Chemistry + Maths + Hindi + English

                Percentage = (Total_scored_marks*100)/Total_max_marks

                if(Percentage >= 90 and Percentage < 100):
                    print("You have passed the exam with a grade of A+.")

                elif(Percentage >=80 and Percentage < 90):
                    print("You have passed the exam with a grade of A.")

                elif(Percentage >=70 and Percentage < 80):
                    print("You have passed the exam with a grade of B+.")

                elif(Percentage >=60 and Percentage < 70):
                    print("You have passed the exam with a grade of B.")

                elif(Percentage >=50 and Percentage < 60):
                    print("You have passed the exam with a grade of C+.")

                elif(Percentage >=40 and Percentage < 50):
                    print("You have passed the exam with a grade of C.")

                elif(Percentage >=36 and Pecentage < 40):
                    print("You have passed the exam with a grade of D.")

            
    elif(English < 36):
        print("You are failed in one subject:")
        print("English:",English)

        
        if(English >= 30 and English <= 35):
            grace= 36-English
            English=English+grace
            print("Grace marks",grace,"added.")
            print("English:",English)

            if(Physics >= 36 and Chemistry >= 36 and Maths >= 36 and Hindi >= 36 and English >= 36):
                Total_scored_marks = Physics + Chemistry + Maths + Hindi + English

                Percentage = (Total_scored_marks*100)/Total_max_marks

                if(Percentage >= 90 and Percentage < 100):
                    print("You have passed the exam with a grade of A+.")

                elif(Percentage >=80 and Percentage < 90):
                    print("You have passed the exam with a grade of A.")

                elif(Percentage >=70 and Percentage < 80):
                    print("You have passed the exam with a grade of B+.")

                elif(Percentage >=60 and Percentage < 70):
                    print("You have passed the exam with a grade of B.")

                elif(Percentage >=50 and Percentage < 60):
                    print("You have passed the exam with a grade of C+.")

                elif(Percentage >=40 and Percentage < 50):
                    print("You have passed the exam with a grade of C.")

                elif(Percentage >=36 and Pecentage < 40):
                    print("You have passed the exam with a grade of D.")

        else:
            English= int(input("Enter the marks scored in English after the reattempt:"))

            if(Physics >= 36 and Chemistry >= 36 and Maths >= 36 and Hindi >= 36 and English >= 36):
                Total_scored_marks = Physics + Chemistry + Maths + Hindi + English

                Percentage = (Total_scored_marks*100)/Total_max_marks

                if(Percentage >= 90 and Percentage < 100):
                    print("You have passed the exam with a grade of A+.")

                elif(Percentage >=80 and Percentage < 90):
                    print("You have passed the exam with a grade of A.")

                elif(Percentage >=70 and Percentage < 80):
                    print("You have passed the exam with a grade of B+.")

                elif(Percentage >=60 and Percentage < 70):
                    print("You have passed the exam with a grade of B.")

                elif(Percentage >=50 and Percentage < 60):
                    print("You have passed the exam with a grade of C+.")

                elif(Percentage >=40 and Percentage < 50):
                    print("You have passed the exam with a grade of C.")

                elif(Percentage >=36 and Pecentage < 40):
                    print("You have passed the exam with a grade of D.")
