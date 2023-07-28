(define 
    (domain hri_world)
    
    
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
        
        (near ?h - human ?r - robot) ; it is the starting point, the robot plan starts when the human is near the robot


        ; il robot aspetta che l'umano lo saluti (risposta)
        (robot_wait_welcome_reply ?r - robot ?h - human)        

        ; il robot aspetta la risposta dell'umano (puo essere "human_say_<qualcosa>" oppure "human_say_no_<qualcosa>") 
        ; dopo aver fatto una specifica domanda
        (robot_wait_registration_reply ?r - robot ?h - human)
        (robot_wait_shopping_reply ?r - robot ?h - human)
        (robot_wait_where_reply ?r - robot ?h - human)
        (robot_wait_info_reply ?r - robot ?h - human)

        ; l'umano dice no alla specifica domanda del robot (l'interazione finisce per ora)
        (human_say_no_registration ?h - human)
        (human_say_no_shopping ?h - human)
        (human_say_no_where ?h - human)
        (human_say_no_info ?h - human)

        ; l'umano dice no alla specifica domanda del robot, ma non vuole uscire dall'interazione 
        
        ; (human_say_not_now_registration ?h - human)
        ; (human_say_not_now_shopping ?h - human)
        ; (human_say_not_now_where ?h - human)
        ; (human_say_not_now_info ?h - human)
        (human_say_not_now_generic ?h - human)


        ; il robot aspetta le keywords specifiche per fare in modo di iniziare una delle possibili interazioni (registrazione, spesa, info, trova prodotto)
        (robot_wait_registration_keyword ?r - robot ?h - human)
        (robot_wait_shopping_keyword ?r - robot ?h - human)
        (robot_wait_where_keyword ?r - robot ?h - human)
        (robot_wait_info_keyword ?r - robot ?h - human)
        
        ; l'umano dice una delle keywords che fanno partire una delle possibili interazioni
        (human_say_registration ?h - human)
        (human_say_shopping ?h - human)
        (human_say_where ?h - human)
        (human_say_info ?h - human)

        ; indica che l'umano e` registrato
        (human_is_registerd ?h - human)
        ; indica che l'umano ha gia fatto la prima interazione (il saluto)
        (human_is_welcome ?h - human)
        
    )


    (:action robot_say_welcome_registered
        :parameters (?r - robot ?h - human)
        :precondition 
        (and 
            (near ?h ?r)
            (human_is_registerd ?h)
            (not (human_is_welcome ?h))
        )
        :effect 
        (and
            (robot_wait_welcome_reply ?r ?h)
        )
    )

    (:action human_reply_welcome_registered
        :parameters (?r - robot ?h - human)
        :precondition 
        (and 
            (not (human_is_welcome ?h))
            (robot_wait_welcome_reply ?r ?h)
            (human_is_registerd ?h)
            
        )
        :effect 
        (and
            (not (robot_wait_welcome_reply ?r ?h))
            (human_is_welcome ?h) 
            (interaction_start ?h ?r)     
            (oneof
                (robot_wait_info_keyword ?r ?h)
                (robot_wait_shopping_keyword ?r ?h)
                (robot_wait_where_keyword ?r ?h) 
            )
        )
    )


    (:action robot_say_welcome
        :parameters (?r - robot ?h - human)
        :precondition 
        (and 
            (near ?h ?r)
            (not (human_is_welcome ?h))
        )
        :effect 
        (and 
            (robot_wait_welcome_reply ?r ?h)
        )
    )

    (:action human_reply_welcome
        :parameters (?r - robot ?h - human)
        :precondition 
        (and 
            (not (human_is_welcome ?h))
            (robot_wait_welcome_reply ?r ?h)
            
        )
        :effect 
        (and
            (not (robot_wait_welcome_reply ?r ?h))
            (human_is_welcome ?h)
            (interaction_start ?h ?r)
            (oneof
                (robot_wait_registration_keyword ?r ?h)
                (robot_wait_info_keyword ?r ?h)
                (robot_wait_shopping_keyword ?r ?h)
                (robot_wait_where_keyword ?r ?h)

            )
            
        )
    )

    ; molto difficile da gestire

    ; (:action robot_say_generic
    ;     :parameters (?r - robot ?h - human)
    ;     :precondition
    ;     (and 
    ;         (human_is_welcome ?h)
    ;         (not (human_is_registerd ?h))
    ;         (interaction_start ?h ?r)
    ;     )
    ;     :effect 
    ;     (and
    ;         (oneof
    ;             (robot_wait_registration_keyword ?r ?h)
    ;             (robot_wait_info_keyword ?r ?h)
    ;             (robot_wait_shopping_keyword ?r ?h)
    ;             (robot_wait_where_keyword ?r ?h)
    ;         )

    ;     )
    ; )

    

    ; (:action robot_say_generic_registered
    ;     :parameters (?r - robot ?h - human)
    ;     :precondition
    ;     (and 
    ;         (human_is_welcome ?h)
    ;         (human_is_registerd ?h)
    ;     )
    ;     :effect 
    ;     (and
    ;         (oneof
    ;             ; qua va appeso l'handler in cui il robot chiede se l'umano ha bisogno di qualcosa
    ;             (robot_wait_info_keyword ?r ?h)
    ;             (robot_wait_shopping_keyword ?r ?h)
    ;             (robot_wait_where_keyword ?r ?h)
    ;         )

    ;     )
    ; )


    (:action human_ask_registration
        :parameters (?r - robot ?h - human)
        :precondition 
        (and 
            (robot_wait_registration_keyword ?r ?h)
        )
        :effect 
        (and 
            (not (robot_wait_registration_keyword ?r ?h))
            (human_say_registration ?h)
        )
    )

    (:action human_ask_shopping
        :parameters (?r - robot ?h - human)
        :precondition 
        (and 
            (robot_wait_shopping_keyword ?r ?h)
        )
        :effect 
        (and 
            (not (robot_wait_shopping_keyword ?r ?h))
            (human_say_shopping ?h)
        )
    )
    
    (:action human_ask_where
        :parameters (?r - robot ?h - human)
        :precondition 
        (and 
            (robot_wait_where_keyword ?r ?h)
        )
        :effect 
        (and 
            (not (robot_wait_where_keyword ?r ?h))
            (human_say_where ?h)
        )
    )

    (:action human_ask_info
        :parameters (?r - robot ?h - human)
        :precondition 
        (and 
            (robot_wait_info_keyword ?r ?h)
        )
        :effect 
        (and 
            (not (robot_wait_info_keyword ?r ?h))
            (human_say_info ?h)
        )
    )


    (:action human_reply_registration
        :parameters (?r - robot ?h - human)
        :precondition (and (robot_wait_registration_reply ?r ?h))
        :effect 
        (and 
            (not (robot_wait_registration_reply ?r ?h)) 
            (oneof 
                (human_say_registration ?h) 
                (human_say_no_registration ?h)        
                (human_say_not_now_generic ?h)

            )
        )
    )

    (:action human_reply_where
        :parameters (?r - robot ?h - human)
        :precondition (and (robot_wait_where_reply ?r ?h))
        :effect 
        (and 
            (not (robot_wait_where_reply ?r ?h)) 
            (oneof 
                (human_say_where ?h) 
                (human_say_no_where ?h)        
                (human_say_not_now_generic ?h)

            )
            
            
        )
    )
    
    (:action human_reply_shopping
        :parameters (?r - robot ?h - human)
        :precondition (and (robot_wait_shopping_reply ?r ?h))
        :effect 
        (and 
            (not (robot_wait_shopping_reply ?r ?h)) 
            (oneof 
                (human_say_shopping ?h) 
                (human_say_no_shopping ?h)
                (human_say_not_now_generic ?h)

            )
            
        )
    )

    (:action human_reply_info
        :parameters (?r - robot ?h - human)
        :precondition (and (robot_wait_info_reply ?r ?h))
        :effect 
        (and 
            (not (robot_wait_info_reply ?r ?h)) 
            (oneof 
                (human_say_info ?h) 
                (human_say_no_info ?h)
                (human_say_not_now_generic ?h)
            )
            
        )
    )

    (:action do_registration
        :parameters (?r - robot ?h - human)
        :precondition 
        (and 
            (human_is_welcome ?h)
            (human_say_registration ?h)
            (not (human_is_registerd ?h))
        )
        :effect 
        (and 
            (human_is_registerd ?h) 
            (not (human_say_registration ?h)) 
            (interaction_done ?h ?r)
            ; todo
            
        )
    )
    
    (:action do_where
        :parameters (?r - robot ?h - human)
        :precondition 
        (and
        
            (human_is_welcome ?h)
            (human_say_where ?h)
        )
        :effect 
        (and 
            (not (human_say_where ?h))
            (interaction_done ?h ?r)
        )
    )

    (:action do_shopping
        :parameters (?h - human ?r - robot)
        :precondition 
        (and 
        
            (human_is_welcome ?h)
            (human_say_shopping ?h)
            (human_is_registerd ?h)
        )
        :effect 
        (and
            (not (human_say_shopping ?h))
            (interaction_done ?h ?r)
        )
    )

    (:action do_registration_during_do_shopping
        :parameters (?h - human ?r - robot)
        :precondition 
        (and
        
            (human_is_welcome ?h)
            (human_say_shopping ?h)
            (not (human_is_registerd ?h))
         
        )
        :effect 
        (and 
            (human_is_registerd ?h)
        )
    )
  
    (:action do_info
        :parameters (?h - human ?r - robot)
        :precondition 
        (and
        
            (human_is_welcome ?h)
            (human_say_info ?h) 
        )
        :effect 
        (and 
            (not (human_say_info ?h))
            (interaction_done ?h ?r)

        )
    )

    (:action human_interrupt_registration
        :parameters (?h - human ?r - robot)
        :precondition 
        (and
            (human_is_welcome ?h)
            (exists
                (?h - human)    
                (human_say_no_registration ?h)
            )
        )
           
        :effect (and 
            (interaction_done ?h ?r)
        )
    )

    (:action human_interrupt_where
        :parameters (?h - human ?r - robot)
        :precondition 
        (and
            
            (human_is_welcome ?h)
            (exists
                (?h - human)    
                (human_say_no_where ?h)
            )
        )
           
        :effect (and 
            (interaction_done ?h ?r)
        )
    )

    (:action human_interrupt_shopping
        :parameters (?h - human ?r - robot)
        :precondition 
        (and
            (human_is_welcome ?h)
            (exists
                (?h - human)    
                (human_say_no_shopping ?h)
            )
        )
           
        :effect (and 
            (interaction_done ?h ?r)
        )
    )

    (:action human_interrupt_info
        :parameters (?h - human ?r - robot)
        :precondition 
        (and
            (human_is_welcome ?h)
            (exists
                (?h - human)    
                (human_say_no_info ?h)
            )
        )
           
        :effect (and 
            (interaction_done ?h ?r)
        )
    )

    
    
    
    
    

    
    
    
)