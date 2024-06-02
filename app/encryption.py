import bcrypt

class Encryption:
    def encrypt_password(password):
        # Ensure the password is bytes
        if isinstance(password, str):
            password = password.encode('utf-8')
        hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
        return hashed_password.decode('utf-8')
        
    def validate_password(password, hashed_password):
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))