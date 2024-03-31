# import win32print
# import win32ui
import os
import subprocess
import sys
import signal

from blabel import LabelWriter

def print_label():
  if sys.platform == 'win32':
    args = '"C:\\\\Program Files\\\\gs\\\\gs10.03.0\\\\bin\\\\gswin64c" ' \
        '-sDEVICE=mswinpr2 ' \
        '-dBATCH ' \
        '-dNOPAUSE ' \
        '-dFitPage ' \
        '-sOutputFile="%printer%Godex EZ-1105 GEPL" '
    ghostscript = args + os.path.join(os.getcwd(), 'qrcode_and_label.pdf').replace('\\', '\\\\')
    subprocess.call(ghostscript, shell=True)

def collect_room_records():
  """Collects room information and creates 3 identical records.

  Returns:
      list: A list containing 3 dictionaries with the same room information.
  """

  room_name = input("What room: ")
  description = input("Description: ")
  fragile = input("Fragile (Y/N)? ").upper()

  record = {"room_name": room_name, "description": description}
  if fragile in ("Y", "y"):  # Check for both uppercase and lowercase "Y"
    record["fragile"] = "FRAGILE"

  # Create 3 identical records with the collected information
  return [record.copy() for _ in range(3)]

def make_label():
  
  label_writer = LabelWriter("moving_label_template.html",
                           default_stylesheets=("moving_labels.css",))

  records = collect_room_records()

  label_writer.write_labels(records, target='qrcode_and_label.pdf', base_url=".")
  print_label()
  

def main():
  running = True
  while running:
      make_label() 

if __name__ == "__main__":
  main()