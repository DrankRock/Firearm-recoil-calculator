
# A very simple gun recoil calculator using Wikipedia's formula.
# The soil purpose of this was to prove an argument, it is thus very simple.
# Don't hesitate to ask for any wanted improvements.

# Author : Matvei Pavlov
# Version : 0.1
# Start date : 9 april 2022

import sys

completeOutput = True

def usage():
	print("Usage : python3 recoil.py [muzzle length] [velocity of bullet out of the muzzle] [bullet weight] [gun weight]")
	print("Example with the Famas G2 : $ python3 recoil.py 0.488 925 0.062 4.170")
	print("Note : Weight in kg, length in cm, velocity in m/s")

if len(sys.argv) != 5:
	usage()
	sys.exit(1)

length = float(sys.argv[1])
velocity = float(sys.argv[2])
bullet = float(sys.argv[3])
gun = float(sys.argv[4])

print("Calculating recoil with arguments : {} ; {} ; {} ; {}".format(length, velocity, bullet, gun))
# duration of the acceleration of the bullet :
duration = 2*(length/velocity)
# acceleration of bullet
acceleration = velocity/duration
# convert acceleration to force :
force = acceleration*bullet
# acceleration of the gun :
gunAcc = force/gun
# velocity of the gun while recoil happens :
gunVelocity = gunAcc*duration
# cinetic energy of bullet :
cinBul = (bullet*velocity*velocity)/2
# cinetic energy of gun :
cinGun = (gun*gunVelocity*gunVelocity)/2
if(completeOutput):
	print("------- Bullet -------")
	print("[Speed]                  - {:.2f} m.s^(-1)".format(velocity))
	print("[Acceleration Duration]  - {:.5f} s".format(duration))
	print("[Acceleration]           - {:.2f} m.s^(-2)".format(acceleration))
	print("[Kinetic Energy]         - {:.2f} J".format(cinBul))
	print("--------- Gun --------")
	print("[Speed]                  - {:.2f} m.s^(-1)".format(gunVelocity))
	print("[Acceleration Duration]  - {:.5f} s".format(duration))
	print("[Acceleration]           - {:.2f} m.s^(-2)".format(gunAcc))
	print("[Kinetic Energy]         - {:.2f} J".format(cinGun))
print("Recoil of {:.2f}J at speed {:.2f}m/s for a duration of {:.5f}s.\n".format(cinGun,gunVelocity,duration))
