
print("hello world")
print("je m'appelle CHRIST\n")
if 5 > 2:
    print("Five is Equal to Two")
print("great")

# comment can be used to explain python code
# comments can be used to make python code more readable

"""this is a comment written in more than one line"""
# Variables are containers for storing data Values
x = 4
print(x)
x = 5
print(x, "\n")

w1 = 34
w2 = 23.45
w3 = "G"
w4 = "christ sagombaye"

print(w1, w2, w3, w4)

Q1 = str(3)
Q2 = float(23)
print(Q1, Q2)
print(type(Q1))
print(type(Q2))
print(w4)
My_variable_name = "christ sagombaye is the boss"
print(My_variable_name)

Q, W, R, T = "banana", "fruit", 123, 23.45

print(Q, W, R, T)

x = t = z = t = "Orange"

print(x, t, z, t)

T = ["ct", 34, 12.3, "christ"]
print(T)

print(Q + W, R)

x = "awesome"


def myFunct():
    print("python is ", x)


myFunct()
y = None
print(y)

tpl = ("apple", "banana", "cherry")
# tpl[1] = "ftr"
print(tpl[1])
t = range(10)
print(t)

my_dic = {
    "TCD": "N'djamena",
    "CMR": "Yaoundé",
    "SNG": "Dakar",
    "ALG": "Alger",
    "pays": {"Mali": "Bamako", "Benin": "Porto_Novo"},
    "Soudan": "Darfour"
}
print(my_dic, "\n")

a = 2000
b = 123
if b > a:
    print("b is greater than a")
else:
    print("a is greater than b")


bool(12)


def meteo(temp):
    match temp:
        case 0:
            print("foid")
        case 30:
            print("tiede")
        case 50:
            print("Chaud")


meteo(0)


def mention(point) -> float:
    if point < 10:
        print("sous moyen")
    elif point >= 10 and point < 11:
        print("moyen")
    elif point >= 11 and point < 12:
        print("passable")
    elif point >= 12 and point < 14:
        print("assez bien")
    elif point >= 14 and point < 16:
        print("bien")
    elif point >= 16 and point <= 20:
        print("EXCELLENT")
    else:
        print("not valide")


mention(12)
mention(3.4)
mention(13.45)
mention(17.5)
mention(19.67)
mention(45)

liste = [23, "CHRIST", 23.56, 0, "T", 23, 45]
liste1 = [23, 45, 1, 56, 78]

print(len(liste))
print(liste[0:7:2], "\n")
print(liste[-1:-8:-2], "\n")
print(liste)
liste.append("sagombaye")
liste.append(100)
liste.append(123.56)

liste.extend(liste1)
print(liste)
liste.remove(100)

print(liste[:])
print(liste.index("sagombaye"))

tab = []
tab = ["hi", "hello"]
for i in range(23, 50, 2):
    tab.append(i)
print(tab)

tab2 = ["python", "est", "un", "language", "incroyable"]
resultat = " ".join(tab2)
print(resultat)


tab3 = "this is a test string"


tabb = ["string1", "string 2", "string 3"]  # example of tab being a list.


tt = [23, 45, 65, 23, 12, 56, 2, 2]
print(tt)
