import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    user = session["user_id"]

    # Need: current cash, grand total
    current_cash = db.execute("SELECT cash FROM users WHERE id = ?", user)[0]["cash"]
    print("_______", current_cash)
    grand_total = float(current_cash)
    # Need: Holdings with Name, Amount, Price and Total Value


    holdings_database = db.execute("SELECT * FROM holdings WHERE user_id = ?", user)

    holdings = []
    for i, row in enumerate(holdings_database):
        # print(i, row)
        # print("_______________" , lookup(row["stock"])[] ,"amount: ", row["amount"])
        price = lookup(row["stock"])["price"]
        total = price * row["amount"]
        grand_total += total
        holdings.append( {
            "name": row["stock"],
            "amount": row["amount"],
            "price": usd(price),
            "total": usd(total)
        } )
    # print(holdings)

    return render_template("index.html", current_cash = usd(current_cash), grand_total = usd(grand_total), holdings = holdings)


    return apology("TODO")


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        # Create Variables From the form
        stock_request = request.form.get("symbol")
        amount = int(request.form.get("shares"))
        # Check for correct Usage
        if amount < 1 or not isinstance(amount, int):
            return apology("Amount must be a positive int")

        # Lookup the Stonk
        lookup_return = lookup(stock_request)
        price = float(lookup_return["price"])
        if lookup_return is None:
            return apology("Stonks not found")

        # get users money
        bank = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]["cash"]

        # check if money is enough
        total = price * amount
        if total > bank:
            return apology("u dont have enough money for this transaction")
        else:
            # Finish the transaction
            user = session["user_id"]
            stock_symbol = lookup_return["symbol"]

            # Update transactions
            db.execute("INSERT INTO transactions (user_id, stock, amount, buy_price, total, trans_type) VALUES (?, ?, ?, ?, ?, ?)", session["user_id"], lookup_return["symbol"], amount, price, total, "bought")
            # Decrease user Money
            db.execute("UPDATE users SET cash = ? WHERE id = ?", bank-total, user)


            # check if stock is already hold
            check = db.execute("SELECT EXISTS (SELECT * FROM holdings WHERE user_id = ? AND stock = ? LIMIT 1) AS record_exists", user, stock_symbol)

            # either create or upgrade the users current holding
            if check[0]["record_exists"] == 0:
                # holding does not exist
                db.execute("INSERT INTO holdings (user_id, stock, amount) VALUES (?, ?, ?)", user, stock_symbol, amount)
            elif check[0]["record_exists"] == 1:
                # holding exists
                db.execute("UPDATE holdings SET amount = amount + ? WHERE user_id = ? AND stock = ?", amount, user, stock_symbol)
            else:
                return apology("internal server error")

            # Redirect user to home page
            return redirect("/")


    return render_template("buy.html")

    pass
    # return apology("TODO")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    return apology("TODO")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method=="POST":
        stock_request = request.form.get("stock-symbol")
        price = lookup(stock_request)
        if price is not None:
        # print(price["price"], price["symbol"])
            return render_template("quoted.html", name=price["symbol"], price=price["price"])
        else:
            return apology("Stonks not Found")
    else:
        return render_template("quote.html")



@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    username = request.form.get("username")
    if request.method=="POST":
        # Ensure valid username
        if not username:
            return apology("must provide username", 403)

        # already in use?
        querry = db.execute("SELECT username FROM users WHERE username = ?", username)
        if querry != []:
            return apology("Username already in use", 403)


        # Ensure password was submitted
        password = request.form.get("password")
        if not password:
            return apology("must provide password", 403)

        elif not request.form.get("confirm") or not request.form.get("confirm") == password:
            return apology("passwords must match", 403)

        # hash password and insert into db
        hashed_pw = generate_password_hash(password)
        db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", username, hashed_pw )


    # Fallback if no POST, if the button in the navbar was pressed
    return render_template("register.html")

    # return apology("TODO")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    user = session["user_id"]

    if request.method == "POST":
        """Sell shares of stock"""

        stock = request.form.get("symbol")

        # check for corrent amount input, render apology
        try:
            amount = int(request.form.get("shares"))
        except ValueError:
            return apology("amount needs to be positive integer")
        if amount < 1:
            return apology("Amount must be a positive integer")


        query = db.execute("SELECT stock FROM holdings WHERE user_id = ? and stock = ?", user, stock)[0]["stock"]

        # render apology on false Stock input
        if not stock or stock != query:
            return apology("stonk not found in holdings")


        # check if amount of stonk is available
        amount_holdings = db.execute("SELECT amount FROM holdings WHERE user_id = ? and stock = ?", user, stock)[0]["amount"]
        if  int(amount_holdings) < amount:
            return apology("U dont have enough of this stonks")

        # get price and total
        lookup_return = lookup(stock)
        price = float(lookup_return["price"])
        total = price * amount

        # update holdings
        db.execute("UPDATE holdings SET amount = amount - ? WHERE user_id = ? and stock = ?", amount, user, stock)
        # update transactions
        db.execute("INSERT INTO transactions (user_id, stock, amount, buy_price, total, trans_type) VALUES (?, ?, ?, ?, ?, ?)", user, stock, amount, price, total, "sold")
        # update user money
        db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", total, user)

        # Redirect user to home page
        return redirect("/")


    """Display Selling Page"""

    holdings_database = db.execute("SELECT * FROM holdings WHERE user_id = ?", user)

    holdings = []
    for i, row in enumerate(holdings_database):
        holdings.append( {
            "name": row["stock"]
        } )
    return render_template("sell.html", holdings=holdings)
