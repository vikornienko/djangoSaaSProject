from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import CategoryForm, LinkForm
from .models import Category, Link

@login_required
def links(request):
    links = Link.objects.filter(created_by=request.user)

    return render(request,
                  "applink/links.html",
                  {"links": links})


@login_required
def categories(request):
    categories = Category.objects.filter(created_by=request.user)

    return render(request, "applink/categories.html", {"categories": categories})


@login_required
def create_link(request):
    if request.method == "POST":
        form = LinkForm(request.POST)
        if form.is_valid():
            link = form.save(commit=False)
            link.created_by = request.user
            link.save()
            return redirect("/dashboard")
    else:
        form = LinkForm()
        form.fields['category'].queryset = Category.objects.filter(created_by=request.user)
    return render(request,
            "applink/create_link.html",
            {"form": form})


@login_required
def create_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.created_by = request.user
            category.save()
            return redirect("/dashboard")
    else:
        form = CategoryForm()

    return render(request,
                  "applink/create_category.html",
                  {"form": form, "title": "Create category"})

@login_required
def edit_category(request, pk):
    category = get_object_or_404(Category, created_by=request.user, pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect("/links/categories/")
    else:
        form = CategoryForm(instance=category)

    return render(request, "applink/edit_category.html", {
        "form": form,
        "title": "Edit category",
    })


@login_required
def delete_category(request, pk):
    category = get_object_or_404(Category, created_by=request.user, pk=pk)
    category.delete()

    return redirect("/links/categories/")

