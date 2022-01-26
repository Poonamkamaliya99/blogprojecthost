from unicodedata import category
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from .models import Blog,Comment, Contact,Like,Category

from .serializers import BlogSerializer,BlogCreateUpdateSerializer,CommentSerializer,LikeSerializer,LikeCreateUpdateSerializer, CategorySerializer, ContactSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.contrib.auth.decorators import login_required
from django.urls import reverse

from rest_framework.views import APIView
from rest_framework import status


# Create your views here.

def home(request):
    return render(request, 'home.html')

def blog(request):
    blog=Blog.objects.all()
    user=request.user
    comment=Comment.objects.filter(blog=blog)
    category = Category.objects.all()

  
    
    
    context={
        'blogs':blog,
        'comments':comment,
        'user':user,
        'category':category,
        # 'num_likes':num_likes, 
       
    }
    return render(request, 'blog.html', context)


# blog post view

def post_blog(request):
    if request.method=='POST':

        title=request.POST.get('title')
        thought=request.POST.get('thought')

        desc=request.POST.get('desc')
        desc1=request.POST.get('desc1')

        image = request.FILES.get('image')
        image1=request.FILES.get('image1')

        category=Category.objects.filter()


        blog=Blog(title=title, category=category, thought=thought, desc=desc, desc1=desc1, image=image, image1=image1, user_name=request.user)

        try:
            blog.save()
        except Exception:
            print(blog)
        messages.success(request,'blog has been sent seccessfully')
        return redirect('post_blog')
    return render(request, 'blog_post.html')





# add category in blog


def category(request):
    if request.method=='POST':
        name=request.POST.get('name')
        
        cat=Category(name=name)

        cat.save()
        messages.success(request,'category has been sent seccessfully')
        
        return redirect('category')   
         
    return render(request, 'category.html')




class CategoryCreateAPIView(CreateAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer



@api_view(['GET'])
def CategoryList(request):
    category=Category.objects.all()
    serializer=CategorySerializer(category, many=True)
    return Response(serializer.data)





# # tag in blog


# def tag_view(request):
#     if request.method=='POST':
#         tag_name=request.POST.get('tag_name')
        
#         tag=Tag(tag_name=tag_name)
#         tag.save()
#         messages.success(request,'tag has been sent seccessfully')
#         return redirect('tag')   
         
#     return render(request, 'tag.html')


# class TagCreateAPIView(CreateAPIView):
#     queryset=Tag.objects.all()
#     serializer_class=TagSerializer

# @api_view(['GET'])
# def TagList(request):
#     tag=Tag.objects.all()
#     serializer=TagSerializer(tag, many=True)
#     return Response(serializer.data)






# like on blog post    

@login_required(login_url="/admin/")

def like_post(request):
    
    user = request.user
    
    if request.method=='POST':
        blog_id = request.POST.get('blog_id')
        blog_obj = Blog.objects.get(id = blog_id)

        if user in blog_obj.liked.all():
            blog_obj.liked.remove(user)
        else:
            blog_obj.liked.add(user)
        
        like , created= Like.objects.get_or_create(user=user , blog_id=blog_id)

        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like_value = 'Like'

        like.save()

    return redirect('blog')



# Like Serializer




@api_view(['GET'])
def LikeList(request):
    like=Like.objects.all()
    serializer=LikeSerializer(like, many=True)
    return Response(serializer.data)










#comment


@login_required(login_url="/admin/")
def comment(request,pk):
    if request.method=='POST':
        blog=Blog.objects.get(id=pk)
        print(blog)

        content=request.POST.get('content')
        print(content)

        email=request.POST.get('email')
        print(email)

        website=request.POST.get('website')
        print(website)

        cmt=Comment(content=content, email=email, website=website, blog=blog, user=request.user)

        try:
            cmt.save()
            print(cmt)

        except Exception:
            print(cmt)
        messages.success(request,'blog has been sent seccessfully')
        return redirect('blog')
    return render(request, 'comment.html')


#comment serializer





# @api_view(['POST', 'GET'])
# def CommentCreate( request, pk):
#     comment=Comment.objects.get(id=pk)
#     serializer=CommentSerializer(comment, data=request.data)
    
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)



@api_view(['GET','POST'])
def comment_blog_api(request, pk):
    try:
        blog = get_object_or_404(Blog, id=pk)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        comments = Comment.objects.filter(blog=blog)
        serializers = CommentSerializer(comments,many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






# class CommentCreateAPIView(CreateAPIView):
#     queryset=Comment.objects.filter()
#     serializer_class=CommentSerializer
    
#     def create(self, request,pk):
#         user = request.user
#         comment=Comment.objects.get(id=pk)
#         data = {
#             "content": request.POST.get('content', None),
            
#             }
#         # _serializer = self.serializer_class(data=data)  
#         serializer=CommentSerializer(comment, data=data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_201_CREATED) 
#         else:
#             return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)





@api_view(['GET'])
def CommentList(request):
    cmt=Comment.objects.all()
    serializer=CommentSerializer(cmt, many=True)
    return Response(serializer.data)






#blog serializer

class BlogCreateAPIView(CreateAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer
    

@api_view(['GET'])
def BlogList(request):
    blog=Blog.objects.all()
    serializer=BlogSerializer(blog, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def BlogDetail( request, pk):
    blog=Blog.objects.filter(id=pk)
    serializer=BlogSerializer(blog, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def BlogUpdate( request, pk):
    blog=Blog.objects.get(id=pk)
    serializer=BlogSerializer(instance=blog, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def BlogDelete( request, pk):
    blog=Blog.objects.get(id=pk)
    blog.delete()
    return Response('deleted')





#contact api

class ContactCreateAPIView(CreateAPIView):
    queryset=Contact.objects.all()
    serializer_class=ContactSerializer



@api_view(['GET'])
def ContactList(request):
    contact=Contact.objects.all()
    serializer=ContactSerializer(contact, many=True)
    return Response(serializer.data)










   
# authentication login,register,logout

def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if password1 != password2:
            messages.warning(request, 'password does not match')
            return redirect('register')
        elif User.objects.filter(username=username).exists():
            messages.warning(request, 'username already taken')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.warning(request, 'email already taken')
            return redirect('register')
        else:
            user=User.objects.create_user(username=username,email=email,password=password1)
            user.save()
            return redirect('login')
            messages.success(request,'user registered successfully')
    return render(request, 'register.html')


def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            auth_login(request,user)
            return redirect('post_blog')
        else:
            messages.warning(request,'user is not register')
            return redirect('login')
    return render(request, 'login.html')

def logout(request):
    auth_logout(request)
    return redirect('/')