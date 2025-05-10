from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Smoothie
from .forms import SmoothieForm

# Views

def smoothie_list(request):
    smoothies = Smoothie.objects.all()
    return render(request, 'smoothies/smoothie_list.html', {'smoothies': smoothies})

@login_required
def smoothie_create(request):
    form = SmoothieForm(request.POST or None)
    if form.is_valid():
        smoothie = form.save(commit=False)
        smoothie.author = request.user
        smoothie.save()
        return redirect('smoothie_list')
    return render(request, 'smoothies/smoothie_form.html', {'form': form})

@login_required
def smoothie_update(request, pk):
    smoothie = get_object_or_404(Smoothie, pk=pk, author=request.user)
    form = SmoothieForm(request.POST or None, instance=smoothie)
    if form.is_valid():
        form.save()
        return redirect('smoothie_list')
    return render(request, 'smoothies/smoothie_form.html', {'form': form})

@login_required
def smoothie_delete(request, pk):
    smoothie = get_object_or_404(Smoothie, pk=pk, author=request.user)
    if request.method == 'POST':
        smoothie.delete()
        return redirect('smoothie_list')
    return render(request, 'smoothies/smoothie_confirm_delete.html', {'smoothie': smoothie})
