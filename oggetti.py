class Studente:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
        self.voti = []

    def get_nome(self):
        return f"{self.nome} {self.cognome}"
    
    def add_voto(self,voti):
        self.voti.append(voti)
    
    def get_media(self):
        return sum(self.voti) / len(self.voti)


students = Studente("Carlo", "Testa")

print("nome e cognome: ", students.get_nome())

students.add_voto(28)
students.add_voto(30)
students.add_voto(25)

print(f"Media voti : {students.get_media():.2f}")
