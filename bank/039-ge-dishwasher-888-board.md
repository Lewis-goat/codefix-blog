---
title: GE dishwasher 888 and CFE: when it's the board
description: GE dishwasher showing 888 or CFE? What the display takeover means, how to check for water on the board, and what plug-in board replacement really involves.
---

Most GE dishwasher codes point at something wet: C1 is a drain timeout, C6 is water that never heated, H2O is no water at all. Then there are the two codes that point at something dry and electronic. [888](https://codefixcoffee.com/ge/dishwasher/888/) means the main control board failed its own self-check, and [CFE](https://codefixcoffee.com/ge/dishwasher/cfe/) means the door-mounted user interface and the main board have stopped talking to each other. Neither is a clogged filter in disguise. This post covers what the takeover on the display actually means, the water checks worth doing before you order a board, and the reality of swapping one.

## What the 888 display takeover means

On a segment display, 888 is what you see when every digit position is lit at once. It is not a fault number in the C-code sense — it is the board lighting everything because it has failed its own check and cannot run its normal program. Where [C1](https://codefixcoffee.com/ge/dishwasher/c1/) means "the pump ran two minutes and the tub stayed full", 888 means the computer that would have noticed that is itself the broken part.

The usual trigger is electrical, not mechanical: a voltage spike from a storm or a generator corrupts a memory register on the board, and from that point the self-check fails every time the machine starts. That is why the classic advice — cut power at the breaker for 60 seconds and restart — is worth one attempt and only one. A reset clears a glitch; it does not repair corrupted memory. If 888 comes back after a reset, the damage is done and the board needs replacing. Occasionally the cause is not a spike but a leak that has wet the board, which is where the checks below come in.

## CFE: the other board code

CFE is a communication fault: the user interface in the door and the main control board have lost their connection. The usual suspects are a loose or chafed harness where the wiring runs through the door hinge area, a connector that has got wet, or one of the two boards failing. The diagnostic order matters here, because the two boards cost different amounts: reset at the breaker first, then (with power off) inspect and reseat the harness at both ends, looking for chafing where the door flexes every cycle. Only if the harness is sound do you move to boards — and the user interface is usually the cheaper one to replace.

## The water-on-board checks

Before ordering any part, spend ten minutes ruling out the leak path, because a new board fitted into a wet machine dies too:

1. Pull the dishwasher out far enough to see underneath, and look for water or tide marks on the floor beneath it.
2. Remove the kick panel at the bottom front and inspect the base with a torch: water sitting in the base pan means a leak found the board's neighbourhood.
3. Check the obvious leak sources — suds from the wrong detergent, a damaged door gasket, a split hose, a weeping pump seal.
4. If anything is wet, dry it fully and fix the leak first, then reset and retest. A board that got splashed once and dried out sometimes recovers; a board sitting in standing water will not.

If everything is bone dry and 888 or CFE still returns after the 60-second breaker reset, order the board.

## The plug-in board replacement reality

Here is the good news that the words "control board" hide: on GE dishwashers the board is a plug-in module, not a soldered one. It lives behind the kick panel or inside the door depending on the model, and the replacement job is fundamentally:

1. Cut power at the breaker — not just the off switch — before removing any panel.
2. Open the kick panel or door front to expose the board.
3. Photograph the wiring connectors before touching anything.
4. Unplug each connector from the old board, mount the new one, and reconnect in the same positions.

No soldering, no rewiring — but the connectors are numerous and unlabeled, which is exactly why the photograph earns its keep. A main control board runs €90 to €200 and a user interface board €60 to €120, so the repair is a genuine judgment call: worth doing on a dishwasher under six or seven years old, and worth comparing against the price of a new machine on an older one. A technician's home visit adds €120 to €250 for diagnosis plus the part if you would rather not do it yourself.

## The short version

The [GE dishwasher index](https://codefixcoffee.com/ge/dishwasher/) covers every code, but the decision tree for the board codes is short. One breaker reset, ten minutes of leak checks, then either a harness reseat (CFE) or a board swap. What it never is: a filter problem, a detergent problem, or something another reset will fix on the third try.
