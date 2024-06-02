import bcrypt

class Encryption:
    def encrypt_password(password):
        hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
        return hashed_password
    
    def validate_password(password, hashed_password):
        return bcrypt.checkpw(password, hashed_password)