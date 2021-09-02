from library.views import AuthorViewSet, BookViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'books', BookViewSet)
router.register(r'author', AuthorViewSet)
urlpatterns = router.urls