#  ***Implementare SNMP. Aplicatie demonstrativa.***


## Informații generale
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;***SNMP (Protocol Simplu de Management al Rețelei)*** este un protocol standard de internet folosit pentru monitorizarea și gestionarea dispozitivelor de rețea conectate prin IP. Acesta este folosit pentru comunicarea între routere, switch-uri, firewall-uri, servere, camere CCTV și dispozitive fără fir.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SNMP colectează, organizează și trimite date de la diferite dispozitive pentru monitorizarea rețelei, ajutând la identificarea și izolarea defecțiunilor. Atât punctele finale monitorizate, cât și sistemul de monitorizare se bazează pe acest protocol pentru o comunicare fără probleme.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Astăzi există o mulțime de instrumente de monitorizare a rețelei care utilizează SNMP pentru controlul performanței în timp real. **Exemple**:

- Verificarea temperaturii din camera serverului. 
- Verificare dacă UPS-ul are suficientă energie de rezervă.
- Aflarea performanțelor switch-urilor și routerelor din rețea. 
- Verificare dacă imprimanta de rețea are suficientă hârtie sau cerneală.
  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Majoritatea dispozitivelor de rețea încă susțin SNMP, lucru datorat faptului că acesta poate fi susținut cu o amprentă de resurse foarte mică, în timp ce alte API-uri și protocoale necesită aplicații/biblioteci suplimentare care fac implementarea lor mai dificilă. În plus față de echipamentele de rețea, SNMP este susținut și de sistemele de operare mai vechi, cum ar fi Open VMS și OS/400. 

## Arhitectura protocolului
![snmp arhitectura](https://github.com/TUIASI-AC-IoT/proiectrcp2023-echipa-7-2023/assets/121617664/9c577e56-6512-4165-ac53-a76bf6f2256c)

### SNMP Agent
  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Un ***agent SNMP*** este un software care rulează pe dispozitivele de rețea și este *responsabil pentru monitorizarea și colectarea datelor de la dispozitivele de rețea locale*. Acesta preia datele de la dispozitivele de rețea locale și le traduce într-o formă care poate fi înțeleasă de către managerul SNMP. Când managerul trimite o cerere, agentul răspunde cu informațiile solicitate din MIB-ul local.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Agentul SNMP este, de asemenea, responsabil pentru trimiterea de trap-uri SNMP către manager atunci când detectează evenimente sau stări importante, cum ar fi o defecțiune sau o situație critică. Aceste trap-uri sunt utilizate pentru a notifica managerul cu privire la problemele de rețea care necesită atenție imediată. Astfel, agentul SNMP joacă un rol important în asigurarea monitorizării și gestionării eficiente a dispozitivelor de rețea.

![snmp agent](https://github.com/TUIASI-AC-IoT/proiectrcp2023-echipa-7-2023/assets/121617664/ee658b98-7354-4967-9b47-cd951dccc806)


### SNMP Manager

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;***Managerul SNMP*** _inițiază cereri către agenți de rețea pentru a colecta informații despre performanță și stare_. Acesta poate interoga diferite obiecte gestionate într-un dispozitiv pentru a obține datele necesare pentru monitorizarea și analiza rețelei.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Managerul SNMP este conceput pentru a colecta date de la dispozitivele de rețea monitorizate și a furniza informații esențiale administratorilor de rețea. De asemenea, acesta poate seta valori în dispozitivele de rețea, cum ar fi configurarea parametrilor de funcționare sau schimbarea anumitor setări. Prin ascultarea trap-urilor SNMP, managerul poate răspunde rapid la evenimente și erori importante care apar în rețea.


### Management Information Base (MIB)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;***MIB***-ul este _o bază de date și un fișier text ASCII care este partajat între un agent SNMP și un manager SNMP_. MIB-ul este o colecție de obiecte gestionate structurate în mod ierarhic într-o structură de tip arbore. Obiectele gestionate vin sub forma unor obiecte scalare cu o singură instanță sau obiecte cu mai multe instanțe (cum ar fi o tabelă).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Fiecărui obiect gestionat i se atribuie un _OID unic_ pentru a-l diferenția de alte obiecte**. OID-ul este, în esență, o etichetă numerică care acționează ca o adresă. Formatul este următorul: 1.3.6.1.1.4.1.2682.1

![pozica](https://github.com/TUIASI-AC-IoT/proiectrcp2023-echipa-7-2023/assets/121617664/38318509-18ef-41af-ab7e-2cd719211278)


## Comunicarea stratificată a SNMP

1. ***Stratul de aplicație***: Folosește protocolul SNMP, generează un mesaj Get pentru a interoga un agent pentru un OID specific.
2. ***Stratul de transport***: Folosește protocolul UDP, identifică destinația portului managerului pentru răspunsul agentului și portul la care ar trebui să asculte agentul.
3. ***Stratul Internet***: Folosește protocolul IP, adaugă adresele de acces media și adresele IP ale managerului SNMP și agentului.
4. ***Stratul interfeței de rețea***: 10BaseT, Verifică media de acces și transferă pachetul la agent.

![stratificare](https://github.com/TUIASI-AC-IoT/proiectrcp2023-echipa-7-2023/assets/121617664/2e82f29f-a232-4d67-b172-195f8e8d0268)


## UDP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;***User Datagram Protocol*** este un _protocol la nivelul transportului de date în rețelele de calculatoare_. Acesta este un protocol fără conexiune, ceea ce înseamnă că nu necesită stabilirea unei conexiuni între expeditor și destinatar înainte de transferul de date. Este utilizat pentru trimiterea de pachete de date în mod neordonat și nu asigură confirmarea primirii acestora sau corectitudinea lor.


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Transferurile de mesaje SNMP au loc prin protocolul de datagrame utilizator (UDP). Protocoalele de securitate a stratului de transport (TLS) sau de securitate a stratului de datagrame de transport (DTLS) sunt uneori utilizate.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Managerii comunică cu agenții prin porturi SNMP desemnate. _Se utilizează atât portul 161 (utilizat de către dispozitivele de rețea SNMP pentru a primi solicitări de interogare și pentru a trimite răspunsuri către manager), cât și portul 162 (utilizat pentru a trimite trap-uri SNMP de la dispozitivele de rețea către manager)._

![udp](https://github.com/TUIASI-AC-IoT/proiectrcp2023-echipa-7-2023/assets/121617664/db31c6a3-6403-44ae-aa11-dc3510cdbdb5)


## Comenzi SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Transferurile de mesaje SNMP au loc prin protocolul de datagrame utilizator (UDP). Protocoalele de securitate a stratului de transport (TLS) sau de securitate a stratului de datagrame de transport (DTLS) sunt uneori utilizate.

![comenzi](https://github.com/TUIASI-AC-IoT/proiectrcp2023-echipa-7-2023/assets/121617664/d48e3158-b245-43fd-b918-c089f311d375)


* ***Get*** - Managerul folosește acest mesaj pentru a interoga valorile din MIB ale unui agent SNMP.
* ***GetNext*** - Managerul folosește acest mesaj pentru a prelua valoarea următoarei OID în arbore. Este adesea folosit pentru a parcurge o serie de OID-uri.
* ***GetResponse*** - Agentul folosește acest mesaj pentru a răspunde la o cerere Get, GetNext sau Set de la Manager.
* ***Set*** - Managerul folosește acest mesaj pentru a comanda unui agent să schimbe valoarea unui obiect gestionat.
* ***TRAP*** - Agentul folosește acest mesaj pentru a raporta evenimente problematice. Este o informație nesolicitată trimisă către manager pentru a notifica un eveniment specific, o stare anormală a dispozitivului. Acesta este un mesaj unidirecțional care nu necesită o confirmare de la manager. _Acționează ca notificări care informează SNMP atunci când are loc ceva important_, cum ar fi supraîncălzirea unui dispozitiv.

![COMMMMM](https://github.com/TUIASI-AC-IoT/proiectrcp2023-echipa-7-2023/assets/121617664/a085f332-131e-4b39-9857-cb13736e2d4d)


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Figura de mai sus arată comunicarea între elementele de rețea gestionate prin SNMP și Manager pentru trimiterea mesajelor de tip trap și informărilor.  Trap-ul este trimis doar o dată și, de asemenea, este eliminat odată ce este trimis. Nu sunt păstrate în memorie pentru a primi un răspuns de la Manager. 


## ASN.1

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;În SNMP, ***ASN.1 (Abstract Syntax Notation One)*** este un _limbaj standard de descriere a interfeței pentru definirea structurilor de date care pot fi serializate și deserializate într-un mod compatibil cu mai multe platforme_. Este utilizat pe scară largă în telecomunicații și protocoale de rețea informatice. 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;În SNMP, UDP (Protocol Data Unit) este unitatea de bază a informațiilor care sunt schimbate între managerii și agenții SNMP. Acesta conține informațiile necesare pentru gestionarea dispozitivelor de rețea. Tipurile de date UDP definite în ASN.1 pentru SNMP permit reprezentarea structurată a datelor schimbate între manager și agent, asigurând interoperabilitatea între diferite sisteme și implementări.


## Diagrama de secvență 
> (diagrama este atașată si separat)

![SNMPdiagrama](https://github.com/TUIASI-AC-IoT/proiectrcp2023-echipa-7-2023/assets/121617664/74d5e0e6-61e3-4500-8fd4-159f963a8f83)
