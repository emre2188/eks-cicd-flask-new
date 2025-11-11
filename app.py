from flask import Flask, jsonify # imports two core objects from the flask library: Flask: the main class used to create your web app instance.jsonify: a helper function that formats Python data (like dicts) into proper JSON HTTP responses.

app = Flask(__name__) #Creates an instance of the Flask class. The special variable __name__ tells Flask where to look for templates, static files, and configuration.


@app.route('/') # A decorator that registers a route — in this case, the root URL (/).
def home(): #Defines a Python function called home that runs when the / route is accessed.
    return jsonify({"message": "Welcome to the Flask CI/CD APP is working !"}) 

@app.route('/health') #Registers another route /health
def health(): #Defines the function tied to the /health route.
    return jsonify({"status": "healthy"}) 

@app.route('/data') #Creates a route /data that returns some mock statistics
def data(): #Defines the function for the /data route.
    sample_data = {"users": 10, "visits": 25, "uptime": "99.9%"} # small dictionary with values
    return jsonify(sample_data) #Return Json


if __name__ == "__main__": #Checks if this file is being run directly (e.g., python app.py) instead of being imported as a module
    app.run(host="0.0.0.0", port=5000) #Starts Flask’s built-in web server on port 5000, listening on all network interfaces (0.0.0.0).
