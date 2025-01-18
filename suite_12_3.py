import unittest
import module_12_2

athleticsTS = unittest.TestSuite()
athleticsTS.addTest(unittest.TestLoader() \
                    .loadTestsFromTestCase(module_12_2.RunnerTest))
athleticsTS.addTest(unittest.TestLoader() \
                    .loadTestsFromTestCase(module_12_2.TournamentTest))
ut_runner = unittest.TextTestRunner(verbosity=2)
ut_runner.run(athleticsTS)