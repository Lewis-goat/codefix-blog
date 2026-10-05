---
title: "Nespresso capsule problems: when the machine blames the pod"
description: "Nespresso machines often blame the pod when the capsule sensor, a dirty window or a stuck descale mode is the real fault. Decode the blinks and 1301."
---

Few coffee-machine faults are as quick to blame the user as a Nespresso Vertuo refusing a capsule. The pod goes in, the lever closes, and the machine acts as if nothing is there — or blinks at you and gives up. The Vertuo line (Next, Plus, Pop, Evoluo) speaks almost entirely in light patterns, which Nespresso documents on its assistance pages, while the numeric codes on connected models come from machine displays and owner reports rather than an official table. Both languages are covered across the [Nespresso section](https://codefixcoffee.com/nespresso/) of our site; this post is about the case where the machine points at the capsule and the capsule is innocent.

## How a Vertuo reads a capsule

Vertuo pods carry a barcode printed around the rim. The machine reads that code through a small window in the head, then pierces the foil and spins the capsule while pushing water through it. Two things have to go right:

- **The sensor must read the barcode.** Coffee splatter and dust on the capsule window are enough for a misread.
- **The pod must seat square** so the foil can be pierced cleanly and the capsule can spin without wobbling.

Fail either one and the machine reports a capsule problem without telling you which side failed — the source of almost all the confusion.

### Symptoms that point at the machine, not the pod

- The machine behaves as if no capsule is present although one is loaded and the head is closed.
- It refuses **every** pod — different sleeves, fresh stock, genuine capsules.
- Cleaning the capsule window and holder improves or clears the problem.
- On connected machines, a 1301-family code appears — the pod-sensor branch of that family, detailed on our [1301–1305 reference page](https://codefixcoffee.com/nespresso/vertuo-machines/1301-1305/).

If the fault follows the machine across every pod you own, stop buying new sleeves and start cleaning.

## When the pod really is the problem

Capsules do fail, and it is worth ruling them out cheaply before touching the machine:

- A dented or crushed rim — from shipping, storage or a drop — stops the pod seating square, so it pierces badly and dribbles instead of brewing.
- Torn or domed foil on old pods; capsules slowly absorb moisture and swell out of tolerance.
- A pod jammed in the holder from a previous cycle, blocking the next one from seating.

The test that settles it: try one fresh genuine capsule from the middle of a new sleeve; if it brews happily, the earlier pods were the issue. And never force the head closed over a capsule that is not sitting right.

## Blinking patterns that point at capsules

Vertuo machines have no dedicated "bad capsule" blink; the single button and light ring encode subsystems, not individual parts. The recurring patterns:

- **Sequential or alternating blinks right after power-on** mean heating mode. Wait fifteen to twenty-five seconds; this is not a fault.
- **Blinking orange in any pattern** is the descale family — needed, in progress or overdue. Orange that never ends usually means a descale was started and never finished.
- **Steady or repeating red** is a fault state, typically overheating or an internal error. Unplug for at least ten minutes, let the machine cool, and retry.

Count the colour, whether it is steady or blinking, and the blinks per group before touching anything — the [Vertuo blinking-lights decoder](https://codefixcoffee.com/nespresso/vertuo-machines/blinking-lights/) maps each pattern to its subsystem. And do the five-press factory reset last, not first: it wipes descale reminders and pairing without fixing anything mechanical.

## The 1301 overlap: the code that blames the pod

On connected Vertuo machines, the 1300-family codes are where capsule trouble and descale trouble meet. Owner reports consistently tie 1301 to two different states: a machine stuck in, or overdue for, descale mode, and the pod sensor not reading a capsule, with the neighbouring codes in the same family. So a code that looks like a pod complaint may actually be a descale complaint wearing the same number. The official sequence addresses both halves at once:

1. Factory reset: with the handle in the UNLOCKED position, press the button five times within three seconds; it blinks orange five times to confirm.
2. Run a complete descaling cycle with Nespresso descaler, uninterrupted — a cancelled descale is the classic way these machines get stuck in the mode.
3. Remove the capsule holder and wipe the capsule window and the machine head so the sensor can read the pod barcode.
4. Empty and refill the water tank, then retest with a fresh capsule.
5. If it persists after all three steps, contact Nespresso support rather than retrying — the company usually replaces faulty Vertuo machines under warranty rather than repairing them.

Two cautions: never descale with vinegar, as it damages the circuit and can void assistance, and budget-wise this sequence usually costs nothing beyond descaler at roughly €10 to €15.

## The contrast with a bean-to-cup machine

A Philips or Saeco that grinds its own beans blocks in its own way — ground coffee packing solid in the funnel behind [Error 01](https://codefixcoffee.com/philips-saeco/espresso-machines/error-01/) — while a pod machine's coffee-path faults nearly always reduce to the same three suspects: the barcode window, the pierce, or a descale that never finished. Clean the window, test one known-good pod, decode the light ring before acting, and the machine will usually stop blaming the pods.
