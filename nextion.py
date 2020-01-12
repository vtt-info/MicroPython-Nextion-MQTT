import machine
import ubinascii

uart = ""

def connect(cnf):
  global uart
  uart = machine.UART(2, tx=cnf["uart"]["tx"], rx=cnf["uart"]["rx"])
  uart.init(cnf["uart"]["br"], bits=8, parity=None, stop=1)
  
def transmit(single):
  global uart
  if single["t"] == "str":
    uart.write(str(single["f"]+"."+single["p"]+"=\""+single["v"]+"\"").encode()+bytearray([255]*3))
  elif single["t"] == "int":
    uart.write(str(single["f"]+"."+single["p"]+"="+str(single["v"])).encode()+bytearray([255]*3))
  elif single["t"] == "cmd":
    uart.write(str(single["cmd"]).encode()+bytearray([255]*3))

def getCommand():
  cmd=uart.readline()
  if(cmd):
    cmd = ubinascii.hexlify(cmd).decode()
    return cmd
  return None

def writeraw(cmd):
  uart.write(cmd)

def dims(val):
  cmd = {}
  cmd["t"] = "cmd"
  cmd["cmd"] = "dims="+str(val)
  transmit(cmd)
