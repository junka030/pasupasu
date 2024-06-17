# PasuPasu: Your Local Password Manager 🐾

Welcome to **PasuPasu**!🐻‍❄️ 
This password manager helps you securely store and manage your passwords with ease. 
Whether it's your favorite social media app or your most important banking login, PasuPasu has got you covered! 

## Features ✨

- **Secure Storage**: Encrypts your passwords using the powerful Fernet encryption.
- **Easy Access**: Quickly retrieve your passwords with a simple click.
- **Organized**: Keep all your applications neatly listed and manage them with ease.
- **Minimalism**: Enjoy a clean and user-friendly interface.

## Getting Started 🔑

### Prerequisites
- Python 3.x
- MySQL

### Installation

1. **Clone the repository**
   ```sh
   git clone https://github.com/yourusername/pasupasu.git
   cd pasupasu

2. **Install requirements**
   pip install -r requirements.txt

3. **Setup your database**
  ```sql
  CREATE DATABASE pasuwarudo;
  USE pasuwarudo;
  
  CREATE TABLE pasurecord (
      id INT AUTO_INCREMENT PRIMARY KEY,
      app_name VARCHAR(255) NOT NULL,
      login_id VARCHAR(255) NOT NULL,
      pw_enc TEXT NOT NULL
  );
  ```

4. **Generate an encryption key**
- Uncomment the generate_and_save_key() line in vault.py
- Run the vault.py once to generate and save your encryption key
- Remember to comment the function again

5. **Run PasuPasu**🧸

## Usage 🧩
- Login: Enter your MySQL database password to access the main interface.
- Add Password: Enter the application name, login ID, and password, then click "Add".
- Get Password: Select an application from the dropdown and click "Get" to view the stored login ID and password.
- List Applications: Click "List" to view all stored applications.
- Delete Password: Select an application from the dropdown and click "Delete" to remove it.

   
