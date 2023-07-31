(define 
    (problem hri_problem_example_v2)
    (:domain hri_world_v2)
    
    (:objects
        
        HUMAN - human
        ROBOT - robot
    
    )
    
    (:init
        (interaction_start HUMAN ROBOT) 
        ; (human_is_registered HUMAN)
    )

    (:goal
        (and
            (interaction_done HUMAN ROBOT)
        )
        
    )
    

)
