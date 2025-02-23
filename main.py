from flask import Flask, request

from expression import Expression

app = Flask(__name__)

@app.route("/", methods=["POST"])
def calculate() -> str:
    posted_content = request.get_json()

    try:
        parsed_content = str(posted_content["expression"])
    except KeyError:
        return "500 Srever Error. Sorry, but server can't parse your expression"
    
    expression = Expression(parsed_content)
    expression.calculate_expression()
    
    return str(expression)

if __name__ == "__main__":
    app.run()
