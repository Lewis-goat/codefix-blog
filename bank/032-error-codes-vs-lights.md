---
title: Error codes vs blinking lights: two languages for the same fault
description: Jura numbers, De'Longhi words, Nespresso Vertuo blinking lights — how the same fault gets three languages, and how to read each one.
---

Underneath the branding, coffee machines fail in familiar ways: a heater or its sensor, a blocked brew group, air in the water circuit, a descale long overdue. What differs is how the machine tells you. Some print a number on a display, some show plain words, and some — with no display at all — blink a light at you. Which language you get depends on the hardware the manufacturer fitted and on who the message is meant for: you, or the technician. Reading the right language fluently is half of the diagnosis.

## Three dialects, one vocabulary

- **Numbers.** Jura uses one numbered set across the E, ENA, S, J, Z and GIGA ranges; Philips and Saeco use Error 01 to 22 on LatteGo, Xelsis and Incanto machines; other appliances do the same with GE's C-codes and Samsung's E-codes.
- **Words.** De'Longhi shows messages on most machines — General Alarm, Insert Infuser Assembly, Water Circuit Empty — written for the owner to act on.
- **Lights.** Nespresso's Vertuo line (Next, Plus, Pop, Evoluo) has no display. Light patterns carry everything: heating, descaling, faults.

## Jura: one number set, every machine

Jura is the purest example of the numeric school. The same numbers mean the same things across the whole range, so [Jura Error 2](https://codefixcoffee.com/jura/automatic-machines/error-2/) is one page for every model: the most common code, covering both a machine too cold to heat and a failed thermoblock sensor. Words do exist on a Jura — "Fill water tank", "Empty drip tray" — but they are consumable messages, not errors, and they are documented separately from the numbered codes. Start from the [Jura overview](https://codefixcoffee.com/jura/) for the full set: the thermoblock errors 1 to 5, the valve codes, the brew-group code.

## De'Longhi: words for you, numbers for the technician

De'Longhi runs the opposite philosophy: words on top, numbers underneath. Most Magnifica, Dinamica and PrimaDonna machines show plain-language alarms, while newer models also log a numeric code — 1101, 1454, 2257 and their neighbours — that service uses. The two layers describe the same fault.

General Alarm is the demonstration case. On the display it is a catch-all, and nine times out of ten the fault is the infuser — stuck, dirty, out of position, or coffee dust on its position sensor. The owner fix is rinsing the infuser and wiping the sensor window, as on the [General Alarm page](https://codefixcoffee.com/delonghi/magnifica-dinamica/general-alarm-code-1101-1512/); the logged number (1101 or 1512 in this family) is what the technician reads so they do not re-diagnose from scratch. "Grinder stuck" logs as 1454, a leak alarm as 3963. When you book a repair, quote the words on the display and ask what number the machine logged — the answer speeds everything up.

## Nespresso Vertuo: decoder thinking

A Vertuo has no display and essentially one button, so the light is the only channel — and Nespresso documents the patterns on its assistance pages. Diagnosis here is decoding, not lookup. Before touching anything, note three things:

- the colour of the light
- whether it is steady, blinking, or alternating in a sequence
- how many blinks per group, and whether the pattern repeats

Then translate. Sequential or alternating blinks right after power-on are heating mode — wait 15 to 25 seconds, not a fault. Orange in any pattern belongs to the descale family, and orange that never ends usually means a descale was started and never finished; the fix is finishing the cycle with proper descaler (about €10 to €15), not another reset. A steady or repeating red is a fault state, typically overheating or an internal error: unplug for at least ten minutes, let the machine cool, retry. Connected models can also show the numeric 1300-family codes, which are strong community signals rather than an official list — the fix sequences are the same either way. The full pattern map is the [Vertuo blinking-lights decoder](https://codefixcoffee.com/nespresso/vertuo-machines/blinking-lights/), and what support and warranty exchanges look like is covered under [Nespresso](https://codefixcoffee.com/nespresso/).

## The same fault, two languages

The clearest proof that these are dialects rather than different faults is the cold machine. A Jura that is too cold to heat prints Error 2; a Philips or Saeco in the same situation prints Error 11 or 19, documented as the machine needing to adjust to room temperature after cold transport — see [Philips Error 11 or 19](https://codefixcoffee.com/philips-saeco/espresso-machines/error-11-or-19/). Identical situation, identical protective intent, different number. That is why you search the exact code string for your brand; searching the concept finds the other brand's answer.

## Reporting a fault in either language

1. Numbers: copy them exactly, including the prefix — "Error 2", "ER02" and "E2" are different dialects on different machines.
2. Words: quote them verbatim; "Insert Infuser Assembly" and "infuser problem" are not the same search.
3. Lights: record colour, rhythm and count before pressing anything, and keep the factory reset as the last resort — on a Vertuo it wipes descale reminders and pairing without fixing anything mechanical.
4. Search that exact token, then apply the fix it points to.

The languages are smaller than they look: a handful of numbers on a Jura, a word list on a De'Longhi, a light map on a Vertuo. Decoding costs nothing, and it is the difference between a ten-minute fix and a needless service call.
