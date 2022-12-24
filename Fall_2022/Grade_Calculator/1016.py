import numpy as np
import math

chooseclass = input('What class would you like to see?\n')

if chooseclass == '210' :
    analogsyst_grades_final = np.array([10,10,10,25,45])
    #labs, hw, quizzes, final, 3 exams
    analogsys_hw = np.array([(60/75), (57/71), (33.3/39), (22.5/35), (45.25/64), (24/33), (33.5/51), (21.2/35), (19.5/22), (24.5/38), (31/49), (30/33)])

    for _ in range(3): #remove three lowest grades
        comparer = 1
        store_i = 0
        for i in range(len(analogsys_hw)): #flip through array
            if analogsys_hw[i] < comparer:
                comparer = analogsys_hw[i]
                store_i = i
        analogsys_hw = np.delete(analogsys_hw, [store_i])    
    averagehw = np.average(analogsys_hw)
    analogsyst_grades_me = np.array([.95,averagehw,.80,.60,.71])
    #my gradess
    analogsyst_calc = analogsyst_grades_me * analogsyst_grades_final
    print (np.sum(analogsyst_calc))

if chooseclass == '313' :
    prob_hw = np.array([(55/100), (67/100), (89/100), (48/100), (70.5/100), (58.5/100), (84.5/100), (63/100), (88/100), (67/100)])

    for _ in range(3): #remove three lowest grades
        comparer = 1
        store_i = 0
        for i in range(len(prob_hw)): #flip through array
            if prob_hw[i] < comparer:
                comparer = prob_hw[i]
                store_i = i
        prob_hw = np.delete(prob_hw, [store_i])    
    averagehw = np.average(prob_hw)

    prob_grades_final1 = np.array([15,25,25,35])
    prob_grades_final2 = np.array([15,15,30,40])
    prob_grades_final3 = np.array([15,30,15,40])
    #hw, mid 1, mid 2, final
    prob_grades_me = np.array([averagehw,.67,.55,.45])
    #my grades
    
    prob_calc1 = prob_grades_me * prob_grades_final1
    prob_calc2 = prob_grades_me * prob_grades_final2
    prob_calc3 = prob_grades_me * prob_grades_final3

    if (np.sum(prob_calc1) > np.sum(prob_calc2)) and (np.sum(prob_calc1)>np.sum(prob_calc3)) :
        printfinal = np.sum(prob_calc1)
    if (np.sum(prob_calc2) > np.sum(prob_calc1)) and (np.sum(prob_calc2)>np.sum(prob_calc3)) :
        printfinal = np.sum(prob_calc2)
    if (np.sum(prob_calc3) > np.sum(prob_calc2)) and (np.sum(prob_calc3)>np.sum(prob_calc1)) :
        printfinal = np.sum(prob_calc3)

    print (printfinal)
