from smbus import SMBus
import time

myi2c = SMBus(2)
def innit17320():
    myi2c.write_word_data(0x36,0x61,0x00)
    myi2c.write_word_data(0x36,0x61,0x00)   # write unlock
    myi2c.write_word_data(0x36,0x00,0x00)   # clear POR
    myi2c.write_word_data(0x0b,0x8c,0xb287)# nValert th
    myi2c.write_word_data(0x0b,0x8d,0x370a)# nT Alert th
    myi2c.write_word_data(0x0b,0x8e,0x3fc0) # I alert threshold
    myi2c.write_word_data(0x0b,0x8f,0x960a)# n SOC ALert 
    myi2c.write_word_data(0x0b,0x9c,0x0114)# n I Chg Term
    myi2c.write_word_data(0x0b,0x9e,0x4141)# nV Empty
    myi2c.write_word_data(0x0b,0xb0,0x8655)# nCfg
    myi2c.write_word_data(0x0b,0xb3,0x10e0)# des capacity
    myi2c.write_word_data(0x0b,0xb5,0x0002)# nPack cfg
    myi2c.write_word_data(0x0b,0xb8,0x8cb8)# nV CFG0
    myi2c.write_word_data(0x0b,0xb9,0x218a)# nv CFG1
    myi2c.write_word_data(0x0b,0xba,0xbeb5)# nv CFG2
    myi2c.write_word_data(0x0b,0xc2,0x3b6f)# preqal charge
    myi2c.write_word_data(0x0b,0xc6,0x6405) # Full SOC th
    myi2c.write_word_data(0x0b,0xd0,0x481e)  # UV prot thr
    myi2c.write_word_data(0x0b,0xcf,0x0064)  #R sense
    myi2c.write_word_data(0x0b,0xd1,0x3700) #Temp Th4/1
    myi2c.write_word_data(0x0b,0xd5,0x2d0a) #Temp Th3/2
    myi2c.write_word_data(0x0b,0xd2,0x552d) #Temp Th3
    myi2c.write_word_data(0x0b,0xd4,0x1074)  # Bal threshold
    myi2c.write_word_data(0x0b,0xd6,0xfa28) # n prot misc
    myi2c.write_word_data(0x0b,0xd7,0x0800)# nProtCFg
    myi2c.write_word_data(0x0b,0xd9,0x8800) # set charging voltage
    myi2c.write_word_data(0x0b,0xd8,0x7d4b) # set charging amps
    myi2c.write_word_data(0x0b,0xdb,0xec84) #  step charge
    myi2c.write_word_data(0x0b,0xda,0xb7a2) # charge ovp
    myi2c.write_word_data(0x0b,0xdc,0xd3fd) # charge delay cfg
    myi2c.write_word_data(0x0b,0xe3,0x84b2)  # min and design cell volt,
    myi2c.write_word_data(0x0b,0xf1,0x0008) # Hprot2 PB enable
    
    
    myi2c.write_word_data(0x36,0xab,0x8000) #restart fuel gauge
    
   # myi2c.write_word_data(0x36,0x04,0x7380) #at rate
   
    return()

def reload_nv():
    myi2c.write_word_data(0x36,0x61,0x00)
    myi2c.write_word_data(0x36,0x61,0x00)   # write unlock
    myi2c.write_word_data(0x36,0x00,0x00)   # clear POR
    myi2c.write_word_data(0x36,0x60,0xe001) # recall nV
    time.sleep(0.01)
    myi2c.write_word_data(0x36,0xab,0x8000) # retart
    time.sleep(0.01)
    myi2c.write_word_data(0x36,0x61,0x00f9)
    myi2c.write_word_data(0x36,0x61,0x00f9)
    return()

def check_updates():
    myi2c.write_word_data(0x36,0x61,0x00)
    myi2c.write_word_data(0x36,0x61,0x00)   # write unlock
    myi2c.write_word_data(0x36,0x60,0xe29b)
    time.sleep(0.005)
    f = myi2c.read_word_data(0x0b,0xfd) # update
    print("update remain","{:04x}".format(f))
    myi2c.write_word_data(0x36,0x61,0x00f9)
    myi2c.write_word_data(0x36,0x61,0x00f9)
    return()

def read_cfg():
     f = myi2c.read_word_data(0x36,0x00) # status
     print("status","{:04x}".format(f))
     f = myi2c.read_word_data(0x36,0x01) # V threshold
     print("vth","{:04x}".format(f))
    #  f = myi2c.read_word_data(0x0b,0xd0) # Vprt threshold
    #  print("v pth","{:04x}".format(f))
    #  f = myi2c.read_word_data(0x36,0x02) # T threshold
    #  print("Tth","{:04x}".format(f))
    #  f = myi2c.read_word_data(0x36,0x03) # SOC threshold
    #  print("Sth","{:04x}".format(f))
    #  f = myi2c.read_word_data(0x0b,0xb0) # nCFG
    #  print("nConFG","{:04x}".format(f))
    #  f = myi2c.read_word_data(0x36,0x0b) # CFG0bh
    #  print("ConFG 0bh","{:04x}".format(f))
    #  f = myi2c.read_word_data(0x36,0xab) # CFG2abh
    #  print("ConFG2 abh","{:04x}".format(f))
     f = myi2c.read_word_data(0x0b,0xb5) # nCFG
     print("npackCFG","{:04x}".format(f))
     f = myi2c.read_word_data(0x0b,0xbb) # nHibCFG
     print("nHibCFG","{:04x}".format(f))
     
     return()

def clear_prot_stat():
    run3 = time.localtime().tm_sec
    if run3 % 10 == 0:
        myi2c.write_word_data(0x36,0x61,0x00)
        myi2c.write_word_data(0x36,0x61,0x00)   # write unlock
        myi2c.write_word_data(0x36,0x00,0x00)
        myi2c.write_word_data(0x36,0xaf,0x00)
        myi2c.write_word_data(0x36,0xd9,0x00)
        myi2c.write_word_data(0x36,0x00,0x00)
    return()
   
def read_reg_prot():
   
    f = myi2c.read_word_data(0x36,0xd9) # prot status
    print("ProtStatus","{:04x}".format(f))
    f = myi2c.read_word_data(0x36,0xaf) #prot alert
    print("ProtAlrt","{:04x}".format(f))
    f = myi2c.read_word_data(0x36,0x00) # status
    print("status","{:04x}".format(f))
    f = myi2c.read_word_data(0x0b,0xa8) # status
    print("nBattstatus","{:04x}".format(f))
    
   # myi2c.write_word_data(0x0b,0xf1,0x00)
    return()
    
def read_Volt():
    f = myi2c.read_word_data(0x36,0x1a) # min V cell
    print("V Cell","{:04x}".format(f),"{:0.3f}".format((f*0.078125)/1000))
    f = myi2c.read_word_data(0x36,0x19) # min V cell
    print("Av VCell","{:04x}".format(f),"{:0.3f}".format((f*0.078125)/1000))
    f = myi2c.read_word_data(0x36,0x2a) # sCharging volt
    print("charge volt","{:04x}".format(f),"{:0.3f}".format((f*0.078125)/1000))
    f = myi2c.read_word_data(0x36,0xfb) # VFOCV
    print("VFOCV","{:04x}".format(f),"{:0.3f}".format((f*0.078125)/1000))
    
    f = myi2c.read_i2c_block_data(0x36,0xD1,0x10) # block read volts
    print("V Cell 1","{:04x}".format(f[14]+f[15]*256),"{:0.3f}".format(((f[14]+f[15]*256)*0.078125)/1000))
    print("V Cell 2","{:04x}".format(f[12]+f[13]*256),"{:0.3f}".format(((f[12]+f[13]*256)*0.078125)/1000))
    print("V Cell 3","{:04x}".format(f[10]+f[11]*256),"{:0.3f}".format(((f[10]+f[11]*256)*0.078125)/1000))
    print("V Cell 4","{:04x}".format(f[8]+f[9]*256),"{:0.3f}".format(((f[8]+f[9]*256)*0.078125)/1000))
    print("Av V Cell 1","{:04x}".format(f[6]+f[7]*256),"{:0.3f}".format(((f[6]+f[7]*256)*0.078125)/1000))
    print("Av V Cell 2","{:04x}".format(f[4]+f[5]*256),"{:0.3f}".format(((f[4]+f[5]*256)*0.078125)/1000))
    print("Av V Cell 3","{:04x}".format(f[2]+f[3]*256),"{:0.3f}".format(((f[2]+f[3]*256)*0.078125)/1000))
    print("Av V Cell 4","{:04x}".format(f[0]+f[1]*256),"{:0.3f}".format(((f[0]+f[1]*256)*0.078125)/1000))
    f = myi2c.read_word_data(0x36,0xda) # Batt
    print("Batt","{:04x}".format(f),"{:0.3f}".format((f*0.3125)/1000))
    f = myi2c.read_word_data(0x36,0xdb) # PCKP
    print("PCKP","{:04x}".format(f),"{:0.3f}".format((f*0.3125)/1000))
    return()
    
def read_temps():
    f = myi2c.read_word_data(0x36,0x1b) # Temp
    print("Temp","{:04x}".format(f),"{:0.3f}".format(f/256))
    f = myi2c.read_word_data(0x36,0x16) #Avg Temp
    print("Av Temp","{:04x}".format(f),"{:0.3f}".format(f/256))
    f = myi2c.read_word_data(0x36,0x09) # Max Min Temp
    print("Max/min Temp","{:04x}".format(f))
    f = myi2c.read_word_data(0x36,0x34) # Die Temp
    print("Die Temp","{:04x}".format(f),"{:0.3f}".format(f/256))
    f = myi2c.read_word_data(0x36,0x40) # Avg Die Temp
    print("Avg Die Temp","{:04x}".format(f),"{:0.3f}".format(f/256))
    f = myi2c.read_i2c_block_data(0x0b,0x33,0x10) # block read temps
    #print("temp raw",f)
    print("temp 1","{:04x}".format(f[14]+f[15]*256),"{:0.3f}".format(((f[14]+f[15]*256)/256)))
    #print("temp 2","{:04x}".format(f[12]+f[13]*256),"{:0.3f}".format(((f[12]+f[13]*256)/256)))
    #print("temp 3","{:04x}".format(f[10]+f[11]*256),"{:0.3f}".format(((f[10]+f[11]*256)/256)))
    #print("temp 4","{:04x}".format(f[8]+f[9]*256),"{:0.3f}".format(((f[8]+f[9]*256)/256)))
    print("Av temp 1","{:04x}".format(f[6]+f[7]*256),"{:0.3f}".format(((f[6]+f[7]*256)/256)))
    #print("Av temp 2","{:04x}".format(f[4]+f[5]*256),"{:0.3f}".format(((f[4]+f[5]*256)/256)))
    #print("Av temp 3","{:04x}".format(f[2]+f[3]*256),"{:0.3f}".format(((f[2]+f[3]*256)/256)))
    #print("Av temp 4","{:04x}".format(f[0]+f[1]*256),"{:0.3f}".format(((f[0]+f[1]*256)/256)))
    return()
    
def read_amps():
    f = myi2c.read_word_data(0x36,0x28) # rec charge amps
    if f > 0x8000:
        g=f - 0x10000
    else :
        g = f
    print("Charging Amps","{:04x}".format(f),"{:0.3f}".format(g*.0015625))
    f = myi2c.read_word_data(0x36,0x1c) # amps
    if f > 0x8000:
        g=f - 0x10000
    else :
        g = f
    print("Amps","{:04x}".format(f),"{:0.3f}".format(g*.0015625))
    f = myi2c.read_word_data(0x36,0x1d) # amps
    if f > 0x8000:
        g==f - 0x10000
    else: 
        g = f
    print("Av Amps","{:04x}".format(f),"{:0.3f}".format(g*.0015625))
    f = myi2c.read_word_data(0x36,0x0a) # amps max min
    print("Amp max min","{:04x}".format(f))
    return()
    
def set_capacity():
    myi2c.write_word_data(0x36,0x4d,0x8000)
    return()
    
def read_capacity():
    f = myi2c.read_word_data(0x36,0x18) # Des Cap
    print("Des cap","{:04x}".format(f),"{:0.3f}".format(f*.005))
    f = myi2c.read_word_data(0x36,0x05) # Rep Cap
    print("Rep cap","{:04x}".format(f),"{:0.3f}".format((f>>1)*.005))
    f = myi2c.read_word_data(0x36,0x1f) # Av Cap
    print("Av cap","{:04x}".format(f),"{:0.3f}".format((f>>1)*.005))
    f = myi2c.read_word_data(0x36,0x0e) # av SOC
    print("avail SOC%","{:04x}".format(f),"{:0.3f}".format(f*1.0/256))
    f = myi2c.read_word_data(0x36,0xff) # VFSOC
    print("VF SOC%","{:04x}".format(f),"{:0.3f}".format((f*1/655.36)))
    f = myi2c.read_word_data(0x36,0x06) # Mix SOC
    print("rep SOC%","{:04x}".format(f),"{:0.3f}".format((f*1/256)))
    f = myi2c.read_word_data(0x36,0x13) # Mix SOC
    print("full SOC% 13h","{:04x}".format(f),"{:0.3f}".format(((f>>8))))
    f = myi2c.read_word_data(0x0b,0xc6) # Mix SOC
    print("full SOC% 1c6h","{:04x}".format(f),"{:0.3f}".format(((f>>8))))
    f = myi2c.read_word_data(0x36,0x0d) # Mix SOC
    print("Mix SOC%","{:04x}".format(f),"{:0.3f}".format(int(f*1/655.36)))
    f = myi2c.read_word_data(0x36,0x0c) # Q residual
    print("Qresid","{:04x}".format(f),"{:0.3f}".format(f*.005))
    f = myi2c.read_word_data(0x36,0x4d) # Qh
    #print("Qh mAh","{:04x}".format(f),"{:0.3f}".format(f*.005))
    g = myi2c.read_word_data(0x36,0x4e) # Ql
    print("Q Ah","{:04x}".format(f),"{:04x}".format(g),"{:0.3f}".format((f+g/65536)*.005))
    f = myi2c.read_word_data(0x36,0x10) # Full Cap rep
    print("Full Cap rep","{:04x}".format(f),"{:0.3f}".format((f>>1)*.005))
    f = myi2c.read_word_data(0x36,0x2b) # Mix Cap rep
    print("Mix Cap rep","{:04x}".format(f),"{:0.3f}".format((f>>1)*.005))
    return()
    
def ship_mode():
    f = myi2c.read_word_data(0x36,0x0b)# config reg
    print("Config","{:04x}".format(f))
    g = myi2c.read_word_data(0x0b,0xb0)# config reg
    print("nConfig","{:04x}".format(g))
    g = myi2c.read_word_data(0x36,0xab)# config reg
    print("Config2","{:04x}".format(g))
    myi2c.write_word_data(0x36,0x61,0x00)
    myi2c.write_word_data(0x36,0x61,0x00)   # write unlock
    myi2c.write_word_data(0x36,0x0b,f&0x480) # Set PB enable and Ship mode
    f = myi2c.read_word_data(0x36,0x0b)# config reg
    print("Config","{:04x}".format(f))
    return()
    

#reload_nv()   
#innit17320()  
#clear_prot_stat()
read_cfg()
#check_updates()
#read_reg_prot()
time.sleep(5)
set_capacity()
x = 0

while True:
    clear_prot_stat()
    time.sleep(0.2)
    read_reg_prot()
    read_Volt()
    read_amps()
    read_capacity()
    read_temps()
   # read_cfg()
    time.sleep(.51)
    # x+=1
    # if x > 100:
    #     ship_mode()
    #     break
    