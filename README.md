Cerinta:
Creati o clasa abstracta numita Gradinita care sa mosteneasca clasa ABC (abstract base class) si sa aiba urmatoarele metode:

activitate_practica()
ora_de_somn()

Corpul primei metode va fi “pass” iar corpul celei de-a doua metode va contine un raise NotImplementedError (estimeaza cineva ce inseamna acest raise NotImplementedError?). 

Fiecare din cele doua metode vor avea decoratorul @abstractmethod (ce este un decorator?)

Implementati doua clase: GradinitaPublica si GradinitaPrivata care sa implementeze (mosteneasca) clasa abstracta Gradinita. 

Prima clasa, GradinitaPublica va rescrie ambele metode in felul urmator:
activitate_practica() va printa pe ecran: “copiii invata sa deseneze”
ora_de_somn() va printa pe ecran: “copiii trebuie sa doarma la ora cinci”

A doua clasa, GradinitaPrivata va rescrie o singura metoda in felul urmator:
activitate_practica() va printa pe ecran: “copiii invata sa modeleze cu plastilina”

Rulati codul. Se intampla ceva? 
Instantiati un obiect din clasa GradinitaPublica si rulati codul. Se printeaza ceva pe ecran? De ce? 
Apelati metoda activitate_practica() si rulati codul. Ce observati? 
Instantiati un obiect din clasa GradinitaPrivata si rulati codul. De ce va da eroare? Cum putem sa rezolvam eroarea?
Creati o noua clasa: GradinitaPublica25 care sa mosteneasca clasa GradinitaPublica. 
Implementati doar una din metode in felul urmator:
activitate_practica() va printa pe ecran: “Copiii se joaca in curte pe balansoar”

Instantiati un obiect din clasa GradinitaPublica25.
Prin intermediul obiectului instantiat apelati metodele activitate_practica() si ora_de_somn(). 
Ce se printeaza pe ecran? De ce putem sa apelam si metoda somn? 
ENCAPSULARE
In interiorul clasei GradinitaPublica25 creati trei atribute: unul public, unul private si unul protected. 



Prin intermediul obiectului instantiat din clasa apelati pe rand: atributul public, atributul private si respectiv pe cel protected. Care din cele trei sunt sugerate atunci cand scriem numele obiectului instantiat urmat de caracterul “.”?



Rulati codul. Accesarea caruia dintre atribute returneaza eroare?



Implementati in interiorul clasei GradinitaPublica25 un getter, un setter si un deleter pentru atributul private. Cum ne putem folosi de acestia pentru accesarea acestui atribut in afara clasei?
