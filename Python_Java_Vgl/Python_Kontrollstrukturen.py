# von funktionen spricht man, wenn sie Außerhalb von Klassen sind, in Klassen von Methoden Deshalb in Python: Funktionen


alter : int = 18; # : int ... Hints (werden nicht von Python, sondern vom Editor berücksichtigt)
                   # Python... dynamische Typisierung

if alter < 18:
    print("Nicht volljährig"); #  ";" optional in Python
else:
    print("Volljährig"); 


# dynamische Typisierung: Python entscheidet selbst, welchen Datentyp eine Variable hat, je nachdem was ihr zugewiesen wird
# Python kann auch im Laufe des Programms den Datentyp ändern, sollte das erforderlich sein
#   z.B.: die Variable ist intern zuerst ein Integer, wird dann größer als 2^32 => Python macht Integer größer
zahl = 20; 
x = 0

# while: 
while x < zahl : 
    x += 1 

# do-while in Python gibt es nicht, kann aber durch while mit break simuliert werden
while True:
    x +=1 
    if x >= zahl:
        break

# Schleifen ähnlich zu foreach in java, können auch eine "else" verzweigung haben
y = [1, 2, 3, 4, 5]
for n in y:
    if n > 0:
        print("positive zahl: ", n)
        break
else:
    print("negative zahlen: ", n)


# pass ... leerer Platzhalter für funtkionen 
if(True):
    pass

# Funktionen (mit def Funktionsname)
def addition(a, b) -> int: # -> int ... hint (rückgabewert)
    return a + b


# break (ident zu Java)
while zahl < 10:
    zahl += 1
    if zahl == 5:
        break
    print(zahl)

# try-except
try:
    zahl = int("Hallo")
except ValueError:          #except ist wie catch in Java
    print("keine Zahl.")


# del: es wird nie "gelöscht", sondern Überschrieben (automatische Speicherbereinigung in Python: Garbage Collector)
# andere Sprachen (zb C) haben keinen Garbage Collector, können dadurch aber ca 10% schneller sein

#Prozessse und Threads:
# Prozesse sind unabhängig voneinander (haben eigenen Speicher), Threads teilen sich den Speicher und sich Prozessen untergeordnet

#Python: funktionale und objektorientierte Programmierung möglich, aber keine echte funktionale Programmierung (wie zB Haskell)

# Interpretor Sprache / Compiler Sprache
# Python ist eine Interpretor Sprache, der Code wird Zeile für Zeile ausgeführt
# Compiler Sprachen (zB C) werden erst in Maschinensprache übersetzt und dann ausgeführt

# Iterativ und rekursiv
# Iterativ: Schleifen (while, for)
# Rekursiv: Funktion ruft sich selbst auf und endet erst durch break

#Instanz und Referenz:
# Instanz: Objekt, das von einer Klasse erzeugt wird
# Referenz: Variable (bzw. Verweis), mit der auf ein Objekt zugegriffen werden kann (mehrere Referenzen können auf ein Objekt zeigen)

# Referenzzähler & garbage Collection
# Referenzzähler: zählt wie viele Referenzen auf ein Objekt zeigen
# garbage Collection: Wenn der Zähler 0 ist, wird das Objekt gelöscht (garbage collection)
