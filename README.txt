Spravil som python script, trápil som sa s tým na windowse :D (je to postavené na vašom bipartitnom, kvôli parsovaniu)

Spúšťam ho:
python k-colors_sat.py <nazov_suboru_s_grafom> <cislo k>

vráti súbor s rovnakým názvom, no pridá ešte príponu ".cnf"

na overenie som spravil malý skript, ktorý využíva knižnicu pycosat (je potrebné doinštalovať cez pip).

Funguje obdobne:
python sat_solver.py <nazov_suboru_s_cnf>

Vráti SAT, ak nájde riešenie, UNSAT ak nie


Mrzí ma, že tak neskôr v noci, no som nechal pustené overenie na úlohu 2.3. a trvalo to oveľa dlhšie ako som čakal :)

3. graf je najskôr ofarbiteľný pre k=8 (čiže nie je 3 ani 5-ofarbiteľný a 10-ofarbiteľný je určite)


4. graf mi pre k=12 prešiel so stavom SAT, k=10 UNSAT, pre k=11 mi po veľmi dlhej dobe ešte stále nevrátilo výsledok
(asi na výkonnejšom stroji by to zbehlo rozumnejšie ako na obyčajnom noťase)
Odhad: 10 < k <= 12

5. graf pre k=9 ešte UNSAT, k={10, 20, 30, 41} nezbehol, k=42 je SAT
Odhad: 9 < k <= 42