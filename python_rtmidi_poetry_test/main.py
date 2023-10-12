
import sys
import rtmidi

def main():
    print("Detected outputs:")

    midi_out = rtmidi.MidiOut()
    print(midi_out.get_ports())

    sys.exit(0)


if __name__ == "__main__":
    main()


