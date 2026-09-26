# 📖 Lesson Plan — E-Ink-Info-Dashboard

> **Chain K — Hardware & Systems Foundations** | A low-power, always-visible display (weather,
> calendar, transit) that only updates when the content changes — the "small always-on service" idea,
> in physical form.

## What This Project Is

Build a display that behaves nothing like a monitor: it draws essentially no power once an image is
set, stays legible with the Pi powered off, and is designed to be written to rarely, not redrawn in a
loop. Get the actual e-ink behavior right first — partial vs full refresh, the ghosting tradeoff — then
wrap it in a real low-power service (a systemd timer, not a busy-loop) that pulls weather/calendar/
transit data on a schedule and redraws deliberately.

## Learning Objectives

By the end I can:

1. Explain how e-ink actually works (bistable, electrophoretic) and why that's fundamentally different
   from an LCD/OLED that needs continuous power to hold an image.
2. Use partial refresh for fast, frequent updates and full refresh to clear the ghosting it leaves
   behind, and explain the actual tradeoff between them.
3. Design a low-power, scheduled service with a systemd timer instead of a busy-loop or naive cron job.
4. Design a layout that deliberately separates rarely-changing content from frequently-changing content,
   matched to which refresh mode each region actually uses.

## Software You Will Use

- The panel manufacturer's driver library (e.g. Waveshare's Python library for its e-Paper HATs).
- Python for pulling data (weather/calendar/transit APIs) and rendering the layout as an image.
- systemd (timers + services) for scheduling redraws — not cron, and never a busy-loop.

## Build Order

1. Set up the display and driver library; render a simple full-refresh test image to confirm the whole
   signal chain works before building any real layout.
   🔗 [E Ink Corporation — Electrophoretic Technology](https://www.eink.com/technology.html)
2. Implement partial refresh for a frequently-changing region (e.g. a clock); watch ghosting accumulate
   over several partial-only updates, then trigger a periodic full refresh and confirm it clears cleanly.
   🔗 [Ben Krasnow — Fast partial refresh on a 4.2" e-paper display](https://benkrasnow.blogspot.com/2017/10/fast-partial-refresh-on-42-e-paper.html)
3. Write a systemd timer (not a busy-loop or plain cron job) that wakes periodically, pulls
   weather/calendar/transit data, and triggers a redraw.
   🎥 [Introduction to systemd timers](https://www.youtube.com/watch?v=DixhIrgMy3M) (tutoriaLinux)
4. Design the actual layout: separate content that rarely changes (weather, calendar) from content
   that changes often (a clock), matched deliberately to full-refresh vs partial-refresh regions.
   🔗 [Build Your Own Ultra-Low-Power E-Ink Dashboard](https://hackaday.io/project/204840-build-your-own-ultra-low-power-e-ink-dashboard) (Hackaday.io)

## Common Mistakes to Avoid

- Ghosting (faint remnants of the previous image) from skipping periodic full refreshes in favor of
  partial-only updates.
- Treating it like a normal display that redraws continuously — e-ink is designed to be written
  rarely, not polled.
- Buying a generic "e-paper" listing with no controller chip specified and no driver library linked —
  e-ink panels vary enough between controllers that a generic, undocumented one can mean days of driver
  debugging.
- Using a busy-loop or an overly-frequent cron job to poll data sources, wasting API calls and power
  for a display that only genuinely needs to change a handful of times a day.
- Redrawing the entire panel with a full refresh for every small change, needlessly paying the
  multi-second full-refresh cost instead of designing a dedicated partial-refresh region.

## Check Your Understanding

The quiz covers why e-ink holds an image with zero power (bistability), the partial-vs-full refresh
tradeoff and the ghosting math behind it, why a systemd timer beats a busy-loop or naive cron job here,
and deliberate layout-region design.

## Why This Matters (Industry Application)

Low-power, infrequently-updated displays are a real embedded-systems category (retail shelf tags,
transit signage, industrial status boards) — understanding *why* you'd choose e-ink over LCD, and how
to design a service around "wakes rarely, does very little, sleeps again," is itself the useful
knowledge here, well beyond this one display.

## Reflection Questions

- What's a piece of "always-on" information in your own life that would genuinely benefit from a
  glanceable, rarely-updating display instead of a phone screen you have to unlock?
- Why does treating this project's redraw logic as "a service that mostly sleeps" matter more here than
  on almost any other Chain K project?
