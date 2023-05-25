from database.some_model import Data
from database.create_db import Session 


import random
import string





def generate_random_string(length: int) -> str:
    '''Генерирование строки'''

    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string




def send_data(some_str: str) -> None:
    '''Запись в БД'''

    session = Session()
    count = session.query(Data).count()
    if count >= 30:
        
        session.query(Data).delete()

    date = Data(some_str=some_str)
    session.add(date)
    session.commit()
    session.close()








