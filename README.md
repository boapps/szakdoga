# szakdoga

## Feladat

A K-Monitor sajtóadatbázisának bővítését segíteni gépi tanulással.

Tehát korrupció* témájú szövegek gépi elemzése, klasszifikációja, ténykinyerés stb.

*korrupcióról, közbeszerzésekről, közpénzfelhasználásról, illetve általában a közélet tisztaságáról, átláthatóságáról szóló

## Megvalósítás

Magas szinten: 

![Folyamatábra](/assets/flowchart.png)

### 1. Új cikk letöltése

Rendszeresen lekérjük hírportálok RSS feed-jét és az új cikkeket letöltjük newspaper3k python könyvtárral.

TODO: majd külön scraperek írása olyan oldalakhoz, amikkel nem (tökéletesen működik a newspaper3k).

### 2. Rovat szerinti szűrés

Egyelőre csak URL alapján kiszűrjük az angol híreket (pl.: `https://telex.hu/english/.*`) vagy életmód, stb. irreleváns rovatba tartozó cikkeket.

### 3. Cikk szövegének tisztítása

### 4. Korrupció klasszifikáció

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

#### Modell

##### Finomhangolás

Mindenképpen LoRA finomhangolást kell végezni.

Alap modellre két lehetőség van:
- [llama 7B](https://huggingface.co/huggyllama/llama-7b): jobb, viszont kell engedélyt szerezni a meta-tól
- [PULI-GPT-3SX](https://huggingface.co/NYTK/PULI-GPT-3SX): rosszabb, viszont szabadon használható

##### Formátum

TODO: kísérletezni, mennyi a különbség (ha nem sok, akkor kevesebb szöveggel tanítás gyorsíthat a finomhangoláson és a használtaon is).

lehetőségek:
- Cím + lead + kulcsszavak
- Cím + lead + random bekezdés + kulcsszavak
- Cím + lead + teljes szöveg + kulcsszavak

### 5. Másik cikkre hivatkozik

Az adatbázist nem szeretnénk redundáns cikkekkel megtölteni, amik a már adatbázisban levő cikkek átvételei és semmilyen plusz információt nem tartalmaznak.

Ehhez egy egyszerű minta-alapú algoritmust használunk, ami például ilyen szerkezetű mondatokat ismer fel: "... írja a telex.hu".

TODO: lehetne HuSpaCy-vel bonyolítani

### 6. Helyreigazítás-e

Szeretnénk külön kezelni helyreigazításokat és esetleg kinyerni melyik cikkre hivatkozik a helyreigazítás.

Erre is egy szabály-alapú algoritmus/HuSpaCy lenne a megoldás.

### 7. Kulcsszavak kinyerése

#### Adathalmaz

#### Modell

Hasonló, mint a "Korrupció klasszifikáció"-nál.

##### Formátum

### 8. Entitásfelismerés

### 9. Személyek, intézmények és helyszínek relevanciája

### 10. Entitások közti kapcsolat

### 11. Webes UI
