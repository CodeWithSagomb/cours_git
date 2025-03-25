

re_bucket = "kevin"
print(re_bucket)
z = 3+5
print(z)
print("hello world bro")
x = 4
w = 5
B = 23
v = 88
print(x, "", w, "", B, "", v)

student = 24
print(student)
print(12)
# this is a comment
print("hello bro\n")
"this is a comment written in more than just one line"
print("hi christ \n")
x = 3
Name = "christ"
print(Name, "", x)
print(type(Name))
A = 4
a = 4
print(A, "", a)
MyVariableName = "YOYO"
myNickName = "TATO"
print(MyVariableName, '\n', MyVariableName)
q = y = w = 3
print(q, y, w)


fruits = ["apple", "banana", "cherry"]
w, y, z = fruits
print(w)
print(y)
print(z)

x = "awesome"


def myfunc():
    print(x)


myfunc()

eleves = {
    'paul': 12,
    'camille': 8,
    'theo': 17
}

print(eleves.get('lea', 'not_in\n'))

# boucle pour la moyenne
for prenom, note in eleves.items():
    print(f"la moyenne de {prenom} est de {note}/20")


# moyenne de la classe
print(round(sum(eleves.values())/len(eleves)))


students = {
    'sago': {
        'note': 14,
        'mention': 'Bien'
    },
    'carine': {
        'note': 13,
        'mention': 'assez-bien'
    },
    'gloria': {
        'note': 11,
        'mention': 'passable'
    }
}
# Recuperer la note et l'appreciation des students
for student in students:
    print(student, students[student]['note'], students[student]['mention'])

students['lea'] = {
    'note': 10,
    'mention': 'moyenne'
}
print(students)
