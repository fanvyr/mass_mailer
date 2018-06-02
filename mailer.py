from marrow.mailer import Mailer, Message

mailer = Mailer(dict(
    transport = dict (
        use = 'smtp',
        host = 'smtp.1und1.de',
        username = "username",
        password = "password"
    )
))

positiv = 0
negativ = 0


def sendMail(mail):

    try:
        message = Message(author="mail-from@domain.com", to=mail)


        message.subject = "Betreff"
        message.plain = "Bitte aktivieren Sie HTML um diese Mail lesen zu können oder sehen Sie sie alternativ in ihrem Webbrowser an."
        message.reply = "reply-to@mailadresse.de"
        message.rich = """ 
        
        <h1>Überschrift</h1>

        """

        message.attach(name='Einladung_QuantiSana-Heilpraxis_Zahnmedizin.pdf')
        message.attach(name='Kontakt.vcf')
        message.attach(name='Termin.ics')
        #message.embed(name='image001.jpg')


        mailer.send(message)
        print('successfull sent mail to ' + mail)
        return True

    except:
        print('There was an error for mail ' + mail + ", skipping this.")
        return False


tfile = open('kontakte.csv', 'r')
lines = tfile.readline()
mails = lines.split()

mailer.start()


for mail in mails:
    mail = mail.replace("'", "")
    mail = mail.replace(";", "")

    res = sendMail(mail)

    if res == True:
        positiv += 1
    else: 
        negativ += 1



print("____________________")
print("Positiv: " + str(positiv))
print("Negativ: " + str(negativ))


mailer.stop()