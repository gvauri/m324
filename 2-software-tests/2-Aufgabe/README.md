# Aufgabe 2
Eine Python Klasse Db greift auf eine Datenbank (MongoDb) zu. Die Entität User wird über die Methoden set_user und get_user gespeichert und gelesen. Für die Klasse Db soll ein Integration Test erstellt werden. Im Integration Test wird ein User in die Datenbank gespeichert und wieder von der Datenbank gelesen. Für die Testumgebung wird die Datenbank in einem Container gestartet.

1. Erstelle die Klasse User mit den Fields name und mail.

2. Erstelle die Klasse Db mit folgenden Eigenschaften:
   - Via Konstruktor Parameter wird der Connection String festgelegt.
   - Die Methode set_user erhält als Parameter ein Objekt der Klasse User und speichert diesen in die Datenbank.
   - Die Methode get_user liest einen beliebigen User aus der Datenbank und gibt ihn als Objekt der Klasse User zurück.

3. Erstelle eine Testklasse TestDb , welche einen Integration Test enthält. Dieser speichert via set_user einen User in die Datenbank und liest via get_user den gespeicherten User wieder aus. Um den Test durchzuführen, soll die Datenbank in einem Container gestartet und letztendlich wieder beendet werden. Mit der Library docker können in Python Container gestartet und beendet werden. Für die Library unittest gibt es Methoden, welche die Testumgebung vorbereiten und bereinigen können: setUp, tearDown. Nutze diese Methoden, um den Container zu starten und zu beenden.

4. Erstelle ein Makefile, welches in einem Vorgang die Datenbank in einem Container startet. In einem weiteren Vorgang wird der Integration Test ausgeführt. Nach dem Ausführen des Integration Tests wird der Container wieder beendet.
