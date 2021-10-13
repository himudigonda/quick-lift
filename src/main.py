#!/usr/bin/env python
# -*- coding: utf-8 -*-
#! @author : @ruhend (Mudigonda Himansh)

from Lift import Lift


def clickAt():
    clickAtFloor = int(input(" > Enter your Location in the building : "))
    return clickAtFloor


def main():
    liftA = Lift("none", 0)
    liftB = Lift("none", 3)

    while True:
        liftRequestedAt = clickAt()
        deltaA = abs(liftA.location - liftRequestedAt)
        deltaB = abs(liftB.location - liftRequestedAt)
        if deltaA <= deltaB:
            print("LiftA is on its way...")
        else:
            print("LiftB is on its way...")


if __name__ == "__main__":
    main()
