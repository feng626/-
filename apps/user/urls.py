from common.routers import Router
from .views import UserViewSet

router = Router()
router.register('user', UserViewSet, basename='user')
urlpatterns = router.urls
