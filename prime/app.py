from flask import Flask

app = Flask(__name__)

# @app.route('/')
# def home():
#     return "Enter a number in the URL like /5 to check if it's prime"

@app.route('/<int:n>')
def prime(n):
    if n < 2:
        return f"{n} is not a prime number"
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return f"{n} is not a prime number"
    
    return f"{n} is a prime number"

if __name__ == '__main__':
    app.run(debug=True)