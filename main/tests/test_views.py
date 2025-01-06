import pytest
from django.urls import reverse
from main.models import Account, Post
from django.utils import timezone


@pytest.mark.django_db
def test_index_view(client):
    """Тест главной страницы"""
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200
    assert "главная страница" in response.content.decode()


@pytest.mark.django_db
def test_account_statistics_view(client):
    """Тест страницы статистики аккаунта"""
    account = Account.objects.create(username="test_user", email="test_user@example.com")
    Post.objects.create(account=account, likes=10, dislikes=2, content_type="text")
    Post.objects.create(account=account, likes=20, dislikes=3, content_type="photo")

    url = reverse('account_statistics', kwargs={'account_id': account.id})
    response = client.get(url)
    assert response.status_code == 200
    content = response.content.decode()
    assert "test_user" in content
    assert "30" in content  # Сумма лайков
    assert "5" in content  # Сумма дизлайков


@pytest.mark.django_db
def test_post_list_view(client):
    """Тест страницы списка постов"""
    account = Account.objects.create(username="test_user", email="test_user@example.com")
    Post.objects.create(account=account, likes=10, dislikes=2, content_type="text")
    Post.objects.create(account=account, likes=20, dislikes=3, content_type="photo")

    url = reverse('all_posts')
    response = client.get(url)
    assert response.status_code == 200
    content = response.content.decode()
    assert "text" in content
    assert "photo" in content


@pytest.mark.django_db
def test_add_account_view(client):
    """Тест создания аккаунта"""
    url = reverse('add_account')
    data = {"username": "new_user", "email": "new_user@example.com"}
    response = client.post(url, data)
    assert response.status_code == 302  # Перенаправление после успешного создания
    assert Account.objects.filter(username="new_user").exists()


@pytest.mark.django_db
def test_add_post_view(client):
    """Тест создания поста с датой"""
    # Создаем аккаунт
    account = Account.objects.create(username="test_user", email="test_user@example.com")

    # Получаем текущую дату и время для поля post_date
    current_datetime = timezone.now()

    # Данные для поста, включая дату
    url = reverse('add_post')
    data = {
        "account": account.id,
        "likes": 15,
        "dislikes": 5,
        "content_type": "text",
        "post_date": current_datetime,  # Указываем текущую дату и время
    }

    # Отправляем POST-запрос для добавления поста
    response = client.post(url, data)

    # Проверяем, что перенаправление произошло (статус 302)
    assert response.status_code == 302

    # Проверяем, что пост был добавлен
    assert Post.objects.filter(account=account, likes=15, content_type="text", post_date=current_datetime).exists()

@pytest.mark.django_db
def test_account_list_view(client):
    """Тест страницы списка аккаунтов"""
    Account.objects.create(username="user1", email="user1@example.com")
    Account.objects.create(username="user2", email="user2@example.com")

    url = reverse('all_accounts')
    response = client.get(url)
    assert response.status_code == 200
    content = response.content.decode()
    assert "user1" in content
    assert "user2" in content


@pytest.mark.django_db
def test_delete_post_view(client):
    """Тест удаления поста"""
    account = Account.objects.create(username="test_user", email="test_user@example.com")
    post = Post.objects.create(account=account, likes=15, dislikes=5, content_type="text")

    url = reverse('delete_post', kwargs={'pk': post.id})
    response = client.post(url)
    assert response.status_code == 302  # Перенаправление после успешного удаления
    assert not Post.objects.filter(id=post.id).exists()
