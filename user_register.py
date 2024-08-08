def usr_register(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfully registerd!!!")
            return redirect('home')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    print(f"Error in field '{field}': {error}")
            messages.success(request, "Oops!!! Something went wrong.")
            return redirect('register')
    form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
