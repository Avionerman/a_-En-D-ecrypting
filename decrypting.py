import os

from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random


def decryption_function(given_key, given_filename):
    block_size = 64 * 1024
    out_put_file = given_filename[5:]   # Declare the new name of the decrypted file.

    with open(given_filename, 'rb') as input_file:
        file_size = int(input_file.read(16))
        Init_vector = input_file.read(16)     # Important line! It is described on the 'Encrypting code' file in the rep/ry.

        decrypter = AES.new(given_key, AES.MODE_CBC, Init_vector)   # Using AES method to decrypt the key, using the Initialization vector.

        with open(out_put_file, 'wb') as last_out_file:
            while not False:
                block = input_file.read(block_size)

                if not(len(block)):
                    break
                last_out_file.write(decrypter.decrypt(block))   # Decryption line!
            last_out_file.truncate(file_size)   # Truncating the file.


def main():

        given_filename = input("Tell me which file you want to decrypt: ")    # Ask for a file to decrypt, fro the user.
        given_password = input("Give me the correct password: ")    # Ask for a password, which is resposible for the decrypting of the above file.

        hashing_method = SHA256.new(given_password.encode('utf-8'))   # Using the SHA256 protocol I am hashin the password,
        final_hash = hashing_method.digest()      # then I am digesting it,

        decryption_function(final_hash, given_filename)     #, and finally I am decrypting the file.
        print("Done!")


if __name__ == "__main__":
    main()
