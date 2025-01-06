
import pytest
from main.models import Account, Post

@pytest.mark.django_db
def test_account_creation():
    """Тест создания аккаунта"""
    account = Account.objects.create(username="test_user", email="test_user@example.com")
    assert Account.objects.count() == 1
    assert account.username == "test_user"
    assert account.email == "test_user@example.com"

@pytest.mark.django_db
def test_post_creation():
    """Тест создания поста"""
    account = Account.objects.create(username="test_user", email="test_user@example.com")
    post = Post.objects.create(
        account=account,
        likes=15,
        dislikes=3,
        content_type="text"
    )
    assert Post.objects.count() == 1
    assert post.account == account
    assert post.likes == 15
    assert post.dislikes == 3
    assert post.content_type == "text"

@pytest.mark.django_db
def test_account_posts_relationship():
    """Тест связи аккаунта с постами"""
    account = Account.objects.create(username="test_user", email="test_user@example.com")
    Post.objects.create(account=account, likes=10, dislikes=2, content_type="photo")
    Post.objects.create(account=account, likes=5, dislikes=1, content_type="text")

    assert account.posts.count() == 2
    assert account.posts.first().content_type == "photo"
    assert account.posts.last().content_type == "text"

@pytest.mark.django_db
def test_post_deletion_on_account_deletion():
    """Тест каскадного удаления постов при удалении аккаунта"""
    account = Account.objects.create(username="test_user", email="test_user@example.com")
    Post.objects.create(account=account, likes=10, dislikes=2, content_type="photo")
    assert Post.objects.count() == 1

    account.delete()  # Удаляем аккаунт
    assert Post.objects.count() == 0  # Все связанные посты также должны быть удалены
