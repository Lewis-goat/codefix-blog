---
title: How to read a Jura service menu safely
description: What the Jura service menu shows, how to read the error counter without touching calibration, and why writing values is a bench job.
---

A Jura that has thrown an error code once or twice often seems fine again after a restart, which leaves an awkward question hanging: was that a one-off glitch or the beginning of a real fault? The answer usually sits in the machine's **service menu** — a diagnostic layer beneath the normal coffee menu that records faults and operating statistics. Reading it is genuinely useful, and it is safe, provided you treat it like a car's odometer: a read-out of facts, not a set of dials to turn.

## What the service menu actually is

The service menu (also called the engineering or technician menu) exists so repair technicians can read a machine's history without opening the case. On most generations it is reached with a button sequence held while the machine switches on, but the exact combination varies by model and production year, and Jura deliberately leaves it out of the user manual. If you are not certain of the sequence for your specific machine, it is safer to ask an official [Jura service partner](https://www.jura.com) than to experiment: on some models, holding a different combination at power-up starts a test routine rather than a menu, and an unintended rinse or pump test is an unwelcome surprise.

## What the menu can show you

### The error counter and error log

This is the most valuable screen in the menu. Most generations keep a cumulative count of faults, and many also store the most recent codes. A single entry dating back six months means something completely different from an entry that climbs every week. When the same code keeps returning, our guides to [Jura error 2](https://codefixcoffee.com/jura/automatic-machines/error-2/), [error 8](https://codefixcoffee.com/jura/automatic-machines/error-8/) and [error 6](https://codefixcoffee.com/jura/automatic-machines/error-6/) explain what each one means and how far a home fix can realistically go.

### Operating counters

Brew cycles, switch-on counts, and rinse or descaling totals. This is the machine's honest maintenance record. It is worth checking before buying a second-hand Jura, and it tells you when a worn part is simply due rather than defective.

### Live values, model-dependent

Some generations can display live component states while the machine runs. Treat these as gauges to look at, nothing more.

## Reading it safely: five ground rules

1. Start with the machine off and cool, the water tank properly seated, and no error currently on screen. You want to note values, not debug a new fault at the same time.
2. Photograph every screen you land on before navigating away. Displays time out, and a photo preserves exact numbers with no transcription errors.
3. Write the date and the machine's serial number next to your notes. A reading only becomes useful as part of a time series.
4. Navigate with short presses of the buttons you already know from the normal menu. Avoid holding a button while a value is displayed — on several generations, a long press is precisely how a value gets changed.
5. Leave the way you came in. Exit through the menu's own exit path and let the machine settle on its normal standby screen before you unplug anything.

One habit deserves to be named: do not reset an error counter to make a fault "go away". Resetting repairs nothing — it destroys the evidence a technician would have used.

## Why writing values is a bench job

The writable settings fall into groups that are all calibrated at the factory with equipment no kitchen has.

- **Flow and pump parameters** are set by timing measured volumes of water through the circuit. Guess a value and your 40 ml espresso can silently become something else — or the machine faults because filling takes longer than the electronics expect.
- **Temperature parameters** are matched to the specific heater and sensor fitted to your unit. A wrong offset means water that is too cool (sour, weak shots) or running hotter than intended, and that second option spends a safety margin you do not own.
- **Mechanical references**, such as grinder stops and brew-unit positions, are set with the machine opened up on a bench, usually right after the relevant part has been replaced.

This is why a technician performs these steps as part of a repair, not before one. Writing a wrong value can also manufacture error codes that never existed before, which sends any diagnosis down the wrong track. Community teardowns on [iFixit](https://www.ifixit.com) give a good sense of how much measured, patient work sits behind those innocent-looking numbers.

## Putting your reading to work

A dated photo of the error counter is the best document you can hand a service partner: it shortens paid diagnostic time and often sharpens the repair estimate on the spot. If your machine is already showing a recurring code, start from our [Jura repair hub](https://codefixcoffee.com/jura/) for model-specific guidance. And if you also run a DeLonghi, our [DeLonghi hub](https://codefixcoffee.com/delonghi/) covers the equivalent diagnostics for that side of the counter.
