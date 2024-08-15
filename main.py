from flask import *
from database import *
from public import *
from admin import *
from seller import *
from buyer import *



app=Flask(__name__)
# Error handler for 404 Not Found errors
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

# Error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_server_error(error):
    return render_template('404.html'), 500

app.secret_key='sparrow'
app.register_blueprint(public)
app.register_blueprint(admin)
app.register_blueprint(seller)  
app.register_blueprint(buyer)


app.run(debug=True,port="5006") 