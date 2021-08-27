from flask import Flask, render_template



# Create a Flask Instance
app = Flask(__name__)

# Create a route decorator
@app.route('/', methods = ['GET'])
def index():
  first_name = "John"
  stuff = "This is the text"

  favorite_pizza = ['Pepperoni', 'Cheese', 'Mushroom', 41]
  return render_template('index.html', first_name = first_name, stuff = stuff, favorite_pizza = favorite_pizza)

@app.route('/user/<name>')
def user(name):
  return render_template('user.html', username = name)

@app.errorhandler(404)
def page_not_found(err):
  return render_template("404.html"), 404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(err):
  return render_template("500.html"), 500


# App execution
if __name__ == "__main__":
  app.run(debug=True)

