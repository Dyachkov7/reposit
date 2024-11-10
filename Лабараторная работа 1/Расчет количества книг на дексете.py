# TODO Найдите количество книг, которое можно разместить на дискете

disk_mb = 1.44
pages = 100
lines_per_page = 50
chars_per_line = 25
bytes_char = 4

book_size = pages * lines_per_page * chars_per_line * bytes_char
disk_bytes = disk_mb * 1024 * 1024
num_books = disk_bytes // book_size

print("Количество книг, помещающихся на дискету:", int(num_books))
