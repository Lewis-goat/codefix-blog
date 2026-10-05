---
title: Samsung oven not heating: E-08 and friends
description: Samsung oven not heating with E-08? The breaker reset first, then bake element, temperature sensor and relay checks — plus the door-lock variant.
---

An oven that runs but stays cold fails in a depressingly well-defined way: the board set a temperature, the cavity did not climb, and the machine logged why. On Samsung ranges and wall ovens, [E-08](https://codefixcoffee.com/samsung/range-wall-oven/e-08/) is the headline code for this — oven not heating, with the bake or broil element, the temperature sensor, or a relay on the board as the suspects. Around it sit a small family of related codes that narrow the fault further. This post walks them in the order worth checking, starting with the step people skip.

## First: the breaker reset

Before you conclude anything, cut power at the breaker for three minutes and restore it. This is not superstition — a range board that has got itself into a bad state can log a heating fault it would not otherwise have, and a clean power cycle clears it. If E-08 returns on the next bake attempt, the fault is real and you move on. The same three-minute reset opens the diagnostic path for nearly every code in the [Samsung oven code list](https://codefixcoffee.com/samsung-oven-error-codes/), so it is a habit worth forming.

## The bake element

The bake element is the workhorse at the bottom of the cavity, and it fails visibly. With the oven on, the element should glow evenly along its whole length. A visible break, blister or burnt spot on the element is a diagnosis you can make with your eyes: replace it. A bake element costs €30 to €60 and is one of the most worthwhile oven repairs there is. If it glows fine but the oven still will not hold temperature, the element is exonerated and the sensor is next — the full decision path is on the [E-08 diagnostic page](https://codefixcoffee.com/samsung/range-wall-oven/e-08/).

## The temperature sensor

The sensor probe reads the cavity temperature and reports back to the board as a resistance. At room temperature a healthy sensor reads about 1080 ohms — and that number is the whole test:

1. Cut power at the breaker.
2. Unscrew the sensor probe from the back wall of the cavity (two screws) and unplug it.
3. Meter it: around 1080 ohms at room temperature is healthy.
4. Reseat the plug if it reads fine; replace the sensor if it is far off.

Two related codes tell you which way the sensor failed without a meter. E-27 means the sensor reads open — resistance too high, over about 2950 ohms — which is a failed probe or a loose plug. E-28 means it reads shorted, under about 930 ohms, which is a shorted probe or a pinched harness behind the oven. Either way the sensor itself is €20 to €40 and screws in from inside the cavity.

## The relay on the board

If the element glows and the sensor meters correctly, what remains is the relay board: the board is not switching power to the element. A relay that never closes looks exactly like a dead element from inside the oven. This is the €100 to €200 outcome, and on an older range it is the point where comparing a repair quote against the machine's value becomes reasonable.

## The door-lock variant

One caveat before you buy parts: on some models, Samsung's own support pages list E-08 as a door-lock fault rather than a heating fault — the motorised lock used for self-clean rather than the bake circuit. Check your model's manual before ordering an element. The related code for lock trouble is E-0E (shown as E-0E or FL), which usually appears after a self-clean cycle when the lock switch sticks or the lock motor fails; the assembly is €40 to €90. Do not force the door in any of these cases — let the oven cool fully first, because it will not unlock hot.

## The code that means the opposite problem

While you are in this family of faults, know [E-0A](https://codefixcoffee.com/samsung/range-wall-oven/e-0a/): the oven overheating. It looks like a different complaint but shares two suspects with E-08 — a sensor reading wrongly (this time under-reading) or a relay stuck closed so the element will not switch off. Treat E-0A with more urgency than a no-heat fault: a stuck relay means the element stays on, so cut power at the breaker immediately and do not use the oven until it is fixed.

## What the repairs cost

Bake element €30 to €60, sensor €20 to €40, door lock assembly €40 to €90, relay board €100 to €200. Element and sensor are clear yes-votes at any reasonable machine age; the board is a judgment call. A technician's home visit runs €120 to €250 for diagnosis plus the part, which is fair money for confirming which of the three you actually need.
