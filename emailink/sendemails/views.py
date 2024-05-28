from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.template import loader


def index(request):

    template = loader.get_template("sendemails/index.html")
    context = {
        "send_result": "Nous vous contacterons bientôt!",
    }
    return HttpResponse(template.render(context, request))

def submit_event(request):
    print('test..........')
    if request.method == 'POST':
        mon_champ_texte = request.POST['name']
    else:
        mon_champ_texte = '---'  
    print(mon_champ_texte)
    send_mail(
        "Nouveau client GoConnexions",
        "Bonjour, Un nouveau client essaye de nous contacter, voici son contact pour lui faire un retour: "+mon_champ_texte,
        "go.connexions.sender@gmail.com",
        ["ideas.flow.dev@hotmail.com", "eric@goconnexions.com"],
        fail_silently=False,
    )
    return render(request, 'sendemails/index.html')
