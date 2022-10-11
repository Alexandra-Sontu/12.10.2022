#1
from random import randint
a=randint(0,100)
b=randint(0,100)
print(f"Suma numerelor {a} si {b} este {a+b}")
print(f"Diferenta numerelor {a} si {b} este {a-b}")
print(f"Diferenta  numerelor {b} si {a} este {b-a}")
print(f"Produsul numerelor {a} si {b} este {a*b}")
#2
from random import randint
v=[]
for i in range(10):
    for i in range(5):
        v.append(randint(1,36))
    print(v)
    v.clear()
#3
from random import randint
nr=48*randint(3,19)
print(nr)


#4
from random import randint as rand
intrebari=[
    ["Biologie",
    "Care este cel mai mare organ al corpului uman?"#Piele
    "Câte oase are un om adult?"#206
    "Heterocromia duce la ce schimbare a aspectului fizic?"#Ochi diferiti de culoare
    "Boala Crohn face parte din ce grup de boli?"#Boala inflamatorie a intestinului
    "Termenul „renal” se referă la ce organe?"#Rinichi
    "Care este numele celei mai mari părți a creierului uman?"#Cerebelul
    "Se pot găsi pereții celulari în celulele vegetale, celulele animale sau ambele?"#Celulele vegetale
    "Cine a descoperit penicilina?"#Alexander Fleming
    "În ce an a fost clonat primul animal?"#1996
    "Boala Hansen este mai frecvent cunoscută sub ce nume?"#Lepra 
    ],
    ["Geografie",
    "Care este cel mai lung fluviu din Europa?",#Volga
    "Care oraș a fost ținta tuturor cruciadelor?",# Ierusalim
    "Ce tip de lac este Lacul lezer?",#glaciar
    "Care este capitala Islandei?",#Reykjavik;
    "Cum se numeau coloniștii din ținuturile nedescoperite ale Americii? ",# Pionierii
    "Câte state are Statele Unite ale Americii?",#50 state
    "Ce zonă din New York este pe insulă?",#7  Manhattan
    "Cum se numește cel mai mare oraș din China?",#8 Shanghai
    "Cu ce state se învecinează Statele Unite ale Americii?",#Mexic si Canada
    "Care este capitala Romaniei?",#10 Bucuresti
    ],
    ["Matematica",
    "Câte laturi are un hexagon?"#6
    "Cu cât este egală rădăcina pătrată din 144?"#12
    "Cu cât este egal 3 la pătrat?"#9
    "Câte fețe pătrate are un cub?"#6
    "28 – 9 = ?"#19
    "Cu cât este egal 5 la puterea 0?"#1
    "Care este denumirea perimetrului unui cerc?"#circumferinta
    "Care este următorul număr prim după 7?"#11
    "21 ÷ 7 = ?"#3
    "Ce formă 2D are 3 laturi?"#triunghi
    ],
    ["Istorie",
    "În ce an s-a născut Regele Mihai I?",#1921 
    "Ce grad de rudenie este între Carol al II-lea și Ferdinand I?",#Ferdinand I este tatăl lui Carol al II-lea;
    "În ce țară s-a născut Adolf Hitler?"#Austria
    "În ce oraș au fost executați soții Ceaușescu?"#Targoviste
    "În ce an a reușit Mihai Viteazul unirea celor trei mari țări medievale?" #1600
    "Când a avut loc Primul Război Mondial?"#1914-1918 
    "În ce an a intrat România în Uniunea Europeana?"#2007 
    "În ce an a murit Prințesa Diana?"#1997 
    "Ce naționalitate are Papa Francisc I?"#argentiniana 
    "În ce an s-a proclamat independența de stat a României?"#1877
    ],
    ["Animale",
    "Cine pe vremuri în Rusia era numit mistreț?",# Vier
    "Cum l-au numit respectuos locuitorii Siberiei ursul brun?",# Detinatorul la Taiga
    "Cine se numește Toptygin în basmele rusești?",# Urs
    "Cum se numea calul preferat al lui Petru I?",# Lisetta
    "Ce animal rus a devenit simbolul Jocurilor Olimpice XXII organizate la Moscova în 1980?",# Ursuletul Misa
    "Ce pasăre se numește „cântăreața câmpurilor rusești”?",# alarcă
    "Rinocerul are coarne care sunt făcute din ce?",# Par
    "Cât timp își digeră mâncarea un leneș?",# Doua saptamani
    "Lemurii sunt originari dintr-o singură țară, care este?",# Madagascar
    "Care este singurul șarpe veninos din Marea Britanie?",# Sumator
    ]
    
    ]
raspunsuri=[["","Piele","206","ochi diferiti de culoare","boala inflamatorie a intestinului","rinichi","cerebel","celule vegetale","Alexander Fleming","1996","lepra"],
            ["","Volga", "Ierusalim", "glaciar", "Reykjavik","Pionierii" ,"50 state", "Manhattan", "Shanghai", "Mexic si Canada", "Bucuresti"],
            ["","6 ","12","9","6","19","1","circumferinta","11","3","triunghi"],
            ["","1921","Ferdinand I este tatal lui Carol al II-lea ","Austria","Targoviste","1600","1914-1918","2007","1997","argentiniana","1877"],
            ["","Vier","Detinatorul la Taiga","Urs","Lisetta","Ursuletul Misa","Alarcă","Păr","Doua saptamani","Madagascar","Sumator"],
]
def milionar():
    n=0
    tema=rand(0,4)
    intrebare=rand(1,10)
    intrebarile_puse=[]
    print("Tema:",intrebari[tema][0])  
    while n<10:
        n+=1
        while intrebare in intrebarile_puse:
            intrebare=rand(1,10)
        intrebarile_puse.append(intrebare)
        print(intrebari[tema][intrebare]) 
        input("Pentru a afla raspunsul tastati Enter")
        print(raspunsuri[tema][intrebare])
        print("\n")
    return print("Sfarsitul jocului!")
milionar()
