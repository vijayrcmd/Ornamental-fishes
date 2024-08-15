from flask import *
from database import *



public=Blueprint('public',__name__)


@public.route('/')
def home():
    return render_template('home.html')



@public.route('/login',methods=['post','get'])
def login():
    if 'login' in request.form:
        username=request.form['username']
        password=request.form['password']
        qry="select * from  login where username='%s' and password='%s'"%(username,password)
        res=select(qry)
        
        if res:
            session['lid']=res[0]['login_id']

            if  res[0]['usertype']=='admin': 
                
                
                return '''<script>alert("welcome admin");window.location="/admin_home"</script>'''
            
            elif res[0]['usertype']=='seller':
                qry="select * from seller where login_id='%s'"%(session['lid'])
                res1=select(qry)
                session['seller']=res1[0]['seller_id']
                return '''<script>alert("welcome to seller");window.location="/seller_home"</script>'''
            
            elif res[0]['usertype']=='buyer':
                
                qry="select * from buyer where login_id='%s'"%(session['lid'])
                res2=select(qry)
                session['buyer']=res2[0]['buyer_id']
                return '''<script>alert("welcome to buyer");window.location="/buyer_home"</script>'''
                
        else:
                return '''<script>alert("user not found ");window.location="/login"</script>'''

                    
              

    return render_template('login.html')

@public.route('/register',methods=['post','get'])
def register():
    if 'submit' in request.form:
        fname=request.form['firstname']
        lname=request.form['lastname']
       
    
        email=request.form['email']
        contact=request.form['contact']
        add=request.form['add']
        username=request.form['username']
        password=request.form['password']
        
        
        
        qry1="insert into  login values(null,'%s','%s','user')"%(username,password)
        res=insert(qry1)
        

        qry="insert into buyer values(null,'%s','%s','%s','%s','%s')"%(res,fname,lname,email,contact)
        insert(qry)
        return'''<script>alert("registeration successfully");window.location="/login"</script>'''

    return render_template('register.html')


@public.route('/seller_register',methods=['post','get'])
def seller_register():
    if 'submit' in request.form:
        fname=request.form['fname']
        lname=request.form['lname']
        email=request.form['email']
        contact=request.form['contact']
        address=request.form['address']
        username=request.form['username']
        password=request.form['password']
        qry="insert into login values(null,'%s','%s','pending')"%(username,password)
        res=insert(qry)
        qry1="insert into seller values(null,'%s','%s','%s','%s','%s','%s')"%(res,fname,lname,email,contact,address)
        insert(qry1)
        return '''<script>alert("Registeration successfully ");window.location="/login"</script>'''
        
        
    
    
    return render_template('seller_register.html')



@public.route('/buyer_register',methods=['get','post'])
def buyer_register():
    if 'submit' in request.form:
        fname=request.form['fname']
        lname=request.form['lname']
        email=request.form['email']
        contact=request.form['contact']
        add=request.form['add']
     
        username=request.form['username']
        password=request.form['password']
        qry="insert into login values(null,'%s','%s','buyer')"%(username,password)
        res=insert(qry)
        qry1="insert into buyer values(null,'%s','%s','%s','%s','%s','%s')"%(res,fname,lname,email,contact,add)
        insert(qry1)
        return '''<script>alert("Registeration successfully ");window.location="/login"</script>'''
    return render_template('buyer_register.html')
