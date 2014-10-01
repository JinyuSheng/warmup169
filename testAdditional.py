"""
Each file that starts with test... in this directory is scanned for subclasses of unittest.TestCase or testLib.RestTestCase
"""

import unittest
import os
import testLib

class TestUnit(testLib.RestTestCase):
    """Issue a REST API request to run the unit tests, and analyze the result"""
    def testUnit(self):
        respData = self.makeRequest("/TESTAPI/unitTests", method="POST")
        self.assertTrue('output' in respData)
        print ("Unit tests output:\n"+
               "\n***** ".join(respData['output'].split("\n")))
        self.assertTrue('totalTests' in respData)
        print "***** Reported "+str(respData['totalTests'])+" unit tests. nrFailed="+str(respData['nrFailed'])
        # When we test the actual project, we require at least 10 unit tests
        minimumTests = 10
        if "SAMPLE_APP" in os.environ:
            minimumTests = 4
        self.assertTrue(respData['totalTests'] >= minimumTests,
                        "at least "+str(minimumTests)+" unit tests. Found only "+str(respData['totalTests'])+". use SAMPLE_APP=1 if this is the sample app")
        self.assertEquals(0, respData['nrFailed'])


        
class TestAddUser(testLib.RestTestCase):
    """Test adding users"""
    def assertResponse(self, respData, count = 1, errCode = testLib.RestTestCase.SUCCESS):
        """
        Check that the response data dictionary matches the expected values
        """
        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count']  = count
        self.assertDictEqual(expected, respData)

#Correct sign up credentials
    def testAdd1(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        self.assertResponse(respData, count = 1)

#empty password is fine
    def testAdd2(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user2', 'password' : ''} )
        self.assertResponse(respData, count = 1)        

#empty username should not work
    def testAdd3(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : '', 'password' : 'emptyusername'} )
        self.assertResponse(respData, None, testLib.RestTestCase.ERR_BAD_USERNAME)
#duplicate username
    def testAdd4(self):
        self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'duplicateusername'} )
        self.assertResponse(respData, None, testLib.RestTestCase.ERR_USER_EXISTS)

#Long username
    def testAdd5(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'toolongausernameihavenoideawhatitisbutithastobeover128charactersisitlongenoughnowtoolongausernameihavenoideawhatitisbutithastobeover128charactersisitlongenoughnow', 'password' : 'password'} )
        self.assertResponse(respData, None, testLib.RestTestCase.ERR_BAD_USERNAME)
#Long password
    def testAdd6(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'duplicatepassword', 'password' : 'toolongausernameihavenoideawhatitisbutithastobeover128charactersisitlongenoughnowtoolongausernameihavenoideawhatitisbutithastobeover128charactersisitlongenoughnow'} )
        self.assertResponse(respData, None, testLib.RestTestCase.ERR_BAD_PASSWORD)
#Successul login, count = 2
    def testLogin1(self):
        self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        self.assertResponse(respData, 2, testLib.RestTestCase.SUCCESS)
#Successul login, count = 10
    def testLogin2(self):
        self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        self.makeRequest("/users/login", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        self.makeRequest("/users/login", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        self.makeRequest("/users/login", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        self.makeRequest("/users/login", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        self.makeRequest("/users/login", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        self.makeRequest("/users/login", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        self.makeRequest("/users/login", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        self.makeRequest("/users/login", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        self.assertResponse(respData, 10, testLib.RestTestCase.SUCCESS)
#Unsuccessful login b/c wrong password
    def testLogin3(self):
        self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : 'user1', 'password' : 'wrongpassword'} )
        self.assertResponse(respData, None, testLib.RestTestCase.ERR_BAD_CREDENTIALS)
#empty username
    def testLogin4(self):
        self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : '', 'password' : 'password'} )
        self.assertResponse(respData, None, testLib.RestTestCase.ERR_BAD_USERNAME)
#username too long
    def testLogin5(self):
        self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : 'toolongausernameihavenoideawhatitisbutithastobeover128charactersisitlongenoughnowtoolongausernameihavenoideawhatitisbutithastobeover128charactersisitlongenoughnow', 'password' : 'password'} )
        self.assertResponse(respData, None, testLib.RestTestCase.ERR_BAD_USERNAME)
#empty password should be fine
    def testLogin6(self):
        self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : ''} )
        self.makeRequest("/users/login", method="POST", data = { 'user' : 'user1', 'password' : ''} )
        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : 'user1', 'password' : ''} )
        self.assertResponse(respData, 3, testLib.RestTestCase.SUCCESS)
#empty username
    def testLogin7(self):
        self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : '', 'password' : 'password'} )
        self.assertResponse(respData, None, testLib.RestTestCase.ERR_BAD_USERNAME)

#See if the login fails after resetFixture
    def testReset(self):
        self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        self.makeRequest("/TESTAPI/resetFixture", method="POST", data = {})
        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        self.assertResponse(respData, None, testLib.RestTestCase.ERR_BAD_CREDENTIALS)





