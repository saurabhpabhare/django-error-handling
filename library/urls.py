from library.views import BookViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'books', BookViewSet)
urlpatterns = router.urls