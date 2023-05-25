from database import db
from send_data import send_data, generate_random_string
from time import sleep




def start_script():

    db.sql_start()

    while True:
        some_str = generate_random_string(16)
        send_data(some_str)
        sleep(2)





if __name__ == '__main__':

    start_script()

