from common.routers import Router
from .views import FractionViewSet

router = Router()
router.register('fraction', FractionViewSet, basename='fraction')
urlpatterns = router.urls
