from app import app #imports the flask app object from main application (app.py). The app object contains all the routes (/,health,data) defiend earlier
                    #Does not import test functions, it just gives us access to the app so requests can be simulated

def test_home(): # Defines a test function for '/' route which is the homepage. Pytest automatically detects functions that start with 'test_' and runs them as tests.
                 #This is a unit test for the home route
    client = app.test_client(). # Creates a test client from flask app. Like a simulated web browser or api client. It can send GET/POST requests to your app's routes internally without running a live server.
    response = client.get('/') # Use the test client to send a GET request to the '/' route, This simulates a user visiting your home page.  The response object contains the status code, headers, and body of the response.
    assert response.status_code == 200 # Checks that HTTP response status code is 200 ensuring the application did not crash
    assert b"Flask CI/CD" in response.data # Check that the response body contains the expected text (in bytes),  Flask test client returns response data as bytes, so we use b"..." to compare.
                                           #This ensures that the home route returns the correct message (or part of it).