from flask import *
from database import *


admin=Blueprint('admin',__name__)

@admin.route('/admin_home')
def admin_home():
    return render_template('admin_home.html')

@admin.route('/admin_view_seller',methods=['post','get'])
def admin_view_seller():
    data={}
    qry="SELECT * FROM seller inner join login using(login_id) "
    res=select(qry)
    data['seller']=res
    
    if 'action' in request.args:
        action = request.args['action']  # get the value of action
        id=request.args['id']
    else:
        action=None
    
    if action=='accept':
        qry1="update login set usertype='seller' where login_id='%s'"%(id)  
        update(qry1)
        return redirect(url_for('admin.admin_view_seller'))

    elif action=='reject':
        qry2="update login set usertype='rejected' where login_id='%s'"%(id)  
        update(qry2)  
        return redirect(url_for('admin.admin_view_seller'))

    return render_template('admin_view_seller.html',data=data)


@admin.route('/admin_view_buyer')
def admin_view_buyer():
    data={}
    qry="select * from  buyer "
    res=select(qry)
    data['buyer']=res
    
    return render_template('admin_view_buyer.html',data=data)


@admin.route('/admin_manage_fish_category',methods=['post','get'])
def admin_manage_fish_category():
    data={}
    qry="select * from  `fish_category`"
    res=select(qry)
    data['cat']=res
    
    if 'submit' in request.form:
        category_name=request.form['category_name']
        qry1="insert into fish_category values(null,'%s')"%(category_name)
        insert(qry1)
        return '''<script>alert("successfully added");window.location="/admin_manage_fish_category"</script>'''
    
    
    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
        
        
    else:
        action=None   
         
    if action=='delete':
        qry2="delete from fish_category where category_id='%s'"%(id)
        delete(qry2)
        return redirect(url_for('admin.admin_manage_fish_category'))  
    
    if action=='update':
        qry3="select * from fish_category  where category_id='%s'"%(id)
        res1=select(qry3)
        data['fish']=res1
    
    
    if 'update' in request.form:
        category_name=request.form['category_name'] 
        qry4="update fish_category  set  category_name='%s' where category_id='%s'"%(category_name,id)
        update(qry4)
        return '''<script>alert("successfully updated");window.location="/admin_manage_fish_category"</script>'''
    return render_template('admin_manage_fish_category.html',data=data)



@admin.route('/admin_manage_age_group',methods=['post','get'])
def admin_manage_age_group():
    data={}
    qry="select * from age_group"
    res=select(qry)
    data['age']=res
    
    if 'submit' in request.form:
        age_group=request.form['age_group']
        qry="insert into age_group values(null,'%s')"%(age_group)
        insert(qry)
        return'''<script>alert("added successfully");window.location="/admin_manage_age_group"</script>'''
    
    
    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
    else:
        action=None
        
    if action=='delete':
        qry="delete from age_group where group_id='%s'"%(id) 
        delete(qry) 
        return redirect(url_for('admin.admin_manage_age_group'))
    if action=='update':
        data={}
        qry="select * from age_group  where group_id='%s'"%(id) 
        res=select(qry)
        data['age1']=res
    
    if 'update' in request.form:
        age_group=request.form['age_group']
        qry="update  age_group set group_name='%s'  where group_id='%s'"%(age_group,id) 
        update(qry)
        return '''<script>alert("successfully updated");window.location="/admin_manage_age_group"</script>'''
    return render_template('admin_manage_age_group.html',data=data)



@admin.route('/admin_viewfishes_on_each_seller')
def admin_viewfishes_on_each_seller():
    # data={}
    # qry="SELECT * FROM fishes INNER JOIN age_group USING (group_id) INNER JOIN fish_category USING(category_id)"
    # res=select(qry)
    # data['fish']=res
    data={}
    qry="SELECT * FROM seller "
    res=select(qry)
    data['seller']=res
    
    return render_template('admin_viewfishes_on_each_seller.html',data=data)


@admin.route('/admin_veach_seller_fish')
def admin_veach_seller_fish():
    id=request.args['id']
    data={}
    qry="select * from fishes inner join fish_category using(category_id) inner join age_group using(group_id) where seller_id='%s'"%(id)
    res=select(qry)
    data['fish']=res
    return render_template('admin_veach_seller_fish.html',data=data)


@admin.route('/admin_view_complaints',methods=['post','get']) 
def admin_view_complaints():
    data={}
    qry="select * from complaints"
    res=select(qry)
    data['com']=res
    
    
    if 'action' in request.args:
        action = request.args['action']
        id=request.args['id']
        
    else:
        action=None
    
    if action=='reply':
        qry1="select * from complaints where complaints_id='%s'"%(id)   
        res1=select(qry1)
        data['reply']=res1 
    
    if 'submit' in request.form:
        reply=request.form['reply']
        qry2="update complaints set reply='%s' where complaints_id='%s'"%(reply,id)
        update(qry2)
        return '''<script>alert("Reply send...");window.location="/admin_view_complaints"</script>'''
    
    return render_template('admin_view_complaints.html',data=data)

