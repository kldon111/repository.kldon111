import sys

print "we are here",sys.argv
import os,inspect
def module_path(local_function):
   ''' returns the module path without the use of __file__.  Requires a function defined 
   locally in the module.
   from http://stackoverflow.com/questions/729583/getting-file-path-of-imported-module'''
   return os.path.abspath(inspect.getsourcefile(local_function))
def main():
   pass # do stuff

global __modpath__
__file__ = module_path(main)
print __file__
######################################


######################################
dpath = os.path.abspath(__file__)
THISPLUG = os.path.dirname(dpath).split('Kodi')[0]+'/Kodi'
Kodi_drive=THISPLUG[:2]
THISPLUG =Kodi_drive+ "/winKodi/Kodi"
log_file=Kodi_drive+'/winKodi/tmp/Kodi_log'
log_file1=Kodi_drive+'/winKodi/tmp/Kodi_log1'
xbmclog_file=Kodi_drive+'/winKodi/tmp/xbmclog.txt'

#############################################


from os import listdir as os_listdir
import sys
import os
dpath = os.path.abspath(__file__)

scripts =THISPLUG+"/scripts"
for name in os_listdir(scripts):
       if "script." in name:
               fold = scripts + "/" + name + "/lib"
               sys.path.append(fold)
#############################################
def trace_error():
                  import sys,traceback
                  traceback.print_exc(file = sys.stdout)
                  traceback.print_exc(file=open(xbmclog_file,"a"))

try:
    sys.argv[0]=sys.argv[0].replace("wsyspath.py","default.py")
    sys.modules["__main__"].__file__=sys.argv[0]

    print "wsyspath",sys.argv[2]
    sys.argv[2]=sys.argv[2].replace('"','')
    print "wsyspath",sys.argv[2]
    
    import default
    
except:
    trace_error()



