from flask import Flask 
 
app = Flask(__name__) 
 
# @app.route("/") 
# def home(): 
#     return "Please add a number to the URL, like /5 or /10" 
 
@app.route("/<int:n>") 
def fibonacci(n): 
    fibs = "First " + str(n) + " Fibonacci numbers: " 
 
    fib1, fib2 = 0, 1 
 
    for i in range(n): 
        fibs += str(fib1) + ", " 
        fib1, fib2 = fib2, fib1 + fib2 
 
    return fibs 
 
if __name__ == '__main__': 
    app.run(debug=True)