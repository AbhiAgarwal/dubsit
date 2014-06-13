from subprocess import call

def runbackup():
    call(["mongoexport", "-h localhost -u -p -db "])

if __name__ == '__main__':
    runbackup()
