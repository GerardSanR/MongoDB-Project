# BDnR (Bases de Dades no Relacionals)

Projecte MongoDB - dadesGICESXIX 
---------------------------------------------------------
Joel Soler Huix - 1531139
---------------------------------------------------------
Gerard Santacatalina Rubio - 1534002 
---------------------------------------------------------

Primera part

En aquesta primera part del projecte el que farem serà:

1)Per una banda fer el disseny de les diferents col·leccions que hi inserirem a la nostra base de dades tenint en compte les consultes que es demanen per poder retornar els resultats fent servir una estructura de documents el més adient possible seguint sempre els patrons de disseny que hi hem vist a classe. 

2)Per un altra banda el que farem serà dissenyar els scripts necessaris amb Python per poder pre-processar les dades i resoldre totes les inconsistències que tinguem en la base de dades donada així com per inserir en les diferents col·leccions els documents que aquestes contindràn seguint el disseny que hem descrit al punt 1) per cadascuna de les col·leccions. En tot moment tindrem també un control per no afegir tots els documents dues vegades així com per controlar el que una col·lecció ja s'hagi creat o per poder esborrar els continguts que haguem inserit a la base de dades. 
En un principi hem anat dividint les diferents funcions que creen les diferents col·leccions i pre-processen les dades dels diferents sheets (donats en format fitxer excel (.xlsx)) en fitxers diferents, tot i que el que executem després sigui el main mitjançant comandes via consola/terminal. 
Per crear i carregar la base de dades o per actualitzar-la si hem afegit més registres als fitxers que contenen les dades: **python main.py -f dadesGICESXIX.xlsx**<br />
Si volem borrar tots els continguts de la BD (dades de les col·leccions): **python main.py --delete_all --bd dadesGICES**

  SUMARI FITXERS PYTHON:<br /><br />
  **main.py** -> fitxer principal que crida a tota la resta de funcions implementades a la resta d'arxius encarregats de crear les col·leccions i pre-processar i afegir les dades.<br />
  **colaboraciones.py** -> script encarregat de crear la col·lecció colaboracions i de fer tot el control d'inconsistències per emplenar la BD.<br />
  **cuentos.py** -> crea la col·lecció contes i afegeix les dades corresponents un cop pre-processades.<br />
  **delete_cols.py** -> script encarregat d'implementar la funció que ens permet esborrar tots els continguts de la BD.<br />
  **editorials.py** -> script que afegeix una col·lecció on emmagatzema les diferents editorials que tractem a la BD. Col·lecció eminentment pilot.<br />
  **revistes.py** -> script encarregat de la col·lecció revistes a la nostra BD i de tota la càrrega de dades.<br />
  **rom_to_int.py** -> script que implementa una funció que ens converteix un nombre expressat en numeració romana a un nombre sencer en el sistema decimal.<br />
  **traduccio.py** -> codi encarregat de crear la col·lecció traduccions.<br />
  **volumenes.py** -> ens crea la col·lecció volums amb totes les dades que aquesta recull.<br />
          

3)Finalment al document **"consultes_projecte.js"** anirem implementant les diferents consultes del joc de proves que se'ns ha proposat per testejar una mica el disseny i la implementació de la nostra base de dades que hem fet. 


Al document **"InformeFinal_BDnR_P1.pdf"** tenim l'explicació detallada sobre la distribució de tasques, una mica algunes explicacions del que hem fet, com ho hem fet i com ha estat per nosaltres tot el desenvolupament del projecte aquestes darreres setmanes. 

Nota: Hem inclòs al repositori el fitxer **dadesGICESXIX.xlsx** que ens va proporcionar el professor per simplificar el procés d'haver de ficar aquest fitxer a dintre del directori cada cop que descarreguem tota la nostra implementació en format .ZIP quan algun de nosaltres actualitza parts de la implementació.
