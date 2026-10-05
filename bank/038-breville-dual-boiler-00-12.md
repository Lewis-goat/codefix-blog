---
title: Breville Dual Boiler 00–12: the two-digit codes
description: The Breville Dual Boiler BES920 reports codes 00 to 12 in a hidden self-check menu: what each family means, steam versus brew side, and the fixes.
---

Breville's espresso machines mostly announce faults on their normal display: the Barista Touch shows ER-codes, the Oracle shows "Error" codes, the Oracle Jet uses E-numbers. The **Dual Boiler BES920** does it differently. Its fault table is a set of plain two-digit codes, **00 through 12**, and they live in a hidden self-check menu rather than on the everyday screen. You will not see them by watching the front panel during a normal day — you have to know the button combination.

The numbering is worth understanding, because it is a tidy table: the block a code sits in tells you what kind of fault it is, and within each block the code names the part that is complaining.

## Reading the error log

The log is reached from the self-check menu:

1. Switch the machine off at the wall.
2. Hold **EXIT** and **MANUAL** while switching the power back on; the self-check menu appears.
3. Press **MENU** to reach item 3, the error log. Item 4 shows the boiler level status, reported as LLL (low) or HHH (high).
4. In the error log, **MENU** steps through codes 00 to 12, each with a stored count.
5. At "ErSt", hold **MANUAL** until it beeps to clear the stored codes; the cup counter is not reset.

Counts matter as much as codes. A fault with a count of one from a year ago is history; a fault whose count climbs every week is a live problem building.

## What the 00 family covers

Codes **00 to 05** are the temperature-sensor block, arranged as three pairs. In each pair, the lower number means the sensor is **not detected** — the board reads it as an open circuit — and the higher number means it is reading as a **short circuit**:

- **00 and 01** — steam boiler temperature sensor, not detected then short.
- **02 and 03** — coffee boiler temperature sensor, not detected then short.
- **04 and 05** — group head heater temperature sensor, not detected then short.

The BES920 has dual stainless boilers plus a heated group head, so those three sensors cover the machine's three heated zones. The [code 00 page](https://codefixcoffee.com/breville/dual-boiler-bes920/00/) deals with the steam boiler sensor, and its practical advice transfers to the other five: reseat and inspect the sensor plug before buying parts, and look for moisture, because water bridging a connector reads as an open or a short depending on how it sits. Genuine NTC sensor assemblies run about €25 to €90 depending on which of the three it is; o-ring kits are €10 to €20 and are often the real culprit anyway.

## Steam side versus brew side

The rest of the table splits along the same hardware line as the sensor pairs:

- **Steam boiler:** 06 (pump issue during startup), 07 (water level or pump fault) and 11 (overheating detected).
- **Coffee boiler — the brew side:** 08 (pump or flow issue), 09 (water level fault) and 10 (overheating detected).
- **Group head:** 12 (overheating detected).

### The codes that travel together

These faults interlock, which is why reading the whole log beats reading one code. Code 08 means the pump ran and the flow meter saw nothing — most often scale on the flow meter's paddle, or a small pump buzzing without moving water, and descaling is the first move either way. Code 11, a steam boiler over-temperature, usually follows a boiler that is not being refilled — check whether 07 or 08 also has a count — because the element keeps heating a low boiler; a leaking probe seal is the other cause. Before ordering anything, read item 4 in the self-check menu: a level status that disagrees with what you hear when the machine fills tells you which side the fault is really on.

Code 12, group head overheating, is the rarer end of the table, and the one where repeated recurrence matters most — an overheat that keeps coming back points at the power board latching a heater on rather than a sensor drift. The [code 12 page](https://codefixcoffee.com/breville/dual-boiler-bes920/12/) goes through it.

## What the parts cost

- Descaler for the flow and level codes: about €10, and it fixes a real share of them.
- Fill pump: €30 to €60.
- Steam boiler probe and o-ring kit: about €85; o-ring kits alone €10 to €20.
- Thermal fuse: €10 to €20 — but find out why it blew.
- Triac or power board: €80 to €150.

Out-of-warranty Breville service quotes for internal faults are commonly €300 to €500 and up, so a pump or a sensor is worth doing yourself; a board on an older machine is worth a quote first. Water and mains electricity share the top of the boiler, so unplug before touching probes.

For how the other machines in the range word their codes, see the [Breville section](https://codefixcoffee.com/breville/) — the ER-family machines share diagnosis ideas but not numbering. In the UK the brand is sold as Sage; UK readers can use the [UK edition](https://codefixcoffee.com/uk/) of the site.
