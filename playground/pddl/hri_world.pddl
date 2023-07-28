(define 
    (domain hri_world)
    
    
    (:requirements 
        :strips 
        :typing 
        :negative-preconditions
        :conditional-effects
        :disjunctive-preconditions
    )
    
    


    (:types
        human - object
    )
    

    (:predicates
        
        (interaction_ok ?h - human)
        (human_here ?h - human)


        (telling_registration ?h - human) 
        (registration_ok ?h - human)
        

        (telling_shopping ?h - human)
        (shopping_ok ?h - human)

        (telling_info ?h - human)
        (info_ok ?h - human)
        

        (telling_where ?h - human)
        (where_ok ?h - human)
        
    
    )


    
    (:action registration_done
        :parameters
        (
            ?h - human
        )
        :precondition
        (and
            (human_here ?h)
            (telling_registration ?h)
        )
        :effect
        (and
            (not (telling_registration ?h))
            (interaction_ok ?h)
        )
        
    )

    (:action shopping_done
        :parameters
        (
            ?h - human
        )
        :precondition
        (and
            (human_here ?h)
            (telling_shopping ?h)
        )
        :effect
        (and
            (not (telling_shopping ?h))
            (interaction_ok ?h)
        )
        
    )

    (:action info_done
        :parameters
        (
            ?h - human
        )
        :precondition
        (and
            (human_here ?h)
            (telling_info ?h)
        )
        :effect
        (and
            (not (telling_info ?h))
            (interaction_ok ?h)
        )
        
    )


    (:action where_done
        :parameters
        (
            ?h - human
        )
        :precondition
        (and
            (human_here ?h)
            (telling_where ?h)
        )
        :effect
        (and
            (not (telling_where ?h))
            (interaction_ok ?h)
        )
        
    )

    (:action tell_welcome
        :parameters
        (
            ?h - human
        )
        :precondition
        (and
            (human_here ?h)
        )
        :effect
        (oneof
            (telling_registration ?h)
            (telling_shopping ?h)
            (telling_info ?h)
            (telling_where ?h)
        )
    )



    
    
    
)