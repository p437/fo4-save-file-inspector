#!/usr/bin/env python3

import os
import time
import struct

def decode_fortran_string(storage,data,offset,name):
  length = struct.unpack('<H',data[offset:offset+2])[0]
  storage[name+'_len'] = length
  try:
    storage[name+'_str'] = str(data[offset+2:offset+2+length],'utf-8')
  except:
    storage[name+'_str'] = data[offset+2:offset+2+length]
  return length + 2

def decode_integer(storage,data,offset,name):
  x = struct.unpack('<I',data[offset:offset+4])[0]
  storage[name] = x
  return 4


class Header:
  def __init__(self,parent):
    self.parent = parent
    self.props = {}

  def parse(self):
    self.props['01_magic'] = self.parent.data[:12]
    self.props['02_magic_correct'] = self.props.get('magic') == bytes('FO4_SAVEGAME','ascii')
    a, b, c = struct.unpack('<III',self.parent.data[12:12+3*4])
    self.props['03_header_length'] = a
    self.props['04_unknown_int_B'] = b
    self.props['05_unknown_int_C'] = c
    self.props['980_full_header'] = self.parent.data[:self.props.get('03_header_length')]
    self.props['981_10last'] = self.parent.data[:self.props.get('03_header_length')][-10:]
    self.props['99_next_32'] = self.parent.data[
        self.props.get('03_header_length'):
        self.props.get('03_header_length') + 32
        ]

    offset = 24
    offset += decode_fortran_string(self.props,self.parent.data,offset,'07_username',)
    offset += decode_integer(self.props,self.parent.data,offset,'08_unknown_int_D')
    offset += decode_fortran_string(self.props,self.parent.data,offset,'09_location')
    offset += decode_fortran_string(self.props,self.parent.data,offset,'10_played_time')
    offset += decode_fortran_string(self.props,self.parent.data,offset,'11_race')


class Save:
  def __init__(self,filepath):
    self.filepath = filepath
    self.props = {}
    self.props['filepath'] = self.filepath

  def load(self):
    with open(self.filepath,'rb') as o:
      self.data = o.read()
    self.props['bytes'] = len(self.data)
    self.props['mtime'] = os.path.getmtime(self.filepath)
    self.props['filename'] = os.path.basename(self.filepath)
    self.props['filename_save_type'], self.props['filename_id_unknown_1_hex'], self.props['filename_id_unknown_2_dec'], self.props['filename_ingame_location'], self.props['filename_played_time'], self.props['filename_timestamp'], self.props['filename_level'], self.props['filename_unknown_constant_2'] = self.props['filename'].split('.')[0].split('_')
    self.props['mtime_asctime'] = time.ctime(self.props['mtime'])

    self.header = Header(self)
    self.header.parse()

  def infos(self):
    keys = [
        ['filename',                      'File name'],
        ['bytes',                         'Byte count'],
        ['mtime_asctime',                 'Last access'],
        ['filename_save_type',            'Save type'],
        ['filename_id_unknown_1_hex',     '?hex id?'],
        ['filename_id_unknown_2_dec',     '?dec id?'],
        ['filename_ingame_location',      'Ingame location'],
        ['filename_played_time',          'Played time'],
        ['filename_timestamp',            'Timestamp'],
        ['filename_level',                'Player level'],
        ['filename_unknown_constant_2',   '?const 2?'],
        ]
    return [[k[1],self.props.get(k[0])] for k in keys if self.props.get(k[0]) is not None]


  def repr(self):
    return '\n'.join([
      '{:20s}: {}'.format(k[0],k[1])
      for k in self.infos()
      ])

  def __len__(self):
    if self.props.get('byte_count') is not None:
      return self.props.get('byte_count')
    return 0

  def __str__(self):
    return '\t'.join([str(i) for i in [
      self.props.get('mtime_asctime'),
      self.props.get('filename_ingame_location'),
      self.props.get('filename_level'),

    ]])
