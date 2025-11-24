# Eine Applikation in C++ soll kompilliert werden. Bei erfolgreicher Kompillierung soll das ausführbare Programm mittels Dockerfile in ein Docker Image kopiert werden. Wird der Container ausgeführt, startet das C++ Programm.

1. Schreibe eine Applikation in C++, welche den Text Programmed in C++; Compiled by g++; Builded by make; Executed in a Container ausgibt.

2. Erstelle das dazugehörige Dockerfile. Es soll auf debian basieren und das kompillierte File a.out im Image ausführen.

3. Erstelle das Makefile, welches das Programm kompilliert und den Container erstellt.

4. Stelle sicher, dass das ausführbare File a.out gelöscht wird, wenn der Container erstellt wurde.

5. Erstelle ein Target clean, welches das Docker Image löscht.
