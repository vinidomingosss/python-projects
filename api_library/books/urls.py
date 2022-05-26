from books.viewsets import BooksViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', BooksViewSet)
urlpatterns = router.urls


