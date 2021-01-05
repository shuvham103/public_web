def project(request):
    if request.method == "GET":
        form = forms.FileUpload
        return render(request, "shuvham_site/project.html", {'form': form})
    if request.method == "POST":
        try:
            form = forms.FileUpload(request.POST, request.FILES)
            if form.is_valid():
                url = "https://jobs.lever.co/parseResume"

                payload = {}
                files = [
                    ('resume', ('upload.pdf', request.FILES.get(
                        'file'), 'application/pdf'))
                ]
                headers = {}

                response = requests.request(
                    "POST", url, headers=headers, data=payload, files=files)

                abc = json.loads(response.text)
                
                abc['summary']['workTime']['months']%=12
                abc['summary']['managementTime']['months']%=12

                b=Log(names=abc['names'][0])
                b.save()

                return render(request, "shuvham_site/project.html", {"response": abc})
            return render(request, "shuvham_site/project.html", {"message": "Are You sure you uploaded the right file. Please make sure it is in pdf format "})
        except Exception as e:
            return render(request, "shuvham_site/project.html", {"message": "Are You sure you uploaded the right file. Please make sure it is in pdf format. Just got an error. "})