# Interazioni

## Fase 0 - welcome
Attivato via tocco testa, avvicinamento frontale e saluto.

P: Come posso aiutarti? Ricorda, se sei già registrato mostrami la tessera.
- Dove: Reparto, prodotto (No login)
- Registrazione: Voglio registrarmi (No login)
- Spesa: Voglio fare la spesa (Login)
- Tutorial: Cosa posso chiederti? (No login)


## Dove

P: Che cosa stai cercando?

## Registrazione:

P: ciao, come ti chiami?
U: nome
P: ciao "nome", d'ora in poi basta che mi mostri il barcode...

## Spesa
P: mostrami il code (se necessario)
Se lista vuota:
P: ho visto che è vuota, ti aiuto a fare la lista della spesa.
Se lista piena:
P: hai già una lista della spesa, vuoi aggiungere altro? [si, no] -> che prodotti vuoi aggiungere? [lista]

P: questa è la strada più veloce per fare la spesa. Se vuoi aggiungere un prodotto dimmi pure, se vuoi rimuoverlo basta cliccarci sopra. 


## Tutorial

- Cosa sa fare pepper.



# Resources
pddl notes: https://ai.dmi.unibas.ch/_files/teaching/hs21/po/exercises/pddl_intro.pdf

online pddl planner: http://editor.planning.domains/#

example planning with costs: https://github.com/planimation/backend/issues/19

(http://editor.planning.domains/#read_session=873KGrMAIa)

https://github.com/mokhtarivahid/safe-planner

https://www.freepik.com/icons


# Note
Bug lobster non diventa verde, manca la categoria dei gamberetti 

# Istruzioni
Start naoqi server: /opt/Aldebaran/naoqi-sdk-2.5.5.5-linux64/naoqi
Start modim: cd ~/src/modim/src/GUI && python ws_server.py -robot pepper
Start main: cd ~/playground/ && python main.py 

Generate plan: cd ~/playground/pddl && ../safe-planner/sp ~/playground/pddl/hri_world.pddl ~/playground/pddl/hri_problem.pddl -j -d

To send asr sentence do: cd ~/src/pepper_tools/asr && python human_say.py --sentence "Phrase"
To send fake sonar: cd ~/src/pepper_tools/sonar && python sonar_sim.py --sensor SonarFront --value 1.0 --duration 10.0