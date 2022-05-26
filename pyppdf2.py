from flask import Flask, render_template, request

from PyPDF2 import PdfFileWriter, PdfFileReader


app = Flask(__name__)


@app.route('/crypte', methods=['POST'])

def crypteFile():

    if request.method == 'POST':

        request_data = request.get_json()
        path = request_data['path']
        password = request_data['password']

        
        # create a PdfFileWriter object
        out = PdfFileWriter()
        
        # Open our PDF file with the PdfFileReader
        file = PdfFileReader(path)
        
        # Get number of pages in original file
        num = file.numPages
        
        # Iterate through every page of the original 
        # file and add it to our new file.
        for idx in range(num):
            
            # Get the page at index idx
            page = file.getPage(idx)
            
            # Add it to the output file
            out.addPage(page)
        
        
        # Create a variable password and store 
        # our password in it.
        # Encrypt the new file with the entered password
        out.encrypt(password)
        
        # Open a new file "myfile_encrypted.pdf"
        with open(path, "wb") as f:
            
            # Write our encrypted PDF to this file
            out.write(f)
        

        return ('', 204)




@app.route('/decrypte', methods=['POST'])

def decrypteFile():

    if request.method == 'POST':

        request_data = request.get_json()
        path = request_data['path']
        password = request_data['password']


        # Create a PdfFileWriter object
        out = PdfFileWriter()
        
        # Open encrypted PDF file with the PdfFileReader
        file = PdfFileReader(path)
        
        # Store correct password in a variable password.
        password = password
        
        # Check if the opened file is actually Encrypted
        if file.isEncrypted:
        
            # If encrypted, decrypt it with the password
            file.decrypt(password)
        
            # Now, the file has been unlocked.
            # Iterate through every page of the file
            # and add it to our new file.
            for idx in range(file.numPages):
                
                # Get the page at index idx
                page = file.getPage(idx)
                
                # Add it to the output file
                out.addPage(page)
            
            # Open a new file "myfile_decrypted.pdf"
            with open(path, "wb") as f:
                
                # Write our decrypted PDF to this file
                out.write(f)
        
            # Print success message when Done
            print("File decrypted Successfully.")
        else:
            
            # If file is not encrypted, print the 
            # message
            print("File already decrypted.")


if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port=5001,
        debug=True
    )



