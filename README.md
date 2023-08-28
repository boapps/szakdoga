# szakdoga

## Feladat

A K-Monitor sajtóadatbázisának bővítését segíteni gépi tanulással.

Tehát korrupció* témájú szövegek gépi elemzése, klasszifikációja, ténykinyerés stb.

*korrupcióról, közbeszerzésekről, közpénzfelhasználásról, illetve általában a közélet tisztaságáról, átláthatóságáról szóló

## Megvalósítás

Magas szinten: 

![Folyamatábra](/assets/flowchart.png)


### Klasszifikáció

Cikkekről eldönteni, hogy korrupciós témát dolgoznak-e fel.

#### Adathalmaz

(huggingface link)

##### Negatív minták

Kiválasztottam 36 012 db cikket manuális annotálásra, ezeket sorba rendeztem régi (~85%-os) modellel és korrupciósabb felétől kezdve elkezdtem annotálni.
Az utolsó 20 000 cikket megjelöltem negatívnak, így kevesebbet kell annotálnom.
Végül csak az első 6000 cikk annotálását végeztem el, de talán így is elég lesz

##### Pozitív minták

K-monitor sajtóadatbázisának scrapelése.

(huggingface link)

##### Használat közben keletkező adatok

A rendszer emberi felügyelet alatt működne, ezekből az emberi beavatkozásokból tanulhat a modell.

Már létrehoztam egy demo oldalt, ami egy kevésbé kifinomult modellt használva megjelenít korrupciósnak vélt cikkeket.
Kész van egy alap felület, amiben felül lehet bírálni a modell döntését és a hibás döntéseket kiírom egy csv file-ba.
Ezt pedig visszapörgetem a tanítóhalmazba.
