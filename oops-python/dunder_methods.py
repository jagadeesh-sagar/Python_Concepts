
class Vector:
    def __init__(self, x, y): 
        self.x, self.y = x, y

    def __repr__(self): 
        return f"Vector({self.x}, {self.y})"
    def __add__(self, o):
        return Vector(self.x+o.x, self.y+o.y)
    def __mul__(self, scalar): 
        return Vector(self.x*scalar, self.y*scalar)
    def __rmul__(self, scalar):
        return self.__mul__(scalar) # scalar * v
    def __eq__(self, o): 
        return (self.x, self.y) == (o.x, o.y)
    def __abs__(self):
        return (self.x**2 + self.y**2)**0.5
    def __iter__(self): 
        return iter((self.x, self.y)) # unpack: x,y=v
    def __bool__(self): 
        return abs(self) != 0
    def __hash__(self): 
        return hash((self.x, self.y)) # needed for sets

    
v1, v2 = Vector(1,2), Vector(3,4)
print(v1 + v2) # Vector(4, 6)
print(3 * v1) # Vector(3, 6) — via __rmul__
print(abs(v2)) # 5.0
x, y = v1 # unpacking via __iter__
# {v1, v2} # works — __hash__ defined
