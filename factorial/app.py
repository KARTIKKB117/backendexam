from flask import Flask  

app = Flask(__name__)  

# Route for the home page  
# @app.route("/")  
# def home():  
#     # Message asking user to enter a number in the URL  
#     return "Please add a number to the URL, like /5 or /10"  

# Route that accepts an integer from the URL  
@app.route("/<int:n>")  
def factorial(n):  
    # Calculate factorial  
    fact = 1  
    for i in range(1, n + 1):  
        fact *= i  

    
    return f"Factorial of {n} is: {fact}"  


if __name__ == '__main__':  
    app.run(debug=True)  