import smtplib,ssl

def read_creds():
    user = passw = ""
    with open ("credentials.txt", "r") as f:
        file = f. readlines()
        user = file[0].strip()
        passw = file[1].strip()
    
    return user, passw

port = 465
sender, password = read_creds()


with open('teks.txt','r') as file_x:
    penerima = file_x.readlines()[0]


receive = penerima

subject = input(str("Tulis Subject:" ))
body = input(str("Tulis Body:" ))
msg = f'Subject:{subject}\n\n{body}'


context = ssl.create_default_context()
print("starting to send")
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender,password)
    server.sendmail(sender, receive, msg)

print("email sended")
