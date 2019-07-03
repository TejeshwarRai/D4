import requests as rq
import threading as tg
import time
lock = tg.Lock()

# print("Started")
#
# class FetchUrl(tg.Thread):
#     def run(self):
#         url1 = "https://www.google.co.in"
#         print("Fetching from url 1")
#         resp1 = rq.get(url1)
#         print(resp1.text)
#
#
# class FetchBook(tg.Thread):
#     def run(self):
#         url2 = "https://www.dell.com"
#         print("Fetching from url 2")
#         resp2 = rq.get(url2)
#         print(resp2.text)
#
#
# urltask = FetchUrl()
# booktask = FetchBook()
#
# urltask.start()
# booktask.start()
#
# for _ in range(10):
#     print(_)

#
#


class Printer:
    def printdocs(self, docname, times):
        lock.acquire()
        for i in range(times+1):
            print(">>Printing {} Copy{}".format(docname, i))
            time.sleep(0.1)
        lock.release()


class Desktop(tg.Thread):

    def attachPrinter(self, printer):
        self.printer = printer

    def run(self):
        self.printer.printdocs("**Learning python.pdf**", 10)


class Laptop(tg.Thread):
    def attachPrinter(self, printer):
        self.printer = printer

    def run(self):
        self.printer.printdocs("**Learning Java.pdf**", 10)


printer = Printer()
desktop = Desktop()
desktop.attachPrinter(printer)
laptop = Laptop()
laptop.attachPrinter(printer)
desktop.start()
laptop.start()
