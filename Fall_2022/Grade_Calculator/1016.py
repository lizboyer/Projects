import numpy as np
import math

chooseclass = input('What class would you like to see?\n')

if chooseclass == '210' :
    analogsyst_grades_final = np.array([10,10,10,25,45])
    #labs, hw, quizzes, final, 3 exams
    analogsyst_grades_me = np.array([.95,.80,.80,.70,.80])
    #my grades
    analogsyst_calc = analogsyst_grades_me * analogsyst_grades_final
    print (np.sum(analogsyst_calc))

if chooseclass == '313' :
    prob_grades_final1 = np.array([15,25,25,35])
    prob_grades_final2 = np.array([15,15,30,40])
    prob_grades_final3 = np.array([15,30,15,40])
    #hw, mid 1, mid 2, final
    prob_grades_me = np.array([.70,.67,.70,.70])
    #my grades
    
    prob_calc1 = prob_grades_me * prob_grades_final1
    prob_calc2 = prob_grades_me * prob_grades_final2
    prob_calc3 = prob_grades_me * prob_grades_final3

    print ((np.sum(prob_calc1) + np.sum(prob_calc2) + np.sum(prob_calc3))/3)
