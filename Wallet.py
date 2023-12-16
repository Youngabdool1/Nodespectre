import hashlib

def find_private_key(wallet_address):
    for i in range(100000000):
        private_key = str(i).zfill(8)
        public_key = hashlib.sha256(private_key.encode()).hexdigest()
        if public_key == wallet_address:
            return private_key
        
    return "Private key not found."

wallet_address = input("Enter your wallet address: ")
private_key = find_private_key(wallet_address)
print("Your wallet's private key is:", private_key)
