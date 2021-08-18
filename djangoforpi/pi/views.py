from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm


def index(request):
    return HttpResponse("Hello, world")


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        post = request.POST
        dict = post.dict()
        print(dict['inputText'])
        # text = form.inputText
        # print(text)
    else:
        form = PostForm()

    return render(request, 'pi/insertText.html', {'form': form, })

