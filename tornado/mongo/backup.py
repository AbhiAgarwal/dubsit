from subprocess import call

def runbackup():
    call(["mongoexport", "-h widmore.mongohq.com:10010 -u tornado -ppT3mW49P81u -db Dubsit"])

if __name__ == '__main__':
    runbackup()
