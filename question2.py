#Defining the function that takes 3 paramenter chips, max_chips and max_text_length and checks for empty chips
def display_chips(chips=None, max_chips=None, max_text_length=None):
    if not chips:
        return ''

#This condition checks if the max_chips parameter is provided and is less than or equal to zero.
    if max_chips is not None and max_chips <= 0:
        return f'<aside data-testid="exceeding-text">{len(chips)} more items</aside>'

#This loop iterates through the chips. It considers the max_chips parameter to limit the number of chips displayed
    result = []
    for index, chip in enumerate(chips):
        if max_chips is not None and index >= max_chips:
            break
        label = chip['label'][:max_text_length] if max_text_length else ''
        if len(chip['label']) > max_text_length:
            label += '...'
        result.append(f'<div data-testid="chip-{index}">{label}</div>')

#After the loop, this condition checks if there are more chips than the max_chips allows.
    if max_chips is not None and len(chips) > max_chips:
        result.append(f'<aside data-testid="exceeding-text">{len(chips) - max_chips} more items</aside>')

    return ''.join(result)
