import sys
import pandas as pd

# Load user data from CSV
csv_file = "backend/login.csv"  # Ensure this file exists
try:
    data = pd.read_csv(csv_file)
except FileNotFoundError:
    data = pd.DataFrame(columns=["user", "password"])

def username_exists(username):
    return username in data["user"].values

def check_credentials(username, password):
    user_data = data[(data["user"] == username) & (data["password"] == password)]
    return not user_data.empty

def register_user(username, password):
    global data
    new_user = pd.DataFrame([{"user": username, "password": password}])
    data = pd.concat([data, new_user], ignore_index=True)
    data.to_csv(csv_file, index=False)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Failure: Missing username or password")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]

    if check_credentials(username, password):
        print("Success")
    else:
        print("Failure: Invalid credentials")
