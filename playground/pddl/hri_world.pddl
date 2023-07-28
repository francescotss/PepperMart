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
        
        (interaction_done ?h - human)
        (human_here ?h - human)


        (telling_registration ?h - human) 
        (registration_done ?h - human)
        

        (telling_shopping ?h - human)
        (shopping_done ?h - human)

        (telling_info ?h - human)
        (info_done ?h - human)
        

        (telling_where ?h - human)
        (where_done ?h - human)
        

        (is_registered ?h - human)
    
    )

    (:action do_registration_during_shopping
        :parameters (?h - human)
        :precondition 
        (and 
            
            (not (is_registered ?h))
            
        )
        :effect 
        (and 
            (is_registered ?h)
            ; (telling_registration ?h)
        )
    )
    


    
    (:action do_registration
        :parameters
        (
            ?h - human
        )
        :precondition
        (and
            (human_here ?h)
            (telling_registration ?h)
            (not (is_registered ?h))

            (not (telling_info ?h))
            (not (telling_shopping ?h))
            (not (telling_where ?h))
        )
        :effect
        (and
            (not (telling_registration ?h))
            (is_registered ?h)
            (oneof
                (telling_shopping ?h)
                (telling_where ?h)
            )
        )
        
    )

    (:action do_shopping
        :parameters
        (
            ?h - human
        )
        :precondition
        (and
            (human_here ?h)
            (telling_shopping ?h)
            (is_registered ?h)

            
            (not (telling_info ?h))
            (not (telling_registration ?h))
            (not (telling_where ?h))
        )
        :effect
        (and
            (not (telling_shopping ?h))
            (interaction_done ?h)
        )
        
    )

    (:action do_info
        :parameters
        (
            ?h - human
        )
        :precondition
        (and
            (human_here ?h)
            (telling_info ?h)

            (not (telling_registration ?h))
            (not (telling_shopping ?h))
            (not (telling_where ?h))
            
        )
        :effect
        (and
            (not (telling_info ?h))
            (oneof
                (telling_shopping ?h)
                (telling_where ?h)
            )
            ; (interaction_done ?h)
        )
        
    )


    (:action do_where
        :parameters
        (
            ?h - human
        )
        :precondition
        (and
            (human_here ?h)
            (telling_where ?h)

            
            (not (telling_info ?h))
            (not (telling_shopping ?h))
            (not (telling_registration ?h))
        )
        :effect
        (and
            (not (telling_where ?h))
            (interaction_done ?h)
        )
        
    )

    (:action wait_welcome_reply
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