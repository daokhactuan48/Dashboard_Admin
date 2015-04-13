from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'mypage.views.performance'),
    url(r'^performance$', 'mypage.views.performance'),
    url(r'^instances$', 'mypage.views.instances'),
    url(r'^demo$','mypage.views.demo'),
    url(r'^demoinstant$','mypage.views.demoinstant'),
    url(r'^mayao$','mypage.views.mayao'),
    url(r'^child$','mypage.views.child'),
    url(r'^taomayao','mypage.views.taomayao'),
    #url(r'^test$', 'mypage.views.test'),
    url(r'^admin/', include(admin.site.urls)),
]
