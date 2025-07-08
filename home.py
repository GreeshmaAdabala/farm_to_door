from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from app import verify_farmer_login, get_db_connection

home = Flask(__name__)
home.secret_key = 'your_secret_key'

@home.route('/')
def homepage():
    return render_template('home.html')

@home.route('/farmer_login', methods=['GET', 'POST'])
def farmer_login():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']

        farmer = verify_farmer_login(name, password)

        if farmer:
            session['farmer_name'] = farmer['name']
            return redirect(url_for('vegetableselection'))
        else:
            return render_template("farmer.html", show_popup=True, popup_message="❌ Invalid name or password!")
    return render_template("farmer.html")

@home.route('/farmer_view_orders')
def farmer_view_orders():
    conn = get_db_connection()
    cursor = conn.cursor()  # ✅

    # Get all customer details
    cursor.execute("SELECT * FROM customer_details")
    customers = cursor.fetchall()

    # Get all customer orders
    cursor.execute("SELECT * FROM customer_order")
    all_orders = cursor.fetchall()

    # Group orders and calculate grand total per customer
    orders_by_customer = {}
    grand_totals = {}

    for order in all_orders:
        name = order['customer_name']
        if name not in orders_by_customer:
            orders_by_customer[name] = []
            grand_totals[name] = 0
        orders_by_customer[name].append(order)
        grand_totals[name] += float(order['total_price'])

    cursor.close()
    conn.close()

    return render_template(
        "vieworders.html",
        customers=customers,
        orders_by_customer=orders_by_customer,
        grand_totals=grand_totals
    )


@home.route('/vegetableselection')
def vegetableselection():
    return render_template('vegetableselection.html')

@home.route('/save_stock', methods=['POST'])
def save_stock():
    data = request.get_json()
    db = get_db_connection()
    cursor = db.cursor()

    farmer_name = session.get('farmer_name')
    cursor.execute("DELETE FROM vegetable_stock WHERE farmer_name = ?", (farmer_name,))


    for item in data:
        cursor.execute("INSERT INTO vegetable_stock (farmer_name, name, price, quantity) VALUES (?, ?, ?, ?)",
        (farmer_name, item['name'], item['price'], item['quantity']))


    db.commit()
    db.close()
    return jsonify({"message": "Stock saved to DB!"})

@home.route('/view_stock')
def view_stock():
    image_map = {
        "Brinjal": "brinjal.jpeg",
        "Cabbage": "cabbage.jpeg",
        "Carrot": "carrot.jpeg",
        "Cauliflower": "cauli.jpg",
        "Cucumber": "cucumber.jpg",
        "Tomato": "tomato.jpeg",
        "CurryLeaves": "curry.jpeg",
        "Drumstick": "drumstick.jpg",
        "IvyGourd": "ivygourd.jpeg",
        "Potato": "potato.jpeg",
        "Ridge Gourd": "ridgegourd.jpg",
        "Spinach": "Spinach.jpeg"
    }

    farmer_name = session.get('farmer_name')
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM vegetable_stock WHERE farmer_name = ?", (farmer_name,))
    vegetable_stock = cursor.fetchall()
    db.close()

    for veg in vegetable_stock:
        veg['image'] = image_map.get(veg['name'], 'default.jpg')

    return render_template('view_stock.html', vegetable_stock=vegetable_stock)

@home.route('/customer_login')
def customer_login():
    return render_template('customer.html')

@home.route('/registration')
def registration_form():
    return render_template('registration.html')

@home.route('/register_customer', methods=['POST'])
def register_customer():
    name = request.form['name']
    phone = request.form['phone']
    alt_phone = request.form['alt_phone']
    email = request.form['email']
    street = request.form['street']
    city = request.form['city']
    pincode = request.form['pincode']
    address = f"{street}, {city} - {pincode}"
    order_type = request.form['order_type']
    payment_method = request.form['payment_method']

    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("""INSERT INTO customer_details (name, phone, alt_phone, email, address, order_type, payment_method)VALUES (?, ?, ?, ?, ?, ?, ?)
""", (name, phone, alt_phone, email, address, order_type, payment_method))

    db.commit()
    db.close()

    session['customer_name'] = name
    session['username'] = name
    return redirect('/customerdashboard')

@home.route('/customerdashboard', methods=['GET', 'POST'])
def customerdashboard():
    if request.method == 'POST':
        username = request.form['username']
        session['username'] = username
        return redirect(url_for('customerdashboard'))

    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM vegetable_stock WHERE quantity > 0")
    vegetable_stock = cursor.fetchall()
    db.close()

    image_map = {
        "Brinjal": "brinjal.jpeg",
        "Cabbage": "cabbage.jpeg",
        "Carrot": "carrot.jpeg",
        "Cauliflower": "cauli.jpg",
        "Cucumber": "cucumber.jpg",
        "Tomato": "tomato.jpeg",
        "CurryLeaves": "curry.jpeg",
        "Drumstick": "drumstick.jpg",
        "IvyGourd": "ivygourd.jpeg",
        "Potato": "potato.jpeg",
        "Ridge Gourd": "ridgegourd.jpg",
        "Spinach": "Spinach.jpeg"
    }

    for veg in vegetable_stock:
        veg['image'] = image_map.get(veg['name'], 'default.jpg')

    username = session.get('username', 'Guest')
    return render_template('customerdashboard.html', username=username, vegetable_stock=vegetable_stock)

@home.route('/orderstock')
def orderstock():
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM vegetable_stock WHERE quantity > 0")
    vegetable_stock = cursor.fetchall()
    db.close()
    image_map = {
        "Brinjal": "brinjal.jpeg",
        "Cabbage": "cabbage.jpeg",
        "Carrot": "carrot.jpeg",
        "Cauliflower": "cauli.jpg",
        "Cucumber": "cucumber.jpg",
        "Tomato": "tomato.jpeg",
        "CurryLeaves": "curry.jpeg",
        "Drumstick": "drumstick.jpg",
        "IvyGourd": "ivygourd.jpeg",
        "Potato": "potato.jpeg",
        "Ridge Gourd": "ridgegourd.jpg",
        "Spinach": "Spinach.jpeg"
    }

    for veg in vegetable_stock:
        veg['image'] = image_map.get(veg['name'], 'default.jpg')

    username = session.get('username', 'Guest')
    return render_template('orderstock.html', vegetable_stock=vegetable_stock)

@home.route('/save_cart', methods=['POST'])
def save_cart():
    cart_data = request.get_json()
    session['cart'] = cart_data
    return jsonify({'status': 'success'})

@home.route('/orderpage')
def orderpage():
    customer_name = session.get('customer_name', 'Customer')
    cart = session.get('cart', [])
    print("DEBUG: Cart in /orderpage:", cart)
    print("DEBUG: Customer in /orderpage:", customer_name)
    return render_template('order.html', customer_name=customer_name, cart_items=cart)
@home.route('/finalize_order', methods=['POST'])
def finalize_order():
    cart = session.get('cart', [])
    customer_name = session.get('customer_name')

    print("DEBUG: Cart =", cart)
    print("DEBUG: Customer =", customer_name)

    if not cart or not customer_name:
        print("❌ Cart or customer_name missing!")
        return jsonify({'status': 'fail', 'message': 'Session expired or missing data'}), 400

    try:
        db = get_db_connection()
        cursor = db.cursor()

        for item in cart:
            veg_id = item['id']
            quantity = float(item['quantity'])

            cursor.execute("SELECT name, price, quantity FROM vegetable_stock WHERE id = ?", (veg_id,))
            result = cursor.fetchone()

            if result and result[2] >= quantity:
                veg_name = result[0]
                price = float(result[1])
                total = price * quantity

                cursor.execute("UPDATE vegetable_stock SET quantity = quantity -? WHERE id = ?", (quantity, veg_id))

                # 👇 Remove veg_id if it's not in your customer_orders table
                cursor.execute("""
                    INSERT INTO customer_order
                    (customer_name, vegetable_name, quantity, price_per_kg, total_price) 
                    VALUES (?,?,?,?,?)
                """, (customer_name, veg_name, quantity, price, total))
            else:
                db.rollback()
                db.close()
                return jsonify({'status': 'fail', 'message': f'Not enough stock for vegetable ID {veg_id}'}), 400

        db.commit()
        db.close()
        session.pop('cart', None)
        return jsonify({'status': 'success'})

    except Exception as e:
        print("❌ Error in finalize_order:", e)
        return jsonify({'status': 'fail', 'message': str(e)}), 500


@home.route('/view_orders')
def view_orders():
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("""
    SELECT 
        customer_name,
        vegetable_name,
        quantity,
        price_per_kg,
        total_price
    FROM 
        customer_order
""")

    orders = cursor.fetchall()
    db.close()
    return render_template('view_orders.html', orders=orders)

