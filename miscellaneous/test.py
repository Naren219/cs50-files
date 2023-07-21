        username = request.form.get("username")
        symbol = db.execute("SELECT symbol FROM portfolio WHERE username = ?", username)
        name = db.execute("SELECT name FROM portfolio WHERE username = ?", username)
        shares = db.execute("SELECT shares FROM portfolio WHERE username = ?", username)
        price = db.execute("SELECT price FROM portfolio WHERE username = ?", username)
        TOTAL = db.execute("SELECT TOTAL FROM portfolio WHERE username = ?", username)

        return render_template("index.html", symbol=symbol, name=name, shares=shares, price=price, TOTAL=TOTAL)