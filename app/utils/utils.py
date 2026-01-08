from passlib.context import CryptContext
password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
def hash(password: str) -> str:  

    print("Hashing the password")
    hash_pswd = password_context.hash(password)
    print("Hash Password: ",hash_pswd)
    # convert string in hash
    return hash_pswd

def verify(plain_password,hash_password):
    
    return password_context.verify(plain_password,hash_password)