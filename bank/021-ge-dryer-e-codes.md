---
title: GE dryer E-codes: thermistors, fuses and the tachometer
description: GE dryer E1, E3-E6, E4, E8 and E11 explained: door switch, thermistors, thermal fuse and motor tach, with vintage differences and costs.
---

GE is one of the few major appliance makers with no official error-code page for its dryers. The E-codes exist and the board stores them, but nobody tells owners what they mean. The pattern is learnable, though: GE dryer codes cluster around four areas, namely the door circuit, the two temperature sensors, the heating safety fuses, and the drive motor with its tachometer. Our [GE dryer section](https://codefixcoffee.com/ge/dryer/) covers each code in detail; this post maps how the family fits together and where the vintage traps are.

## First, read the stored code

On GTD and GFD dryers from 2016 on, you can pull the last stored error yourself. With the dryer off, press and hold the **Signal** and **Temp** buttons together for five seconds to enter service mode; the most recent fault shows on the display. On SmartHQ-enabled machines the app lists stored codes. If you only want to clear the board, unplug the dryer for five minutes.

## E1: the door switch

[E1](https://codefixcoffee.com/ge/dryer/e1/) means the board does not see the door as closed. It is usually mechanical rather than electronic: a worn latch, a bent strike, or a switch that has stopped clicking.

- Close the door firmly and press Start — a half-latched door is the most common cause.
- Check the latch strike on the door for a bent or broken tab.
- Unplug the dryer, remove the front panel and check the door switch plug; a switch that no longer clicks when pressed needs replacing, at roughly €10 to €25 for the part.

## E3 to E6: the thermistors

GE dryers watch air temperature with two thermistors: the inlet sensor on the heater housing and the outlet sensor on the blower housing. The [E3 to E6 family](https://codefixcoffee.com/ge/dryer/e3-to-e6/) fires when one of them reads open or shorted. Loose or corroded wiring causes as many of these as failed sensors, and a genuinely blocked vent can overheat a healthy dryer into tripping them.

1. Unplug for 30 seconds and restart.
2. Clean the lint filter and confirm the vent run is not blocked.
3. Open the cabinet and check the thermistor plugs and harness for loose or corroded contacts.
4. Meter the thermistor — about 10k ohms at room temperature is healthy; replace it if it reads open.

A replacement thermistor is €10 to €25. On some models E6 is instead an airflow-restriction code, so confirm the meaning for your model before ordering parts.

## E4: the thermal fuse

[E4](https://codefixcoffee.com/ge/dryer/e4/) is the no-heat code: the drum turns but nothing dries, because a safety fuse has opened. Thermal fuses blow for a reason — restricted airflow from lint or a blocked vent let the heater overheat. Fix the airflow first or the new fuse blows too, and never bypass a thermal fuse; it is the part that keeps a genuine overheat from becoming a fire.

1. Clean the lint filter and the whole exhaust run to the outside.
2. Meter the thermal fuse and the high-limit thermostat on the heater housing; replace whichever reads open.
3. Run a short cycle with the vent briefly disconnected to confirm heat returns, then reconnect.

The fuse itself is €5 to €15; the high-limit thermostat €10 to €25.

## E8 and E11: the tachometer and the motor

[E8](https://codefixcoffee.com/ge/dryer/e8/) is the tachometer code on current GE dryers: the board switched the motor on and never received a speed signal back. The tach wiring may be loose, the drum may be jammed — a slipped belt, or something behind it — or the tach or motor has failed. Because the tach is part of the motor assembly, a confirmed tach failure means a motor, at €80 to €150; a belt is €15 to €25.

E11 sits next to it: the motor is not doing what the board asks — a worn belt, a seized drum roller, or the motor start switch or motor itself. Turn the drum by hand first; stiffness points at rollers or bearings rather than the motor. A motor that hums without starting, with the belt off, is a motor replacement; rollers run €20 to €40 a set.

## Vintage differences

Three vintage traps catch people out. First, the same number is not always the same fault: on some older and combo units, E8 is a drum-light or drain fault rather than the tachometer, so confirm which dryer you have before buying parts. Second, E6 is an airflow code on some models and a thermistor code on others. Third, the Signal-and-Temp service mode described above applies to GTD/GFD machines from 2016 on — on older models you are working from whatever the display shows at the moment of failure. The family also includes E7, for a power-supply problem where the dryer is not seeing both legs of its supply, and E14, a stuck key on the control panel; neither is heat-related.

## What the repairs cost

Sensor- and switch-level repairs are cheap: door switches €10 to €25, thermistors €10 to €25, thermal fuses €5 to €15, belts €15 to €25, drum rollers €20 to €40. The expensive item is the drive motor at €80 to €150 — on an older dryer that is a judgment call rather than an obvious yes. A technician's home visit runs about €120 to €250 for diagnosis plus the part — worth it for motor-circuit work if you would rather not open the cabinet.
