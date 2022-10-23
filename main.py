import Escola
from pprintpp import pprint as pp

dao = Escola.EscolaDB()

def Professor(nome, idade, area):
    professor1 = {
        'name': nome,
        'age': idade,
        'area': area
    }
    aux = dao.createProfessor(professor1)

def Materia( assunto, horario):
    assunto = 'Computacao Grafica'
    horario = 'Vespertino'
    materia2 = {
    'assunto': assunto,
    'horario': horario
    }
    aux = dao.createMateria(materia2)

def Relacionamento (ano, professor, materia):
    relacionamento = {
        'year':ano
    }
    aux = dao.create_relation(professor, materia, relacionamento)

    pp(aux)

prof1 = Professor('Marcelo', 30, 'Computacao')
prof2 = Professor('Renzo', 30, 'Software')
prof3 = Professor('Chris', 30, 'Software')
prof4 = Professor('Yvo', 40, 'Computacao')

mat1 = Materia('POO', 'Matutino')
mat2 = Materia('CG', 'Vespertino')

Relacionamento(2016, prof1, mat2)

dao.db.close()



                                  

