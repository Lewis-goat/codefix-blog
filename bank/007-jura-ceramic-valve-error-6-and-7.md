---
title: "Jura Error 6 and 7: the ceramic valve, explained honestly"
description: "What Jura Error 6 and Error 7 really mean: the motor-driven ceramic valve, scale, the position encoder, and why Error 7 usually needs a bench repair."
---

Jura's numbered errors are refreshingly specific. Errors 1 to 5 point at the thermoblock heaters and their sensors, Error 8 at the brew group, and Error 12 at the grinder. Errors 6 and 7 both point at the same component: the electronic ceramic valve, the motor-driven disc that routes water inside the machine. The difference between them is roughly the difference between "run a descale and see" and "book a bench repair". Here is what is actually going on.

## What the ceramic valve does

Most bean-to-cup machines switch water between coffee, hot water and steam with simple solenoid valves. Higher-specified Jura machines — the Z5 through Z10, the X series, J5 to J9, the GIGA range, and newer S and E models — use an electronic ceramic valve instead. A small motor rotates a ceramic disc between positions, and the channels in that disc direct water to the coffee outlet, the hot-water spout or the steam circuit. A position sensor (an encoder) reports where the disc is at every moment, so the control board always knows it is routing water where it intended.

That feedback loop is why Errors 6 and 7 exist at all. The board commands a position, waits for the encoder to confirm arrival, and raises an error when the confirmation never comes.

## Error 6: the disc did not arrive

[Error 6](https://codefixcoffee.com/jura/automatic-machines/error-6/) means the ceramic valve is not operating correctly: the disc did not reach the position the board asked for. In practice there are three causes, in order of likelihood. Scale has stiffened the mechanism so the motor cannot turn it freely. A leaking valve seal has let water into the drive, wetting the motor and the encoder. Or the motor or its position sensor has failed outright.

The most likely cause has a free fix, so start there.

1. Run a full descaling cycle first. Scale is the number-one cause of a stiff ceramic disc, and the fix costs a tablet and an hour.
2. Restart and listen. On startup the valve cycles through its positions with an audible click. If it now completes its startup cycle, you are done.
3. If Error 6 persists, the machine has to be opened: check for water around the valve body. Dampness there means a leaking seal is contaminating the drive.
4. Cleaning or replacing the valve is the repair. The motor and the valve are normally replaced as one assembly, not separately.

Budget roughly €55 to €110 for a ceramic valve assembly, or €10 to €18 if only the seal kit is needed.

## Error 7: the serious sibling

[Error 7](https://codefixcoffee.com/jura/automatic-machines/error-7/) covers the same hardware failing harder, with the brew-group drive added in: the machine commanded the ceramic valve (on GIGA models, the multi-valve) to a position and never saw it arrive, or the brew-group drive misbehaved on the way. On the GIGA X3c and X8c it specifically indicates a faulty multi-valve, and on the GIGA 6 it is often reported as a motor or pump blockage. It is one of the few Jura codes with no reliable user-level fix.

That does not mean nothing is worth trying before you book.

1. Unplug for five minutes and restart. The startup cycle re-homes the brew group and the valve, so a transient stall can clear on its own.
2. Rule out the cheap causes: empty the grounds container and drip tray, check that nothing is jammed in the coffee outlet, and run one full cleaning programme uninterrupted.
3. If the code still returns, the usual finding inside is the valve assembly itself — a cracked ceramic disc, a jammed actuator, or a failed position encoder.

## Why Error 7 is usually a bench repair

The honest advice for this code is "workbench, unless you already service these machines". The reasons are practical rather than mysterious.

- Jura cases are held with security (oval-head Torx-Plus) screws, and mains voltage sits close to the work area.
- The machine must be fully drained before the valve can be touched, and the assembly itself is fiddly.
- After a valve or brew-group motor replacement, the mechanism needs recalibrating so the board can trust its position readings again.

Parts do exist for most models — a ceramic or multi-valve assembly runs roughly €55 to €140 depending on model, a brew-group motor €40 to €65 — but service labour typically exceeds the part, so get a quote before ordering anything. Out-of-warranty manufacturer service for a super-automatic typically lands between €230 and €460 including return shipping, and an independent espresso repairer is usually cheaper when it is one known part.

## Is the machine worth repairing?

The machines fitted with the ceramic valve are generally the ones worth keeping, and an Error 6 that clears after a descale costs you nothing. For Error 7 the arithmetic depends on the model: on a high-end Z or GIGA the repair usually makes sense, while on a ten-year-old entry-level E or ENA it is worth comparing the quote with a refurbished unit before committing.

Not every Jura code ends at a workbench. [Error 12](https://codefixcoffee.com/jura/automatic-machines/error-12/), the classic stone-in-the-grinder jam, is usually solved with a vacuum cleaner and a closer look at your beans. The full list, including the thermoblock and brew-group codes, is on the [Jura error-code index](https://codefixcoffee.com/jura/).
