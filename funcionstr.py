
def reverse_string(string_to_reverse):
    string_to_reversed = ""
    current_index = len(string_to_reverse) - 1
    while current_index >= 0:
        string_to_reversed += string_to_reverse[current_index]
        current_index -= 1
    return string_to_reversed



print(reverse_string("Hola"))



