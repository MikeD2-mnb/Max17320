# Max17320
mini autonomus bms configure for LifePO4 cells
This has 2 pieces of code that run on a Beaglebone black or green, using i2c interface 2, though this can easily be changed. 
Can be ported easily to any unix platform running python wiht i2c interface.
Once configured, the chip is autonomous, data can be read over the i2c interface.
one piece of cose (i2ctest3.py) will program the constants needed for the run into volatile memory.
The other (Max17320init_test.py) will permanently program the NV rom.
Code not guaranteed bug free.
