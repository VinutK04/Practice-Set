import re

txt_str = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam et eros pharetra, fringilla neque vitae, congue dolor. Sed aliquam nisi nec volutpat sagittis. Curabitur iaculis ligula eget nisi porta hendrerit. Donec malesuada ut purus in maximus. Phasellus aliquam sit amet ante eu cursus. Pellentesque iaculis id mauris vel dapibus. Praesent blandit, nulla non feugiat mattis, nibh leo mollis mi, id rutrum lorem dui sed neque. Fusce malesuada cursus ligula vel lobortis. Nulla libero augue, pulvinar eget lacus ac, maximus gravida nulla. Cras facilisis finibus ante quis faucibus. Maecenas feugiat augue elit. Donec blandit justo sit amet porta faucibus. Sed placerat."

x = re.sub(r'[^a-zA-Z0-9\s]', '', txt_str).lower()
new_list = x.split(" ")
unique_dict = {}

for item in new_list:
    if item not in unique_dict:
        unique_dict[item] = 1
    else:
        unique_dict[item] +=1

for key, value in unique_dict.items():
    print(key, value)
