import numpy as np
import math

chooseclass = input('What class would you like to see?\n')

if chooseclass == '210' :
    analogsyst_grades_final = np.array([10,10,10,25,45])
    #labs, hw, quizzes, final, 3 exams

    Lab_List = []
    Analog_HW_List = []
    Quiz_List = []
    Analog_Midterm_List = []
    analog_doesfinal = True

    Lab_Number = int(input("How many Lab Grades do you have back? "))

    if Lab_Number == 0:
        Lab_Grade = 1
    else:
        print("Input your Lab grades (in percent, IE 90% = .9). Hit Enter after each grade. ")

        for i in range(0, Lab_Number):
            lab_element = float(input())
            Lab_List.append(lab_element) 
        
        Lab_Grade = np.average(Lab_List)

    Analog_HW_Number = int(input("How many HW Grades do you have back? "))

    if Analog_HW_Number == 0:
        averagehw = 1
    else:

        print("Input your HW grades (in percent, IE 90% = .9). Hit Enter after each grade. ")

        for i in range(0, Analog_HW_Number):
            analog_hw_element = float(input())
            Analog_HW_List.append(analog_hw_element) 

        if (len(Analog_HW_List)) > 3:   #Only runs if there are more than 3 HW grades
            for _ in range(3): #remove three lowest grades
                comparer = 1
                store_i = 0
                for i in range(len(Analog_HW_List)): #flip through array
                    if Analog_HW_List[i] < comparer:
                        comparer = Analog_HW_List[i]
                        store_i = i
                Analog_HW_List = np.delete(Analog_HW_List, [store_i])  
        averagehw = np.average(Analog_HW_List)

    Quiz_Number = int(input("How many Quiz Grades do you have back? "))

    if Quiz_Number == 0:
        Quiz_Grade = 1
    else:
        print("Input your Quiz grades (in percent, IE 90% = .9). Hit Enter after each grade. ")
        for i in range(0, Quiz_Number):
            quiz_element = float(input())
            Quiz_List.append(quiz_element)        
        Quiz_Grade = np.average(Quiz_List)

    Analog_Midterm_Number = int(input("How many Midterm Grades do you have back? "))

    if Analog_Midterm_Number == 0:
        Analog_Midterm_Grade = 1
    else:
        print("Input your Midterm grades (in percent, IE 90% = .9). Hit Enter after each grade. ")
        for i in range(0, Analog_Midterm_Number):
            analog_midterm_element = float(input())
            Analog_Midterm_List.append(analog_midterm_element)        
        Analog_Midterm_Grade = np.average(Analog_Midterm_List)

    while analog_doesfinal == True:
        Analog_Final = (input("Have you taken the final? (Y/N) "))
        print (Analog_Final)
        if Analog_Final == "Y":
            analog_doesfinal = False
            Analog_Final_Grade = float(input("Input the grade you received on your final. "))
        else:
            if Analog_Final == "N":
                analog_doesfinal = False
                Analog_Final_Grade = 1
            else:
                print("Not a valid input. Try again. ")

    analogsyst_grades_me = np.array([Lab_Grade,averagehw,Quiz_Grade,Analog_Final_Grade,Analog_Midterm_Grade])

    #my grades
    analogsyst_calc = analogsyst_grades_me * analogsyst_grades_final
    print (np.sum(analogsyst_calc))


# 313

if chooseclass == '313' :
#    prob_hw = np.array([(55/100), (67/100), (89/100), (48/100), (70.5/100), (58.5/100), (84.5/100), (63/100), (88/100), (67/100)])

    Prob_HW_List = []
    Prob_Midterm_List = []
    prob_doesmidterm = True
    prob_doesfinal = True

    Prob_HW_Number = int(input("How many HW Grades do you have back? "))
    if Prob_HW_Number == 0:
        averagehw = 1
    else:
        print("Input your HW grades (in percent, IE 90% = .9). Hit Enter after each grade. ")
        for i in range(0, Prob_HW_Number):
            prob_hw_element = float(input())
            Prob_HW_List.append(prob_hw_element) 
        if (len(Prob_HW_List)) > 3:   #Only runs if there are more than 3 HW grades
            for _ in range(3): #remove three lowest grades
                comparer = 1
                store_i = 0
                for i in range(len(Prob_HW_List)): #flip through array
                    if Prob_HW_List[i] < comparer:
                        comparer = Prob_HW_List[i]
                        store_i = i
                Prob_HW_List = np.delete(Prob_HW_List, [store_i])    
        averagehw = np.average(Prob_HW_List)

    while prob_doesmidterm == True:
        Prob_Midterm_Number = int(input("How many Midterm Grades do you have back? "))

        if Prob_Midterm_Number == 0:
            prob_doesmidterm = False
            Prob_Midterm1_Grade = 1
            Prob_Midterm2_Grade = 1
        else:
            if Prob_Midterm_Number == 1: 
                prob_doesmidterm = False
                Prob_Midterm1_Grade = float(input("Input your Midterm 1 Grade (in percent, IE 90% = .9). "))
                Prob_Midterm2_Grade = 1
            else:
                if Prob_Midterm_Number == 2:
                    prob_doesmidterm = False
                    Prob_Midterm1_Grade = float(input("Input your Midterm 1 Grade (in percent, IE 90% = .9). "))
                    Prob_Midterm2_Grade = float(input("Input your Midterm 2 Grade (in percent, IE 90% = .9). "))
                else:
                    print("Invalid Input. Input should be between 0 and 2. ")

    
    while prob_doesfinal == True:
        Prob_Final = (input("Have you taken the final? (Y/N) "))
        print (Prob_Final)
        if Prob_Final == "Y":
            prob_doesfinal = False
            Prob_Final_Grade = float(input("Input the grade you received on your final. "))
        else:
            if Prob_Final == "N":
                prob_doesfinal = False
                Prob_Final_Grade = 1
            else:
                print("Not a valid input. Try again. ")
            
    prob_grades_final1 = np.array([15,25,25,35])
    prob_grades_final2 = np.array([15,15,30,40])
    prob_grades_final3 = np.array([15,30,15,40])
    #hw, mid 1, mid 2, final
    prob_grades_me = np.array([averagehw,Prob_Midterm1_Grade,Prob_Midterm2_Grade,Prob_Final_Grade])
    #my grades
    
    prob_calc1 = prob_grades_me * prob_grades_final1
    prob_calc2 = prob_grades_me * prob_grades_final2
    prob_calc3 = prob_grades_me * prob_grades_final3

    if np.sum(prob_calc1) == np.sum(prob_calc2):
        prob_calc2 = 0
    if np.sum(prob_calc1) == np.sum(prob_calc3):
        prob_calc3 = 0

    if (np.sum(prob_calc1) > np.sum(prob_calc2)) and (np.sum(prob_calc1)>np.sum(prob_calc3)) :  # if grading scheme 1 is highest, choose it
        printfinal = np.sum(prob_calc1)
    if (np.sum(prob_calc2) > np.sum(prob_calc1)) and (np.sum(prob_calc2)>np.sum(prob_calc3)) :  # if grading scheme 2 is highest, choose it
        printfinal = np.sum(prob_calc2)
    if (np.sum(prob_calc3) > np.sum(prob_calc2)) and (np.sum(prob_calc3)>np.sum(prob_calc1)) :  # if grading scheme 3 is highest, choose it
        printfinal = np.sum(prob_calc3)

    print (printfinal)
