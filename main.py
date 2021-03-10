from Enigma import Enigma
import string
if __name__ == '__main__':
    test = Enigma()
    message_to_deliver = test.encript('kalosha','wza')
    test.decript(message_to_deliver)