# E-Ink-Info-Dashboard

### A low-power, always-visible display (weather, calendar, transit) that only updates when the content changes — the "small always-on service" idea, in physical form.

![Chain K](https://img.shields.io/badge/Chain%20K-64748B?style=for-the-badge) [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue?style=for-the-badge)](LICENSE-GPL) [![License: AGPL v3](https://img.shields.io/badge/License-AGPLv3-blue?style=for-the-badge)](LICENSE-AGPL)

[📖 Lesson Plan](docs/LESSON_PLAN.md)

<!-- SCREENSHOT PLACEHOLDER: docs/screenshots/overview.png -->

> ⬜ **Scaffold pending.** Directory created to portfolio standard; full content to be built. Part of **Chain K — Hardware & Systems Foundations**.

## Why This Was Built

E-ink is the opposite of every screen most projects reach for: it draws essentially no power once an
image is set, is readable in direct sunlight, and stays legible with the Pi powered off entirely. That
makes it the right display for something meant to just sit on a wall or desk and be glanced at — closer
to a picture frame than a monitor.

## Hardware Buying Guide (What to look for & red flags)

**Parts list:** an e-ink display HAT/module (common sizes: 2.13", 4.2", 7.5" — bigger means more content
per glance but slower full-refresh), a Raspberry Pi Zero 2 W (plenty for periodic redraws, and sips power),
a microSD card, and a simple stand or picture frame for mounting.

**What to look for:** check the panel's **full refresh time** (can be several seconds — normal for e-ink,
not a defect) and whether it supports **partial refresh** (updates just a region, much faster, useful for
a clock/time display within an otherwise static layout).

**Red flags:** "e-paper" listings with no controller chip specified and no driver library linked —
e-ink panels vary enough between controllers that a generic, undocumented one can mean days of driver
debugging for a beginner.

**Common failure points:** ghosting (faint remnants of the previous image) from skipping periodic full
refreshes in favor of partial-only updates, and treating it like a normal display that redraws
continuously — e-ink is designed to be written rarely, not polled.

## Wiring Diagram

A standard SPI HAT connection — power/ground plus six control lines (MOSI, SCLK, CS, DC, RST, BUSY). The
physical wiring is identical across all three panel-size tiers; only the panel itself and its refresh time
change:

![E-ink dashboard wiring diagram](docs/diagrams/wiring.svg)

## Parts & Pricing

Pulled from the chain-wide [Hardware Shopping List](../HARDWARE_SHOPPING_LIST.md#e-ink-info-dashboard) —
check there for current links; prices drift. **Budget/Mid/Luxury are the same tiers the shopping list calls
Budget/Mid/Premium.**

| Item | Budget | Mid | Luxury |
|---|---|---|---|
| Display | 2.13" Waveshare e-Paper HAT, ~$20 — clock/status only | [4.2" Waveshare e-Paper HAT, ~$35–40](https://www.waveshare.com/4.2inch-e-paper-module.htm) — good content/speed balance | [7.5" Waveshare e-Paper HAT, ~$55–65](https://www.amazon.com/waveshare-7-5inch-HAT-Raspberry-Consumption/dp/B075R4QY3L) — full weather + calendar + transit layout |
| Board | Pi Zero 2 W, ~$15 official / ~$28–35 retail | Same | Same — purpose-built for this, no reason to upgrade |
| Mounting | Any stand or picture frame you already have | A proper picture-frame mount | A custom-printed stand or frame via **3D-Printer-Build** |

Running total: **~$35–50 budget → ~$70–80 luxury**, almost entirely driven by panel size, not the board.

## Why This Matters (Industry Application)

Low-power, infrequently-updated displays are a real embedded-systems category (retail shelf tags, transit
signage, industrial status boards) — understanding *why* you'd choose e-ink over LCD is itself the useful
knowledge here.

## Topics Covered

| Area | What this project covers |
|------|--------------------------|
| E-ink displays | How they differ from LCD/OLED, and why |
| Partial vs. full refresh | Speed/ghosting tradeoffs |
| Low-power design | A Pi Zero running a service that mostly sleeps |
| Data sources | Pulling weather/calendar/transit data on a schedule |
| Layout | Designing for a screen that updates slowly |
| Always-on services | systemd timers instead of a busy-loop |

## How This Connects

Chain K (Hardware & Systems Foundations). A smaller, focused sibling to the "small always-on services"
part of **Raspberry-Pi-Tinkering**'s own scope.

---
Dual licensed — [GPL v3](LICENSE-GPL) and [AGPL v3](LICENSE-AGPL).
