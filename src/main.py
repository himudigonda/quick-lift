#!/usr/bin/env python
# -*- coding: utf-8 -*-
#! @author : @ruhend (Mudigonda Himansh)

from Lift import Lift
import time


def clickAt():
    clickAtFloor = input(" > Enter your Location in the building : ")
    if clickAtFloor:
        return clickAtFloor
    exit


def liftMovementCounter(_present_location, _to_location):
    if _present_location > int(_to_location):
        for _ in range(int(_present_location), int(_to_location), -1):
            print(" >>>", _)
            time.sleep(0.1)
    else:
        for _ in range(int(_present_location), int(_to_location)):
            print(" >>>", _)
            time.sleep(0.1)
    return 0


def main():

    LiftA = Lift("none", 0)
    LiftB = Lift("none", 9)

    while True:
        LiftRequestedAt = clickAt()
        if LiftRequestedAt is not None:
            LiftALocation = int(LiftA.getLiftLOC())
            LiftBLocation = int(LiftB.getLiftLOC())
            DeltaA = abs(int(LiftALocation) - int(LiftRequestedAt))
            DeltaB = abs(int(LiftBLocation) - int(LiftRequestedAt))
            if LiftALocation == int(LiftRequestedAt):
                print("LiftB is already at your service...")
                continue
            elif LiftBLocation == int(LiftRequestedAt):
                print("LiftA is already at your service...")
                continue
            if DeltaA <= DeltaB:
                print("LiftA is on its way...")
                liftMovementCounter(LiftALocation, LiftRequestedAt)
                print("LiftA is here!")
                LiftA.setLiftLocation(LiftRequestedAt)
            else:
                print("LiftB is on its way...")
                liftMovementCounter(LiftBLocation, LiftRequestedAt)
                print("LiftB is here!")
                LiftB.setLiftLocation(LiftRequestedAt)
        else:
            print(" > Closing Lift Service Now...")
            break


if __name__ == "__main__":
    main()
