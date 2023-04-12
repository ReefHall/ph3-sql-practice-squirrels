from lib import CONN, CURSOR

class Squirrel:

    def __init__(self, name, num_acorns, rabid, id = None):
        if(isinstance(name, str) and 1 <= len(name) < 15 ):
            self._name = name
        else:
            print("Name must be string, and greater 1 and less than 15 charcaters")
        self.num_acorns = num_acorns
        self.rabid = rabid
        self.id =id

    def __repr__(self):
        return f"<Squirrel id={self.id} name={self.name} num_acorns={self.num_acorns} rabid={self.rabid}>"

    # build your name property here
    def get_name(self):
        return self._name
    def set_name(self, name):
        if(isinstance(name, str) and 1 <= len(name) < 15 ):
            self._name = name
        else:
            print("Name must be string, and greater 1 and less than 15 charcaters")

    name = property(get_name,set_name)

    def create(self):
        sql = """ INSERT INTO squirrels (name, num_acorns, rabid)
           VALUES (?,?,?)   """
        CURSOR.execute(sql,[self._name, self.num_acorns,self.rabid])
        CONN.commit()
        self.id = CURSOR.execute("SELECT id FROM squirrels ORDER BY id DESC").fetchone()[0]
            
    def update(self):
        sql = """ UPDATE squirrels SET name = ?, num_acorns = ?, rabid = ? WHERE id = ? """
        CURSOR.execute(sql, [self._name, self.num_acorns, self.rabid, self.id])
        CONN.commit()

    def save(self):
        if(self.id):
            self.update()
        else:
            self.create()
        

    @classmethod
    def query_all(cls):
        sql = "SELECT * FROM squirrels"
        squirrels = CURSOR.execute(sql).fetchall()
        squirrels_list =[]
        for data in squirrels:
            squirrel = Squirrel(data[1], data[2], data[3])
            squirrel.id = data[0]
            squirrels_list.append(squirrel)
        return squirrels_list

        

    @classmethod
    def query_rabid(cls):
        sql = "SELECT * FROM squirrels WHERE rabid = ?"
        squirrels = CURSOR.execute(sql,[True]).fetchall()
        squirrels_list =[]
        for data in squirrels:
            squirrel = Squirrel(data[1], data[2],data[3])
            squirrel.id = data[0]
            squirrels_list.append(squirrel)
        return squirrels_list

    @classmethod
    def query_most_acorns(cls):
        sql = "SELECT * FROM squirrels ORDER BY num_acorns DESC"
        squirrel_data = CURSOR.execute(sql).fetchone()
        squirrel = Squirrel(squirrel_data[1], squirrel_data[2], squirrel_data[3])
        squirrel.id = squirrel_data[0]
        return squirrel
        
