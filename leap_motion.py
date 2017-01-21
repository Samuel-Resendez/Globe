#Author: Samuel Resendez


import Leap
import sys
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture


class listener(Leap.Listener):


    def on_frame(self, controller):
        frame = controller.frame()
        print(frame.hands[0].palm_normal)

def main():
    control = Leap.Controller()

    listen =  listener()

    control.add_listener(listen)

    print("Press Enter to quit...")
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        control.remove_listener(listener)




if __name__ == "__main__":
    main()