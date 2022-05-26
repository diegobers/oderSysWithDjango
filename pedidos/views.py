from django.shortcuts import render 


def index(request):
    # filter(created_at__lte=timezone.now()).select_related("author").only/.defer("title")
     

    return render(request, "pedidos/index.html")#, {"oferta": ofer})