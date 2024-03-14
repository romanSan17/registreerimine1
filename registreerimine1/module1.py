import smtplib
import ssl
from email.message import EmailMessage

def registreerimine(fail: str) -> list:
    """Funktsioon tagastab loetelu kasutajaloginidest
    param str fail: faili nimi, kust andmed loetakse
    """
    f = open(fail, 'r', encoding="utf-8")
    logins = []
    for rida in f:
        login, _ = rida.strip().split(":")
        logins.append(login)
    f.close()
    return logins


def kirjuta_failisse(fail: str, existing_logins=[]):
    """Funktsioon registreerib kasutaja
    param str fail: faili nimi, kuhu andmed salvestatakse
    """
    with open(fail, 'a', encoding = "utf-8") as f:
        n = int(input("Sisestage kasutajate arv: "))
        for i in range(n):
            while True:
                login = input(f"Sisestage kasutaja login {i + 1}: ")
                if login not in existing_logins:
                    break
                else:
                    print("Selline kasutajanimi on juba kasutusel. Palun valige teine kasutajanimi.")
            password = input(f"Sisestage kasutaja parool {i + 1}: ")
            f.write(f"{login}:{password}\n")
    print("Te olete registreerunud.")
    

def autoriseerimine(fail: str) -> bool:
    """Funktsioon kontrollib kasutaja volitusi
    param str fail: faili nimi, kuhu andmed salvestatakse
    return: True - edukalt, False - ei
    """
    global login
    login = input("Sisestage kasutajanimi: ")
    password = input("Sisestage parool: ")
    
    with open(fail, 'r', encoding = "utf-8") as f:
        for line in f:
            stored_login, stored_password = line.strip().split(":")
            if login == stored_login and password == stored_password:
                print("Te olete edukalt sisse loginud")
                return True
        print("Vale kasutajanimi või parool")
        return False
    

def change_data(login: str, fail: str):
    """Funktsioon võimaldab kasutajal muuta sisselogimist või parooli
    """
    print("1-Vaheta login\n2-Vaheta parool\n")
    choice = int(input("mida soovite muuta: "))

    if choice == 1:
        new_login = input("Sisestage uus sisselogimine: ")
        with open(fail, 'r', encoding = "utf-8") as f:
            lines = f.readlines()

        with open(fail, 'w', encoding = "utf-8") as f:
            for line in lines:
                stored_login, stored_password = line.strip().split(":")
                if stored_login == login:
                    f.write(f"{new_login}:{stored_password}\n")
                else:
                    f.write(line)
        print("Sisselogimine on muudetud")
    elif choice == 2:
        new_password = input("Sisestage uus parool: ")
        with open(fail, 'r', encoding = "utf-8") as f:
            lines = f.readlines()

        with open(fail, 'w', encoding = "utf-8") as f:
            for line in lines:
                stored_login, stored_password = line.strip().split(":")
                if stored_login == login:
                    f.write(f"{stored_login}:{new_password}\n")
                else:
                    f.write(line)
        print("Parool muudetud")
    else:
        print("valige 1 või 2")
        
def send_email(sender_email: str, password: str, receiver_email: str, subject: str, content: str):
    """Funktsioon saadab sõnumeid
    """
    smtp_server = "smtp.gmail.com"
    port = 587

    msg = EmailMessage()
    msg.set_content(content)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    context = ssl.create_default_context()
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.send_message(msg)
        print("Kiri saadetud!")
    except Exception as e:
        print("Viga ", e)
    finally:
        server.quit()




