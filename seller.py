import uuid
from flask import*
from database import *

seller=Blueprint('seller',__name__)

@seller.route('/seller_home')
def seller_home():
    return render_template('seller_home.html')




@seller.route('/seller_view_feedback')
def seller_view_feedback():
    data={}
    qry="SELECT *,buyer.first_name AS buyer  FROM feedback INNER JOIN buyer USING (buyer_id) INNER JOIN seller USING(seller_id) where seller_id='%s'"%(session['seller'])
    res=select(qry)
    data['feed']=res
    return render_template('seller_view_feedback.html',data=data)

@seller.route('/seller_view_payment_history')
def seller_view_payment_history():
    data={}
    qry="SELECT *,buyer.first_name AS buyer FROM payments  INNER JOIN buyer USING(buyer_id) INNER JOIN seller USING(seller_id)where status='paid' and seller_id='%s'"%(session['seller'])
    res=select(qry)
    data['pay']=res
    return render_template('seller_view_payment_history.html',data=data)

@seller.route('/seller_view_category')
def seller_view_category():
    data={}
    qry="SELECT * FROM `fish_category`"
    res=select(qry)
    data['cat']=res
    
    return render_template('seller_view_category.html',data=data)

@seller.route('/seller_age_group',methods=['post','get'])
def seller_age_group():
    cat=request.args['id']
    session['cat']=cat
    data={}
    qry="SELECT * FROM age_group"
    res=select(qry)
    data['age']=res
    return render_template('seller_age_group.html',data=data)

@seller.route('/seller_add_fish',methods=['post','get'])
def seller_add_fish():
    id=request.args['id']
    if 'submit' in request.form:
        name = request.form['name']
        des=request.form['des']
        amount=request.form['amount']
        image=request.files['image']
        fcount=request.form['fcount']
        path="static/"+ str(uuid.uuid4())+image.filename
        print(path)
        image.save(path)
        qry="insert into fishes values(null,'%s','%s','%s','%s','%s',curdate(),'%s','%s')"%(session['cat'], id,name,path,des,amount,session['seller'])
        res1=insert(qry)
        qry1="insert into count values(null,'%s','%s',curdate())"%(res1,fcount)
        insert(qry1)
        
        # return '''<script>alert("successfully Added");window.location="/seller_add_fish"</script>'''

    data={}
    qry="SELECT * FROM fishes INNER JOIN `fish_category` USING(category_id) INNER JOIN `age_group` USING(group_id) where category_id='%s' and seller_id='%s'  and group_id='%s'"%(session['cat'],session['seller'],id)
    res=select(qry)
    data['add']=res

    if 'action' in request.args:
        action = request.args['action']
        id=request.args['id']
        
    else:
        action=None
    
    if action=='delete':
        qry="delete from fishes where fish_id='%s'"%(id)
        delete(qry)
    return render_template('seller_add_fish.html',data=data)

@seller.route('/seller_update_fish',methods=['post','get'])
def seller_update_fish():
    id=request.args['id1']
    data={}
    qry="select * from fishes where fish_id='%s'"%(id)
    res=select(qry)
    data['fish']=res
    
    if 'submit' in request.form:
        name = request.form['name']
     
        des=request.form['des']
        amount=request.form['amount']


        qry1="update fishes set fish_name='%s',description='%s',amount='%s'where fish_id='%s'"%(name,des,amount,id)
        update(qry1)
        return redirect(url_for('seller.seller_view_fish'))

        
    return render_template('seller_update_fish.html',data=data)


@seller.route('/add_fish_count',methods=['post','get'])
def add_fish_count():
    id=request.args['id1']
    if 'submit' in request.form:
        count=request.form['count']
   
        qry="update count set count=(count+'%s') where fish_id='%s'"%(count,id)
        update(qry)
       
        return '''<script>alert("successfully Added");window.location="/seller_view_fish"</script>'''
   
    data={}
    qry="select * from count inner join fishes using (fish_id) where fish_id='%s' and seller_id='%s'"%(id,session['seller']) 
    res=select(qry)
    data['count']=res
    return render_template('add_fish_count.html',data=data)

@seller.route('/seller_update_count',methods=['post','get'])
def seller_update_count():
    id=request.args['id']
    co=request.args['co']
    if 'submit' in request.form:
        count=request.form['count']
        up=int(count)+int(co)
        qry="update count set count='%s' where count_id='%s'"%(up,id)
        update(qry)
        return '''<script>alert("successfully updated");window.location="/seller_view_fish"</script>'''

    return render_template('seller_update_count.html')

@seller.route('/seller_assistance_with_buyer',methods=['post','get'])
def seller_assistance_with_buyer():
    data={}
    qry="SELECT  * FROM assistance INNER JOIN seller USING (seller_id) INNER JOIN buyer USING(buyer_id) WHERE seller_id='%s'"%(session['seller'])
    res=select(qry)
    data['ass']=res
    

    
    return render_template('seller_assistance_with_buyer.html',data=data)

@seller.route('/seller_assitance_reply',methods=['post','get'])
def seller_assitance_reply():
    id=request.args['id'] 
    if 'submit' in request.form:
        reply=request.form['reply']
        qry="update assistance set reply='%s' where assistance_id='%s'"%(reply,id)
        update(qry)
        return '''<script>alert("successfully Reply send");window.location="/seller_assistance_with_buyer"</script>'''
    return render_template('seller_assitance_reply.html')

@seller.route('/seller_view_fish')
def seller_view_fish():
    data={}
    qry="SELECT * FROM  fishes INNER JOIN `count` USING(fish_id) WHERE seller_id='%s'"%(session['seller'])
    res=select(qry)
    data["fish"] = res
      
    if 'action' in request.args:
        action = request.args['action']
        id=request.args['id1']
        
    else:
        action=None
    
    if action=='delete':
        qry="delete from fishes where fish_id='%s'"%(id)
        delete(qry)
    return render_template('seller_view_fish.html',data=data)

# @seller.route('/add_fish_count')
# def add_fish_count