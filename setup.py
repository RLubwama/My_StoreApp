from flask import Flask  
from app.routes import app 
    
    
if __name__ =='__main__':
     app.run(debug=True, port=8080)

