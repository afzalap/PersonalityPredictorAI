
import numpy as np

words = []

def extract_words(binary):
    words = []

    # # Calculate the vertical sum of the binary image
    rows, cols = binary.shape
    vertical_sum = np.zeros(cols, dtype=int)
    for j in range(cols):
        for i in range(rows):
            if binary[i, j] == 255:
                vertical_sum[j] += 1
    
    # Find the start and end indices of the words
    start_word = []
    end_word = []
    in_word = False
    for j in range(cols):
        if vertical_sum[j] > 0 and not in_word:
            start_word.append(j)
            in_word = True
        if vertical_sum[j] == 0 and in_word:
            is_end = True
            for k in range(1, 30):
                if j + k >= cols:
                    end_word.append(j)
                    in_word = False
                    break
                if vertical_sum[j + k] > 0:
                    is_end = False
                    break
            if is_end:
                end_word.append(j)
                in_word = False
    
    lenw = len(start_word)
    # Check if start_word and end_word have the same length
    if len(start_word) != len(end_word):
        if len(start_word) <= len(end_word):
          lenw = len(start_word)
        else:
          lenw = len(end_word)
        # raise ValueError("start_word and end_word have different lengths")
    
    # Extract the words from the binary image and save them as separate images
    word_spacing = []
    min_word_width = 5
    for j in range(lenw):
        word_width = end_word[j] - start_word[j]
        if word_width >= min_word_width:
            word_img = binary[:, start_word[j]:end_word[j]]
            words.append(word_img)
            # Calculate the average word spacing
            if j > 0:
                word_spacing.append(start_word[j] - end_word[j - 1])
    avg_word_spacing = np.mean(word_spacing)
    
    return words, avg_word_spacing


def extract_word_spacing(lines):
  words_in = []
  spacing_in = []
  for line in lines:
    words, spacing = extract_words(line)
    # print(spacing)
    spacing_in.append(spacing)
    words_in.extend(words)

  avg_word_spacing = np.mean(spacing_in)

  return words_in, avg_word_spacing