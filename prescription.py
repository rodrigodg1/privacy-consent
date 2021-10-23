# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from umbral import SecretKey, Signer
from umbral import encrypt, decrypt_original
from umbral import generate_kfrags
from umbral import reencrypt
from umbral import decrypt_reencrypted





class Prescription:
    
    def __init__(self,personal_id,medication,diagnosis):
        self.personal_id = personal_id
        self.medication = medication
        self.diagnosis = diagnosis
    


class Privacy:
    def __init__(self):
        pass

    def create_delegator_keys(self): 
    # Generate Umbral keys for Alice.
        self.alices_secret_key = SecretKey.random()
        self.alices_public_key = self.alices_secret_key.public_key()
    
        self.alices_signing_key = SecretKey.random()
        self.alices_signer = Signer(self.alices_signing_key)
        self.alices_verifying_key = self.alices_signing_key.public_key()
        
        return self.alices_secret_key,self.alices_public_key,self.alices_signing_key,self.alices_signer, self.alices_verifying_key
        
    def create_delegatee_keys(self):
        # Generate Umbral keys for Bob.
        self.bobs_secret_key = SecretKey.random()
        self.bobs_public_key = self.bobs_secret_key.public_key()
        
        return self.bobs_secret_key,self.bobs_public_key
    
    
    def encryption(self,data,public_key):
        # Encrypt data with public key.
        plaintext = data
        capsule, ciphertext = encrypt(public_key, plaintext)
        
        return capsule,ciphertext

            
    def decrypt(self,capsule,ciphertext,secret_key):
        cleartext = decrypt_original(secret_key, capsule, ciphertext)
        
        return cleartext
    
   

user1 = Privacy()
alices_secret_key,alices_public_key,alices_signing_key,alices_signer,alices_verifying_key = user1.create_delegator_keys()

user2 = Privacy()
bobs_secret_key,bobs_public_key = user2.create_delegatee_keys() 
    
    
capsule,ciphertext = user2.encryption(b"eaee", alices_public_key)
    

my_text = user1.decrypt(capsule, ciphertext, alices_secret_key)

print(my_text)
    
        