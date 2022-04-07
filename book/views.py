from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def add_publisher(request):
    if request.method == 'GET':
        return render(request, 'add_publisher.html')
    else:
        publisher_name = request.POST.get('uname','')
        publisher_address = request.POST.get('address','')
        publisher = Publisher(name=publisher_name,address=publisher_address)
        publisher.save()
        return redirect('/book/publisher_list/',permanent=True)
    return HttpResponse('/book/')


def publisher_list(request):
    publisher_list = Publisher.objects.all()
    return render(request, 'publisher_list.html', {'publisher_obj_list':publisher_list})


def edit_publisher(request):
    if request.method == 'GET':
        cid = request.GET.get('id','')  #cid = request.GET.get('id','')这里括号里的id来源于publisher.html中的<a href="/book/edit_publisher/?id={{ publisher_list.id }}">修改</a>  ?后面的id
        id=int(cid)
        publisher_obj = Publisher.objects.get(id=id)
        publisher_obj_list = Publisher.objects.all()
        return render(request,'edit_publisher.html',{'publisher_obj':publisher_obj,'publisher_obj_list':publisher_obj_list})
    else:
        #获取表单edit_publisher的参数
        id = request.POST.get('id','')
        name = request.POST.get('uname','')
        address = request.POST.get('address','')

        #publisher_obj = Publisher.objects.get(id=id)

        #publisher_obj.name = name
        #publisher_obj.address = address
        publisher_obj = Publisher(id=id, name=name, address=address)
        publisher_obj.save()
        return redirect('/book/publisher_list/',permanent=True)



def delete_publisher(request):
    id = request.GET.get('id','')
    Publisher.objects.filter(id=id).delete()
    return redirect('/book/publisher_list/',permanent=True)


def book_list(request):
    book_obj_list = Book.objects.all()
    return render(request,'book_list.html',{'book_obj_list':book_obj_list})


def add_book(request):
    if request.method == "POST":
        bname = request.POST.get('bname','')
        price = request.POST.get('price', '')
        inventery = request.POST.get('inventery', '')
        sale_num = request.POST.get('sale_num', '')
        publisher_id = request.POST.get('publisher_id', '')

        Book.objects.create(bname=bname,price=price,inventery=inventery,sale_num=sale_num,publisher_id=publisher_id)
        return redirect('/book/book_list/',permanent=True)
    else:
        publisher_obj_list = Publisher.objects.all()
        return render(request,'add_book.html',{'publisher_obj_list':publisher_obj_list})


def edit_book(request):
    if request.method == 'GET':
        id = request.GET.get('id','')
        bid = int(id)
        #bid=1
        #book_obj = Book.objects.filter(bid=bid).first()
        book_obj = Book.objects.get(bid=bid)
        publisher_list = Publisher.objects.all()
        return render(request,'edit_book.html',{'book_obj':book_obj,'publisher_list':publisher_list})
    else:
        bid = request.POST.get('bid', '')
        bname = request.POST.get('bname', '')
        price = request.POST.get('price', '')
        inventery = request.POST.get('inventery', '')
        sale_num = request.POST.get('sale_num', '')
        publisher_id = request.POST.get('publisher_id', '')

        Book.objects.filter(bid=bid).update(bname=bname, price=price, inventery=inventery, sale_num=sale_num, publisher_id=publisher_id)

    return redirect('/book/book_list/', permanent=True)


def delete_book(request):
    bid = request.GET.get('id', '')
    Book.objects.filter(bid=bid).delete()
    return redirect('/book/book_list/', permanent=True)


def author_list(request):
    ret_list = []
    author_obj_list = Author.objects.all()
    for author_obj in author_obj_list:
        book_obj_list = author_obj.book.all()
        ret_dic = {}
        ret_dic['author_obj'] = author_obj
        ret_dic['book_list'] = book_obj_list
        ret_list.append(ret_dic)
    return render(request,'author_list.html',{'ret_list':ret_list})


def add_author(request):
    if request.method == 'GET':
        book_obj_list = Book.objects.all()
        return render(request, 'add_author.html', {'book_obj_list': book_obj_list})
    else:
        name = request.POST.get('name','')
        book_ids = request.POST.getlist('books')

        author_obj = Author.objects.create(name=name)
        author_obj.book.set(book_ids)
        return redirect('/book/author_list/', permanent=True)


def edit_author(request):
    if request.method == 'GET':
        id = request.GET.get('id','')
        id = int(id)
        author_obj = Author.objects.get(id=id)
        book_obj_list = Book.objects.all()
        return render(request,'edit_author.html',{'author_obj':author_obj,'book_obj_list':book_obj_list})
    else:
        id = request.POST.get('id','')
        name = request.POST.get('name', '')
        book_ids = request.POST.getlist('books')

        author_obj = Author.objects.filter(id=id).first()
        author_obj.name=name
        author_obj.book.set(book_ids)
        author_obj.save()
        return redirect('/book/author_list/', permanent=True)


def delete_author(request):
    id = request.GET.get('id', '')
    Author.objects.filter(id=id).delete()
    return redirect('/book/author_list/', permanent=True)