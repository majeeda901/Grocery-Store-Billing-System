#---Database Connection---
import mysql.connector as db

conn = db.connect(
    host="localhost",
    user="root",
    password="Majeeda901@",
    database="grocery"
)

cur = conn.cursor()

cart = []


#---Admin----
def Add_products(cur,conn):
    #---Id Inputs--- 
    try:
        prd_id = int(input("enter product id: "))
        cur.execute("select prd_id from product_info where prd_id = %s",(prd_id,))
        r = cur.fetchone()        
        #---Product id validation---
        if r:
            print("❌Product ID already exists!")
            return
        #---Inputs---
        prd_qty = float(input("enter product weight: "))
        prd_in_stock = int(input("enter product stock: "))
        org_prd_price = int(input("enter product original price: "))
        sell_prd_price = int(input("enter ur product price: "))
        prd_name = input("enter product name: ")
        #---Insert into database---
        query = "insert into product_info values (%s, %s, %s, %s, %s, %s)"
        values = (prd_id, prd_name, prd_qty, prd_in_stock, org_prd_price, sell_prd_price)
        cur.execute(query,values)
        conn.commit()
        print("Product added successfully")
    except Exception as e:
        print("Error:",e)


def Remove_products(cur,conn):
    #---remove values DB---
    try:
        del_inp = int(input("enter the product id you want to delete"))
    except:
        print("Invalid input")
        return
    #---Remove from database--- 
    query = "delete from product_info where prd_id = %s"
    values = (del_inp,)
    cur.execute(query,values)
    conn.commit()
    print("Product deleted successfully")
   

def Modify_products(cur,conn):
    #---Get inputs---
    try:
        prd_id = int(input("Enter product id you want to update: "))
        new_price = int(input("Enter new price of the product: "))
        new_stock = int(input("Enter new quantity of the product: "))
    except:
        print("Invalid input")
        return
    #---Update in DB---
    query = """
        UPDATE product_info 
        SET sell_prd_price = %s, prd_in_stock = %s 
        WHERE prd_id = %s"""
    values = (new_price, new_stock, prd_id)
    cur.execute(query, values)
    conn.commit()
    print("Product updated successfully")


def Revenue(cur):
    #---Getting total amount---
    cur.execute("select sum(total_amount) from bills")
    res = cur.fetchone()
    if res[0] is None:
        print("Total Revenue: 0")
    else:
        print("Total Revenue:", res[0])


def Itemized_profit(cur,conn):
    #---Profit by item from DB---
    query = """select prd_name,(sell_prd_price - org_prd_price)
            as profit from product_info            
            """
    cur.execute(query)
    data = cur.fetchall()
    print("\n---Itemized Profit---")
    print("\n"+"-"*40)
    #---Header---
    print(f'{"Product Name":<30}{"Profit":<10}')
    print("-"*40)
    for item in data:
        print(f"{item[0]:<30} {item[1]:<10}")
    print("-"*40)

    
def Total_bills(cur, conn):
    #---Total bills---
    cur.execute("SELECT COUNT(*) FROM bills")
    total_bills = cur.fetchone()[0]
    print("\nTotal Bills Generated:", total_bills)
    print("\n--- Products Sold Summary ---")
    print("-"*70)
    query = """select p.prd_name,sum(bi.qty) as total_qty,
           sum(bi.total) as total_amount from bill_items bi
           join product_info p on bi.prd_id = p.prd_id
           group by p.prd_name
           order by total_qty desc;"""
    cur.execute(query)
    data = cur.fetchall()
    print(f"{'Product':<25}{'Total Qty':<15}{'Total Sales':<15}")
    print("-"*70)
    for name, qty, amount in data:
        print(f"{name:<25}{qty:<15}{amount:<15.2f}")
    print("-"*70)


def View_user_details(cur, conn):
    print("\n--- Customer Details with Purchased Items ---")
    print("\n" + "-"*80)
    query = """select c.cusmr_id,c.cusmr_name,c.mobile,b.bill_id,p.prd_name,
            bi.qty,bi.prd_price, bi.total from customer_info c
            join bills b on c.cusmr_id = b.cusmr_id
            join bill_items bi on b.bill_id = bi.bill_id
            join product_info p on bi.prd_id = p.prd_id
            order by c.cusmr_id, b.bill_id;"""
    cur.execute(query)
    data = cur.fetchall()
    current_customer = None
    for row in data:
        cusmr_id, name, mobile, bill_id, prd_name, qty, price, total = row
        #---Customer header---
        if current_customer != cusmr_id:
            print("\n" + "="*80)
            print(f"Customer ID: {cusmr_id} | Name: {name} | Mobile: {mobile}")
            print("="*80)
            print(f"{'Bill ID':<10}{'Product':<20}{'Qty':<5}{'Price':<10}{'Total':<10}")
            print("-"*80)
            current_customer = cusmr_id
        #---Product details---
        print(f"{bill_id:<10}{prd_name:<20}{qty:<5}{price:<10.2f}{total:<10.2f}")
    print("-"*80)


def Total_products(cur, conn):
    #---Total products---
    query = "select * from product_info"
    cur.execute(query)
    data = cur.fetchall()
    
    #---Header---
    print(f"{'ID':<3} {'Product Name':<25} {'Qty':<6} {'Stock':<6} {'Cost':<6} {'Price':<6}")
    print("-" * 65)

    #---Products---
    for item in data:
        print(f"{item[0]:<3} {item[1]:<25} {item[2]:<6} {item[3]:<6} {item[4]:<6} {item[5]:<6}")
    
#---Admin block---
def admin_access():
    while True:
        print(" \n 1.Add products \n 2.Remove products \n 3.Modify products \n 4.Itemized profit \n 5.Revenue \n 6.Total bills \n 7.View user details \n 8.Total products \n 9.exit \n")
        try:
            inp = int(input('enter the an option from above: '))
        except:
            print("Invalid input")
            continue
        
        if inp == 1:
            Add_products(cur,conn)
        elif inp == 2:
            Remove_products(cur,conn)
        elif inp == 3:
            Modify_products(cur,conn)
        elif inp == 4:
            Itemized_profit(cur,conn)
        elif inp == 5:
            Revenue(cur)
        elif inp == 6:
            Total_bills(cur,conn)
        elif inp == 7:
            View_user_details(cur,conn)
        elif inp == 8:
            Total_products(cur,conn)
        elif inp == 9:
            print("exit from admin page")
            break
       
#---Admin login---        
def Admin_page():
    if input("enter the password: ") == "admin123":
        admin_access()
    else:
        print("Invalid password")
        Admin_page()


#---Customer block---
#---Add to cart---
def Add_to_cart(cur,conn):
    #---Customer input---
    try:
        prd_id = int(input("enter product id to add: "))
        P_qty = float(input("enter quantity: "))
    except:
        print("Invalid input")
        return
    #---getting data from DB---
    query = "select * from product_info where prd_id = %s"
    values = (prd_id,)
    cur.execute(query,values)
    data = cur.fetchone()
    #--- if data not found---
    if not data:
        print("Product not found")
        return
    prd_id = data[0]
    prd_name = data[1]
    prd_qty = data[2]
    prd_in_stock = data[3]
    org_price = data[4]
    sell_prd_price = data[5]
    #---If required products less than stock---
    if P_qty > prd_in_stock:
        print("Not enough stock available")
        return
    #---Calculate total---
    total = sell_prd_price * P_qty
    cart.append((prd_name,P_qty,sell_prd_price,total,prd_id))
    print("Added to cart successfully")

#---Remove from cart---
def Remove_from_cart(cur,conn):
    if Empty_Cart():
        return
    View_cart()
    #---Remove input from cart---
    try:
        r_inp = int(input("enter product Id to remove: "))
    except:
        print("Invalid Id")
        return

    for item in cart:
        if item[4] == r_inp:
            #---Item removed---
            cart.remove(item)
            print("Product removed")
            return
    print("Product not found in cart")


#---Modify cart---    
def Modify_from_cart(cur,conn):
    if Empty_Cart():
        return
    View_cart()
    #---Modify input---
    try:
        m_inp = int(input("enter Product Id to modify: "))
        m_qty = float(input("Enter quantity: "))
    except:
        print("Invalid inputs")
        return
    for i in range(len(cart)):
        if cart[i][4] == m_inp:
            prd_name = cart[i][0]
            #---get data from DB---
            query = "select sell_prd_price, prd_in_stock from product_info where prd_id=%s"
            cur.execute(query,(m_inp,))
            res = cur.fetchone()
            if not res:
                print("Product not found in DB")
                return
            price, stock = res
            if m_qty > stock:
                print("Not enough stock available")
                return
            #--Calculate total after modified---
            total = price * m_qty
            cart[i] = (prd_name, m_qty, price, total, m_inp)
            print("Cart updated")
            return
    print("Product not found in cart")


#---empty cart---
def Empty_Cart():
    if not cart:
        print("cart is Empty")
        return True
    return False

#---view cart---
def View_cart():
    if Empty_Cart():
        return    
    else:
        print("\n---Cart---")
        print("\n" + "-"*70)
        #---Header---
        print(f'{"Product Name":<30}{"Quantity":<10}{"Price":<10}{"Total":<10}{"Product Id":<10}')
        print("-"*70)
        for item in cart:
            prd_name, qty, price, total, prd_id = item            
            #---Cart printing---
            print(f'{prd_name:<30}{qty:<10}{price:<10}{total:<10}{prd_id:<10}')
        print("-"*70)
    
#---Bill---
def Bill(cur, conn):
    if Empty_Cart():
        return
    cusmr_name = input("Enter customer name: ")
    mobile = input("Enter mobile no: ")
    #---Insert customer---
    cur.execute(
        "insert into customer_info (cusmr_name, mobile) values (%s, %s)",
        (cusmr_name, mobile))
    conn.commit()
    cusmr_id = cur.lastrowid
    #---Calculate total bill---
    grand_total = sum(item[3] for item in cart)
    #---Insert into bills table---
    cur.execute(
        "insert into bills (cusmr_id, total_amount) values (%s, %s)",
        (cusmr_id, grand_total))
    conn.commit()
    bill_id = cur.lastrowid 
    # ---- PRINT BILL ----
    print("\n" + "=" *40)
    print("        GROCERY STORE SYSTEM")
    print("=" *40)
    print(f"{'Name':<30}{'Qty':<5}{'Price':<10}{'Total':<10}")
    print("-" *40)
    #---Insert into bill_items---
    for item in cart:
        name, qty, price, total, prd_id = item
        cur.execute(
            """insert into bill_items 
               (bill_id, prd_id, qty, prd_price, total)
               values (%s, %s, %s, %s, %s)""",
            (bill_id, prd_id, qty, price, total))
        print(f"{name:<30}{qty:<5}{price:<10}{total:<10}")
        #---Update stock---
        cur.execute(
            "update product_info set prd_in_stock = prd_in_stock - %s where prd_id = %s",
            (qty, prd_id))
    conn.commit()
    print("-" *40)
    print(f"GRAND TOTAL: ₹{grand_total}")
    print("=" *40)
    cart.clear()
    print("Order completed successfully ✅")
    print("Thank You🙏")
    print("Visit Again🙏")
        
#---Search product---
def Search_product(cur,conn):
    #---search input---
    s_name = input("Enter product name: ")
    #---get the search data from DB---
    query = "select * from product_info where prd_name like %s"
    cur.execute(query,("%"+s_name+"%",))
    data = cur.fetchall()
    #---if data not found---
    if not data:
        print("No product found")
        return
    #---print the search result---
    print("\n----Search Results----\n")
    for item in data:
        print(f"ptd_id: {item[0]} | prd_name: {item[1]} | prd_qty: {item[2]} | prd_in_stock: {item[3]} | sell_prd_price: {item[5]}")
    #---Ask customer to add search to cart---
    choice = input("Do you want add the product in cart? (y/n): ")
    if choice.lower() == "y":
        Add_to_cart(cur,conn)
    
#---Customer---    
def Customer_order():
    while True:
        print('\n 1.Add Product \n 2.Remove \n 3.Modify \n 4.Cart \n 5.Bill \n 6.Search_product \n 7.Exit \n')
        try:
            ch=int(input("enter the an option from above: "))
        except:
            print("Invalid Choice")
        if ch == 1:
            Total_products(cur,conn)
            Add_to_cart(cur,conn)
        elif ch == 2:
            Remove_from_cart(cur,conn)
        elif ch == 3:
            Modify_from_cart(cur,conn)
        elif ch == 4:
            View_cart()
        elif ch == 5:
            Bill(cur,conn)
        elif ch  == 6:
            Search_product(cur,conn)
        elif ch  == 7:
            print("Exiting")
            break


#---Main Menu---       
def main_menu():
    while True:
        print("\n 1.Admin \n 2.Customer \n 3.Exit \n")
        try:
            inpt = int(input("enter the an option from above: "))
        except:
            print("Invalid input")
            continue
        if inpt == 1:
            Admin_page()
        elif inpt == 2:
            Customer_order()
        elif inpt == 3:
            print('<-----Exiting----->')
            break

#---Calling---
main_menu()
