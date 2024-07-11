from .tasks import process_video

class FileUploadView(View):
    def post(self, request):
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.save(commit=False)
            uploaded_file.user = request.user
            uploaded_file.save()
            process_video.delay(uploaded_file.id)
            return redirect('file_list')
        return render(request, 'upload.html', {'form': form})
