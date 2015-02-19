import webapp
import random


class aleat(webapp.webApp):

    def process(self, parsedRequest):
        randNumber = random.randint(1, 1000000)
        return ('200 OK', "<html><body><p>Hola." +
                          "<a href=" + str(randNumber) + ">Dame otra</a></p>" +
                          "</body></html>")
if __name__ == "__main__":
    testWebApp = aleat("localhost", 1234)
