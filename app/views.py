from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render, redirect
from .forms import ImageForm, ResultForm
from .models import Image
from .remove import remove_background

@csrf_exempt
def remove_bg(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save()
            image_path = image.image.path
            image_res = remove_background(image_path,f"{image_path}.png")
            print(" image_path ",image_path)
            x=image_res.name.split("/remove_bg")
            return render(request, 'remove_bg.html',{'image': x[1]})
    else:
        form = ImageForm()
    return render(request, 'remove_bg.html', {'form': form})



