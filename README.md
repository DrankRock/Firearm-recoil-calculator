# Firearm-recoil-calculator
A very simple python recoil calculator for firearms using Wikipedia's recoil formula.

## Install
```shell
git clone https://github.com/DrankRock/Firearm-recoil-calculator.git
```

## Usage
```shell
Usage : python3 recoil.py [muzzle length] [velocity of bullet out of the muzzle] [bullet weight] [gun weight]
Example with the Famas G2 : $ python3 recoil.py 0.488 925 0.062 4.170
Note : Weight in kg, length in cm, velocity in m/s
```
## Output example
```shell
------- Bullet -------
[Speed]                  - 925.00 m.s^(-1)
[Acceleration Duration]  - 0.00106 s
[Acceleration]           - 876664.96 m.s^(-2)
[Kinetic Energy]         - 26524.38 J
--------- Gun --------
[Speed]                  - 13.75 m.s^(-1)
[Acceleration Duration]  - 0.00106 s
[Acceleration]           - 13034.35 m.s^(-2)
[Kinetic Energy]         - 394.37 J
Recoil of 394.37J at speed 13.75m/s for a duration of 0.00106s.
```  
Note : this was obtained using the data in the example, for the Famas G2.

### Dependencies  
None.

