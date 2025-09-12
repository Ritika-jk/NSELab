import hashlib
def generate_hash(data: str | bytes) -> str:
    if isinstance(data, str):
        data = data.encode()
    return hashlib.sha256(data).hexdigest()

def verify_integrity(data: str | bytes, expected_hash: str) -> bool:
    return generate_hash(data) == expected_hash

if __name__ == "_main_":
    # Original data
    original = "Secure data that needs protection"
    
    # Generate hash
    data_hash = generate_hash(original)
    print(f"Data: {original}")
    print(f"Hash: {data_hash}")
    
    # Verify integrity
    print(f"Integrity verified: {verify_integrity(original, data_hash)}")
    
    # Tamper detection
    tampered = "Modified insecure data"
    print(f"Tamper detected: {not verify_integrity(tampered, data_hash)}")