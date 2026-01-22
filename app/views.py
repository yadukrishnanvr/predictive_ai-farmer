import os
from django.shortcuts import render,HttpResponse
from sklearn.tree import DecisionTreeClassifier
from .models import *
import datetime
from django.core.files.storage import FileSystemStorage

def index(request):
    return render(request,'public/index.html')

def expert_home(request):
    return render(request,'expert/expert_home.html')

def login(request):
    if 'submit' in request.POST:
        username=request.POST['username']
        password=request.POST['password']
        
        if Login.objects.filter(username=username,password=password).exists():
            q=Login.objects.get(username=username,password=password)
            request.session['login_id']=q.pk
            login_id=request.session['login_id']
            if q.user_type=='admin':
                return HttpResponse(f"<script>alert('admin login success');window.location='/admin_home'</script>")

            if q.user_type=='farmer':
                q1 = Farmer.objects.get(LOGIN_id=login_id)
                if q1:
                    request.session['farmer_id']=q1.pk
                    return HttpResponse(f"<script>alert('Farmer login success');window.location='/farmer_home'</script>")
                else:
                    return HttpResponse(f"<script>alert('invalid Farmer login');window.location='/login'</script>")
                   
            if q.user_type=='user':
                q2 = User.objects.get(LOGIN_id=login_id)
                if q2:
                    request.session['user_id']=q2.pk
                return HttpResponse(f"<script>alert('User login success');window.location='/user_home'</script>")
            
            if q.user_type=='expert':
                q2 = Expert.objects.get(LOGIN_id=login_id)
                if q2:
                    request.session['expert_id']=q2.pk
                return HttpResponse(f"<script>alert('Expert login success');window.location='/expert_home'</script>")
   
            # if obj.usertype=='company':
            #     q = Company.objects.get(LOGIN_id=request.session['login_id'])
            #     if q:
            #         request.session['company_id']=q.pk
            #     return HttpResponse(f"<script>alert('Company login succes');window.location='company_home'</script>")
            
        else:
             return HttpResponse(f"<script>alert('invalid..');window.location='/login'</script>")
    return render(request,'public/login.html')

# def register(request):
#     if 'submit' in request.POST:
#             first_name = request.POST['f_name']
#             last_name = request.POST['l_name']
#             email = request.POST['email']
#             phone = request.POST['phone']
#             gender = request.POST['gender']
#             dob = request.POST['dob']
#             place = request.POST['place']
#             post = request.POST['post']
#             district = request.POST['district']
#             state = request.POST['state']
#             pin = request.POST['pin']
#             photo = request.FILES['photo']
#             username = request.POST['username']
#             password = request.POST['password']

#             import datetime
#             date=datetime.datetime.now().strftime("%Y%m%d-%H%M%S")+".jpg"
#             fs = FileSystemStorage() 
#             fp = fs.save(date, photo)

#             q1=Login(username=username,password=password,user_type='user')
#             q1.save()
#             q2=User(first_name=first_name ,last_name=last_name , email=email , phone=phone , gender=gender , dob=dob , place=place , post=post , district=district , state=state , pin=pin , photo=fs.url(fp) , LOGIN_id=q1.pk)
#             q2.save()
#             return HttpResponse(""" <script> alert('added successfully');window.location='/register'</script>""")
#     return render(request,"public/registration.html")

# def farmer_register(request):
#     if 'submit' in request.POST:
#             first_name = request.POST['f_name']
#             last_name = request.POST['l_name']
#             email = request.POST['email']
#             phone = request.POST['phone']
#             gender = request.POST['gender']
#             dob = request.POST['dob']
#             place = request.POST['place']
#             post = request.POST['post']
#             district = request.POST['district']
#             state = request.POST['state']
#             pin = request.POST['pin']
#             aadhar = request.POST['aadhar']
#             photo = request.FILES['photo']
#             username = request.POST['username']
#             password = request.POST['password']

#             import datetime
#             date=datetime.datetime.now().strftime("%Y%m%d-%H%M%S")+".jpg"
#             fs = FileSystemStorage() 
#             fp = fs.save(date, photo)

#             q1=Login(username=username,password=password,user_type='farmer')
#             q1.save()
#             q2=Farmer(first_name=first_name ,last_name=last_name , aadhar=aadhar ,  email=email , phone=phone , gender=gender , dob=dob , place=place , post=post , district=district , state=state , pin=pin , photo=fs.url(fp) , LOGIN_id=q1.pk)
#             q2.save()
#             return HttpResponse(""" <script> alert('added successfully');window.location='/register'</script>""")
#     return render(request,"public/farmer_registration.html")

from django.shortcuts import get_object_or_404
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse

def manage_experts(request):
    if 'submit' in request.POST:
        expert_id = request.POST.get('expert_id', None)
        first_name = request.POST['f_name']
        last_name = request.POST['l_name']
        email = request.POST['email']
        phone = request.POST['phone']
        gender = request.POST['gender']
        dob = request.POST['dob']
        specialized_area = request.POST['specialized_area']
        place = request.POST['place']
        post = request.POST['post']
        district = request.POST['district']
        state = request.POST['state']
        pin = request.POST['pin']
        username = request.POST['username']
        password = request.POST['password']
        photo = request.FILES.get('photo', None)

        if expert_id:
            expert = get_object_or_404(Expert, id=expert_id)
            login = get_object_or_404(Login, id=expert.LOGIN_id)

            expert.first_name = first_name
            expert.last_name = last_name
            expert.email = email
            expert.phone = phone
            expert.gender = gender
            expert.dob = dob
            expert.specialized_area = specialized_area
            expert.place = place
            expert.post = post
            expert.district = district
            expert.state = state
            expert.pin = pin

            login.username = username 
            login.password = password 
            login.save()

            if photo:
                import datetime
                date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
                fs = FileSystemStorage()
                fp = fs.save(date, photo)
                expert.photo = fs.url(fp)

            expert.save()
            return HttpResponse("<script>alert('Expert updated successfully!');window.location='/manage_experts'</script>")
        
        else: 
            import datetime
            date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
            fs = FileSystemStorage()
            fp = fs.save(date, photo)
            login = Login(username=username, password=password, user_type='expert')
            login.save()
            expert = Expert(
                first_name=first_name, last_name=last_name, email=email, phone=phone,
                gender=gender, dob=dob, specialized_area=specialized_area, place=place,
                post=post, district=district, state=state, pin=pin, photo=fs.url(fp), LOGIN_id=login.pk)
            expert.save()

            return HttpResponse("<script>alert('Expert added successfully!');window.location='/manage_experts'</script>")

    elif 'delete' in request.POST:
        expert_id = request.POST.get('expert_id')
        expert = get_object_or_404(Expert, id=expert_id)
        expert.delete()
        return HttpResponse("<script>alert('Expert deleted successfully!');window.location='/manage_experts'</script>")

    experts = Expert.objects.all()
    return render(request, "admin/manage_experts.html", {'experts': experts})




def user_home(request):
    return render(request,'user/user_home.html')

def admin_home(request):
    return render(request,'admin/admin_home.html')

def farmer_home(request):
    return render(request,'farmer/farmer_home.html')

def view_users(request):
    user = User.objects.all()
    return render(request, "admin/view_users.html", {'user': user})

def remove_user(request, id):
    user = User.objects.get(LOGIN_id=id)
    login = Login.objects.get(id=id)
    user.delete()
    login.delete()
    return HttpResponse(""" <script> alert('Removed successfully');window.location='/view_users'</script>""")

def view_farmers(request):
    farmers = Farmer.objects.all()
    return render(request, "admin/view_farmers.html", {'farmers': farmers})

def remove_farmer(request, id):
    farmer = Farmer.objects.get(LOGIN_id=id)
    login = Login.objects.get(id=id)
    farmer.delete()
    login.delete()
    return HttpResponse(""" <script> alert('Removed successfully');window.location='/view_farmers'</script>""")

def view_doubts(request):
    doubt=Doubt.objects.all()
    if "submit" in request.POST:
        id=request.POST['id']
        rep=Doubt.objects.get(id=id)
        reply=request.POST['reply']
        rep.reply=reply
        rep.save()
        return HttpResponse(""" <script> alert('Replied successfully');window.location='/view_doubts'</script>""")
    return render(request,'expert/view_doubts.html' , {'doubt':doubt})

def manage_notification(request):
    if request.method == "POST":
        if "submit" in request.POST:
            notification_text = request.POST['notification']
            notification_id = request.POST.get('notification_id', None)
            
            if notification_id:
                notification = Notification.objects.get(id=notification_id)
                notification.notification = notification_text
                notification.save()
                return HttpResponse("""<script> alert('Edited successfully'); window.location='/manage_notification'; </script>""")
            else:
                Notification.objects.create(notification=notification_text)
                return HttpResponse("""<script> alert('Added successfully'); window.location='/manage_notification'; </script>""")
        
        elif "delete" in request.POST:
            notification_id = request.POST.get('notification_id')
            if notification_id:
                Notification.objects.filter(id=notification_id).delete()
                return HttpResponse("""<script> alert('Deleted successfully'); window.location='/manage_notification'; </script>""")
    notifications = Notification.objects.all()
    return render(request, 'admin/manage_notification.html', {'notifications': notifications})


def view_feedback(request):
    if request.method == "POST":
        feedback_id = request.POST.get('feedback_id')
        reply_text = request.POST.get('reply')
        
        if feedback_id and reply_text: 
            feedback = Feedback.objects.get(id=feedback_id)
            feedback.reply = reply_text
            feedback.save()
            return HttpResponse("""<script> alert('Reply sent successfully'); window.location='/view_feedback'; </script>""")
    feedback_list = Feedback.objects.all()
    return render(request, 'admin/view_feedback.html', {'feedback_list': feedback_list})

def send_feedback(request):
    user_id = request.session.get('user_id')
    
    if request.method == "POST":
        feedback_text = request.POST['feedback']
        Feedback.objects.create(USER_id=user_id, feedback=feedback_text, reply='Pending')
        return HttpResponse("<script>alert('Feedback submitted successfully!');window.location='/send_feedback'</script>")

    feedback_list = Feedback.objects.filter(USER_id=user_id)
    return render(request, 'user/send_feedback.html', {'feedback_list': feedback_list})


def manage_crop(request):
    if 'submit' in request.POST:
        crop_id = request.POST.get('crop_id')
        crop_name = request.POST['crop_name']
        soil_type = request.POST['soil_type']
        temperature_range = request.POST['temperature_range']
        quantity = request.POST['quantity']

        if crop_id: 
            crop = Crop.objects.get(id=crop_id)
            crop.crop_name = crop_name
            crop.soil_type = soil_type
            crop.temperature_range = temperature_range
            crop.quantity = quantity
            crop.save()
            return HttpResponse("<script>alert('Crop updated successfully!');window.location='/manage_crop'</script>")
        else:
            crop = Crop(crop_name=crop_name, soil_type=soil_type, temperature_range=temperature_range, quantity=quantity)
            crop.save()
            return HttpResponse("<script>alert('Crop added successfully!');window.location='/manage_crop'</script>")

    if 'delete' in request.POST: 
        crop_id = request.POST['crop_id']
        Crop.objects.filter(id=crop_id).delete()
        return HttpResponse("<script>alert('Crop deleted successfully!');window.location='/manage_crop'</script>")
    crops = Crop.objects.all()
    return render(request, 'admin/manage_crop.html', {'crops': crops})

# Expert----------------------------------------------------------------------------------------------------

from django.shortcuts import get_object_or_404

def manage_fertilizer(request):
    if request.method == 'POST':
        if 'add' in request.POST:
            expert_id = request.session.get('expert_id')
            crop_id = request.POST['crop_id']
            fertilizer_name = request.POST['fertilizer_name']

            fertilizer = Fertilizer(EXPERT_id=expert_id, CROP_id=crop_id, fertilizer_name=fertilizer_name)
            fertilizer.save()

            return HttpResponse("<script>alert('Fertilizer added successfully!');window.location='/manage_fertilizer'</script>")

        if 'edit' in request.POST:
            fertilizer_id = request.POST['fertilizer_id']
            fertilizer_name = request.POST['fertilizer_name']
            crop_id = request.POST['crop_id']

            fertilizer = get_object_or_404(Fertilizer, id=fertilizer_id)
            fertilizer.fertilizer_name = fertilizer_name
            fertilizer.CROP_id = crop_id
            fertilizer.save()

            return HttpResponse("<script>alert('Fertilizer updated successfully!');window.location='/manage_fertilizer'</script>")
        if 'delete' in request.POST:
            fertilizer_id = request.POST['fertilizer_id']
            Fertilizer.objects.filter(id=fertilizer_id).delete()

            return HttpResponse("<script>alert('Fertilizer deleted successfully!');window.location='/manage_fertilizer'</script>")
    crops = Crop.objects.all()
    fertilizers = Fertilizer.objects.all()

    return render(request, 'expert/manage_fertilizer.html', {'crops': crops, 'fertilizers': fertilizers})

def manage_tips(request):
    if request.method == 'POST':
        if 'add' in request.POST:
            expert_id = request.session.get('expert_id')
            tips_text = request.POST['tips']
            date = datetime.datetime.now().date()
            tip = Tips(EXPERT_id=expert_id, tips=tips_text, date=date)
            tip.save()
            return HttpResponse("<script>alert('Tip added successfully!');window.location='/manage_tips'</script>")

        elif 'edit' in request.POST:
            tip_id = request.POST['tip_id']
            tips_text = request.POST['tips']
            date = datetime.datetime.now().date()
            tip = Tips.objects.get(id=tip_id)
            tip.tips = tips_text
            tip.date = date
            tip.save()
            return HttpResponse("<script>alert('Tip updated successfully!');window.location='/manage_tips'</script>")

        elif 'delete' in request.POST:
            tip_id = request.POST['tip_id']
            Tips.objects.filter(id=tip_id).delete()
            return HttpResponse("<script>alert('Tip deleted successfully!');window.location='/manage_tips'</script>")
    tips = Tips.objects.all()
    return render(request, 'expert/manage_tips.html', {'tips': tips})


def expert_notifications(request):
    notifications = Notification.objects.all()
    return render(request, 'expert/expert_notifications.html', {'notifications': notifications})


def viewfarmers(request):
    fa = Farmer.objects.all()
    return render(request, 'expert/viewfarmers.html', {'fa': fa})    


def viewcrops(request):
    fa = Crop.objects.all()
    return render(request, 'expert/viewcrops.html', {'fa': fa})  

def viewcomplaints(request):
    fa = Complaint.objects.all()
    return render(request, 'expert/viewcomplaints.html', {'fa': fa})


# -------------------------------------ANDROID----------------------------------------------------------


def user_registration(request):
    f_name = request.POST['first_name']
    l_name = request.POST['last_name']
    email = request.POST['email']
    phone = request.POST['phone']
    gender = request.POST['gender']
    dob = request.POST['dob']
    photo = request.FILES['photo']
    import datetime
    date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
    fs = FileSystemStorage()
    fp = fs.save(date, photo)
    
    username = request.POST['username']
    password = request.POST['password']
    m = Login(username=username,password=password,user_type = 'user')
    m.save()
    print(m,"Login_id")
    m1 = User(first_name=f_name , last_name=l_name ,email=email,phone=phone,dob=dob,gender=gender,photo=fs.url(fp) ,LOGIN_id=m.pk)
    m1.save()
    return JsonResponse({'status':'ok'})

def farmer_registration(request):
    f_name = request.POST['first_name']
    l_name = request.POST['last_name']
    email = request.POST['email']
    phone = request.POST['phone']
    gender = request.POST['gender']
    dob = request.POST['dob']
    photo = request.FILES['photo']
    import datetime
    date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
    fs = FileSystemStorage()
    fp = fs.save(date, photo)
    
    username = request.POST['username']
    password = request.POST['password']
    m = Login(username=username,password=password,user_type = 'farmer')
    m.save()
    print(m,"Login_id")
    m1 = Farmer(first_name=f_name , last_name=l_name ,email=email,phone=phone,dob=dob,gender=gender,photo=fs.url(fp) ,LOGIN_id=m.pk)
    m1.save()
    return JsonResponse({'status':'ok'})

def login_and(request):
    username = request.POST['username']
    password = request.POST['password']
    
    print(f"Received login attempt for username: {username}")
    
    if Login.objects.filter(username=username, password=password).exists():
        qa = Login.objects.get(username=username, password=password)
        lid = qa.pk
        print(f"Login successful for user ID: {lid} with usertype: {qa.user_type}")
        
        if qa.user_type == 'user':
            try:
                qd = User.objects.get(LOGIN_id=lid)
                print(f"User found: {qd}")
                uid = qd.pk
                return JsonResponse({'status': 'ok', 'lid': lid, 'uid': uid, 'usertype': 'user'})
            except User.DoesNotExist:
                print("User does not exist.")
                return JsonResponse({'status': 'no'})
            
        if qa.user_type == 'farmer':
            try:
                qd = Farmer.objects.get(LOGIN_id=lid)
                print(f"Farmer found: {qd}")
                uid = qd.pk
                return JsonResponse({'status': 'ok', 'lid': lid, 'uid': uid, 'usertype': 'farmer'})
            except User.DoesNotExist:
                print(" does not exist.")
                return JsonResponse({'status': 'no'})

        else:
            print("Invalid usertype.")
            return JsonResponse({'status': 'no'})
    else:
        print("Login failed.")
        return JsonResponse({'status':'no'})
    
def send_complaint(request):
    lid = request.POST['lid']
    print(lid,"uuuuuuuuuuuuuuuussssssseeeeerrrrrr")
    complaint = request.POST['complaint']
    m = Complaint(complaint=complaint , LOGIN_id=lid , user_type='user')
    m.save()
    return JsonResponse({'status':'ok'}) 

from django.http import JsonResponse
from .models import Complaint

def view_complaints(request):
    lid = request.GET.get('lid')
    if lid is None:
        return JsonResponse({'status': 'error', 'message': 'Login ID not provided'}, status=400)
    complaints = Complaint.objects.filter(LOGIN_id=lid)

    complaint_list = []
    for complaint in complaints:
        complaint_data = {
            'id': complaint.id,
            'complaint': complaint.complaint,
            'date': complaint.date,
            'user_type': complaint.user_type,
        }
        complaint_list.append(complaint_data)

    return JsonResponse({'status': 'ok', 'data': complaint_list})

from django.http import JsonResponse
from .models import Complaint

def delete_complaint(request):
    complaint_id = request.GET.get('id')

    if complaint_id is None:
        return JsonResponse({'status': 'error', 'message': 'Complaint ID not provided'}, status=400)

    try:

        complaint = Complaint.objects.get(id=complaint_id)
        complaint.delete()
        return JsonResponse({'status': 'ok', 'message': 'Complaint deleted successfully'})
    except Complaint.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Complaint not found'}, status=404)

from django.http import JsonResponse
from .models import Notification

def get_notifications(request):
    notifications = Notification.objects.all().order_by('-date')  
    notifications_data = []
    for notification in notifications:
        notifications_data.append({
            'notification': notification.notification,
            'date': notification.date.strftime('%Y-%m-%d'),  
        })

    return JsonResponse({'notifications': notifications_data})

from django.http import JsonResponse
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import base64
import datetime

def add_product(request):
    if request.method == "POST":
        try:
            fid = request.POST['fid']
            product_name = request.POST['product_name']
            stock = request.POST['stock']
            description = request.POST['description']
            price = request.POST['price'] 
            product_image_data = request.POST['product_image']

            if ';base64,' in product_image_data:
                format, imgstr = product_image_data.split(';base64,')  
                ext = format.split('/')[-1] 
            else:
                imgstr = product_image_data 
                ext = "jpg" 

            decoded_image = base64.b64decode(imgstr)

            date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
            filename = f"{date}.{ext}"
            file_path = os.path.join(settings.MEDIA_ROOT, filename)

            fs = FileSystemStorage(location=settings.MEDIA_ROOT)
            fs.save(filename, ContentFile(decoded_image))

            Product.objects.create(
                FARMER_id=fid,
                product_name=product_name,
                stock=stock,
                description=description,
                price=price, 
                product_image=fs.url(filename)
            )

            return JsonResponse({"status": "ok"})
        except Exception as e:
            print(f"Error: {e}")
            return JsonResponse({"status": "error", "message": str(e)})

    return JsonResponse({"status": "error", "message": "Invalid request method"})

from django.conf import settings

def get_products(request):
    products = Product.objects.all()
    product_list = []
    for product in products:
        
        product_data = {
            'id': product.id,
            'name': product.product_name,
            'image': product.product_image,
            'stock': product.stock,
            'description': product.description,
            'price': product.price, 
        }
        product_list.append(product_data)

    return JsonResponse({'status': 'ok', 'products': product_list})


def add_to_cart(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity')) 
        price = float(request.POST.get('price')) 

        try:
            user = User.objects.get(id=user_id)
            product = Product.objects.get(id=product_id)

            total_price = quantity * price

            cart_item = Cart(USER=user, PRODUCT=product, quantity=quantity, price=total_price)
            cart_item.save()

            return JsonResponse({"status": "ok", "message": "Product added to cart"})
        except User.DoesNotExist:
            return JsonResponse({"status": "error", "message": "User not found"})
        except Product.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Product not found"})
    return JsonResponse({"status": "error", "message": "Invalid request"})

def view_cart(request):
    user_id = request.GET.get('user_id')
    
    if user_id:
        cart_items = Cart.objects.filter(USER_id=user_id)
        
        if cart_items.exists():
            cart_data = []
            total_price = 0

            for item in cart_items:
                product = item.PRODUCT
                quantity = item.quantity
                price = item.price
                total_price += int(quantity) * float(price) 
                
                cart_data.append({
                    'product_name': product.product_name,
                    'quantity': quantity,
                    'price': price,
                    'total': int(quantity) * float(price), 
                })
            
            return JsonResponse({
                'status': 'ok',
                'cart_items': cart_data,
                'total_price': total_price
            })
        
        else:
            return JsonResponse({'status': 'error', 'message': 'No items in cart'})
    else:
        return JsonResponse({'status': 'error', 'message': 'User ID not provided'})


from django.http import JsonResponse
from .models import Cart, Booking_master, Booking_child, Payment

def complete_payment(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        ifsc = request.POST.get('ifsc')
        account_number = request.POST.get('account_number')
        address = request.POST.get('address') 

        try:
            cart_items = Cart.objects.filter(USER_id=user_id)
            
            if not cart_items.exists():
                return JsonResponse({'status': 'error', 'message': 'Cart is empty'})

            total_amount = 0
            for item in cart_items:
                total_amount += int(item.quantity) * float(item.price)
            
            booking_master = Booking_master(USER_id=user_id, PRODUCT=cart_items[0].PRODUCT, single_price=cart_items[0].price)
            booking_master.save()

            booking_child = Booking_child(BOOKING_MASTER=booking_master, total_amount=str(total_amount), order_status="Pending", address=address)
            booking_child.save()

            payment = Payment(BOOKING_CHILD=booking_child, total_amount=str(total_amount), payment_status="Success")
            payment.save()

            cart_items.delete()

            return JsonResponse({'status': 'ok', 'message': 'Payment successful and cart cleared'})

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

    return JsonResponse({'status': 'error', 'message': 'Invalid request'})


def view_orders(request):
    if request.method == 'GET':
        user_id = request.GET.get('user_id')

        try:
            booking_masters = Booking_master.objects.filter(USER_id=user_id)
            orders = []

            for master in booking_masters:
                booking_child = Booking_child.objects.get(BOOKING_MASTER=master)
                order = {
                    'product_name': master.PRODUCT.product_name,
                    'order_status': booking_child.order_status,
                    'total_amount': booking_child.total_amount
                }
                orders.append(order)

            return JsonResponse({'status': 'ok', 'orders': orders})

        except Exception as e:
            # Log the exception for debugging
            print(f"Error fetching orders: {str(e)}")
            return JsonResponse({'status': 'error', 'message': str(e)})

    return JsonResponse({'status': 'error', 'message': 'Invalid request'})

def farmer_sales_order(request):
    if request.method == 'GET':
        farmer_id = request.GET.get('farmer_id', '')

        if not farmer_id:
            return JsonResponse({"status": "error", "message": "Farmer ID is missing"})

        products = Product.objects.filter(FARMER_id=farmer_id)
        bookings = Booking_master.objects.filter(PRODUCT__in=products)

        result = []

        for booking in bookings:
            booking_children = Booking_child.objects.filter(BOOKING_MASTER=booking)
            for child in booking_children:
                result.append({
                    "booking_id": child.pk, 
                    "product_name": booking.PRODUCT.product_name,
                    "single_price": booking.single_price,
                    "total_amount": child.total_amount,
                    "address": child.address,
                    "order_status": child.order_status,
                    "date": booking.date
                })
        
        return JsonResponse({"status": "ok", "bookings": result})
    return JsonResponse({"status": "error", "message": "Invalid request method"})


from django.views.decorators.csrf import csrf_exempt
import json
import logging

logger = logging.getLogger(__name__)

@csrf_exempt
def mark_as_delivered(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            booking_id = data.get('booking_id', '')
            logger.info(f"Received booking_id: {booking_id}")  # Log received booking_id

            if not booking_id:
                logger.error("Booking ID is missing")
                return JsonResponse({"status": "error", "message": "Booking ID is missing"})

            try:
                booking_child = Booking_child.objects.get(pk=booking_id)
                logger.info(f"Booking found: {booking_child}")  # Log the found booking_child
                booking_child.order_status = 'delivered'
                booking_child.save()
                logger.info(f"Booking status updated to delivered for booking_id: {booking_id}")  # Log status update
                return JsonResponse({"status": "ok"})
            except Booking_child.DoesNotExist:
                logger.error(f"Booking not found for booking_id: {booking_id}")
                return JsonResponse({"status": "error", "message": "Booking not found"})
        except json.JSONDecodeError:
            logger.error("Failed to decode JSON")
            return JsonResponse({"status": "error", "message": "Invalid JSON"})

    logger.error("Invalid request method")
    return JsonResponse({"status": "error", "message": "Invalid request method"})

@csrf_exempt
def send_doubt(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            farmer_id = data.get('farmer_id', '')
            doubt_text = data.get('doubt', '')

            if not farmer_id or not doubt_text:
                return JsonResponse({"status": "error", "message": "Farmer ID or doubt text is missing"})

            Doubt.objects.create(
                LOGIN_id=farmer_id,
                doubt=doubt_text,
                reply='pending'
            )
            return JsonResponse({"status": "ok"})
        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "message": "Invalid JSON"})

    return JsonResponse({"status": "error", "message": "Invalid request method"})

def fetch_doubts(request):
    if request.method == 'GET':
        farmer_id = request.GET.get('farmer_id', '')

        if not farmer_id:
            return JsonResponse({"status": "error", "message": "Farmer ID is missing"})

        doubts = Doubt.objects.filter(LOGIN_id=farmer_id)
        result = []

        for doubt in doubts:
            result.append({
                "doubt": doubt.doubt,
                "reply": doubt.reply,
                "date": doubt.date.strftime("%Y-%m-%d")
            })

        return JsonResponse(result, safe=False)
    return JsonResponse({"status": "error", "message": "Invalid request method"})

def view_tips(request):
    lid = request.GET.get('lid')
    if lid is None:
        return JsonResponse({'status': 'error', 'message': 'Login ID not provided'}, status=400)
    
    tips = Tips.objects.all()
    
    tips_list = []
    for tip in tips:
        tips_data = {
            'id': tip.id,
            'expert': tip.EXPERT.first_name, 
            'tip': tip.tips,
            'date': tip.date
        }
        tips_list.append(tips_data)

    return JsonResponse({'status': 'ok', 'data': tips_list})


from django.http import JsonResponse
from .models import Complaint
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def send_farmer_complaint(request):
    if request.method == 'POST':
        lid = request.POST['lid']
        complaint = request.POST['complaint']
        m = Complaint(complaint=complaint, LOGIN_id=lid, user_type='farmer')
        m.save()
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)

def view_farmer_complaints(request):
    lid = request.GET.get('lid')
    if lid is None:
        return JsonResponse({'status': 'error', 'message': 'Login ID not provided'}, status=400)
    complaints = Complaint.objects.filter(LOGIN_id=lid, user_type='farmer')

    complaint_list = []
    for complaint in complaints:
        complaint_data = {
            'id': complaint.id,
            'complaint': complaint.complaint,
            'date': complaint.date,
            'user_type': complaint.user_type,
        }
        complaint_list.append(complaint_data)

    return JsonResponse({'status': 'ok', 'data': complaint_list})

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Complaint

@csrf_exempt
def delete_farmer_complaint(request):
    if request.method == 'POST':
        complaint_id = request.POST.get('id')

        if not complaint_id:
            return JsonResponse({'status': 'error', 'message': 'Complaint ID not provided'}, status=400)

        try:
            complaint = Complaint.objects.get(id=complaint_id, user_type='farmer')
            complaint.delete()
            return JsonResponse({'status': 'ok', 'message': 'Complaint deleted successfully'})
        except Complaint.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Complaint not found'}, status=404)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)


def PredictDisease(request):
    try:
        # Check if the photo is in FILES or POST
        if 'photo' in request.FILES:
            # Get the file from FILES
            file = request.FILES['photo']
            import datetime
            date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
            filepath = f"C:\\Users\\yadhukrishnan vr\\OneDrive\\Desktop\\finall predictive\\farmer\\predictive Final backup 12-03-25\\predictive\\predictive\\predictive_ai\\static\\media\\{date}.jpg"
            
            # Save the file
            with open(filepath, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
        elif 'photo' in request.POST:
            # Original code path for base64 encoded images
            photo = request.POST['photo']
            import datetime
            import base64
            date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
            a = base64.b64decode(photo)
            filepath = f"C:\\Users\\yadhukrishnan vr\\OneDrive\\Desktop\\finall predictive\\farmer\\predictive Final backup 12-03-25\\predictive\\predictive\\predictive_ai\\static\\media\\{date}.jpg"
            with open(filepath, "wb") as fh:
                fh.write(a)
        else:
            # No photo found
            return JsonResponse({"status": "error", "result": "No photo found in request"})
        
        # Continue with the existing code
        import tensorflow as tf
        import sys
        import os

        # Disable tensorflow compilation warnings
        os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

        # Read the image_data
        image_data = tf.io.gfile.GFile(filepath, 'rb').read()
        
        # Loads label file, strips off carriage return
        label_lines = [line.rstrip() for line
                       in tf.io.gfile.GFile("C:\\Users\\yadhukrishnan vr\\OneDrive\\Desktop\\finall predictive\\farmer\\predictive Final backup 12-03-25\\predictive\\predictive\\predictive_ai\\static\\logsold\\logsold\\output_labels.txt")]

        # Unpersists graph from file
        with tf.io.gfile.GFile("C:\\Users\\yadhukrishnan vr\\OneDrive\\Desktop\\finall predictive\\farmer\\predictive Final backup 12-03-25\\predictive\\predictive\\predictive_ai\\static\\logsold\\logsold\\output_graph.pb", 'rb') as f:
            graph_def = tf.compat.v1.GraphDef()
            graph_def.ParseFromString(f.read())
            _ = tf.import_graph_def(graph_def, name='')
            
        df = []
        with tf.compat.v1.Session() as sess:
            # Feed the image_data as input to the graph and get first prediction
            softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')

            predictions = sess.run(softmax_tensor, \
                                {'DecodeJpeg/contents:0': image_data})

            # Sort to show labels of first prediction in order of confidence
            top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]

            for node_id in top_k:
                human_string = label_lines[node_id]
                score = predictions[0][node_id]
                print('%s (score = %.5f)' % (human_string, score))
                df.append(human_string)
                
        result = df[0]
        return JsonResponse({"status": "ok", "result": 'Result:\n' + result})
    
    except Exception as e:
        import traceback
        print(traceback.format_exc())
        return JsonResponse({"status": "error", "result": str(e)})
    


import numpy as np
import pickle
import pandas as pd
from django.http import JsonResponse
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from django.views.decorators.csrf import csrf_exempt

# Load model and scalers
model = pickle.load(open(r'C:\Users\yadhukrishnan vr\OneDrive\Desktop\finall predictive\farmer\predictive Final backup 12-03-25\predictive\predictive\predictive_ai\app\model.pkl', 'rb'))
sc = pickle.load(open(r'C:\Users\yadhukrishnan vr\OneDrive\Desktop\finall predictive\farmer\predictive Final backup 12-03-25\predictive\predictive\predictive_ai\app\standscaler.pkl', 'rb'))
ms = pickle.load(open(r'C:\Users\yadhukrishnan vr\OneDrive\Desktop\finall predictive\farmer\predictive Final backup 12-03-25\predictive\predictive\predictive_ai\app\minmaxscaler.pkl', 'rb'))

crop_dict = {
    1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya",
    7: "Orange", 8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes",
    12: "Mango", 13: "Banana", 14: "Pomegranate", 15: "Lentil", 16: "Blackgram",
    17: "Mungbean", 18: "Mothbeans", 19: "Pigeonpeas", 20: "Kidneybeans",
    21: "Chickpea", 22: "Coffee"
}

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def predict_crop(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            # Extract input values
            nitrogen = float(data.get('Nitrogen', 0))
            phosphorus = float(data.get('Phosphorus', 0))
            potassium = float(data.get('Potassium', 0))
            temperature = float(data.get('Temperature', 0))
            humidity = float(data.get('Humidity', 0))
            ph = float(data.get('Ph', 0))
            rainfall = float(data.get('Rainfall', 0))

            # Simple crop recommendation logic
            crop = "Rice"
            if nitrogen > 50 and phosphorus > 50 and potassium > 50:
                crop = "Maize"
            elif humidity > 80 and temperature > 25:
                crop = "Cotton"
            elif ph > 6.5 and rainfall > 200:
                crop = "Wheat"
            elif nitrogen < 30 and ph < 6.0:
                crop = "Groundnut"

            return JsonResponse({"result": crop}, status=200)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Invalid request"}, status=400)

@csrf_exempt
def retrain_model(request):
    if request.method == 'GET':
        try:
            dataset = pd.read_csv('Crop_recommendation.csv')
            X = dataset[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
            y = dataset['crop']
            
            ms = MinMaxScaler()
            X_scaled = ms.fit_transform(X)
            
            sc = StandardScaler()
            X_scaled = sc.fit_transform(X_scaled)
            
            model = DecisionTreeClassifier(random_state=42)
            model.fit(X_scaled, y)
            
            pickle.dump(model, open(r'C:\Users\yadhukrishnan vr\OneDrive\Desktop\finall predictive\farmer\predictive Final backup 12-03-25\predictive\predictive\predictive_ai\app\model.pkl', 'wb'))
            pickle.dump(sc, open(r'C:\Users\yadhukrishnan vr\OneDrive\Desktop\finall predictive\farmer\predictive Final backup 12-03-25\predictive\predictive\predictive_ai\app\standscaler.pkl', 'wb'))
            pickle.dump(ms, open(r'C:\Users\yadhukrishnan vr\OneDrive\Desktop\finall predictive\farmer\predictive Final backup 12-03-25\predictive\predictive\predictive_ai\app\minmaxscaler.pkl', 'wb'))

            return JsonResponse({'status': 'ok', 'message': 'Model retrained successfully'})
        
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)
