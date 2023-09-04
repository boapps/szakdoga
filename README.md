# szakdoga

## Feladat

A K-Monitor sajtóadatbázisának bővítését segíteni gépi tanulással.

Tehát korrupció* témájú szövegek gépi elemzése, klasszifikációja, ténykinyerés stb.

*korrupcióról, közbeszerzésekről, közpénzfelhasználásról, illetve általában a közélet tisztaságáról, átláthatóságáról szóló

## Megvalósítás

Magas szinten: 

![Folyamatábra](/assets/flowchart.png)

### 1. Új cikk letöltése [kb kész]

Rendszeresen lekérjük hírportálok RSS feed-jét és az új cikkeket letöltjük newspaper3k python könyvtárral.

TODO: majd külön scraperek írása olyan oldalakhoz, amikkel nem (tökéletesen) működik a newspaper3k.

### 2. Rovat szerinti szűrés [kb kész]

Egyelőre csak URL alapján kiszűrjük az angol híreket (pl.: `https://telex.hu/english/.*`) vagy életmód, stb. irreleváns rovatba tartozó cikkeket.

### 3. Cikk szövegének tisztítása [kész]

A newspaper3k nem tökéletes, a szövegbe kerülnek felesleges sorok.
Ezek gyakran ismétlődnek, így globális előfordulási gyakoriság alapján szűrhetők.
Magyarul: van egy common_lines fájl, ami a gyakori sorokat tartalmazza.

### 4. Korrupció klasszifikáció [kb kész]

Cikkekről eldönteni, hogy korrupciós témát dolgoznak-e fel.

#### Adathalmaz

[kmdb_classification](https://huggingface.co/datasets/boapps/kmdb_classification)

##### Negatív minták

Kiválasztottam 36 012 db cikket manuális annotálásra, ezeket sorba rendeztem régi (~85%-os) modellel és korrupciósabb felétől kezdve elkezdtem annotálni.
Az utolsó 20 000 cikket megjelöltem negatívnak, így kevesebbet kell annotálnom.
Végül csak az első 6000 cikk annotálását végeztem el, de talán így is elég lesz

##### Pozitív minták

K-monitor sajtóadatbázisának scrapelése.

[kmdb_base](https://huggingface.co/datasets/boapps/kmdb_base)

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

TODO: kísérletezni, mennyi a különbség (ha nem sok, akkor kevesebb szöveggel tanítás gyorsíthat a finomhangoláson és a használaton is).

lehetőségek:
- Cím + lead + kulcsszavak
- Cím + lead + random bekezdés + kulcsszavak
- Cím + lead + teljes szöveg + kulcsszavak

### 5. Másik cikkre hivatkozik [kb kész]

Az adatbázist nem szeretnénk redundáns cikkekkel megtölteni, amik a már adatbázisban levő cikkek átvételei és semmilyen plusz információt nem tartalmaznak.

Ehhez egy egyszerű minta-alapú algoritmust használunk, ami például ilyen szerkezetű mondatokat ismer fel: "... írja a telex.hu".

TODO: lehetne HuSpaCy-vel bonyolítani

### 6. Helyreigazítás-e [todo]

Szeretnénk külön kezelni helyreigazításokat és esetleg kinyerni melyik cikkre hivatkozik a helyreigazítás.

Erre is egy szabály-alapú algoritmus/HuSpaCy lenne a megoldás.

### 7. Kulcsszavak kinyerése [elkezdve]

#### Adathalmaz

[kmdb_base](https://huggingface.co/datasets/boapps/kmdb_base)

#### Modell

Hasonló, mint a "Korrupció klasszifikáció"-nál.

##### Formátum

### 8. Entitásfelismerés [kész]

Spacy-vel előre kinyerjük a szövegben előforduló entitásokat.
Majd ezek közül választja ki a következő lépés a relevánsakat.

(lehet hogy a végleges megoldásban el lesz hagyva, ha nem javít sokat a végeredményen)

### 9. Személyek, intézmények és helyszínek relevanciája [elkezdve]

Kiválasztja a releváns entitásokat a szövegből, tehát pl. személy esetén azt aki a cikk szerint korrupciós tevéknenységgel összefüggésbe hozható.

#### Adathalmaz

[kmdb_base](https://huggingface.co/datasets/boapps/kmdb_base)

### 10. Entitások közti kapcsolat [todo]

Entitások közti reláció kinyerése.
Pl. millyen kapcsolat van két személy esetén.

Ilyen hármasok formájában: `{Jancsi, Juliska, testvér}` + bekezdés, ami erről ír + indoklás

#### Adathalmaz

Ehhez OpenAI API-t fogok használni: Megadok egy bekezdést és megkérem, hogy indoklással együtt adja meg a benne szereplő kapcsolatokat.

TODO:
1. cikkeket bekezdésre bontani
2. szűrni azokat, amik tartalmaznak 2 entitást
3. OpenAI API-nak odaadni, hogy gyűjtse ki belőlük az entitások közti kapcsolatokat, indoklással 

### 11. Webes UI [elkezdve]

Egy egyszerű webes felület, ami a modell által korupciósnak ítélt cikkeket megjeleníti egy listában.
A cikkekhez két gomb lenne: helyes a döntés vagy sem.
Ugyanígy a kulcsszavakra, entitás kapcsolatokra és releváns entitásokra is kell egy szerkesztői felület.
