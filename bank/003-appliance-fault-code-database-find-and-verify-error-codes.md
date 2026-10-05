---
title: How to find and verify an appliance fault code
description: How to track down any appliance error code: where manufacturers bury their lists, cross-checking forums against service docs, and the same-code traps.
---

The code on your display is only half the answer: it tells you the machine detected a fault, rarely which part to buy. A code is a symptom description written by the control board's programmer, and the board that detects a fault can also misreport it. Before ordering anything, you need the meaning for your exact brand, appliance type and model — from more than one source.

## Manufacturer lists exist — they are just buried or absent

The first surprise is how often there is no official list at all, or the list hides where owners never look.

- Some brands publish nothing. GE dishwashers show C-codes, H2O and 888, but GE hosts no official error-code page; the gap is filled by repair sites. A code like [888 on a GE dishwasher](https://codefixcoffee.com/ge/dishwasher/888/) is a control-board fault — you will not learn that from GE.
- Some brands split the information in two. De'Longhi machines mostly show words such as General Alarm, while newer models also log numeric codes like 1101 or 1512 that only technicians normally see; both layers are listed together on the [De'Longhi General Alarm and numeric codes page](https://codefixcoffee.com/delonghi/magnifica-dinamica/general-alarm-code-1101-1512/).
- Some brands publish only the friendly subset. Philips lists a small set of user-fixable codes for its espresso machines and routes everything else to support, even though the "service" codes have identifiable causes.
- Where a manual does have a table, it is usually at the back, in the troubleshooting chapter, one line per code, with no component names and no fix steps.

The information usually exists — you just have to look past the quick-start guide.

## How to verify a code like a technician

### Write down exactly what the display shows

Record the exact string, the appliance type, the full model number from the rating plate, and when the code appears. A single misread digit sends you to the wrong subsystem. "SE" on a Samsung range or wall oven is a stuck-key fault in the touchpad membrane — see [Samsung SE explained](https://codefixcoffee.com/samsung/range-wall-oven/se/) — and lookalike strings on other appliance types point elsewhere.

Note whether the code appears at startup or mid-cycle: startup faults are caught by the power-on self-test, mid-cycle faults usually involve whatever was active — pump, heater or valve. Also note what makes it go away; Samsung ovens, for example, keep the code on the display until the cause is fixed or power is cut at the breaker for three minutes, and the brand's full oven-code run is indexed on the [Samsung oven error codes](https://codefixcoffee.com/samsung-oven-error-codes/) page.

### Find the manufacturer's meaning first

Check the troubleshooting chapter, the brand's parts-and-service portal, and any service-bulletin PDFs for your model before touching forums. The official meaning is the baseline; everything else is commentary.

### Cross-check forums against service documentation

Forum threads are where you learn what actually breaks. A service table tells you a code means "brew-group fault"; a forum tells you that on your model it is usually a jammed coffee puck and fifteen minutes of cleaning. Treat threads as evidence, not truth:

- Give weight to posts that name your exact model and describe a fix that was still holding weeks later.
- Distrust any thread that recommends the same part for every code on every machine.
- When a forum claim and a service document disagree, the service document wins on meaning; the forum wins on likelihood.

## The trap: the same code, different meaning

This is where most self-diagnosis goes wrong, because error codes are not standardised — not across brands, and sometimes not even within one brand's product range.

- The same number can mean unrelated things. On a Jura, [Error 2](https://codefixcoffee.com/jura/automatic-machines/error-2/) is a coffee-thermoblock sensor fault — or just a machine too cold to heat. On a Philips or Saeco, Error 02 is an internal fault routed straight to service. Same number, same category, different subsystems and bills.
- Words can hide codes. A De'Longhi "General Alarm" has a numeric twin logged for technicians; fixing it well means knowing both layers.
- Category matters as much as brand. A code string on a range means something different on the same brand's dishwasher or washer. Filter by appliance type first, model second.

Sanity-check the meaning against the symptom: a heater code on a machine that still heats, or a drain code on one that drains, usually means you are reading the wrong entry — or the entry for the wrong model.

## A five-step verification checklist

1. Photograph the display and note the full model number from the rating plate.
2. Get the manufacturer's meaning from the manual or the service documentation.
3. Confirm with at least two forum threads that name your model and report a lasting fix.
4. Cross-check the meaning on an independent reference page — for example, [Philips Error 11 or 19](https://codefixcoffee.com/philips-saeco/espresso-machines/error-11-or-19/) should read the same wherever you find it; when two sources disagree, trust the one quoting service documentation.
5. Reset the machine once, then decide: if the code returns immediately, treat it as real and choose between a cheap part, a clean, or a technician.

## When to stop researching

Close the tabs once two independent sources agree on the meaning and the symptom matches. No further reading changes a code that returns right after a reset — from there the decision is practical: the price of the part against the age of the machine.
