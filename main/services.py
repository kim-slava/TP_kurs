
import numpy as np

class PostStatistics:
    def __init__(self, posts):
        self.posts = posts

    # def get_likes_sum(self):
    #     likes = [post.likes for post in self.posts]
    #     return np.sum(likes)

    # def get_dislikes_sum(self):
    #     dislikes = [post.dislikes for post in self.posts]
    #     return np.sum(dislikes)
    #
    # def get_average_likes(self):
    #     likes = [post.likes for post in self.posts]
    #     return np.mean(likes)
    #
    # def get_median_likes(self):
    #     likes = [post.likes for post in self.posts]
    #     return np.median(likes)
    def _get_likes(self) -> np.ndarray:
        """Получаем массив лайков всех постов."""
        return np.array([post.likes for post in self.posts])

    def get_likes_sum(self) -> int:
        """Возвращаем сумму всех лайков."""
        return np.sum(self._get_likes())

    def get_dislikes_sum(self) -> int:
        """Возвращаем сумму всех дизлайков."""
        return np.sum([post.dislikes for post in self.posts])

    def get_average_likes(self) -> float:
        """Возвращаем среднее значение лайков."""
        return np.mean(self._get_likes())

    def get_median_likes(self) -> float:
        """Возвращаем медиану лайков."""
        return np.median(self._get_likes())