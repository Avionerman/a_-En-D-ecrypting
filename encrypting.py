import os

from Crypto.Hash import SHA256
from Crypto import Random
from Crypto.Cipher import AES


def encrypt(given_key, given_filename):       # Take the data from the user (through main).
    block_size = 64 * 1024
    out_put_file = "(enc)" + given_filename   # Here I modify the name with my way of thinking.
    file_size = str(os.path.getsize(given_filename)).zfill(16)      # Declaring of the size.
    Init_vector = Random.new().read(16)       # Really important value! Declare the randomization variable for the encryption.

    encryptor = AES.new(given_key, AES.MODE_CBC, Init_vector) # Creation of an AES protocol
    
    
    """ Inside here I read and then I create the new file that is going to be encrypted. 
     The encode is really important,
    because without utf-8 the lines are not going to be encrypted properly."""
    
    
     with open(given_filename, 'rb') as input_file:
        with open(out_put_file, 'wb') as out_file:
            out_file.write(file_size.encode('utf-8'))
            out_file.write(Init_vector)

            while not False:
                block = input_file.read(block_size)

                if not(len(block)):
                    break
                elif len(block) % 16 != 0:
                    block += b' ' * (16 - (len(block) % 16))

                out_file.write(encryptor.encrypt(block))


def main():
        given_filename = input("Type the file you want to encrypt: ")     # Ask for a file name to encrypt.
        given_password = input("Give a password [Tip! Please remember it] : ")     # Ask for a password.

        hashing_method = SHA256.new(given_password.encode('utf-8'))      # After the hashing of the password with SHA256,
        final_hash = hashing_method.digest()        # and after the digest of the above hashing,

        encrypt(final_hash, given_filename)     # I finally encrypt the file.
        print("Done!")


if __name__ == "__main__":
    main()
