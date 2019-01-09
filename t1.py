import sys
import time
import platform
from datetime import date
from datetime import datetime
from datetime import timedelta

def main( argv=None ):
    if argv is None:
        argv = sys.argv

    print "[%s] Hello, World!" % __name__

    t2 = datetime.now()
    print "DateTime Now: [%s]" % ( t2.isoformat() )

    print "Python Version: [%s]" % ( platform.python_version() )

    print platform.sys.version

    return 0

if __name__ == "__main__":
    sys.exit( main( sys.argv ) )
    
    
