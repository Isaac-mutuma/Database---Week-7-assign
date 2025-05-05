-- Create Clients Table
CREATE TABLE clients (
    client_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone_number VARCHAR(20),
    registered_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create Packages Table
CREATE TABLE packages (
    package_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    price DECIMAL(10,2) NOT NULL
);

-- Create Photo Sessions Table
CREATE TABLE photo_sessions (
    session_id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT,
    package_id INT,
    session_date DATE NOT NULL,
    location VARCHAR(100),
    status ENUM('Pending', 'Completed', 'Cancelled') DEFAULT 'Pending',
    FOREIGN KEY (client_id) REFERENCES clients(client_id),
    FOREIGN KEY (package_id) REFERENCES packages(package_id)
);  



  -- Create payments Table
CREATE TABLE payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    session_id INT,
    amount_paid DECIMAL(10,2) NOT NULL,
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    payment_method ENUM('Cash', 'Mpesa', 'Card', 'Bank Transfer') NOT NULL,
    FOREIGN KEY (session_id) REFERENCES photo_sessions(session_id)
);


--Sample data
client_id,full_name,email,session_id,session_date,location,status,package_name,price,amount_paid,payment_method,payment_date
1,"Christine Wanjiru",christine.wanjiru@gmail.com,1,2025-05-15,Nairobi,Pending,"Corporate Event",25000.00,15000.00,Mpesa,"2025-04-29 16:23:17"
2,"David Mwangi",david.mwangi@gmail.com,2,2025-06-01,"Uhuru Park",Completed,"Newborn Package",15000.00,8000.00,Cash,"2025-04-29 16:23:17"
1,"Christine Wanjiru",christine.wanjiru@gmail.com,3,2025-06-10,"Studio A",Completed,"Maternity Shoot",12000.00,5000.00,Card,"2025-04-29 16:23:17"
2,"David Mwangi",david.mwangi@gmail.com,4,2025-07-05,"Karen Blixen Gardens",Pending,"Corporate Event",25000.00,20000.00,"Bank Transfer","2025-04-29 16:23:17"
1,"Christine Wanjiru",christine.wanjiru@gmail.com,5,2025-07-20,"Giraffe Centre",Cancelled,"Newborn Package",15000.00,0.00,Mpesa,"2025-04-29 16:23:17"
2,"David Mwangi",david.mwangi@gmail.com,6,2025-08-01,"Studio B",Completed,"Maternity Shoot",12000.00,5000.00,Cash,"2025-04-29 16:23:17"
1,"Christine Wanjiru",christine.wanjiru@gmail.com,7,2025-08-15,"KICC Rooftop",Pending,"Corporate Event",25000.00,10000.00,Mpesa,"2025-04-29 16:23:17"
2,"David Mwangi",david.mwangi@gmail.com,8,2025-08-25,"Nairobi Arboretum",Completed,"Newborn Package",15000.00,8000.00,Card,"2025-04-29 16:23:17"
