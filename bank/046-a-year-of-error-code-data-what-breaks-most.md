---
title: What actually breaks: patterns across thousands of error codes
description: A year of error-code data: cold lockouts, brew-group cycles, valves, leaks and boards dominate — and why the cheapest-first diagnostic order wins.
---

We maintain error-code pages for espresso machines and, increasingly, for the rest of the kitchen — dishwashers, dryers, ovens. After a year of collecting and writing them up, the interesting result is not any single code. It is how few fault families the whole menagerie needs. Strip the brand names off and five patterns account for most of what we document: cold and sensor lockouts, brew-group cycles, valves, leaks and — rarest and most expensive — control boards. The same five appear in a Jura, a GE dishwasher and a Samsung oven wearing different code numbers.

## Family 1: cold machines and sensor lockouts

The most common single pattern is a machine refusing to heat because it believes it is too cold — or because its temperature sensor has gone open circuit and it cannot tell the difference. Jura's [Error 2](https://codefixcoffee.com/jura/automatic-machines/error-2/) is the flagship: the most common Jura code, with a benign cause (a machine below about 10 °C after winter transport, which clears by warming up) and a real one (a failed thermoblock sensor, a €20 to €40 part). Philips and Saeco's Error 11 and 19 carry the same protective intent under different numbers. The lesson the data teaches: a temperature code on a cold machine is a weather report, not a parts order. Warm it up and retry before you diagnose anything.

## Family 2: brew-group cycles that never finish

Second in volume, and the most fixable family. The brew group is a motorised mechanism that tamps, brews and ejects, and it lives in coffee oil. [Jura Error 8](https://codefixcoffee.com/jura/automatic-machines/error-8/) fires when the position encoder does not see the cycle complete — usually a sticky mechanism, usually fixed by the cleaning programme. De'Longhi's General Alarm resolves to the infuser nine times out of ten: rinse it, wipe the sensor window, [refit it correctly](https://codefixcoffee.com/delonghi/magnifica-dinamica/general-alarm-code-1101-1512/). Philips' [Error 20](https://codefixcoffee.com/philips-saeco/espresso-machines/error-20/) family clears on the reseat-and-rinse reset most of the time. The family fix is a cleaning tablet (€15 to €25 a box) and food-safe grease (€8 to €12) — call it €25 of consumables against an €80-plus assembly if you let the mechanism grind itself to death.

## Family 3: valves that stop switching

Valves route water, and scale stiffens everything that moves in water. Jura's Error 6 (the ceramic valve) lists a full descale as the first step because scale is the number-one cause; Error 7, its harsher sibling, is one of the few codes with no reliable owner-level fix. Miele's F77 is a valve-initialisation fault with an honest manual remedy: switch off, unplug, wait, retry — then service. And the pattern is not coffee-specific: a GE dishwasher throwing [C4](https://codefixcoffee.com/ge/dishwasher/c4/) is usually an inlet valve that will not close or a stuck float. Valve assemblies run €50 to €120; the seal kits inside them €10 to €20. The data-backed rule: before any valve is replaced, one full descale cycle is attempted. It costs almost nothing and it resolves a real share of them.

## Family 4: leaks found in the base

De'Longhi machines (leak alarm, logged as 3963) and GE dishwashers (E1) detect leaks the same way: a sensor in the base pan sees water. Detection is electronics; the cause is plumbing — a flattened O-ring, a split tube, a weeping heater fitting. O-ring kits cost €5 to €15, which gives this family the best parts-to-consequence ratio in the catalogue, because water in the base is what kills control boards. The stop rule writes itself: unplug, and do not run the machine again until it is dry and the wet path has been traced.

## Family 5: control boards — rare, expensive, last

Boards do fail — GE's 888, Samsung's cE-56 family — and when they do, the part is €90 to €250. But across our pages they are a minority, and codes that look like board faults often are not. The cautionary case is Samsung's [C-F2](https://codefixcoffee.com/samsung/range-wall-oven/c-f2/): it reads like a control-communication fault, and the usual finding is the cooling-fan circuit — a €40 to €90 fan and a connector. A board diagnosis should be arrived at by elimination, not by despair.

## The cheapest-first ladder

Put the families side by side and frequency and cost run in opposite directions: the codes that fire most often map to the cheapest fixes. So the diagnostic order follows:

1. **Free moves first.** Reset, warm a cold machine, reseat the brew group and trays, cycle power at the breaker. This alone clears a large share of everything.
2. **€10 consumables.** Descaler, cleaning tablets, grease. These attack families 2 and 3 directly.
3. **€20 to €50 parts.** Sensors, switches, O-rings, thermal fuses — most of the named parts in families 1, 3 and 4 live here.
4. **€60 to €150 assemblies.** Brew groups, valve assemblies, pumps — only once steps 1 to 3 have genuinely failed.
5. **Boards last.** €100 to €250, only after everything feeding the board has checked out.

Skipping rungs — the parts-cannon approach — inverts that relationship: you pay assembly prices for consumable problems. [Philips](https://www.philips.com) publishes only a handful of owner-fixable codes and routes the rest to service, and [Jura's own documentation](https://www.jura.com) names its heater-sensor errors among its most common repairs; both are consistent with the same ladder. Whatever the brand, search the exact code, fix what it names at the cheapest rung that can explain it, and only then spend real money.
