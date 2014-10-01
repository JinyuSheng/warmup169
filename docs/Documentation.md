\mainpage

CS169 Warmup Project is a project designed as a quick tutorial for building and deploying a web app for students in the CS169 class.
The implementation documented here does not use any web framework, but is otherwise fully functional.
The tests included with this implementation can be used as functional and acceptance tests for other implementations as well.

The description for this project is at: https://docs.google.com/document/d/1iHroF22fABIIzGV8pRypRcg0Oh0-5PiTugOpzWfsrT8


Installation
-------------

  - Unpack the loginCounterWarmup.tar.gz.

Running the server
------------------
   - You need to have python 2.x (>= 2.7) installed

             python server.py

     - this will run a web server on port 5000 on localhost

   - To run unit tests for the mock server backend:

              make unit_tests

      - This will run the unit tests specified in serverTest.TestUsers
      - These unit tests are specific to the way the mock server is implemented. You will have to
        write your own unit tests using the conventions of the framework you are using.

   - Functional testing is done against a deployed backend. The file
     testSimple.py contains some examples of functional tests, using the code
     in testLib.py. You can see that these tests send HTTP requests to a given
     url (default, http://localhost:5000) and verify that the backend deployed
     at that url implements the required protocol. 

            # start a server
            python server.py
            make func_tests

       - This will issue requests to localhost:5000 and will check the results
       - The actual test specification are collected from all the test*.py files in the
        current directory (using Python standard unittest framework)
       - By default we are giving you the test in testSimple.TestUnit (the same tests as the serverTest.TestUsers
         unit tests but executed through the HTTP api), and testSimple.TestAddUser

       - To run functional tests against some other running backend

             # start your backend, e.g., on Heroku at myapp.herokuapp.com
             make func_tests TEST_SERVER=myapp.herokuapp.com

       - the TEST_SERVER environment variable can be set to the hostname:port for
          the server to test (defaults to localhost:5000)
       - We will grade your project by running these tests, the tests you will provide in testAdditional,
         and other tests too.


Writing more tests
-------------------

  - You should write more functional tests, in Python, following the model of the
    tests in testSimple.py. Put your tests in a file "testAdditional.py"
    next to testSimple.py. The "test" prefix of the name is required by the unittest
    framework, the rest is a requirement of our grading script.

