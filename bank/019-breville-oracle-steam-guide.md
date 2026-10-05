---
title: Breville/Sage Oracle steam and ER codes: what to check first
description: Steam faults on the Breville/Sage Oracle: what the steam-side Error and ER codes mean, the purge routine to try first, and when scale is the real fault.
---

The steam side of a Breville Oracle is its busiest place: a stainless steam boiler, an auto-texturing wand, level probes and a fill pump, all at temperature daily. It also produces a large share of the machine's error codes. The Oracle family uses a 32-entry service table that Breville does not publish, and in the UK the same hardware wears a **Sage** badge — the codes are identical. Before you assume a broken part, work through the cheap checks: most steam-side stops are a blocked wand tip, a purge that did not happen, or limescale on a probe.

## Where the steam codes sit in the Oracle table

The Oracle (BES980) and Oracle Touch (BES990) share one table; the BES980 shows entries as "Error 1" to "Error 32" while the BES990 prefixes them ER. The steam-related entries cluster in five places:

- **Error 1 to 4** — the steam boiler temperature sensor, cycling through open circuit at start-up, lost during operation, and short circuit in both situations. One sensor, four ways to report it.
- **Error 13 to 16** — the same quartet for the steam wand's own temperature sensor, the probe that stops auto-texturing at the right milk temperature. It lives in the wettest place on the machine.
- **Error 18** — the steam boiler is not heating up normally.
- **Error 20 and 21** — steam boiler water level or fill-pump problems, and a level-probe reading that does not match what the board expects.
- **Error 26** — the steam boiler overheated above target; **Error 32** is a steam boiler leak or refill failure.

Not everything near the wand is steam-side: codes 5 to 8 belong to the coffee boiler's sensor, with [Error 8](https://codefixcoffee.com/breville/oracle-bes980/error-8/) its short-circuit-during-operation entry. Reading the stored log helps you tell the families apart — on the BES980, hold 1 CUP, 2 CUP and POWER together with the machine off to open Error Storage and step through all 32 codes with their counts.

## What to check first: the purge routine

Weak or spluttering steam, or a code straight after a milk drink, usually points at the wand tip rather than the boiler:

1. Unplug the machine and let the wand cool.
2. Unscrew the steam tip and soak it in hot water with a little descaler; clear every hole with the pin on the cleaning tool.
3. Run the purge — about ten seconds of steam into the drip tray with the tip off, then again with it on.
4. Purge the wand after every milk session from now on; dried milk in the tip is what starts most of these stops.

If the machine monitors steam pressure, as the Oracle Jet does with its E16 code, a crusted tip can trip a code before you even notice the steam has gone weak.

## Hardness, scale and the level probes

Where the water is hard, scale writes its own error codes. The steam boiler's level probes sit in hot water constantly, and a scaled coating insulates them so the board reads "no water" even when the boiler is full — that is the classic route to Error 20 or 21, and to Error 32's refill failure. Scale also builds in the wand path and on the fill pump's inlet. A full descale, including the steam-boiler cycle, is the cheapest diagnostic you can run and clears a surprising number of these codes on its own.

The sibling machine in the range makes the same point: the Dual Boiler keeps its codes 00 to 12 hidden in a self-check menu, and [code 00](https://codefixcoffee.com/breville/dual-boiler-bes920/00/) — the steam boiler sensor not detected — sits at the top of a table whose level and fill entries behave exactly the same way under hard water.

## When to descale rather than disassemble

Descale first, disassemble second — but know where descaling stops helping:

- **Descale first** for level, probe and refill codes (20, 21, 32), for weak steam with no code, and for any machine more than three months since its last cycle. Cost: a bottle of descaler.
- **Descale will not fix** a sensor code that returns immediately on a freshly descaled, warm machine — whether that is a steam-boiler entry from codes 1 to 4 or [Error 8](https://codefixcoffee.com/breville/oracle-bes980/error-8/) on the coffee side. A code that survives a descale points at the sensor, its cable or a connector.
- **Stop and check seals** if Error 26 recurs: a leaking steam-probe o-ring lets steam heat the sensor cable and mimics a runaway boiler. New probe o-rings are cheap; a triac board that will not switch the heater off is not.
- **Error 18** on a machine that no longer heats steam at all is usually heater-side — thermal fuse, element or board — not scale, so treat it as a repair rather than a cleaning job.

## What the parts cost

Genuine temperature-sensor assemblies run about €25 to €95 depending on which sensor it is; steam wand assemblies, which include their sensor, are around €60 to €95; a probe and o-ring kit is about €85 and a fill pump €30 to €60. Against that, out-of-warranty manufacturer quotes for internal faults are commonly €300 to €500, so a descaler bottle first and a sensor-level fix second is almost always the better arithmetic. UK readers will find the Sage-branded coverage of the same tables on the [UK edition of the site](https://codefixcoffee.com/uk/).
