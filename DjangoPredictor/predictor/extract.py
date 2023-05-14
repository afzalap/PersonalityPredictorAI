
import cv2
from tabulate import tabulate

from .ExtractionMethods.extract_baseline import detect_and_correct_baseline
from .ExtractionMethods.extract_top_margin import top_margin
from .ExtractionMethods.extract_line_spacing import extract_lines
from .ExtractionMethods.extract_slant_angle import extract_slant
from .ExtractionMethods.extract_word_spacing import extract_word_spacing
from .ExtractionMethods.calculate_letter_size import extract_letter_size


BASE_LINE_ANGLE = None
TOP_MARGIN = None
LETTER_SIZE = None
LINE_SPACING = None
WORD_SPACING = None
PEN_PRESSURE = None
SLANT_ANGLE = None




def extract_feature(img):
  # Base Line
  img , BASE_LINE_ANGLE = detect_and_correct_baseline(img)

  #top Margin
  TOP_MARGIN = top_margin(img)

  # line_spacing
  lines, LINE_SPACING = extract_lines(img)

  #slant angle 
  lines, SLANT_ANGLE = extract_slant(lines)

  #word_spacing
  words, WORD_SPACING = extract_word_spacing(lines)

  #letter size
  upper_zone_height, middle_zone_height, lower_zone_height = extract_letter_size(words)
  LETTER_SIZE = middle_zone_height


  table = [
      ["BASE_LINE_ANGLE", "{:.2f} deg".format(BASE_LINE_ANGLE)],
      ["TOP_MARGIN", "{:.2f} % of whole page".format(TOP_MARGIN)],
      ["LINE_SPACING", "{:.2f} mm".format(LINE_SPACING * 0.086)],
      ["SLANT_ANGLE", "{:.2f} deg".format(SLANT_ANGLE)],
      ["WORD_SPACING", "{:.2f} mm".format(WORD_SPACING * 0.086)],
      ["LETTER_SIZE", "{:.2f} mm".format(LETTER_SIZE * 0.086)]
  ]

  print(tabulate(table, headers=["Parameter", "Value"]))


  return [BASE_LINE_ANGLE, TOP_MARGIN, LINE_SPACING, SLANT_ANGLE, WORD_SPACING, LETTER_SIZE]
