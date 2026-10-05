---
title: Thermoblock vs boiler: long-term failure modes
description: Which parts fail in thermoblock and boiler coffee machines, how NTC sensor faults differ from heating element faults, and what that means for repairs.
---

When an espresso machine dies slowly rather than suddenly, the culprit is usually the heating system — and which parts fail first depends on one design decision the buyer rarely thinks about: how the water is heated. Consumer machines almost all use a thermoblock; traditional espresso machines use a boiler. Knowing which one sits inside your machine tells you what is likely to break, what a given error code is pointing at, and whether a repair bill makes sense.

## Two ways to heat water

A **thermoblock** is a compact aluminium or stainless block with a serpentine channel machined into it and a heating element pressed against it. Only a few tens of millilitres of water are heated at a time, which is why compact bean-to-cup and capsule machines reach brewing temperature in under a minute and can switch to steam quickly.

A **boiler** is a small vessel that heats water in bulk, from a third of a litre up to several. Single-boiler machines switch one vessel between brew and steam temperatures; dual-boiler designs such as the [Breville Dual Boiler BES920](https://codefixcoffee.com/breville/dual-boiler-bes920/00/) (sold as Sage in the UK and Ireland, per [Sage Appliances](https://www.sageappliances.co.uk)) keep one boiler for each job; prosumer machines thread a heat exchanger through a single steam boiler.

### What typically fails in a thermoblock

- Scale in the channel, which narrows flow, insulates the metal and weakens steam long before anything registers as a fault.
- The **NTC temperature sensor** — a small thermistor clamped to the block, whose connector oxidises or whose resistance drifts with age and heat cycles.
- The heating element itself, or the one-shot thermal fuse that opens when heavy scale causes the block to run dry and overheat.
- The O-rings at the inlet and outlet fittings, which harden and begin to weep.

### What typically fails in a boiler

- The heating element gasket — the seal where the element enters the vessel. A slow weep there corrodes the connectors beneath it.
- Scale on an immersed element: a heavy crust makes the element overheat until it burns open or leaks current to earth and trips the household RCD.
- Overheat thermostats and pressure switches, which drift out of calibration or scale up internally.
- High-current wiring and crimp terminals, which fatigue with years of thermal cycling.

## NTC sensor faults versus element faults

The two most common heating faults announce themselves differently, and telling them apart saves an unnecessary parts order.

- **NTC faults surface at startup.** The machine checks its temperature readings during self-test, so an open or shorted sensor usually produces an error before any coffee is attempted. The part itself is cheap — typically €10–€25 — and replacement is mostly connector and clip work, well documented in [iFixit](https://www.ifixit.com) teardowns.
- **Element faults surface as heat that never arrives.** The pump runs, the lights behave, but the water stays cold; or the machine times out partway through heating; or it trips the RCD the instant it would heat, which points to insulation breakdown. A replacement element or thermoblock assembly runs €60–€150 before labour, which on a €300 machine is a genuine repair-or-replace decision.

## What error codes suggest in each design

The architecture changes what a temperature-related code most likely means.

- On **thermoblock machines**, heat-related codes often trace back to scale rather than a dead part: the insulating crust simultaneously upsets the sensor reading and stretches the heating time. A thorough descale is a reasonable first move before ordering sensors. Numeric codes on Jura automatics — [Error 1](https://codefixcoffee.com/jura/automatic-machines/error-1/) and [Error 5](https://codefixcoffee.com/jura/automatic-machines/error-5/) among them — have specific meanings covered on their own pages, but the diagnosis path runs through the heating block and its sensors either way.
- On **boiler machines**, slow-heat timeouts and steam-pressure complaints more often mean the element, a thermostat or a pressure component. Scale usually shows itself as weak steam months before any code appears.
- Some warnings are reminders, not faults. A [descale light that stays on after a completed cycle](https://codefixcoffee.com/delonghi/magnifica-dinamica/descale-light-stays-on-after-descaling/) is a reset or rinse problem, not a failing heater — and [Saeco's Error 14](https://codefixcoffee.com/philips-saeco/espresso-machines/error-14/) has its own diagnosis, separate from heating faults entirely.

## Making either design last

1. Sort the water first. Filtered or correctly softened feedwater prevents most of the faults listed above, in both architectures.
2. Descale on schedule with a manufacturer-named citric or lactic acid solution. Many manufacturers advise against vinegar, which attacks aluminium thermoblocks.
3. Treat weak steam and slow heat-up as early warnings rather than quirks — both are scale symptoms with weeks of runway left.
4. If the machine trips the house RCD, stop resetting it. That pattern indicates an insulation fault, and it needs a qualified check before further use.

Neither design is universally more reliable. Thermoblocks keep machines compact and cheap but punish neglected water; boilers are robust and repairable but their failures tend to cost more when they come. Buy the design that matches your maintenance appetite, and give it water it can live with.
