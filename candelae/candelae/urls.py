"""
URL configuration for candelae project.

The `urlpatterns` list routes URLs to views_pack. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views_pack
    1. Add an import:  from my_app import views_pack
    2. Add a URL to urlpatterns:  path('', views_pack.home, name='home')
Class-based views_pack
    1. Add an import:  from other_app.views_pack import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("candelae_app.urls")),
    path('api/candles/', include("candelae_app.grouped_urls.candle_urls")),
    path('api/ingredients/', include("candelae_app.grouped_urls.ingredient_urls")),
    path('api/story_types/', include("candelae_app.grouped_urls.story_urls")),
    path('api/stories/', include("candelae_app.grouped_urls.story_type_urls")),
    #path("web/", include("TODO: URLS FOR WEB"))
]
