from flask import *
from database import *


buyer=Blueprint('buyer',__name__)


@buyer.route('/buyer_home')
def buyer_home():
    return render_template('buyer_home.html')


@buyer.route('/buyer_search_fishes',methods=['post','get'])
def buyer_search_fishes():
    data={}
    
    if 'submit' in request.form:
        search=request.form['search']
    
        qry="SELECT * FROM fishes INNER JOIN `fish_category` USING (category_id) WHERE fish_name LIKE  '%s' or category_name like '%s'"%(search,search)
        res=select(qry)

        data['search']=res
    return render_template('buyer_search_fishes.html',data=data)


@buyer.route('/buyer_order_history')
def buyer_order_history():
    data={}
    qry="SELECT * FROM order_detail INNER JOIN order_master USING(order_master_id) INNER JOIN seller USING (seller_id) INNER JOIN fishes USING (fish_id)INNER JOIN `age_group` USING(group_id)INNER JOIN `fish_category` USING (category_id) WHERE STATUS='paid' and buyer_id='%s'"%(session['buyer'])
    res=select(qry)
    data['his']=res
    
    return render_template ('buyer_order_history.html',data=data)



@buyer.route('/buyer_send_complaints',methods=['post','get'])
def buyer_send_complaints():
    data={}
    qry="select * from complaints where sender_id='%s'"%(session['buyer'])
    res=select(qry)
    data['com']=res
    
    if 'submit' in request.form:
        comp=request.form['comp']
        qry="insert into complaints values(null,'%s','%s',curdate(),'pending')"%(session['buyer'],comp)
        insert(qry)
        return'''<script>alert("Complaint send successfully");window.location="/buyer_send_complaints"</script>'''

        
    return render_template('buyer_send_complaints.html',data=data)


@buyer.route('/buyer_view_category',methods=['post','get'])
def buyer_view_category():
    
    data={}
    qry="select * from fish_category "
    res=select(qry)
    data['cat']=res
    

    
    if 'submit' in request.form:
        search=request.form['search']

    
        qry="SELECT * FROM fishes INNER JOIN `fish_category` USING (category_id) WHERE fish_name LIKE  '%s' or category_name like '%s'"%(search,search)

        res=select(qry)
     

        data['search']=res
    return render_template('buyer_view_category.html',data=data)


@buyer.route('/buyer_view_fish')
def buyer_view_fish():
    id=request.args['id']
    data={}
    qry="select * from fishes where category_id='%s'"%(id)
    res=select(qry)
    
    if  res:
        data['fish']=res
    
    return render_template('buyer_view_fish.html',data=data)


@buyer.route('/cart',methods=['post','get'])
def cart():
    
    fish_id=request.args['fish_id']
    seller_id=request.args['seller_id']
    amt=request.args['amt']

    data={}
    qry="select * from fishes where fish_id='%s'"%(fish_id)
    res=select(qry)
    
    if res:
        data['fish']=res
    
        
        if 'submit' in request.form:
            count=request.form['quantity']
            amount=request.form['amount']
     
            data={}
            qry="select * from count where fish_id='%s'"%(id)
            res4=select(qry)
            
            if res4:
                des=0
                q1=res4[0]['count']
                count=request.form['quantity']
                des=int(q1)-int(count)
                qry7="update count set quantity='%s' where fish_id='%s'"%(des,fish_id)  
                update(qry7)  
           

            qry3="select * from order_master where buyer_id='%s' and status='pending'"%(session['buyer'])
            res1=select(qry3) 
            
            if  res1:
                om_id=res1[0]["order_master_id"]
                
                qry4="update order_master set total_amount=(total_amount+'%s') where order_master_id='%s'"%(amount,om_id)
                update(qry4)
                
                pay="update payments set amount=(amount+'%s') where order_master_id='%s'"%(amount,om_id)
                update(pay)
                
                qry5="INSERT INTO order_detail VALUES(NULL,'%s','%s','%s','%s')"%(om_id,fish_id,count,amt)

                insert(qry5)
                return  '''<script>alert("Add to cart successfully");window.location="/buyer_view_category"</script>'''

            else: 
                qry="insert into order_master values(null,'%s','%s','%s',curdate(),'pending')"%(seller_id,session['buyer'],amount) 


                res=insert(qry)
                pay1="insert into payments values(null,'%s','%s','%s','%s',curdate(),'pending')"%(seller_id,res,session['buyer'],amount)
                insert(pay1)
                qry1="insert into order_detail values(null,'%s','%s','%s','%s')"%(res,fish_id,count,amt)

                insert(qry1)
                
                return  '''<script>alert("Add to cart successfully");window.location="/buyer_view_category"</script>'''

    return render_template('cart.html',data=data)


@buyer.route('/buyer_cart_view',methods=['post','get'])
def buyer_cart_view():
    data={}
    qry="SELECT * FROM order_detail INNER JOIN order_master USING(order_master_id) INNER JOIN seller USING (seller_id) INNER JOIN fishes USING (fish_id)INNER JOIN `age_group` USING(group_id)INNER JOIN `fish_category` USING (category_id) WHERE STATUS='pending' and buyer_id='%s'"%(session['buyer'])
    res2=select(qry)
    if res2:
        omid=res2[0]['order_master_id']
        data['cartivew']=res2
        total=res2[0]['total_amount']
        session['omid1']=res2[0]['order_master_id']
        data['total']=total
    
        if 'submit' in request.form:
            
            qry3="SELECT *,order_detail.count AS scount  FROM order_detail INNER JOIN COUNT USING(fish_id) inner join order_master using(order_master_id) where order_master_id='%s'"%(session['omid1'])
            res=select(qry3)
            
        

            if res:
                
                for i in res:
                    a=i['count_id']
                    b=i['count']

                    c=i['scount']
                    print(c,"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")

                    
                    qry13="update count set count=(count-'%s') where count_id='%s'"%(c,a)
                    update(qry13)
            qry33="update order_master set status='paid' where order_master_id='%s'"%(omid)

            update(qry33)
                    
                
            
            

            qry1="update payments set status='paid' where order_master_id='%s'"%(omid)
            update(qry1)
            
            
            return '''<script>alert("Go to payment page");window.location="/buy_payment"</script>'''
        
        if 'action' in request.args:
            action=request.args['action']
            om_id=request.args['omid']
            odid=request.args['odid']
            amt=request.args['amt']
            co=request.args['count']
            tot=int(co)*int(amt)
            
            
        else:
            action=None
        if action=='delete':
            qry10="delete from order_detail where order_detail_id='%s'"%(odid)
            delete(qry10)
            qry11="update order_master set total_amount=(total_amount-'%s') where order_master_id='%s'"%(tot,om_id)
            res3=update(qry11)
        
    
            qry12="update payments set amount=(amount-'%s') where order_master_id='%s'"%(tot,om_id)
            update(qry12)
            return '''<script>alert("delete");window.location="/buyer_cart_view"</script>'''
    else:
        return render_template("404a.HTML")
        

    return render_template('buyer_cart_view.html',data=data)

@buyer.route('/buy_payment',methods=['post','get'])
def buy_payment():
    if 'pay' in request.form:
          return '''<script>alert("payment successfully");window.location="/buyer_home"</script>'''

    return render_template('buy_payment.html')


@buyer.route('/buyer_filter' ,methods=['post','get'])
def buyer_filter():
    data={}
    qry="select * from fish_category "
    res=select(qry)
    data['cat']=res
    
        # drop down category

    
    if 'fill' in request.form:
        data['fill']="search"
        cat=request.form['category']
        qry="SELECT * FROM fishes INNER JOIN `fish_category` USING (category_id) WHERE fish_name LIKE  '%s' or category_name like '%s'"%(cat,cat)
        res=select(qry)

        data['search']=res

        
    if 'price' in request.form:
        min1=request.form['min']
        max1=request.form['max']
        print(min1,max1)

        qry1 = "SELECT * FROM fishes WHERE amount BETWEEN %s AND %s ORDER BY amount ASC"%(min1, max1)
    
        res1 = select(qry1)
    
        data['search']=res1
        print(res1)
        
    return render_template('buyer_filter.html',data=data)

@buyer.route('/buyer_send_feedback')
def buyer_send_feedback():
    data={}
    qry="SELECT * FROM seller "
    res=select(qry)
    data['seller']=res
    return render_template('buyer_send_feedback_seller.html',data=data)

@buyer.route('/buyer_send_feed',methods=['post','get'])
def buyer_send_feed():
    id=request.args['id']
    if 'submit' in request.form:
        feed=request.form['feed']
        qry="insert into feedback values(null,'%s','%s',curdate(),'%s')"%(session['buyer'],id,feed)
        insert(qry)
        return '''<script>alert("feedback successfully send");window.location="/buyer_send_feedback"</script>'''
    return render_template('buyer_send_feed.html')


@buyer.route('/buyer_seller_v_as',methods=['post','get'])
def buyer_seller_v_as():
    data={}
    qry="select * from seller"
    res=select(qry)
    data['seller']=res
    
    return render_template('buyer_seller_v_as.html',data=data)
@buyer.route('/buyer_assistance_with_seller',methods=['post','get'])
def buyer_assistance_with_seller():
    id=request.args['id']
    data={}
    qry="select * from assistance"
    data['ass']=select(qry)
    if 'submit' in request.form:
        des=request.form['des']
        qry="insert into assistance values(null,'%s','%s','%s','pending',curdate())"%(session['buyer'],id,des)
        insert(qry)
        return '''<script>alert("Assistance send....");window.location="/buyer_seller_v_as"</script>'''

    return render_template('buyer_assistance_with_seller.html',data=data)