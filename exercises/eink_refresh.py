"""
E-Ink Refresh -- fill in the four functions below.

A simplified but real model of the actual tradeoff the Refresh &
Ghosting Simulator tab demonstrates live: partial refresh nudges each
pixel only part of the way toward its target (real e-ink driver
behavior under a partial-update waveform), so repeated partial-only
refreshes leave a residual "ghost" that only a full refresh clears
exactly -- at a real time cost.

Run the tests as you go:  pytest exercises/test_eink_refresh.py -v
All four start failing. Implement one function, re-run, watch it turn
green, move to the next.
"""


def apply_partial_refresh(displayed, target, gain=0.65):
    """A partial refresh doesn't snap each pixel straight to its target
    -- it moves gain fraction of the way there, same as a real partial-
    update waveform doesn't fully migrate every ink particle. Repeating
    this against an unchanging target converges toward it over several
    refreshes, never landing on it in a single step.

    >>> apply_partial_refresh([0, 0, 1], [1, 1, 1], gain=0.65)
    [0.65, 0.65, 1.0]
    """
    # TODO: return [d + gain*(t - d) for d, t in zip(displayed, target)]
    raise NotImplementedError


def apply_full_refresh(target):
    """A full refresh clears the panel and redraws cleanly -- every
    pixel snaps exactly to its target, with zero residual. Slower in
    real hardware (several seconds of flashing), but exact.

    >>> apply_full_refresh([1, 0, 1])
    [1, 0, 1]
    """
    # TODO: return list(target) -- a full refresh reaches the target exactly
    raise NotImplementedError


def ghost_score(displayed, target):
    """A ghosting metric: the average absolute difference between what's
    actually displayed and what should be displayed, as a percentage.
    0 means no visible ghosting; higher means more residual "burn-in"
    from previous content still showing through.

    >>> ghost_score([0.35, 0.35, 1], [1, 1, 1])
    43.333333333333336
    """
    # TODO: return sum(abs(d - t) for d, t in zip(displayed, target)) / len(displayed) * 100
    raise NotImplementedError


def partial_refreshes_to_converge(initial_error, gain, threshold):
    """If a pixel's target stops changing, how many consecutive partial
    refreshes does it take before the ghost error drops below a given
    threshold? Each partial refresh multiplies the remaining error by
    (1 - gain) -- this is the real, checkable reason "just do a few
    more partial refreshes" eventually works, but a full refresh clears
    it in exactly one step instead.

    >>> partial_refreshes_to_converge(1.0, 0.65, 0.05)
    3
    """
    # TODO: starting from n=0 and err=initial_error, loop: while err > threshold,
    # multiply err by (1 - gain) and increment n. Return n.
    raise NotImplementedError
