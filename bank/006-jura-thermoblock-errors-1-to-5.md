---
title: "Jura errors 1 to 5: the thermoblock family explained"
description: "Jura Errors 1 to 5 all trace back to the thermoblocks, their NTC sensors or thermal-fuse cords. Which code maps to which part, and the Error 2 cold trap."
---

Jura error codes 1 through 5 look like a random handful of numbers, but they share one subject: heat. Every one of them traces back to the thermoblocks — the compact inline heaters that make coffee water and steam — or to the sensors and protective cords that watch over them. Once you can read the family, a code tells you which heater is unhappy and whether the problem is measurement, temperature or power.

## Two heaters, five codes

A Jura has two thermoblocks. The coffee thermoblock heats brew water; the steam thermoblock feeds the steam and hot-water side. Each carries an NTC sensor — a resistor whose value changes with temperature — that reports back to the control board, and each is protected by thermal-fuse cords that cut power if the block overheats. Errors 1 to 5 are the board's way of saying one of those elements is misbehaving:

- **Errors 1 and 2** point at the coffee thermoblock's sensor circuit.
- **Errors 3 and 4** point at the steam thermoblock — reading too low, or overheating.
- **Error 5** is the heater itself not delivering.

## The coffee-side codes

### Error 1: coffee thermoblock sensor fault

[Error 1](https://codefixcoffee.com/jura/automatic-machines/error-1/) means the board cannot get a sane reading from the temperature sensor on the coffee thermoblock — on the S, X, J and Z families it is the classic sensor fault, and on the F and E80 it typically means a damaged sensor. One quirk worth knowing: a machine that has just come in from a cold car or garage can trip this code without anything being broken. If it appears on a warm machine and returns instantly after a restart, the sensor circuit is open — the sensor, its cable, or the thermal-fuse cords feeding the block.

### Error 2: sensor interrupted — or the machine is just cold

[Error 2](https://codefixcoffee.com/jura/automatic-machines/error-2/) is the most common Jura code of all, and it has a split personality. The benign version: the machine is below roughly 10 °C and the heater is deliberately locked out until it warms up — common with machines delivered in winter or kept in a cold room. The real version: the coffee thermoblock sensor or the thermal-fuse cords have gone open circuit.

That makes the warm-up test the diagnostic. Bring the machine to room temperature — owners use a hair dryer on low blown into the water-tank cavity for five minutes, or a tank filled with warm (not hot) water — then restart. If the code clears, nothing is broken; keep the machine somewhere warmer. If it persists on a warm machine, the sensor circuit is open and the NTC and fuse cords need checking inside.

## The steam-side codes

### Error 3: steam thermoblock reading low

[Error 3](https://codefixcoffee.com/jura/automatic-machines/error-3/) is the steam-side mirror of Error 1: the steam thermoblock is not reporting temperature, because of its sensor, its cable, or a machine that is still too cold. One extra angle: heavy scale slows heating enough to trip the check on some firmware, so a full descale belongs on the list before anything is dismantled. Inside, the sensor cable is worth inspecting where it flexes.

### Error 4: steam thermoblock overheating

[Error 4](https://codefixcoffee.com/jura/automatic-machines/error-4/) is the one to take seriously. The steam thermoblock ran hotter than the board expected — either the sensor is under-reading (scale insulating it, corroded contacts) or the power board failed to cut the heater. Jura lists Errors 2 and 4 as the two most common repairs. After cooling and descaling, the sensor is the first replacement; if the block overheats again with a new NTC in place, the power board is not switching the heater off and must be replaced (budget €120 to €250). A heater that will not switch off is a fire risk: do not leave the machine powered unattended while this code is live.

### Error 5: heater not reaching temperature

[Error 5](https://codefixcoffee.com/jura/automatic-machines/error-5/) means the heater was switched on and the temperature never climbed. On a Jura that is almost always the thermal-fuse cords protecting the thermoblock, which blow after an overheat or simply with age; a dead thermoblock element is the other cause. A very cold machine can also trigger it, so warm it up first. Inside, meter both fuse cords and the element: whichever reads open is the part to replace — then find out why the fuses blew (scale, a stuck relay, or a dry-fire when the tank ran empty).

## The part that links them together

Across this family, the thermal-fuse cords and the NTC sensors are the recurring characters — a genuine Jura NTC runs about €25 to €40, a fuse-cord set €15 to €30, and a thermoblock €90 to €180. When a sensor is replaced, practitioners replace the fuse cords at the same time. And one pattern matters: a fuse cord that blows again within days means the power board is latching the heater on, not that the new cord was unlucky.

Be aware that Jura cases use security screws and the thermoblocks carry mains voltage — this family is a bench repair unless you are set up for it. Worth fixing on S, Z, GIGA and newer E-series machines; on a ten-year-old Impressa, weigh the quote against a refurbished unit. The [Jura error-code hub](https://codefixcoffee.com/jura/) puts the rest of the range in context.
