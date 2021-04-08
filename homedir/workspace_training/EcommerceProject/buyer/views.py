from django.shortcuts import render,redirect
from django.http import HttpResponse
from seller.models import Product,Category
from EcommerceProject.models import UserProfile
from.models import Cart
from django.db import connection

myCursor = connection.cursor()

def home(request):
    pObjs = Product.objects.all()
    catObjs = Category.objects.all()
    uObj = UserProfile.objects.get(user__username = request.user)

    myCursor.execute("select count(*) from buyer_cart where user_id={}".format(uObj.id))
    res = myCursor.fetchone()
    return render(request,'welcomeBuyer.html',{'products': pObjs,'category':catObjs,'count':res[0]})

def cart(request,id):
    pObj = Product.objects.get(id=id)
    uObj = UserProfile.objects.get(user__username = request.user)
    url = '/buyer/home/'

    try:
        c = Cart(product = pObj,user = uObj)
        c.save()
    except:
        return HttpResponse('<script>alert("Product is already in your cart");\
            window.location="%s"</script>'%url)

    return HttpResponse('<script>alert("Product added to your cart.");\
        window.location="{}"</script>'.format(url))

    return redirect('/buyer/home/')

def cartdetails(request):
    uObj = UserProfile.objects.get(user__username= request.user)
    cartObjs = Cart.objects.filter(user_id = uObj.id)
    proItems = []
    for i in cartObjs:
        proItems.append(Product.objects.get(id = i.product_id))

    return render(request,"cart_details.html",{'added_products': proItems})

def cartcalculate(request):
    q = request.POST.getlist('product_qty')
    price = request.POST.getlist('price')
    print(price)
    pid = request.POST.getlist('pid')
    total = 0
    uObj = UserProfile.objects.get(user__username=request.user)
    for i in range(len(q)):
        total = total + (int(q[i]) * int(float(price[i])))

        #Updating Product Stock
        updatePro = Product.objects.filter(id=pid[i])
        #print(updatePro.qty)
        updatedQty =int(updatePro[0].qty) - (int(q[i])) 
        updatePro.update(qty = updatedQty)

    cartObjs=Cart.objects.filter(user_id=uObj.id)
    cartObjs.delete()

    return render(request,"checkout.html",{'billAmount':total })
    