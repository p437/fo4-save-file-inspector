import string


def safe(x):
  if 0x1f < x < 0x7f:
    return chr(x)
  return '·'

def hexdump(data):
  line_length = 16
  return '\n'.join([
    ' '.join([
      ('{:'+str(line_length * 2)+'}').format(
        ''.join(['{:02x}'.format(byte) for byte in data[i:i+line_length]])
      ),
      ('{:'+str(line_length    )+'}').format(
        ''.join([safe(byte)            for byte in data[i:i+line_length]])
      ),
      ])
    for i in range(0,len(data),line_length)
  ])

def prefix_block(prefix,text):
  lines = [line.strip() for line in text.splitlines()]
  return '\n'.join(['{}{}'.format(prefix,line) for line in lines])

def print_props(d):
  keys = list(d.keys())
  keys.sort()
  for key in keys:
    if type(d.get(key)) is bytes:
      print('{:20s}: '.format(key),end='')
      hd = hexdump(d.get(key))
      hd = prefix_block(' '*22,hd)
      hd = hd[22:]
      print(hd)

    else:
      print('{:20s}: {}'.format(key,repr(d.get(key))))
