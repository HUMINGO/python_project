#
import unittest
# from Unitestcase.testcase01 import Testcase01
# from Unitestcase.testcase02 import Testcase02
# from Unitestcase.testcase03 import Testcase03
#
# #套件的运用
# case_01 = unittest.TestLoader().loadTestsFromTestCase(Testcase01)
# case_02 = unittest.TestLoader().loadTestsFromTestCase(Testcase02)
# case_03 = unittest.TestLoader().loadTestsFromTestCase(Testcase03)
#
# suite = unittest.TestSuite([case_01, case_02, case_03])
# unittest.TextTestRunner().run(suite)

import os

case_path = os.getcwd()

# print(case_path)
discover = unittest.defaultTestLoader.discover(case_path)

unittest.TextTestRunner().run(discover)
# print(discover)





