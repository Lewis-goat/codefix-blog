---
title: Sage/Breville ER codes: reading the hidden service table
description: Sage and Breville espresso machines show ER codes from a service table Breville never published. How ER01-ER18 work and why Oracle numbering differs.
---

If a Breville espresso machine stops dead and shows ER05 on the panel, the manual will not tell you what it means. That is not an oversight: Breville's error codes come from the internal service tables the company uses for repairs and does not publish for owners. The same hardware is sold in the UK under the **Sage** brand — identical machines, Sage on the badge — so an ER code on a Sage Barista Touch means exactly what it means on a Breville one. Our [Breville / Sage section](https://codefixcoffee.com/breville/) covers the current range; this post explains how the numbering is organised, so a code you have never seen still tells you something useful.

## Why Breville doesn't publish them

The user manual covers cleaning and descaling, not diagnostics. The full code tables live behind each machine's service mode: password-protected screens intended for technicians, with stored error counters and live sensor readings. Because the codes are a repair tool rather than a consumer feature, Breville has never issued them in a public document, and most owners only ever see the single code that caused a shutdown. The contrast is stark: Miele prints its F-code meanings in the operating instructions, which is why the [Miele code pages](https://codefixcoffee.com/miele/) can quote the manual directly.

## The Barista Touch table: ER01 to ER18

The Barista Touch (BES880) and the Barista Touch Impress (BES881) — which shares the same control-board family and code table — use an 18-entry table. Once you see the structure it reads easily: the sensor codes arrive in **groups of four**, one group per sensor, cycling through open circuit at start-up, open circuit during operation, short circuit at start-up, and short circuit during operation.

- **ER01 to ER04** — the ThermoJet ("ferro") heater's temperature sensor in its four open/short variants. [ER01](https://codefixcoffee.com/breville/barista-touch-bes880/er01/) is the start-up open-circuit entry.
- **ER05 to ER08** — the milk-jug temperature sensor, the small probe on the drip-tray area that reads the jug while the wand textures milk. ER05, the start-up open circuit, is the single most reported Barista Touch code, and all four entries share one fix.
- **ER09 to ER12** — the inline (brew-water) temperature sensor, same four-variant pattern.
- **ER13 and ER14** — flow-meter count errors, at start-up and during operation: the pump ran and the machine could not count the water moving through it.
- **ER15** — a communication fault between internal electronic modules; often a worked-loose ribbon cable or a wet connector rather than a dead board.
- **ER16 and ER17** — the grinder: motor overheated and shut itself down for protection, then motor timed out without finishing its task.
- **ER18** — E-fast protection, an electrical or safety fault such as leakage current; the code that can also trip the RCD or GFCI on your socket.

## The Oracle family numbers differently

Buy an Oracle and the same idea gets a longer table. The Oracle (BES980) and Oracle Touch (BES990) share a 32-entry list, but the BES980 displays entries as "Error 1" to "Error 32" while the BES990 prefixes them ER. The first sixteen follow the quartet logic across four sensors — steam boiler codes 1 to 4, coffee boiler codes 5 to 8 (with [Error 8](https://codefixcoffee.com/breville/oracle-bes980/error-8/) the coffee-boiler sensor shorting during operation), heated group head 9 to 12, steam wand 13 to 16. The rest covers boilers not heating (17 to 19), steam-boiler level and fill faults (20 and 21), flow-meter problems (22 and 23), level probes and overheating (24 to 27), a board communication fault at 28, the grinder at 29 and 30, the tamping motor at 31, and a steam-boiler leak or refill failure at 32.

Two smaller tables complete the family. The Oracle Jet (BES985) uses a shorter E1-to-E19 table of its own, and the Dual Boiler (BES920) keeps two-digit codes 00 to 12 hidden in a self-check menu rather than on the normal display — so a Dual Boiler can sit on a fault you have never seen on screen.

## Reading the hidden error log yourself

Because the tables are service data, the way to read your machine's history is through the same service screens. The routes are technician-flavoured but well documented by repairers:

- **Barista Touch and Oracle Touch** — switch off at the wall, hold the front Power button while switching the wall power back on, release when the logo appears, enter the service password 00000, then open Error Counter for stored faults or Live Debug for live temperatures and water levels.
- **Barista Touch Impress** — the same button sequence, but the service password is 02015.
- **Oracle BES980** — with the machine plugged in but switched off, hold 1 CUP, 2 CUP and POWER together for at least a second; after the long beep, press the SELECT dial to open Error Storage and step through errors 1 to 32 with their stored counts.

Treat these as read-only screens: note what is stored, leave settings alone, and clear the log only after a repair, so you can tell whether a code comes back.

## What the repairs typically cost

Even against an unpublished table, the economics are predictable. Temperature-sensor assemblies run about €25 to €95 depending on which sensor (steam-wand and milk-jug sensors are the dear ones), and o-ring kits €10 to €20; a milk-sensor repair kit is around €30 to €50 against €80 to €95 for the genuine assembly. Out-of-warranty manufacturer quotes for internal faults are commonly €300 to €500, so a sensor-level fix at independent-repairer rates is usually the better path. UK readers can check the [UK edition of the site](https://codefixcoffee.com/uk/) for Sage-branded coverage of the same tables.
