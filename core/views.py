from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required


from .forms import SharePageForm, SpecializationForm
from .models import SharePage, SpecializationPage


@login_required(login_url='/admin')
def create_page(request):
    if request.method == 'GET':
        form = SharePageForm
        return render(request, "create.html", context={'form': form})

    elif request.method == 'POST':
        bound_form = SharePageForm(request.POST)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(reverse('page', kwargs={'id': new_obj.id}))
        return render(request,  "create.html", context={'form': bound_form})


@login_required(login_url='/admin')
def update_page(request, id):
    if request.method == 'POST':
        obj = SharePage.objects.get(id=id)
        bound_form = SharePageForm(request.POST, instance=obj)
        if bound_form.is_valid():
            obj = bound_form.save()
            if obj.is_for_specialization is True:
                return redirect(reverse('specialization', kwargs={'id': obj.specialization_id}))
            return redirect(reverse('page', kwargs={'id': id}))

    elif request.method == 'GET':
        obj = SharePage.objects.get(id=id)
        form = SharePageForm(instance=obj)
        return render(request, "update.html", {'form': form, 'id_page': id})


@login_required(login_url='/admin')
def delete_page(request, id):
    if request.method == 'POST':
        obj = SharePage.objects.get(id=id)
        if obj.is_for_specialization is True:
            obj.delete()
            return redirect(reverse('specialization', kwargs={'id': obj.specialization_id}))
        obj.delete()
        return redirect(reverse('home'))

    elif request.method == 'GET':
        obj = SharePage.objects.get(id=id)
        return render(request, "delete.html", context={'title': obj.title})


def page_list(request):
    # share_page = reversed(SharePage.objects.filter(is_for_specialization=None))
    share_page = SharePage.objects.filter(is_for_specialization=None).order_by('-likes')
    return render(request, "list_page.html", {'pages': share_page})


def page_view(request, id):
    page = SharePage.objects.get(id=id)
    return render(request, "page.html", {'page': page})


@login_required(login_url='/admin')
def create_specialization(request):
    if request.method == 'GET':
        form = SpecializationForm
        return render(request, "add_specialization.html", context={'form': form})

    elif request.method == 'POST':
        bound_form = SpecializationForm(request.POST)
        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(reverse('specialization', kwargs={'id': new_obj.id}))
        return render(request, "add_specialization.html", context={'form': bound_form})


def specialization_view(request, id):
    page = SpecializationPage.objects.get(id=id)
    return render(request, "specialization_page.html", {'spage': page})


@login_required(login_url='/admin')
def create_specialization_page(request, id):
    if request.method == 'GET':
        form = SharePageForm
        return render(request, "add_specialization_sp.html", context={'form': form, 'id': id})

    elif request.method == 'POST':
        bound_form = SharePageForm(request.POST)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            new_obj.is_for_specialization = True
            specialization = SpecializationPage.objects.get(id=id)
            new_obj.specialization = specialization
            new_obj.save()
            return redirect(reverse('specialization', kwargs={'id': id}))
        return render(request,  "add_specialization_sp.html", context={'form': bound_form})


def specialization_page_list(request):
    # specialization_pages = reversed(SpecializationPage.objects.all())
    specialization_pages = SpecializationPage.objects.all().order_by('likes', '-id')
    return render(request, "specialization_list_page.html", {'specialization_pages': specialization_pages})


@login_required(login_url='/admin')
def update_specialization_page(request, id):
    if request.method == 'POST':
        obj = SpecializationPage.objects.get(id=id)
        bound_form = SpecializationForm(request.POST, instance=obj)
        if bound_form.is_valid():
            bound_form.save()
            return redirect(reverse('specialization', kwargs={'id': id}))

    elif request.method == 'GET':
        obj = SpecializationPage.objects.get(id=id)
        form = SpecializationForm(instance=obj)
        return render(request, "update_specialization.html", {'form': form, 'id_page': id})


@login_required(login_url='/admin')
def delete_specialization_page(request, id):
    if request.method == 'POST':
        obj = SpecializationPage.objects.get(id=id)
        obj.delete()
        return redirect(reverse('specialization_list'))

    elif request.method == 'GET':
        obj = SpecializationPage.objects.get(id=id)
        return render(request, "delete_specialization.html", context={'title': obj.title, 'id_page': id})
