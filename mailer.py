from marrow.mailer import Mailer, Message

mailer = Mailer(dict(
    transport = dict (
        use = 'smtp',
        host = 'smtp.xx.com',
        username = "username",
        password = "password"
    )
))

positiv = 0
negativ = 0


def sendMail(mail):

    try:
        message = Message(author="mail-from@domain.com", to=mail)


        # mail subject, obviously
        message.subject = "Subject"
        
        # plain text variant:
        message.plain = "Please view this mail with html enabled."
        
        # when pressing "reply", send mail to:
        message.reply = "reply-to@mailadresse.com"
        
        # HTML variant:
        message.rich = """ 
        
        <h1>Header</h1>
        <p>some text</p>

        """

        message.attach(name='path-to-attachment.pdf')

        mailer.send(message)
        print('successfull sent mail to ' + mail)
        return True

    except:
        print('There was an error for mail ' + mail + ", skipping this.")
        return False


tfile = open('kontakte.csv', 'r')

# format this matching to your file 
lines = tfile.readline()
mails = lines.split()

mailer.start()


for mail in mails:
    
    #csv? remove seperator:
    mail = mail.replace("'", "")
    mail = mail.replace(";", "")

    # call method, if true: mail successfully sent
    res = sendMail(mail)
    
    # counter
    if res:
        positiv += 1
    else: 
        negativ += 1



print("____________________")
print("Positiv: " + str(positiv))
print("Negativ: " + str(negativ))


mailer.stop()
