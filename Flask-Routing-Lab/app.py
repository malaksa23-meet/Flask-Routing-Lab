from flask import Flask, redirect, request, render_template, url_for


app = Flask(__name__,
    template_folder='templates',  
    static_folder='static' 
    )

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/product')
def product():
    return render_template("product.html")


@app.route('/cart ')
def cart ():
    return render_template("cart.html")





if __name__ == "__main__": 
    app.run(debug=True)
