import sched, time
import urllib2
from HTMLParser import HTMLParser
import sendEmail
import os, sys, time




class MLStripper(HTMLParser):
    findDivAfter = False
    foundData = False

    def handle_starttag(self, tag, attrs):
        if tag == 'tr':
            for name, value in attrs:
                if name == 'data-section-id' and value == '50382':
                    MLStripper.findDivAfter = True
        if MLStripper.findDivAfter:
            if tag == 'div':
                MLStripper.foundData = True
    def handle_data(self, data):
        if MLStripper.foundData:
            if data != "160 of 160":
                emailtest.notificateMe("new spot")
            # else:
            #     emailtest.notificateMe("no change")

            MLStripper.foundData = False
            MLStripper.findDivAfter = False

def checkForChange():
    request = urllib2.Request('http://classes.usc.edu/term-20163/course/phys-151')

    try:
        response = urllib2.urlopen(request) # Make the request
        htmlString = response.read()
        checker = MLStripper()
        checker.feed(htmlString)
    except urllib2.URLError, e:
        print e.args
        print "error"





def do_something(sc):
    print "checking"
    checkForChange()
    sc.enter(5, 1, do_something, (sc,))


def startTack():
    s = sched.scheduler(time.time, time.sleep)
    s.enter(5, 1, do_something, (s,))
    s.run()


def main():
    startTack()

if __name__ == "__main__":
    main()
