# blog/views.py
#from django.views.generic import ListView

#from .models import Post


#class BlogListView(ListView):
    #model = Post
    #template_name = 'home.html'



# blog/views.py
from django.views.generic import ListView, DetailView  # новое

from .models import Post




class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):  # новое
    model = Post
    template_name = 'post_detail.html'

class BlogDetailView(DetailView):  # новое
    model = Post
    template_name = 'post_detaill.html'

    def post_share(request, post_id):
        # Получить пост по id
        post = get_object_or_404(Post, id=post_id, status='published')
        if request.method == 'POST':
        # Форма была отправлена
           form = EmailPostForm(request.POST)
           if form.is_valid():
        # Поля формы прошли проверку
              cd = form.cleaned_data
        # ... отправить письмо

        else:
            form = EmailPostForm()


        return render(request, 'blog/post/share.html', {'post': post,
                                                'form': form})
