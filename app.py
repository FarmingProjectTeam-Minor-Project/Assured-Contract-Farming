from flask import Flask, render_template, redirect, url_for
from database import create_tables

app = Flask(__name__)
app.secret_key = "secretkey"

# Create tables (future use)
create_tables()


# ---------------- HOME ----------------
@app.route("/")
def home():
    return render_template("home.html")


# ---------------- GUEST PAGES ----------------

@app.route("/how-it-works")
def how_it_works():
    return render_template("how_it_works.html")


@app.route("/features")
def features():
    return render_template("features.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


# ---------------- AUTH (DUMMY FOR NOW) ----------------
# Abhi sirf pages open honge, logic baad me aayega

@app.route("/login")
def login():
    return render_template("auth/login.html")


@app.route("/register")
def register():
    return render_template("auth/register.html")


# ---------------- MAIN ----------------
if __name__ == "__main__":
    app.run(debug=True)
