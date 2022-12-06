# import the necessary modules
# # from googleapiclient.discovery import build
# # from google.oauth2.credentials import Credentials
import os
import random
import string

# define a function that generates a random string
# of a given length


def generate_random_string(length):
    # create a list of all possible characters
    # that can be used in the random string
    chars = string.ascii_letters + string.digits

    # shuffle the list of characters to create a random
    # order
    random.shuffle(chars)

    # take the first `length` characters from the shuffled
    # list to create the random string
    random_string = chars[:length]

    # return the random string
    return random_string

# define a function that generates a random file
# with a given size


def generate_random_file(file_name, file_size):
    # open the file in write mode
    with open(file_name, "w") as f:
        # create a variable to keep track of the total
        # number of bytes written to the file
        total_bytes_written = 0

        # write random data to the file until the desired
        # file size is reached
        while total_bytes_written < file_size:
            # generate a random string of a random length
            # between 1 and 1000
            random_data = generate_random_string(random.randint(1, 1000))

            # write the random string to the file
            f.write(random_data)

            # update the total number of bytes written
            total_bytes_written += len(random_data)

# define a function that generates a random directory
# with a given number of files and a given total size


def generate_random_directory(directory_name, num_files, total_size):
    # create the directory
    os.makedirs(directory_name)

    # calculate the average file size
    average_file_size = total_size / num_files

    # generate the specified number of random files
    # in the directory, with sizes that are close to
    # the average file size
    for i in range(num_files):
        # generate a random file name
        file_name = generate_random_string(10)

        # generate a random file size that is within
        # 10% of the average file size
        file_size = random.randint(
            int(average_file_size * 0.9),
            int(average_file_size * 1.1),
        )

        # generate the random file
        generate_random_file(os.path.join(
            directory_name, file_name), file_size)


def calculate_fibonacci_numbers(max_num):
    # create a list to store the fibonacci numbers
    fibonacci_numbers = []

    # add the first two fibonacci numbers to the list
    fibonacci_numbers.append(0)
    fibonacci_numbers.append(1)

    # calculate the next fibonacci number in the sequence
    # until the maximum number is reached
    i = 0
    while fibonacci_numbers[i] + fibonacci_numbers[i + 1] <= max_num:
        # calculate the next fibonacci number
        next_fibonacci_number = fibonacci_numbers[i] + fibonacci_numbers[i + 1]

        # add the next fibonacci number to the list
        fibonacci_numbers.append(next_fibonacci_number)

        # increment the counter
        i += 1

    # return the list of fibonacci numbers
    return fibonacci_numbers


# define a function that calculates the total size
# of a directory and all of its subdirectories
def calculate_directory_size(directory_path):
    # create a variable to keep track of the total size
    total_size = 0

    # iterate through the files and subdirectories in the
    # directory
    for item in os.listdir(directory_path):
        # get the full path to the current item
        item_path = os.path.join(directory_path, item)

        # check if the current item is a directory
        if os.path.isdir(item_path):
            # if it is a directory, recursively calculate
            # its size and add it to the total size
            total_size += calculate_directory_size(item_path)
        else:
            # if it is a file, add its size to the total size
            total_size += os.path.getsize(item_path)

    # return the total size
    return total_size


def get_rectangle_string(size):
    rectangle_string = ""
    for i in range(1, size + 1):
        if i == 1 or i == size:
            # First and last rows are full of * characters
            rectangle_string += "*" * (2 * size - 1) + "\n"
        else:
            # Other rows have a * character at the beginning and end, and spaces in the middle
            rectangle_string += "*" + " " * (2 * size - 3) + "*" + "\n"
    return rectangle_string


def get_triangle_string(size):
    triangle_string = ""
    for i in range(1, size + 1):
        triangle_string += " " * (size - i) + "*" * (2 * i - 1) + "\n"
    return triangle_string


# print a triangle
triangle_string = get_triangle_string(5)
print(triangle_string)


# print a rectangle
rectangle_string = get_rectangle_string(5)
print(rectangle_string)

# # # # # # Call & test part

# calculate the total size of the "random_dir" directory
total_size = calculate_directory_size("random_dir")
# print the total size
print(total_size)


# calculate the fibonacci numbers up to 1000
fibonacci_numbers = calculate_fibonacci_numbers(1000)
# print the fibonacci numbers
print(fibonacci_numbers)


# generate a random directory with 10 files and a total size
# of 100 MB
generate_random_directory("random_dir", 10, 100000000)


#####################################################

#       GMAIL GET NUMBER OF UNREAD EMAIL FUNCTION
#
# def get_unread_email_count(user_id):
#     # Authenticate with the Gmail API using OAuth 2.0
#     credentials = Credentials.from_authorized_user_info(info=user_info)
#     service = build('gmail', 'v1', credentials=credentials)

#     # Use the Gmail API to get the list of emails in the user's inbox
#     inbox = service.users().messages().list(
#         userId=user_id, labelIds=['INBOX']).execute()
#     messages = inbox.get('messages', [])

#     # Count the number of unread emails in the user's inbox
#     unread_count = 0
#     for message in messages:
#         msg = service.users().messages().get(
#             userId=user_id, id=message['id']).execute()
#         if not msg['labelIds'].__contains__('UNREAD'):
#             unread_count += 1

#     return unread_count


#       CALL UNREAD GMAIL FUNCTION
#
# user_id = 'example@gmail.com'
# user_info = {
#     'access_token': 'ACCESS_TOKEN',
#     'client_id': 'CLIENT_ID',
#     'client_secret': 'CLIENT_SECRET',
#     'refresh_token': 'REFRESH_TOKEN',
#     'token_expiry': 'TOKEN_EXPIRY',
#     'token_uri': 'TOKEN_URI',
#     'user_agent': 'USER_AGENT',
#     'revoke_uri': 'REVOKE_URI'
# }
# unread_count = get_unread_email_count(user_id)
# print(f'Number of unread emails: {unread_count}')
