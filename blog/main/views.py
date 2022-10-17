from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import PostForm, EditForm, CategoryForm, CommentForm
from .models import Post, Category, Comment


class HomeView(ListView):
    model = Post
    template_name = "home.html"
    ordering = ("-time_create", "-id",)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        # stuff = get_object_or_404(Post, id=self.kwargs['pk'])

        cat_menu = Category.objects.all()
        context["cat_menu"] = cat_menu

        # total_likes = stuff.total_likes()
        # liked = False
        # if stuff.likes.filter(id=self.request.user.id).exists():
        #     liked = True
        # context["total_likes"] = total_likes
        # context["liked"] = liked
        return context


class PostView(DetailView):
    model = Post
    template_name = "post.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        cat_menu = Category.objects.all()
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])

        total_likes = stuff.total_likes()
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = "update_post.html"
    # fields = ('title', 'title_tag', 'body')


class DeletePostView(DeleteView):
    model = Post
    template_name = "delete_post.html"

    def get_success_url(self):
        return reverse_lazy('home')


class AddCategoryView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "add_category.html"


class PostsByUsersView(ListView):
    template_name = "posts_by_user.html"

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        queryset = Post.objects.filter(author__id=pk)
        return queryset

    def get_context_data(self, *args, **kwargs):
        pk = self.kwargs['pk']
        context = super().get_context_data(*args, **kwargs)
        user = User.objects.get(pk=pk)
        context['user'] = user

        return context


class SeeByCategoryView(ListView):
    # model = Category
    template_name = "category.html"

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        queryset = Post.objects.filter(category__slug=slug)
        return queryset

    def get_context_data(self, *args, **kwargs):
        slug = self.kwargs['slug']
        context = super().get_context_data(*args, **kwargs)
        cat = Category.objects.get(slug=slug)
        context['cat'] = cat
        cat_menu = Category.objects.all()
        context["cat_menu"] = cat_menu
        return context


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('post', args=[str(pk)]))


class AddCommentView(CreateView):
    model = Comment
    template_name = "add_comment.html"
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        context = super().get_context_data(**kwargs)
        context['post'] = Post.objects.get(pk=pk)
        return context

    def get_success_url(self):
        return reverse_lazy('comments', args=(self.object.post.id,))


class CommentsView(ListView):
    model = Comment
    template_name = "comments.html"

    def get_context_data(self, *args, **kwargs):
        pk = self.kwargs['pk']
        context = super().get_context_data(*args, **kwargs)
        comments = Comment.objects.filter(post_id=pk)
        context['comments'] = comments
        context['post'] = Post.objects.get(pk=pk)

        return context


class UpdateCommentView(UpdateView):
    model = Comment


class DeleteCommentView(DeleteView):
    model = Comment
