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
        (human_say_welcome ?h - human)

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
        
        ; ; indica che l'umano ha gia fatto la prima interazione (il saluto)
        ; (human_doing_welcome ?h - human)
        ; (human_doing_registration ?h - human)
        ; (human_doing_shopping ?h - human)
        ; (human_doing_where ?h - human)
        ; (human_doing_info ?h - human)


        ; ; il robot aspetta la risposta dell'umano (puo essere "human_say_<qualcosa>" oppure "human_say_no_<qualcosa>") 
        ; ; dopo aver fatto una specifica domanda

        ; (robot_wait_registration_reply ?r - robot ?h - human)
        ; (robot_wait_shopping_reply ?r - robot ?h - human)
        ; (robot_wait_where_reply ?r - robot ?h - human)
        ; (robot_wait_info_reply ?r - robot ?h - human)

        

        ; ; il robot aspetta le keywords specifiche per fare in modo di iniziare una delle possibili interazioni (registrazione, spesa, info, trova prodotto)
        ; (robot_wait_registration_keyword ?r - robot ?h - human)
        ; (robot_wait_shopping_keyword ?r - robot ?h - human)
        ; (robot_wait_where_keyword ?r - robot ?h - human)
        ; (robot_wait_info_keyword ?r - robot ?h - human)
        
        
        
    )



    (:action robot_say_welcome
        :parameters (?r - robot ?h - human)
        :precondition 
        (and 
            (interaction_start ?h ?r)
        )
        :effect 
        (and 
            (human_say_welcome ?h)
        )
    )

    (:action robot_wait_human_decision
        :parameters (?r - robot ?h - human)
        :precondition (and (human_say_welcome ?h) (not (human_is_registered ?h)))
        :effect (and 
            (oneof
                (human_say_registration ?h)
                (human_say_shopping ?h)
                (human_say_where ?h)
                (human_say_info ?h)
            )
        )
    )

    (:action robot_wait_human_decision_registered
        :parameters (?r - robot ?h - human)
        :precondition (and (human_say_welcome ?h) (human_is_registered ?h))
        :effect (and 
            (oneof
                (human_say_shopping ?h)
                (human_say_where ?h)
                (human_say_info ?h)
            )
        )
    )

    (:action robot_do_registration
        :parameters (?r - robot ?h - human)
        :precondition (and (human_say_registration ?h) (not (human_is_registered ?h)))
        :effect (and 
            (human_is_registered ?h)
            (not (interaction_start ?h ?r))
            (interaction_done ?h ?r)
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

    (:action robot_do_registration_during_do_shopping
        :parameters (?r - robot ?h - human)
        :precondition (and (human_say_shopping ?h) (not (human_is_registered ?h)))
        :effect (and 
            (human_is_registered ?h)
            (not (interaction_start ?h ?r))
            (interaction_done ?h ?r)
        )
    )
    
    
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
            (not (interaction_start ?h ?r))
            (interaction_done ?h ?r)
        )
    )
    
)
    