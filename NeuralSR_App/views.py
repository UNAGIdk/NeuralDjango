from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .NetworksProject.globalExec import globalExec


def index(request):
    if request.method == 'POST' and request.FILES:
        print("Condition works")
        file = request.FILES['image1']
        networkType = request.POST['networkType']
        print(file)
        print(networkType)
        print(globalExec(file, networkType))
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        file_url = fs.url(filename)

        return render(request, 'NeuralSR_App/index.html', {'file_url': file_url})

    return render(request, 'NeuralSR_App/index.html')
    # form = ProcessingImageForm(request.POST)
    # data = ProcessingImage.objects.all() #����� ������� ��� �������� �������

    # data = {
    #     'form': form
    # }

    # if request.method == "POST":
    #     if form.is_valid():
    #         form.save()
    #     else:
    #         print('is_valid didnt pass')


# def create(request):
#     # if request.method == "POST":
#         # processingImage = ProcessingImage()
#         # processingImage.name = "onGoingImage"
#         # processingImage.sourceFile = request.POST.get("file")
#         # processingImage.save()
#     form = ProcessingImageForm(request.POST)
#     form.save()
#     data = {
#         'form': form
#     }
#     return render(request, 'NeuralSR_App/index.html')
