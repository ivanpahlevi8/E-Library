from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookForm
from django.contrib.auth.decorators import login_required
from .models import BookModel, BookImage

# Create your views here.
@login_required()
def home(request):
    return render(request, 'bookApp/home.html')

# Views for create form
@login_required()
def createBook(request):
    if request.method == 'POST':
        bookForm = BookForm(request.POST)

        uploaded_images = request.FILES.getlist('images') 

        if bookForm.is_valid():
            # Save the book information first
            book = bookForm.save()

            # loop all images
            for image in uploaded_images:
                # Create a BookImage object and save it
                book_image = BookImage(book=book, image=image)
                book_image.save()

            # Redirect to the book list or any other success page
            return redirect('all-book')

    else:
        # create empty forms to show to template
        bookForm = BookForm()

    # Pass the forms to the template
    data = {
        'bookForm': bookForm,
    }

    return render(request, 'bookApp/bookForm.html', data)

# view to show single book
@login_required()
def showBook(request, id):
    # get book data by id
    getBook = get_object_or_404(BookModel, book_id=id)

    # get all images related to books
    getBookImages = BookImage.objects.filter(book=getBook)

    # Prepare the context data to be passed to the template
    data = {
        'book': getBook,
        'bookImages': getBookImages,
    }

    return render(request, 'bookApp/showBook.html', data)

# view to show all books
@login_required()
def showAllBook(request):
    # Get all books
    allBooks = BookModel.objects.all()

    #Create data
    data ={'allBook':allBooks}

    # render all
    return render(request, 'bookApp/showAllBook.html', data)

# view to update book
@login_required()
def updateBook(request, id):
    # Get book by id
    getBook = get_object_or_404(BookModel, book_id=id)

    # Get all current images related to the book
    current_images = BookImage.objects.filter(book=getBook)
    print(current_images)

    # Initialize the BookForm with the existing book instance
    bookForm = BookForm(instance=getBook)

    if request.method == 'POST':
        bookForm = BookForm(request.POST, instance=getBook)

        # get images uploaded by user, if want to change image
        uploaded_images = request.FILES.getlist('images')

        # Validate the book form
        if bookForm.is_valid():
            # Save the book info first
            bookForm.save()

            # Check if new images are uploaded
            if uploaded_images:
                # Delete old images
                current_images.delete()

                # Add new images
                for image in uploaded_images:
                    book_image = BookImage(book=getBook, image=image)
                    book_image.save()

            # Redirect to the book list or any other view
            return redirect('all-book')

    # Prepare data for rendering in template
    data = {
        'bookForm': bookForm,
        'current_images': current_images  # You can show current images in the form if needed
    }

    return render(request, 'bookApp/bookForm.html', data)

# view to delete book
@login_required()
def deleteBook(request, id):
    # get book by id
    getBook = BookModel.objects.get(book_id=id)

    if request.method == 'POST':
        #Delete book
        # Get all the related book images and delete them
        book_images = BookImage.objects.filter(book=getBook)
        
        # Loop through and delete each image associated with the book
        for book_image in book_images:
            book_image.image.delete() 
            book_image.delete() 

        # Now delete the book itself
        getBook.delete()

        # Redirect to the book list or any other page
        return redirect('all-book') 
    
    data = {'book' : getBook}

    return render(request, 'bookApp/deleteBook.html', data)