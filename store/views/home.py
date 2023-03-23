from django.http import HttpResponse
from django.shortcuts import render, redirect, HttpResponseRedirect
from store.models.products import Products
from store.models.category import Category
from django.views import View


class Index(View):

    def post(self, request):
        product = request.POST.get("products")
        remove = request.POST.get('remove')
        cart = request.session.get("cart")
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1
                else:
                    cart[product] = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session["cart"] = cart
        print(cart)
        return redirect("homepage")

    def get(self, request):

        cart = request.session.get("cart")
        if not cart:
            request.session.cart = {}

        # product = Products.get_all_products()
        products = None
        category = Category.get_all_categories()
        Cid = request.GET.get('category')
        if (Cid):
            product = Products.get_all_products_by_categoryid(Cid)
        else:
            product = Products.get_all_products()

        data = {'Products': product, 'Category': category}
        # print("are You" , request.session.get("email"))

        return render(request, 'index.html', data)
        # return HttpResponse("hello")
