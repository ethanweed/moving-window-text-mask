# apply a word-by-word mask to a text file
def moving_window_text_mask (file):
    
    # open the file with the input text
    with open(file,'r') as f:
        text = f.read()
        
    # make a mask for the text with symbols instead of characters
    text=text.split()
    mask = list(text)
    for s, val in enumerate(mask):
        val = '*' * len(val)
        mask[s] = val    
    
    # make masked version of the text, with one word revealed at a time
    output = []
    window = []
    counter = 0
    for s in mask:
        for s, val in enumerate(mask):
            window.append(val)
        window[counter] = text[counter]
        window = ' '.join(window)
        output.append('\n')
        output.append(window)
        counter = counter +1
        window = []

    # make a new text file, with the output of applied mask
    newfile = file + '_masked.txt'
    output = '\n'.join(output)
    with open(newfile, 'a+') as newfile:
        newfile.write(output)
    newfile.close()
    print('All done!')