(define 
    (domain supermarket)
    
    
    (:requirements 
        :strips 
        :typing 
        :negative-preconditions
        :action-costs
    )
    
    


    (:types
        cart list - entity
        cell section - location
        human product - object
    )
    

    (:predicates
        
        (walkable ?cell - cell)
        (adj ?c1 - cell ?c2 - cell)
        (contains ?container - entity ?product - product)
        (at ?o - object ?cell - cell)
        (is ?cell - cell ?section - section)
        (reached ?human - human ?section - section)
        
    
    )
    
    (:action reach
        :parameters
        (
            ?human - human
            ?human_cell - cell
            ?section - section
            ?section_cell - cell
            
        )
        :precondition
        (and
            (at ?human ?human_cell)
            (adj ?human_cell ?section_cell)
            (is ?section_cell ?section)
        )
        :effect
        (and
            (reached ?human ?section)
        )
        
    )


    (:action move
        :parameters 
        (
            ?human - human 
            ?from_cell - cell
            ?to_cell -cell
        )
        :precondition 
            (and 
                (at ?human ?from_cell) 
                (adj ?from_cell ?to_cell) 
                (walkable ?to_cell)
            )
        :effect 
            (and 
                (not(at ?human ?from_cell)) 
                (at ?human ?to_cell)
            )
    )
    
    (:action take
        :parameters 
            (   
                ?human - human
                ?cart - cart 
                ?list - list
                ?where_human - cell
                ?product - product
                ?where_product - cell
            )
        :precondition
            (and 
                    (at ?human ?where_human) 
                    (at ?product ?where_product) 
                    (adj ?where_human ?where_product) 
                    (contains ?list ?product) 
                    (not(contains ?cart ?product))
            )
        :effect
            (and 
                (not (at ?product ?where_product)) 
                (not (contains ?list ?product)) 
                (contains ?cart ?product)
                
            )
    )
    
    
)