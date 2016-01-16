#!/usr/bin/env python3

import os
import sys
import time
import platform

import saveformat
from util import *

def main_dev():


  save_folder = os.path.sep.join([os.getenv('USERPROFILE'),'Documents','My Games','Fallout4','Saves'])
  print(save_folder,file=sys.stderr)
  for dirpath, dirnames, filenames in os.walk(save_folder):
    saves_filenames = filenames
  saves_filenames.sort()
  saves = [saveformat.Save(os.path.join(save_folder,save_filename)) for save_filename in saves_filenames]

  for save in saves:
    save.load()
  saves.sort(key=lambda x : x.props.get('mtime'))

  # saves = saves[:10]

  for save in saves:
    print(save.repr())
    print_props(save.header.props)

def termprint(x,step=0.05):
  time.sleep(50 * step)
  for c in x:
    print(c,end='')
    sys.stdout.flush()
    time.sleep(step)
  time.sleep(50 * step)

def main_roboco():
  banner = '''
ROBOCO INDUSTRIES (TM) TERMINK PROTOCOL

     Fallout4 save file inspector

  '''.strip()
  termprint(banner+'\n\n\n')
  termprint('Identifying runtime :\n\n')


  runtime_props = {}
  runtime_props['01 system'] = platform.system()
  runtime_props['02 platform'] = platform.platform()
  runtime_props['04 architecture'] = platform.architecture()
  runtime_props['03 machine'] = platform.machine()
  runtime_props['05 processor'] = platform.processor()
  runtime_props['06 python'] = platform.python_implementation()
  termprint('\n'.join(['{:20s} : {}'.format(k,runtime_props[k]) for k in sorted(list(runtime_props))]))
  print()
  print()

  save_folder = os.path.sep.join([os.getenv('USERPROFILE'),'Documents','My Games','Fallout4','Saves'])
  termprint('Using save directory: {}\n'.format(save_folder))
  termprint('Listing directory..\n')
  for dirpath, dirnames, filenames in os.walk(save_folder):
    saves_filenames = filenames
  saves_filenames.sort()
  saves = [saveformat.Save(os.path.join(save_folder,save_filename)) for save_filename in saves_filenames]
  termprint('Found {} saves.\n'.format(len(saves)))
  termprint('Parsing..\n')

  for save in saves:
    save.load()

  termprint('Sorting..\n')
  saves.sort(key=lambda x : x.props.get('mtime'))
  termprint('\n'.join([
    '{:4d}\t{:25s}'.format(
        i,
        '\t'.join([
          str(i) for i in
            [
              saves[i].props.get('mtime_asctime'),
              saves[i].props.get('filename_level'),
              saves[i].props.get('filename_ingame_location'),
            ]
          ])
      )
      for i in range(len(saves))
      ]
    ),
    step=0)

  termprint('\n\nReady. Enter a save number, "q" to quit, and "a" to print all information\n')
  valid = False
  while not valid:

    termprint('> ')
    usermsg = input()
    print(usermsg,type(usermsg))

    valid = False
    try:
      selected = [int(usermsg)]
      valid = True
    except ValueError:
      if usermsg.lower() == 'q':
        exit(0)
      if usermsg.lower() == 'a':
        selected = range(len(saves))
        valid = True


  for index in selected:
    save = saves[index]
    print(save.repr())
    print_props(save.header.props)


if __name__ == '__main__':

  clicked_cmd = ( platform.system() == 'Windows' )
  if clicked_cmd:
    try:
      main_roboco()
    except:
      pass
    print('Press enter to exit.')
    input()
  else:
    main_dev()
