# from django.contrib import messages
# from django.shortcuts import render, redirect, get_object_or_404
# from .models import Account, Post
# from .services import PostStatistics
# from .forms import AccountForm, PostForm
#
# # Create your views here.
# def index(request):
#     return render(request, 'main/index.html')
#
#
#
# def account_statistics(request, account_id):
#     account = Account.objects.get(id=account_id)
#     posts = Post.objects.filter(account=account)
#
#     stats = PostStatistics(posts)
#
#     context = {
#         'account': account,
#         'likes_sum': stats.get_likes_sum(),
#         'dislikes_sum': stats.get_dislikes_sum(),
#         'average_likes': stats.get_average_likes(),
#         'median_likes': stats.get_median_likes(),
#     }
#     return render(request, 'main/statistics.html', context)
#
# # Пример представления для всех постов
# def all_posts(request):
#     posts = Post.objects.all()
#     return render(request, 'main/posts_list.html', {'posts': posts})
#
#
# def add_account(request):
#     if request.method == 'POST':
#         form = AccountForm(request.POST)
#         if form.is_valid():
#             form.save()  # Сохраняем нового пользователя в базе данных
#             messages.success(request, 'Account created successfully!')
#             return redirect('all_posts')  # Перенаправляем на страницу со всеми постами, например.
#     else:
#         form = AccountForm()
#
#     return render(request, 'main/add_account.html', {'form': form})
#
# def add_post(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()  # Сохраняем новый пост в базе данных
#             messages.success(request, 'Post added successfully!')
#             return redirect('all_posts')  # Перенаправляем на страницу со всеми постами.
#     else:
#         form = PostForm()
#
#     return render(request, 'main/add_post.html', {'form': form})
#
#
# def all_accounts(request):
#     accounts = Account.objects.all()  # Получаем все аккаунты из базы данных
#     context = {
#         'accounts': accounts
#     }
#     return render(request, 'main/accounts_list.html', context)
#
# def delete_post(request, post_id):
#     if request.method == 'POST':
#         post = get_object_or_404(Post, pk=post_id)
#         post.delete()
#         messages.success(request, 'Post deleted successfully!')
#     return redirect('all_posts')  # Перенаправляем на страницу всех постов

from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Account, Post
from .services import PostStatistics
from .forms import AccountForm, PostForm

# Главная страница
class IndexView(TemplateView):
    template_name = 'main/index.html'


# Статистика аккаунта
class AccountStatisticsView(TemplateView):
    template_name = 'main/statistics.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        account_id = self.kwargs.get('account_id')
        account = get_object_or_404(Account, id=account_id)
        posts = Post.objects.filter(account=account)

        stats = PostStatistics(posts)

        context.update({
            'account': account,
            'likes_sum': stats.get_likes_sum(),
            'dislikes_sum': stats.get_dislikes_sum(),
            'average_likes': stats.get_average_likes(),
            'median_likes': stats.get_median_likes(),
        })
        return context


# Список всех постов
class PostListView(ListView):
    model = Post
    template_name = 'main/posts_list.html'
    context_object_name = 'posts'


# Добавление аккаунта
class AddAccountView(CreateView):
    model = Account
    form_class = AccountForm
    template_name = 'main/add_account.html'
    success_url = reverse_lazy('all_accounts')

    def form_valid(self, form):
        messages.success(self.request, 'Account created successfully!')
        return super().form_valid(form)


# Добавление поста
class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'main/add_post.html'
    success_url = reverse_lazy('all_posts')

    def form_valid(self, form):
        messages.success(self.request, 'Post added successfully!')
        return super().form_valid(form)


# Список всех аккаунтов
class AccountListView(ListView):
    model = Account
    template_name = 'main/accounts_list.html'
    context_object_name = 'accounts'


# Удаление поста
class DeletePostView(DeleteView):
    model = Post
    # template_name = 'main/post_confirm_delete.html'
    success_url = reverse_lazy('all_posts')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Post deleted successfully!')
        return super().delete(request, *args, **kwargs)
