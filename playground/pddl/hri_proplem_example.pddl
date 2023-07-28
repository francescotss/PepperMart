(define 
    (problem hri_problem_example)
    (:domain hri_world)
    
    (:objects
        
        HUMAN - human
    
    )
    
    (:init
        (human_here HUMAN)     
    )

    (:goal
        (and
            (interaction_ok HUMAN)
        )
        
    )
    

)
