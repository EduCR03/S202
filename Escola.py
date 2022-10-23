from db.database import Graph

class EscolaDB(object):
    def __init__(self):
        self.db = Graph(uri='bolt://35.173.187.96:7687',user='neo4j', password='board-apparatuses-smashes' )
                       
    def createProfessor(self, professor):
        return self.db.execute_query('CREATE (n:Professor{name:$name, age:$age, area:$area}) return n',{'name': professor['name'], 'age': professor['age'], 'area':professor['area']})

    def createMateria(self, materia):
        return self.db.execute_query('CREATE (n:Materia {assunto:$assunto, horario:$horario}) return n',{'assunto': materia['assunto'], 'horario': materia['horario']})
                                     
    def read_by_name(self, professor):
        return self.db.execute_query('MATCH (n:Person {name:$name}) RETURN n',{'name': professor['name']})
                                     
    def read_all_nodes(self):
        return self.db.execute_query('MATCH (n) RETURN n')

    def update_age(self, professor):
        return self.db.execute_query('MATCH (n:Person {name:$name}) SET n.age = $age RETURN n',{'name': professor['name'], 'age': professor['age'], 'area':professor['area']})
                                     
    def delete(self, professor):
        return self.db.execute_query('MATCH (n:Person {name:$name}) DELETE n',{'name': professor['name']})
                                     
    def delete_all_nodes(self):
        return self.db.execute_query('MATCH (n) DETACH DELETE n')

    def create_relation(self, professor, materia, year):
        return self.db.execute_query('MATCH (p:Professor {name:$name}), (m:Materia {assunto:$assunto}) CREATE (n)-[r:KNOWS{year: $year}]->(m) RETURN p, r, m',{'name': professor['name'], 'assunto': materia['assunto'], 'year': year})
                                     
    def read_relation(self, professor, materia):
        return self.db.execute_query('MATCH (p:Person {name:$name})-[r]->(m:materia {assunto:$assunto}) RETURN p, r, m', {'name':professor['name'], 'assunto': materia['assunto']})

