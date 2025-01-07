# Data Indexer

## Módszertana

1. Aadatok beolvasása
2. Adatok optimális indexelés
3. Elkészített indexek validálása

## Fejlesztő

- Név: Solymosi Attila
- E-mail: mr.solymi@mailbox.unideb.hu

- Név: Lakatos Róbert
- E-mail: lakatos.robert@inf.unideb.hu

# Szövegdarabolási Technikák Vizsgálata

Ez a projekt különböző szövegdarabolási technikák implementációját és azok értékelését tartalmazza. A cél az optimális paraméterek és megközelítések meghatározása volt, melyek alkalmasak szöveges adatok feldolgozására és hatékony keresési eredmények elérésére.

## Bevezetés
A projekt célja különböző szövegdarabolási technikák algoritmizálása, azok hatékonyságának mérése, valamint az optimális paraméterek meghatározása. A szövegdarabolás során token- és mondatalapú technikákat, illetve csúszóablakos megoldásokat alkalmaztunk. Az eredményeket a k paraméter függvényében elemeztük, ahol k az adott lekérdezéshez visszaadott hasonló kontextusok számát jelölte.

## Használt Technológiák
- Python
- Hugging Face `evaluate` könyvtár
- Rouge, Meteor, és Bleu mérőszámok
- Tokenizálás és mondatalapú szegmentáció

## Szövegdarabolási Technikák

### 1. Tokenalapú Technikák
- **Rögzített Méretű Szeletek**: A szöveget rögzített tokenhosszúságú szeletekre bontottuk (pl. 512, 256, 128, 64, 32, 16).
- **Csúszóablakos Megközelítés**: A szeletek között átfedést (overlap) alkalmaztunk, különböző százalékos értékekkel (50%, 25%, 12.5%).

### 2. Mondatalapú Technikák
- **Rögzített Mondathosszúságú Szeletek**: A szöveget mondatonként bontottuk. Megállapítottuk, hogy egy mondat átlagosan 16 token hosszúságú.
- **Csúszóablakos Megközelítés**: Ennek implementálása nem valósult meg, de az alábbi módon képzelnénk el: a 128 tokenes technikában egy szelet átlagosan hány mondatot tartalmaz, az a szám lenne az ablak mérete, és ebből a fele, negyede, nyolcada (ha belefér) lenne az overlap.

## Mérési Metodológia

### Elsődleges Mérőszámok
- F1-score
- Pontosság (Accuracy)
- Visszahívási Arány (Recall)
- Precizitás (Precision)

Ezek az értékek azt vizsgálták, hogy a visszaadott kontextushalmaz mennyire felel meg az adott kérdéshez tartozó adatoknak. Azonban ezek az eredmények nem bizonyultak elég informatívnak vagy jól feldolgozhatónak, így új mérési módszert vezettünk be.

### Alternatív Mérési Eszközök
Az új mérési rendszerben a Hugging Face `evaluate` könyvtárát használtuk, amely:
- **ROUGE**
- **METEOR**
- **BLEU** 

mérőszámokat biztosított. Ezek az új metrikák informatívabb és feldolgozhatóbb eredményeket adtak.

## Eredmények

### Tokenalapú Technikák
- **512 és 256 token**: Nem volt megfelelő pontosság.
- **128 token**: Optimális eredményt nyújtott, különösen kis k értékek mellett.
- **64, 32 és 16 token**: Használható, de a 128-as technika jobbnak bizonyult.

### Csúszóablakos Tokenalapú Technikák
- **128 token, 50%, 25%, 12.5% overlap**: Az eredmények kismértékű javulást mutattak a fix méretű tokenalapú technikához képest.
- **64 token, 50%, 25%, 12.5% overlap**: Hasonló eredmények születtek, az előzetes várakozásoknak megfelelően.

### Mondatalapú Technikák
- Egy mondat ~16 token.
- Csúszóablakos technika további kutatást igényel.

## Keresztvalidáció
A 128 tokenalapú technikát keresztvalidáltuk 5 másik 1000 kérdéses halmazon. Az eredmények hasonló viselkedést mutattak az első halmazhoz, ami arra utal, hogy a technika általánosítható és más adathalmazokon is jól működik.

## Következtetések és Javaslatok
- A **128 tokenalapú technika** bizonyult a legjobb választásnak, különösen kisebb k értékek mellett.
- A csúszóablakos technikák kismértékű javulást mutattak, de a bonyolultabb implementáció miatt mérlegelendő az alkalmazásuk.
- A mondatokra alapuló csúszóablakos technika további kutatást igényel, különösen a szemantikai relevancia miatt.

## Jövőbeli Tervek
- A mondatalapú csúszóablakos technika kidolgozása és tesztelése.
- További validációk elvégzése különböző kérdéshalmazokon.
- A technikák finomhangolása a szemantikai összefüggések jobb kihasználásához.

## Felhasználás
1. Klónold a repót: `git clone https://github.com/robertlakatos/data-indexer.git`
2. Telepítsd a szükséges csomagokat: [`setup.ipynb`](codes/setup.ipynb) notebook
3. A használata:
   - [`indexer.ipynb`](codes/indexer.ipynb) - vektoradatbázisok létrehozása
   - [`validation-v3.ipynb`](codes/validation-v3.ipynb) - a mérések és .csv fájlok létrehozása
   - [`graphs.ipynb`](codes/graphs.ipynb) - a mérési eredmények vizuálása

## Licenc
Ez a projekt [Apache-2.0 licenc](LICENSE) alatt áll.
