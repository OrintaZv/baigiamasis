 ##  **BAIGIAMASIS DARBAS**

Baigiamasis projektas Vilnius Coding School duomenų analitikos ir python programavimo pagrindų kursui

**Darbo autoriai:** Inga Kizevičienė ir Orinta Žvirzdinė

**Projekto tema:** "Kelionių Svetainių Kainų Palyginimas"

**Projekto tikslas:** Apžvelgti internetiniuose puslapiuose siūlomų kelionių agentūrų pasiūlymus

**Pasirinktos duomenų bazės apimtis:** 1120 eilučių, 8 stulpeliai.

Darbas atliktas Python kalba.


Atlikti išsamią analizę pasirinkome dvi skirtingas kelionių agentūras, kurios pateikia panašius tyrimui naudojamus duomenis [Baltictours](https://www.baltictours.lt/) ir [Kelioniu panorama](https://www.kelioniupanorama.lt/).
Tai kelionių agentūros siūlančios įvairaus pobūdžio keliones, kelionių tipus ir būdus. Siekiant suvienodinti analizei reikiamą informaciją, pasirinkome lyginti tris siūlomus kelionių tipus: poilsines, pažintines bei egzotines keliones.


#  **PROJEKTO SEKA**


**DATABASE.PY**

**Panaudotos bibliotekos:** requests, pandas, BeautifulSoup

Duomenis pasiėmėme iš internetinių puslapių filtruojant keliones pagal kelionių tipus. Pažymima, kad tarp duomenų pasitaikė atvejų, kai kelionės pasiūlymų yra matomos ir tos kelionės, kurios jau yra su žyma “išparduota” arba kelionės data “Nenurodoma". Pažymime, kad šitos kelionės yra įtrauktos į analizę siekiant įvertinti kelionių agentūrų siūlomas populiariausias kryptis. Tačiau tokių kelionių negalėjome analizuoti pagal keliones datas, kadangi tokia informacijas apie jas nebuvo teikiama.


**ANALYSIS.PY**

**Panaudotos bibliotekos:** Pandas, MatplotLib, SeaBorn, Statistics
1.	Pirmiausia sugrupavome abiejų agentūrų keliones pagal daugiausia pasiūlymų (populiariausios kelionės). Siekiant estetiškai atvaizduoti duomenis, grafike pateikėme  top 10 populiariausių kelionių krypčių ir jų kainos vidurkį.
 ![Vidutinės kelionės kainos pagal TOP 10 šalių](https://github.com/OrintaZv/baigiamasis/assets/157809580/fa361166-00ad-43aa-a19f-3eb0eb44ae70)


2.Suradome pačias brangiausias agentūrų siūlomas keliones top10 .
 ![image](https://github.com/OrintaZv/baigiamasis/assets/157809580/ed3b1cb4-e3c2-4091-a435-61d61c927eee)


3.Sugrupavome duomenis, kokių kelionių procentaliai siūlo agentūros pagal kelionės reitingą.
![image](https://github.com/OrintaZv/baigiamasis/assets/157809580/b4a72243-a312-471f-860c-a93f6c53dac0)



4.Grafike pateikiama informacija apie siūlomas keliones pagal kelionių tipus kiekvienoje agentūroje.
 ![Agentūrų siūlomos kelionės pagal tipus](https://github.com/OrintaZv/baigiamasis/assets/157809580/94231c48-60f0-481b-84e7-214416e572e0)


5.Grafikas atvaizduoja siūlomus kelionių paketus pagal datas.
 ![image](https://github.com/OrintaZv/baigiamasis/assets/157809580/3f4cfb26-2ead-4ae3-b95e-79294c994fa9)


 6.Lyginamasis grafikas, kuriame atsispindi agentūrų kelionių pasiūlymai pagal mėnesius.
 ![Mėnesinis kelionių kiekis pagal agentūras](https://github.com/OrintaZv/baigiamasis/assets/157809580/366ed42c-a94f-4ae0-a0ed-22864448312e)



#  **ANALIZĖS IŠVADOS**


Atlikus Kelionių Svetainių Kainų Palyginimo analizę padarėme išvadą, kad populiariausios kelionės yra poilsinės kelionės. Kelionių agentūros tokių kelionių siūlo daugiausiai. Taip pat galima daryti išvadą, dažniausiai siūlomos kelionės yra 4 ar 5 žvaigždučių įvertinimu. Analizuotose agentūrose šios kelionės sudaro 88 % visų siūlomų kelionių.

Taip pat pažymima, kad populiariausių kelionių kainų vidurkis prasideda nuo 644,27 Eur ir siekia 1826,33 Eur.

Nagrinėjant brangiausių kelionių pasiūlymus galima pastebėti tendencijas, kad brangiausių kelionių kryptys dažniausiai būna egzotinės kelionės.
Analizė rengta 2024m sausio mėnesio pabaigoje, todėl iš agentūrų pateikiamų pasiūlymų galima daryti išvadą, kad daugiausiai pasiūlymų yra artimiausiu metu, t.y. vasario mėnesiui. Taip pat iš grafiko pateikiamos informacijos galime teigti, kad vasaros sezonui yra siūloma mažiau pasiūlymų. Tam turi įtakos sezoniškumas ir tinkamas klimatas atostogoms Lietuvoje.

Pažymima, kad Baltictours kelionių agentūra turi didesnių kelionių pasiūlymų spektrą.
