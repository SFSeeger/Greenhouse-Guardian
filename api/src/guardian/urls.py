from django.urls import include, path

from guardian.views import EntryList

urlpatterns = [path("entry", EntryList.as_view(), name="entry-list")]
