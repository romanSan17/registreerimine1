from module1 import *
from module1 import autoriseerimine

login = None

while True:
    print("1-registreerimine\n2-autoriseerimine\n3-Vahetage volitusi\n4-Saatke e-kiri\n")
    valik=int(input("select action:"))
    if valik == 1:
        existing_logins = registreerimine("TextFile1.txt")
        kirjuta_failisse("TextFile1.txt", existing_logins)
        pass
    elif valik == 2:
        if autoriseerimine("TextFile1.txt"):
            change_data(login, "TextFile1.txt")
        else:
            print(" ")
    elif valik == 3:
        if login:
            change_data(login, "TextFile1.txt")
        else:
            print("Ei saa muuta, sest te pole sisse logitud.")
    elif valik ==4:
        if login:
            sender_email = input("Sisestage oma e-post: ")
            password = input("Sisestage oma parool: ")
            receiver_email = input("Sisestage saaja e-posti aadress: ")
            subject = input("Postituse teema: ")
            content = input("Sisestage tekst: ")
            send_email(sender_email, password, receiver_email, subject, content)
        else:
            print("Logi kõigepealt sisse")

