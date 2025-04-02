from django.urls import path
from LinkedList.LetterLinkedList import letters_views
urlpatterns = [
    path("letters", letters_views.letters, name="linked-list-letters"),
]