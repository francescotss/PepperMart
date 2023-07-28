(define 
    (problem hri_problem_example)
    (:domain hri_world)
    
    (:objects
        
        HUMAN - human
        ROBOT - robot
    
    )
    
    (:init
        (near HUMAN ROBOT) 
        (human_is_registerd HUMAN)
    )

    (:goal
        (and
            (interaction_done HUMAN ROBOT)
        )
        
    )
    

)
