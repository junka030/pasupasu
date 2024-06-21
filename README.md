# PasuPasuパスパス: Your Local Password Manager　🐾　君のパスワードマネージャー

Welcome to **PasuPasu**!🐻‍❄️ パスパスへようこそ！
This password manager helps you securely store and manage your passwords with ease. 
Whether it's your favorite social media app or your most important banking login, PasuPasu has got you covered! 
パスワードをローカルに保存して、安全と簡単の管理ができます！

## Features ✨　機能

- **Secure Storage**   安全ストレージ: Encrypts your passwords using the powerful Fernet encryption.
- **Easy Access**      簡単にアクセス: Quickly retrieve your passwords with a simple click.
- **Organized**        アプリで分類:   Keep all your applications neatly listed and manage them with ease.
- **Minimalism**       きれいなメニュ: Enjoy a clean and user-friendly interface.

## Getting Started 🔑　初めに

### Prerequisites　事前必須
- Python 3.x
- MySQL

### Installation　インストール方法

1. **Clone the repository**　レポをクローンする
   ```sh
   git clone https://github.com/yourusername/pasupasu.git
   cd pasupasu

2. **Install requirements**　必要なライブラリのインストール
   ```sh
   pip install -r requirements.txt

3. **Setup your database**　データベースを作る
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

4. **Generate an encryption key**　暗証キー作る
- Uncomment the generate_and_save_key() line in vault.py
- Run the vault.py once to generate and save your encryption key
- Remember to comment the function again

5. **Run PasuPasu**🧸　パスパス実行

## Usage 🧩　使い方
- **Login**: Enter your MySQL database password to access the main interface.　データベースの暗証番号でログイン。
- **Add Password**: Enter the application name, login ID, and password, then click "Add".　アプリのIDと暗証番号を入力して、保存する。
- **Get Password**: Select an application from the dropdown and click "Get" to view the stored login ID and password.　アプリを選んで、IDと暗証番号を読み取る。
- **List Applications**: Click "List" to view all stored applications.　すべてのアプリを展示。
- **Delete Password**: Select an application from the dropdown and click "Delete" to remove it.　パスワード削除。

   
