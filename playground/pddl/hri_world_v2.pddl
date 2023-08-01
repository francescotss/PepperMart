(define 
    (domain hri_world_v2)
    
    
    (:requirements 
        :strips 
        :typing 
        :negative-preconditions
        :conditional-effects
        :disjunctive-preconditions
        :existential-preconditions
    )
    
    


    (:types
        human robot - object
    )
    

    (:predicates
        
        (interaction_start ?h - human ?r - robot)
        (interaction_done ?h - human ?r - robot) ; it is the GOAL

        ; umano risponde al messagio di welcome
        (can_wait_welcome ?h - human)

        ; l'umano dice una delle keywords che fanno partire una delle possibili interazioni
        (human_say_registration ?h - human)
        (human_say_shopping ?h - human)
        (human_say_where ?h - human)
        (human_say_info ?h - human)

        ; l'umano dice no alla specifica domanda del robot (l'interazione finisce per ora)
        (human_say_no_registration ?h - human)
        (human_say_no_shopping ?h - human)
        (human_say_no_where ?h - human)
        (human_say_no_info ?h - human)

        ; l'umano dice no alla specifica domanda del robot, ma non vuole uscire dall'interazione 
        
        (human_say_not_now_registration ?h - human)
        (human_say_not_now_shopping ?h - human)
        (human_say_not_now_where ?h - human)
        (human_say_not_now_info ?h - human)
        (human_say_not_now_generic ?h - human)

        ; indica che l'umano e` registrato
        (human_is_registered ?h - human)
                
        
    )



    (:action robot_say_welcome
        :parameters (?r - robot ?h - human)
        :precondition 
        (and 
            (interaction_start ?h ?r)
        )
        :effect 
        (and 
            (can_wait_welcome ?h)
        )
    )

    (:action robot_wait_human_decision
        :parameters (?r - robot ?h - human)
        :precondition (and (can_wait_welcome ?h) (not (human_is_registered ?h)))
        :effect (and 
            (oneof
                 (human_say_registration ?h)
                 (interaction_start ?h ?r)
                 (human_say_where ?h)
                 (human_say_info ?h)
            )
            (not (can_wait_welcome ?h))
            (not (interaction_start ?h ?r))
        )
    )

    (:action robot_wait_human_decision_registered
        :parameters (?r - robot ?h - human)
        :precondition (and (can_wait_welcome ?h) (human_is_registered ?h))
        :effect (and 
            (oneof
                (human_say_shopping ?h)
                (human_say_where ?h)
                (human_say_info ?h)
                (interaction_start ?h ?r)
                (can_wait_welcome ?h)
            )
            (not (can_wait_welcome ?h))
            (not (interaction_start ?h ?r))
        )
    )

    (:action robot_do_registration
        :parameters (?r - robot ?h - human)
        :precondition (and (human_say_registration ?h) (not (human_is_registered ?h)))
        :effect (and 
            (human_is_registered ?h)
 ;            (interaction_start ?h ?r)
            (can_wait_welcome ?h)
        )
    )
    
    (:action robot_do_shopping
        :parameters (?r - robot ?h - human)
        :precondition (and (human_say_shopping ?h) (human_is_registered ?h))
        :effect (and 
            (not (interaction_start ?h ?r))
            (interaction_done ?h ?r)
        )
    )

    ; (:action robot_do_registration_during_do_shopping
    ;     :parameters (?r - robot ?h - human)
    ;     :precondition (and (human_say_shopping ?h) (not (human_is_registered ?h)))
    ;     :effect (and 
    ;         (human_is_registered ?h)
    ;         (not (interaction_start ?h ?r))
    ;         (interaction_done ?h ?r)
    ;     )
    ; )
    
    
    (:action robot_do_where
        :parameters (?r - robot ?h - human)
        :precondition (and (human_say_where ?h))
        :effect (and 
            (not (interaction_start ?h ?r))
            (interaction_done ?h ?r)
        )
    )
    
    (:action robot_do_info
        :parameters (?r - robot ?h - human)
        :precondition (and (human_say_info ?h))
        :effect (and 
            (interaction_start ?h ?r)
;            (interaction_done ?h ?r)
        )
    )
    
)
    