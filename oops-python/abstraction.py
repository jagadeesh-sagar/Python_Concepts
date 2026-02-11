# Abstraction

# Reduce complexity by hiding unnecessary details.

class EmailSerivce:

    def _connect(self):
      print("connecting to email server")

    def _authenticate(self):
       print("Authenticating...")

    def send_email(self):
       self._connect()
       self._authenticate()  # if user sends an email he will never know that this many things happening behind the scenes
       print('Sending email')
       self._disconncet()
    
    def _disconncet(self):
       print("disconnecting from email server..")

eamil=EmailSerivce()
eamil.send_email()
 