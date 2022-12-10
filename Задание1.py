first_string = 'абвгд привет абв 123456789 приветабв'
substring = 'абв'

def remove_substring_from_string(string, substring):
  my_list = list(filter(lambda x : not substring in x, string.split()))
  return ' '.join(my_list)

print (remove_substring_from_string(first_string, substring))