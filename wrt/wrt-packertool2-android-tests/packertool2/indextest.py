#!/usr/bin/env python

import unittest
import os, sys, commands
import comm

class TestPackertoolsFunctions(unittest.TestCase):
     
    def test_index1(self):
        comm.setUp()
        cmd = "python %smake_apk.py --package=org.hello.world --name=world --arch=%s --mode=%s --app-root=%s --app-local-path=%s" % \
        (comm.Pck_Tools, comm.ARCH, comm.MODE, comm.APP_PATH, comm.INDEX_PATH[0])
        packstatus = commands.getstatusoutput(cmd)
        if packstatus[0] == 0:
            print "Generate APK ----------------> OK!"
            result = commands.getstatusoutput("ls")
            self.assertIn(comm.AppName, result[1])
        else:
            print "Generate APK ----------------> Error!"
            result = commands.getstatusoutput("ls")
            self.assertNotIn(comm.AppName, result[1])
        os.remove(comm.AppName)

    def test_index2(self):
        comm.setUp()
        cmd = "python %smake_apk.py --package=org.hello.world --name=world --arch=%s --mode=%s --app-root=%s --app-local-path=%s" % \
        (comm.Pck_Tools, comm.ARCH, comm.MODE, comm.APP_PATH, comm.INDEX_PATH[1])
        packstatus = commands.getstatusoutput(cmd)
        if packstatus[0] == 0:
            print "Generate APK ----------------> OK!"
            result = commands.getstatusoutput("ls")
            self.assertIn(comm.AppName, result[1])
        else:
            print "Generate APK ----------------> Error!"
            result = commands.getstatusoutput("ls")
            self.assertNotIn(comm.AppName, result[1])
        os.remove(comm.AppName)

    def test_index3(self):
        comm.setUp()
        cmd = "python %smake_apk.py --package=org.hello.world --name=world --arch=%s --mode=%s --app-root=%s --app-local-path=%s" % \
        (comm.Pck_Tools, comm.ARCH, comm.MODE, comm.APP_PATH, comm.INDEX_PATH[2])
        packstatus = commands.getstatusoutput(cmd)
        if packstatus[0] == 0:
            print "Generate APK ----------------> OK!"
            result = commands.getstatusoutput("ls")
            self.assertIn(comm.AppName, result[1])
        else:
            print "Generate APK ----------------> Error!"
            result = commands.getstatusoutput("ls")
            self.assertNotIn(comm.AppName, result[1])
        os.remove(comm.AppName)

if __name__ == '__main__':  
    unittest.main()  
