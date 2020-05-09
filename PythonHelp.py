
Static Typing in Python

https://medium.com/@ageitgey/learn-how-to-use-static-type-checking-in-python-3-6-in-10-minutes-12c86d72677b
https://realpython.com/python-type-checking/

def circumference(radius: float) -> float:
    return 2 * math.pi * radius
    
major: str='Tom' # type:str, this comment is no longer necessary
pi: float = 3.142

----------------------------

from typing import List, Tuple, Dict
l: List[int] = [1, 2, 3]
t1: Tuple[float, str, int] = (1.0, 'two', 3)
t2: Tuple[int, ...] = (1, 2.0, 'three')
d: Dict[str, int] = {'uno': 1, 'dos': 2, 'tres': 3}


-------------------------------------------


from typing import Union
l2: List[Union[int, float]] = [1, 2.0, 3]


------------------------------------------

from typing import Callable
my_func: Callable[[int, str], str] = foo

--------------------------------

Using Comments for Static Typing

def circumference(radius):
    # type: (float) -> float
    return 2 * math.pi * radius
    
def headline(text, width=80, fill_char="-"):
    # type: (str, int, str) -> str
    return f" {text.title()} ".center(width, fill_char)
    
# headlines.py

def headline(
    text,           # type: str
    width=80,       # type: int
    fill_char="-",  # type: str
):                  # type: (...) -> str
    return f" {text.title()} ".center(width, fill_char)
    






