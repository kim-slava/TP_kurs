import pytest
import numpy as np
from main.models import Account, Post
from main.services import PostStatistics

@pytest.fixture
def sample_posts(db):
    """Создаем фиктивные посты для тестов"""
    account = Account.objects.create(username="test_user", email="test_user@example.com")
    posts = [
        Post.objects.create(account=account, likes=10, dislikes=2, content_type="text"),
        Post.objects.create(account=account, likes=20, dislikes=3, content_type="photo"),
        Post.objects.create(account=account, likes=30, dislikes=4, content_type="video"),
    ]
    return posts

@pytest.mark.django_db
def test_get_likes_sum(sample_posts):
    """Тест суммы лайков"""
    stats = PostStatistics(sample_posts)
    assert stats.get_likes_sum() == 60  # 10 + 20 + 30

@pytest.mark.django_db
def test_get_dislikes_sum(sample_posts):
    """Тест суммы дизлайков"""
    stats = PostStatistics(sample_posts)
    assert stats.get_dislikes_sum() == 9  # 2 + 3 + 4

@pytest.mark.django_db
def test_get_average_likes(sample_posts):
    """Тест среднего количества лайков"""
    stats = PostStatistics(sample_posts)
    assert stats.get_average_likes() == pytest.approx(20.0)  # (10 + 20 + 30) / 3

@pytest.mark.django_db
def test_get_median_likes(sample_posts):
    """Тест медианного количества лайков"""
    stats = PostStatistics(sample_posts)
    assert stats.get_median_likes() == 20  # Медиана [10, 20, 30] == 20
