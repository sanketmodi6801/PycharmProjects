from django.shortcuts import render
from .models import Category, Posts
import random


def index(request):
    categories = Category.objects.all()
    # a = random.choice(categories)
    # print(a)
    # obj = Category.objects.get(a)
    posts = Posts.objects.all()
    # print(posts.name[0])
    # print(type(posts))



    # id1 = []
    # for e in categories:
    #     id1.append(e.id)
    #
    # print(id1)
    #
    # l = []
    # l1 = []
    # for i in id1:
    #     for e in posts:
    #         if i == e.category_id_id:
    #             l1.append(e)
    #     l.append(l1)
    # print(l)
    # post = []
    # for i in l:
    #     for j in i:
    #         post.append(j)





    # print(post)  # for e in posts:
    #     print(e.__dict__)
    # print(categories)
    # print(obj)

    # for i in categories:
    #     for j in posts:
    #         post = Posts.objects.filter(id(categories))
    #         print(post)
    #         if j.category_id == i.id:

    Data = {"cat": categories, "post": posts}
    # print(post)
    return render(request, 'index2.html', Data)


# def index(request):
#     # allPosts = Posts.objects.all()
#     category1 = Posts.objects.all().filter(Category="Automotive")
#     category2 = Posts.objects.all().filter(Category="Computer & Electronics")
#     category3 = Posts.objects.all().filter(Category="Construction & Contractors")
#     category4 = Posts.objects.all().filter(Category="Education")
#     category5 = Posts.objects.all().filter(Category="Entertainment")
#     category6 = Posts.objects.all().filter(Category="Food & Dining")
#     category7 = Posts.objects.all().filter(Category="Health & Medicine")
#     category8 = Posts.objects.all().filter(Category="Lux")
#     category9 = Posts.objects.all().filter(Category="Real estate")
#     category10 = Posts.objects.all().filter(Category="Others")
#
#     params = {"real": category9, "lux": category8, "ce": category2, "cc": category3, "edu": category4,
#               "enter": category5, "fd": category6, "hm": category7, "auto": category1, "other": category10}  # "posts":
#
#     return render(request, 'index2.html', params)
#
#
# def realEstate(request):
#     real = Posts.objects.all().filter(Category="Real estate")
#     params = {"real": real}
#     return render(request, 'RE.html', params)