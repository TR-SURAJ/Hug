import hug

#Local Package
@hug.cli()
@hug.get('/books')
@hug.local()
def get_books(title:hug.types.text):
    return {'title':title.upper()}


#API
#CLI
if __name__ == '__main__':
    get_books.interface.cli()