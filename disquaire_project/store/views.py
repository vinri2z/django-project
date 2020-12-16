from django.http import HttpResponse
from .models import ALBUMS


# Create your views here.
def index(request):
    message = "Hello world!"
    return HttpResponse(message)


def listing(request):
    albums = ["<li>{}</li>".format(album['name']) for album in ALBUMS]
    message = """<ul>{}</ul>""".format("\n".join(albums))
    return HttpResponse(message)


def detail(request, album_id):
    id = int(album_id)  # make sure we have an integer.
    album = ALBUMS[id]  # get the album with its id.
    artists = " ".join(
        [artist['name'] for artist in album['artists']])  # grab artists name and create a string out of it.
    message = "Le nom de l'album est {}. Il a été écrit par {}".format(album['name'], artists)
    return HttpResponse(message)


def search(request):
    obj = str(request.GET)
    query = request.GET.get('query')
    message = "propriété GET : {} et requête : {}".format(obj, query)
    return HttpResponse(message)
