# MoneySplit
MoneySplit is a telegram Bot written in python.
Its aim is to save items in different wallets and store a list of them
You can have different wallets and for each wallet it's possible to store a list of items like "30 meat", "25 shoes", etc.
## Available commands:
```
To add a new list:
add listname

To remove an existing list:
rem listname

To add an item:
listname price description

To show a list:
show listname

To show the total of a list:
tot listname || total listname

To clear a list:
clear listname || clr listname

To list all created lists:
ls

Note: if you have a list only, you can omit the listname!
```

Project main folder
src -- Sorgenti
res -- Risorse (icone, file di configurazione...)
lib -- Librerie esterne (e.g. file .jar, .so, .dll...)
bin -- Binario (con copia delle risorse)
doc -- Documentazione
README.md