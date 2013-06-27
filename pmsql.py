import sqlite3
conn = sqlite3.connect('password.db')
c = conn.cursor()

print "Welcome to the password manager"
print "1: Enter a new account"
print "2: Retrieve a password"
print "3: Delete an account"
print "4: Change a Passowrd"
print "5: View all Passwords"
sel = raw_input("Enter your Selection: ")
if sel == '1':
	acc = raw_input("Enter the account name: ")
	pw = raw_input("Enter the password: ")
	c.execute('INSERT INTO PW VALUES (?,? )', (acc, pw))
	conn.commit()
	conn.close()

if sel == '2':
	acc = raw_input("Which account password would you like to retrieve? ")
	t = (acc,)
	c.execute('SELECT * FROM PW WHERE source=?', t)
	accline = c.fetchone()
	print "Your Password for " + acc + ": " + accline[1]
	
if sel == '3':
	acc = raw_input("Which account do you want to delete? ")
	t = (acc,)
	c.execute('DELETE FROM PW WHERE source=?', t)
	conn.commit()
	conn.close()

if sel == '4':
	acc = raw_input("Which account's password do you want to change? ")
	p1 = raw_input("Enter the old password: ")
	t = (acc,)
	c.execute('SELECT * FROM PW WHERE source=?', t)
	accline = c.fetchone()
	if accline[1] != p1:
		print "Incorrect Password!!!"
	else:
		p2 = raw_input("Enter the new password: ")
		t1 = (p2)
		t2 = (acc,)
		c.execute('UPDATE PW SET password=? WHERE source=?', (p2, acc))        
    	conn.commit()
		
	
if sel == '5':
	conn = sqlite3.connect('password.db')
	c = conn.cursor()	

	for row in c.execute('SELECT * FROM PW ORDER BY source'):
		print row
	




