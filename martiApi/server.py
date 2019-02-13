import hug
import apiLogic

@hug.get('/topics')
def getTopics(padre):
    return apiLogic.get_botones(padre)


@hug.get('/videojuegos')
def getVideojuegos():

    videojuegos = apiLogic.get_botones("0")
    return (videojuegos)
