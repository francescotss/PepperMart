(define 
    (problem supermarket_problem_example)
    (:domain supermarket)
    
    (:objects
        
        cell_1_1	cell_2_1	cell_3_1	cell_4_1	cell_5_1	cell_6_1	cell_7_1	cell_8_1	cell_9_1	cell_10_1
        cell_1_2	cell_2_2	cell_3_2	cell_4_2	cell_5_2	cell_6_2	cell_7_2	cell_8_2	cell_9_2	cell_10_2
        cell_1_3	cell_2_3	cell_3_3	cell_4_3	cell_5_3	cell_6_3	cell_7_3	cell_8_3	cell_9_3	cell_10_3
        cell_1_4	cell_2_4	cell_3_4	cell_4_4	cell_5_4	cell_6_4	cell_7_4	cell_8_4	cell_9_4	cell_10_4
        cell_1_5	cell_2_5	cell_3_5	cell_4_5	cell_5_5	cell_6_5	cell_7_5	cell_8_5	cell_9_5	cell_10_5
        cell_1_6	cell_2_6	cell_3_6	cell_4_6	cell_5_6	cell_6_6	cell_7_6	cell_8_6	cell_9_6	cell_10_6
        cell_1_7	cell_2_7	cell_3_7	cell_4_7	cell_5_7	cell_6_7	cell_7_7	cell_8_7	cell_9_7	cell_10_7
        cell_1_8	cell_2_8	cell_3_8	cell_4_8	cell_5_8	cell_6_8	cell_7_8	cell_8_8	cell_9_8	cell_10_8
        cell_1_9	cell_2_9	cell_3_9	cell_4_9	cell_5_9	cell_6_9	cell_7_9	cell_8_9	cell_9_9	cell_10_9
        cell_1_10	cell_2_10	cell_3_10	cell_4_10	cell_5_10	cell_6_10	cell_7_10	cell_8_10	cell_9_10	cell_10_10 - cell
        
        cell_5_11 cell_11_9 - cell ; entrace and exit
        ; household personal_care beverages frozen_foods meatcounter fishcounter infopoint cashdesk entrace exit - section
    
		HUMAN - human
		CART - cart
		LIST - list
		TOOTHPASTE - product
		SHAMPOO - product
		BODYLOTION - product
		DEODORAN - product
		BEEF - product
		CHICKEN - product
		HAMBURGER - product
		SALMON - product
		TUNA - product
		OCTOPUS - product
		OYSTER - product
		EGGS - product
		MILK - product
		BREAD - product
		CHEESE - product
		RICE - product
		SUGAR - product
		SALT - product
		COFFEE - product
		COOKIES - product
		KETCHUP - product
		COCACOLA - product
		ORANGEJUICE - product
		WATER - product
		CHINOTTO - product
		FROZENPIZZA - product
		FROZENFISH - product
		ICECREAM - product
		FROZENSHRIMP - product
		FROZENFISHSTICKS - product
		WAFFLE - product
		MAGNUM - product
		POPSICLE - product
		household - section
		personal_care - section
		beverages - section
		frozen_foods - section
		meatcounter - section
		fishcounter - section
		infopoint - section
		cashdesk - section
		entrace - section
		exit - section

    
    )
    
    (:init
        
        
        (walkable cell_1_1)	(walkable cell_2_1)	(walkable cell_3_1)	(walkable cell_4_1)	(walkable cell_5_1)	(walkable cell_6_1)	(walkable cell_7_1)	(walkable cell_8_1)	(walkable cell_9_1)	(walkable cell_10_1)
        (walkable cell_1_2)			                                (walkable cell_4_2)			                                (walkable cell_7_2)			                                (walkable cell_10_2)
        (walkable cell_1_3)	(walkable cell_2_3)	(walkable cell_3_3)	(walkable cell_4_3)	(walkable cell_5_3)	(walkable cell_6_3)	(walkable cell_7_3)			                                (walkable cell_10_3)
        (walkable cell_1_4)			                                (walkable cell_4_4)			                                (walkable cell_7_4)			                                (walkable cell_10_4)
        (walkable cell_1_5)			                                (walkable cell_4_5)			                                (walkable cell_7_5)			                                (walkable cell_10_5)
        (walkable cell_1_6)	(walkable cell_2_6)	(walkable cell_3_6)	(walkable cell_4_6)	(walkable cell_5_6)	(walkable cell_6_6)	(walkable cell_7_6)	(walkable cell_8_6)	(walkable cell_9_6)	(walkable cell_10_6)
        (walkable cell_1_7)			                                (walkable cell_4_7)	(walkable cell_5_7)	(walkable cell_6_7)		                (walkable cell_8_7)		                (walkable cell_10_7)
        (walkable cell_1_8)			                                (walkable cell_4_8)	(walkable cell_5_8)	(walkable cell_6_8)		                (walkable cell_8_8)	(walkable cell_9_8)	(walkable cell_10_8)
        (walkable cell_1_9)			                                (walkable cell_4_9)	(walkable cell_5_9)	(walkable cell_6_9)		                (walkable cell_8_9)		                (walkable cell_10_9) (walkable cell_11_9)
        (walkable cell_1_10) (walkable cell_2_10) (walkable cell_3_10) (walkable cell_4_10) (walkable cell_5_10) (walkable cell_6_10) (walkable cell_7_10) (walkable cell_8_10) (walkable cell_9_10) (walkable cell_10_10)
                                                                                            (walkable cell_5_11)
        
        (adj cell_1_1 cell_2_1)        (adj cell_1_1 cell_1_2)        (adj cell_1_2 cell_2_2) (adj cell_1_2 cell_1_3) (adj cell_1_2 cell_1_1) (adj cell_1_3 cell_2_3) (adj cell_1_3 cell_1_4) (adj cell_1_3 cell_1_2) (adj cell_1_4 cell_2_4) (adj cell_1_4 cell_1_5) (adj cell_1_4 cell_1_3) (adj cell_1_5 cell_2_5) (adj cell_1_5 cell_1_6) (adj cell_1_5 cell_1_4) (adj cell_1_6 cell_2_6) (adj cell_1_6 cell_1_7) (adj cell_1_6 cell_1_5) (adj cell_1_7 cell_2_7) (adj cell_1_7 cell_1_8) (adj cell_1_7 cell_1_6) (adj cell_1_8 cell_2_8) (adj cell_1_8 cell_1_9) (adj cell_1_8 cell_1_7) (adj cell_1_9 cell_2_9) (adj cell_1_9 cell_1_10) (adj cell_1_9 cell_1_8) (adj cell_1_10 cell_2_10) (adj cell_1_10 cell_1_9)
        (adj cell_2_1 cell_3_1)        (adj cell_2_1 cell_2_2)        (adj cell_2_1 cell_1_1)        (adj cell_2_2 cell_3_2)        (adj cell_2_2 cell_2_3)        (adj cell_2_2 cell_1_2)        (adj cell_2_2 cell_2_1)        (adj cell_2_3 cell_3_3)        (adj cell_2_3 cell_2_4)        (adj cell_2_3 cell_1_3)        (adj cell_2_3 cell_2_2)        (adj cell_2_4 cell_3_4)        (adj cell_2_4 cell_2_5)        (adj cell_2_4 cell_1_4)        (adj cell_2_4 cell_2_3)        (adj cell_2_5 cell_3_5)        (adj cell_2_5 cell_2_6)        (adj cell_2_5 cell_1_5)        (adj cell_2_5 cell_2_4)        (adj cell_2_6 cell_3_6)        (adj cell_2_6 cell_2_7)        (adj cell_2_6 cell_1_6)        (adj cell_2_6 cell_2_5)        (adj cell_2_7 cell_3_7)        (adj cell_2_7 cell_2_8)        (adj cell_2_7 cell_1_7)        (adj cell_2_7 cell_2_6)        (adj cell_2_8 cell_3_8)        (adj cell_2_8 cell_2_9)        (adj cell_2_8 cell_1_8)        (adj cell_2_8 cell_2_7)        (adj cell_2_9 cell_3_9)        (adj cell_2_9 cell_2_10)        (adj cell_2_9 cell_1_9)        (adj cell_2_9 cell_2_8)        (adj cell_2_10 cell_3_10)        (adj cell_2_10 cell_1_10)        (adj cell_2_10 cell_2_9)
        (adj cell_3_1 cell_4_1)        (adj cell_3_1 cell_3_2)        (adj cell_3_1 cell_2_1)        (adj cell_3_2 cell_4_2)        (adj cell_3_2 cell_3_3)        (adj cell_3_2 cell_2_2)        (adj cell_3_2 cell_3_1)        (adj cell_3_3 cell_4_3)        (adj cell_3_3 cell_3_4)        (adj cell_3_3 cell_2_3)        (adj cell_3_3 cell_3_2)        (adj cell_3_4 cell_4_4)        (adj cell_3_4 cell_3_5)        (adj cell_3_4 cell_2_4)        (adj cell_3_4 cell_3_3)        (adj cell_3_5 cell_4_5)        (adj cell_3_5 cell_3_6)        (adj cell_3_5 cell_2_5)        (adj cell_3_5 cell_3_4)        (adj cell_3_6 cell_4_6)        (adj cell_3_6 cell_3_7)        (adj cell_3_6 cell_2_6)        (adj cell_3_6 cell_3_5)        (adj cell_3_7 cell_4_7)        (adj cell_3_7 cell_3_8)        (adj cell_3_7 cell_2_7)        (adj cell_3_7 cell_3_6)        (adj cell_3_8 cell_4_8)        (adj cell_3_8 cell_3_9)        (adj cell_3_8 cell_2_8)        (adj cell_3_8 cell_3_7)        (adj cell_3_9 cell_4_9)        (adj cell_3_9 cell_3_10)        (adj cell_3_9 cell_2_9)        (adj cell_3_9 cell_3_8)        (adj cell_3_10 cell_4_10)        (adj cell_3_10 cell_2_10)        (adj cell_3_10 cell_3_9)
        (adj cell_4_1 cell_5_1)        (adj cell_4_1 cell_4_2)        (adj cell_4_1 cell_3_1)        (adj cell_4_2 cell_5_2)        (adj cell_4_2 cell_4_3)        (adj cell_4_2 cell_3_2)        (adj cell_4_2 cell_4_1)        (adj cell_4_3 cell_5_3)        (adj cell_4_3 cell_4_4)        (adj cell_4_3 cell_3_3)        (adj cell_4_3 cell_4_2)        (adj cell_4_4 cell_5_4)        (adj cell_4_4 cell_4_5)        (adj cell_4_4 cell_3_4)        (adj cell_4_4 cell_4_3)        (adj cell_4_5 cell_5_5)        (adj cell_4_5 cell_4_6)        (adj cell_4_5 cell_3_5)        (adj cell_4_5 cell_4_4)        (adj cell_4_6 cell_5_6)        (adj cell_4_6 cell_4_7)        (adj cell_4_6 cell_3_6)        (adj cell_4_6 cell_4_5)        (adj cell_4_7 cell_5_7)        (adj cell_4_7 cell_4_8)        (adj cell_4_7 cell_3_7)        (adj cell_4_7 cell_4_6)        (adj cell_4_8 cell_5_8)        (adj cell_4_8 cell_4_9)        (adj cell_4_8 cell_3_8)        (adj cell_4_8 cell_4_7)        (adj cell_4_9 cell_5_9)        (adj cell_4_9 cell_4_10)        (adj cell_4_9 cell_3_9)        (adj cell_4_9 cell_4_8)        (adj cell_4_10 cell_5_10)        (adj cell_4_10 cell_3_10)        (adj cell_4_10 cell_4_9)
        (adj cell_5_1 cell_6_1)        (adj cell_5_1 cell_5_2)        (adj cell_5_1 cell_4_1)        (adj cell_5_2 cell_6_2)        (adj cell_5_2 cell_5_3)        (adj cell_5_2 cell_4_2)        (adj cell_5_2 cell_5_1)        (adj cell_5_3 cell_6_3)        (adj cell_5_3 cell_5_4)        (adj cell_5_3 cell_4_3)        (adj cell_5_3 cell_5_2)        (adj cell_5_4 cell_6_4)        (adj cell_5_4 cell_5_5)        (adj cell_5_4 cell_4_4)        (adj cell_5_4 cell_5_3)        (adj cell_5_5 cell_6_5)        (adj cell_5_5 cell_5_6)        (adj cell_5_5 cell_4_5)        (adj cell_5_5 cell_5_4)        (adj cell_5_6 cell_6_6)        (adj cell_5_6 cell_5_7)        (adj cell_5_6 cell_4_6)        (adj cell_5_6 cell_5_5)        (adj cell_5_7 cell_6_7)        (adj cell_5_7 cell_5_8)        (adj cell_5_7 cell_4_7)        (adj cell_5_7 cell_5_6)        (adj cell_5_8 cell_6_8)        (adj cell_5_8 cell_5_9)        (adj cell_5_8 cell_4_8)        (adj cell_5_8 cell_5_7)        (adj cell_5_9 cell_6_9)        (adj cell_5_9 cell_5_10)        (adj cell_5_9 cell_4_9)        (adj cell_5_9 cell_5_8)        (adj cell_5_10 cell_6_10)        (adj cell_5_10 cell_4_10)        (adj cell_5_10 cell_5_9)
        (adj cell_6_1 cell_7_1)        (adj cell_6_1 cell_6_2)        (adj cell_6_1 cell_5_1)        (adj cell_6_2 cell_7_2)        (adj cell_6_2 cell_6_3)        (adj cell_6_2 cell_5_2)        (adj cell_6_2 cell_6_1)        (adj cell_6_3 cell_7_3)        (adj cell_6_3 cell_6_4)        (adj cell_6_3 cell_5_3)        (adj cell_6_3 cell_6_2)        (adj cell_6_4 cell_7_4)        (adj cell_6_4 cell_6_5)        (adj cell_6_4 cell_5_4)        (adj cell_6_4 cell_6_3)        (adj cell_6_5 cell_7_5)        (adj cell_6_5 cell_6_6)        (adj cell_6_5 cell_5_5)        (adj cell_6_5 cell_6_4)        (adj cell_6_6 cell_7_6)        (adj cell_6_6 cell_6_7)        (adj cell_6_6 cell_5_6)        (adj cell_6_6 cell_6_5)        (adj cell_6_7 cell_7_7)        (adj cell_6_7 cell_6_8)        (adj cell_6_7 cell_5_7)        (adj cell_6_7 cell_6_6)        (adj cell_6_8 cell_7_8)        (adj cell_6_8 cell_6_9)        (adj cell_6_8 cell_5_8)        (adj cell_6_8 cell_6_7)        (adj cell_6_9 cell_7_9)        (adj cell_6_9 cell_6_10)        (adj cell_6_9 cell_5_9)        (adj cell_6_9 cell_6_8)        (adj cell_6_10 cell_7_10)        (adj cell_6_10 cell_5_10)        (adj cell_6_10 cell_6_9)
        (adj cell_7_1 cell_8_1)        (adj cell_7_1 cell_7_2)        (adj cell_7_1 cell_6_1)        (adj cell_7_2 cell_8_2)        (adj cell_7_2 cell_7_3)        (adj cell_7_2 cell_6_2)        (adj cell_7_2 cell_7_1)        (adj cell_7_3 cell_8_3)        (adj cell_7_3 cell_7_4)        (adj cell_7_3 cell_6_3)        (adj cell_7_3 cell_7_2)        (adj cell_7_4 cell_8_4)        (adj cell_7_4 cell_7_5)        (adj cell_7_4 cell_6_4)        (adj cell_7_4 cell_7_3)        (adj cell_7_5 cell_8_5)        (adj cell_7_5 cell_7_6)        (adj cell_7_5 cell_6_5)        (adj cell_7_5 cell_7_4)        (adj cell_7_6 cell_8_6)        (adj cell_7_6 cell_7_7)        (adj cell_7_6 cell_6_6)        (adj cell_7_6 cell_7_5)        (adj cell_7_7 cell_8_7)        (adj cell_7_7 cell_7_8)        (adj cell_7_7 cell_6_7)        (adj cell_7_7 cell_7_6)        (adj cell_7_8 cell_8_8)        (adj cell_7_8 cell_7_9)        (adj cell_7_8 cell_6_8)        (adj cell_7_8 cell_7_7)        (adj cell_7_9 cell_8_9)        (adj cell_7_9 cell_7_10)       (adj cell_7_9 cell_6_9)        (adj cell_7_9 cell_7_8)        (adj cell_7_10 cell_8_10)        (adj cell_7_10 cell_6_10)        (adj cell_7_10 cell_7_9)
        (adj cell_8_1 cell_9_1)        (adj cell_8_1 cell_8_2)        (adj cell_8_1 cell_7_1)        (adj cell_8_2 cell_9_2)        (adj cell_8_2 cell_8_3)        (adj cell_8_2 cell_7_2)        (adj cell_8_2 cell_8_1)        (adj cell_8_3 cell_9_3)        (adj cell_8_3 cell_8_4)        (adj cell_8_3 cell_7_3)        (adj cell_8_3 cell_8_2)        (adj cell_8_4 cell_9_4)        (adj cell_8_4 cell_8_5)        (adj cell_8_4 cell_7_4)        (adj cell_8_4 cell_8_3)        (adj cell_8_5 cell_9_5)        (adj cell_8_5 cell_8_6)        (adj cell_8_5 cell_7_5)        (adj cell_8_5 cell_8_4)        (adj cell_8_6 cell_9_6)        (adj cell_8_6 cell_8_7)        (adj cell_8_6 cell_7_6)        (adj cell_8_6 cell_8_5)        (adj cell_8_7 cell_9_7)        (adj cell_8_7 cell_8_8)        (adj cell_8_7 cell_7_7)        (adj cell_8_7 cell_8_6)        (adj cell_8_8 cell_9_8)        (adj cell_8_8 cell_8_9)        (adj cell_8_8 cell_7_8)        (adj cell_8_8 cell_8_7)        (adj cell_8_9 cell_9_9)        (adj cell_8_9 cell_8_10)        (adj cell_8_9 cell_7_9)        (adj cell_8_9 cell_8_8)        (adj cell_8_10 cell_9_10)        (adj cell_8_10 cell_7_10)        (adj cell_8_10 cell_8_9)
        (adj cell_9_1 cell_10_1)        (adj cell_9_1 cell_9_2)        (adj cell_9_1 cell_8_1)        (adj cell_9_2 cell_10_2)        (adj cell_9_2 cell_9_3)        (adj cell_9_2 cell_8_2)        (adj cell_9_2 cell_9_1)        (adj cell_9_3 cell_10_3)        (adj cell_9_3 cell_9_4)        (adj cell_9_3 cell_8_3)        (adj cell_9_3 cell_9_2)        (adj cell_9_4 cell_10_4)        (adj cell_9_4 cell_9_5)        (adj cell_9_4 cell_8_4)        (adj cell_9_4 cell_9_3)        (adj cell_9_5 cell_10_5)        (adj cell_9_5 cell_9_6)        (adj cell_9_5 cell_8_5)        (adj cell_9_5 cell_9_4)        (adj cell_9_6 cell_10_6)        (adj cell_9_6 cell_9_7)        (adj cell_9_6 cell_8_6)        (adj cell_9_6 cell_9_5)        (adj cell_9_7 cell_10_7)        (adj cell_9_7 cell_9_8)        (adj cell_9_7 cell_8_7)        (adj cell_9_7 cell_9_6)        (adj cell_9_8 cell_10_8)        (adj cell_9_8 cell_9_9)        (adj cell_9_8 cell_8_8)       (adj cell_9_8 cell_9_7)        (adj cell_9_9 cell_10_9)        (adj cell_9_9 cell_9_10)        (adj cell_9_9 cell_8_9)        (adj cell_9_9 cell_9_8)        (adj cell_9_10 cell_10_10)        (adj cell_9_10 cell_8_10)        (adj cell_9_10 cell_9_9)
        (adj cell_10_1 cell_10_2)       (adj cell_10_1 cell_9_1) (adj cell_10_2 cell_10_3) (adj cell_10_2 cell_9_2) (adj cell_10_2 cell_10_1) (adj cell_10_3 cell_10_4) (adj cell_10_3 cell_9_3) (adj cell_10_3 cell_10_2) (adj cell_10_4 cell_10_5) (adj cell_10_4 cell_9_4) (adj cell_10_4 cell_10_3) (adj cell_10_5 cell_10_6) (adj cell_10_5 cell_9_5) (adj cell_10_5 cell_10_4) (adj cell_10_6 cell_10_7) (adj cell_10_6 cell_9_6) (adj cell_10_6 cell_10_5) (adj cell_10_7 cell_10_8) (adj cell_10_7 cell_9_7) (adj cell_10_7 cell_10_6) (adj cell_10_8 cell_10_9) (adj cell_10_8 cell_9_8) (adj cell_10_8 cell_10_7) (adj cell_10_9 cell_10_10) (adj cell_10_9 cell_9_9) (adj cell_10_9 cell_10_8) (adj cell_10_10 cell_9_10) (adj cell_10_10 cell_10_9)
        
        
        
        (adj cell_10_9 cell_11_9) ; exit
        (adj cell_11_9 cell_10_9) ; exit
        
        (adj cell_5_10 cell_5_11) ; entrace
        (adj cell_5_11 cell_5_10) ; entrace
        
        (is cell_11_9 exit)
        (is cell_5_11 entrace)
        
        ; ; reparti del supermercato
        ; (is cell_2_2 meatcounter) (is cell_3_2 meatcounter)
        ; (is cell_5_2 fishcounter) (is cell_6_2 fishcounter)
        
        ; (is cell_2_4 personal_care) (is cell_3_4 personal_care)
        ; (is cell_2_5 personal_care) (is cell_3_5 personal_care)
        
        
        ; (is cell_2_7 household) (is cell_3_7 household)
        ; (is cell_2_8 household) (is cell_3_8 household)
        ; (is cell_2_9 household) (is cell_3_9 household)
        
        ; (is cell_8_2 frozen_foods) (is cell_9_2 frozen_foods)
        ; (is cell_9_3 frozen_foods) (is cell_9_3 frozen_foods)
        ; (is cell_8_4 frozen_foods) (is cell_9_4 frozen_foods)
        ; (is cell_8_5 frozen_foods) (is cell_9_5 frozen_foods)
        
        ; (is cell_5_4 beverages) (is cell_6_4 beverages)
        ; (is cell_5_5 beverages) (is cell_6_5 beverages)

        ; (is cell_7_7 infopoint) (is cell_7_8 infopoint) (is cell_7_9 infopoint)
        
        ; (is cell_9_7 cashdesk) (is cell_9_9 cashdesk)
        
		(at HUMAN cell_5_9)
		(at TOOTHPASTE cell_2_4)
		(at SHAMPOO cell_2_5)
		(at BODYLOTION cell_3_4)
		(at DEODORAN cell_3_5)
		(at BEEF cell_2_2)
		(at CHICKEN cell_3_2)
		(at HAMBURGER cell_3_2)
		(at SALMON cell_5_2)
		(at TUNA cell_5_2)
		(at OCTOPUS cell_6_2)
		(at OYSTER cell_6_2)
		(at EGGS cell_2_7)
		(at MILK cell_2_8)
		(at BREAD cell_2_9)
		(at CHEESE cell_3_7)
		(at RICE cell_3_7)
		(at SUGAR cell_3_8)
		(at SALT cell_3_9)
		(at COFFEE cell_2_8)
		(at COOKIES cell_3_8)
		(at KETCHUP cell_2_9)
		(at COCACOLA cell_5_4)
		(at WATER cell_5_5)
		(at CHINOTTO cell_6_4)
		(at ORANGEJUICE cell_6_5)
		(at FROZENPIZZA cell_8_2)
		(at FROZENFISH cell_8_2)
		(at ICECREAM cell_8_2)
		(at WAFFLE cell_8_2)
		(at MAGNUM cell_8_2)
		(at POPSICLE cell_8_2)
		(at FROZENSHRIMP cell_8_2)
		(at FROZENFISHSTICKS cell_8_2)
		(is cell_2_2 meatcounter)
		(is cell_3_2 meatcounter)
		(is cell_5_2 fishcounter)
		(is cell_6_2 fishcounter)
		(is cell_2_4 personal_care)
		(is cell_3_4 personal_care)
		(is cell_2_5 personal_care)
		(is cell_3_5 personal_care)
		(is cell_2_7 household)
		(is cell_3_7 household)
		(is cell_2_8 household)
		(is cell_3_8 household)
		(is cell_2_9 household)
		(is cell_3_9 household)
		(is cell_8_2 frozen_foods)
		(is cell_8_2 frozen_foods)
		(is cell_8_2 frozen_foods)
		(is cell_8_2 frozen_foods)
		(is cell_8_2 frozen_foods)
		(is cell_8_2 frozen_foods)
		(is cell_8_2 frozen_foods)
		(is cell_8_2 frozen_foods)
		(is cell_5_4 beverages)
		(is cell_6_4 beverages)
		(is cell_5_5 beverages)
		(is cell_6_5 beverages)
		(is cell_7_7 infopoint)
		(is cell_7_8 infopoint)
		(is cell_7_9 infopoint)
		(is cell_9_7 cashdesk)
		(is cell_9_9 cashdesk)


    )

    (:goal
        
        (and 
    		(reached HUMAN meatcounter)

        )
    )
    

)
