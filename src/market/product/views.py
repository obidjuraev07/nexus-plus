from django.shortcuts import render
from .forms import ProductForm, ProductImageFormSet
from .models import ProductImage


def product_create(request):
    print(request)
    form = ProductForm()
    if request.POST:
        form = ProductForm(request.POST or None)
        # formset = ProductImageFormSet()
        # print(request.POST.getlist('file'))
        if form.is_valid():
            product = form.save()
            files = request.POST.getlist('file')
            for f in files:
                ProductImage.objects.create(
                    product=product,
                    image=f
                )
    context = {
        "form": form,
        # "formset": formset
    }
    return render(request, 'create.html', context)
