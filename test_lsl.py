from pylsl import resolve_streams

print("Searching for EEG streams...")

streams = resolve_streams(wait_time=5)

if not streams:
    print("No streams found. Check OpenBCI networking settings.")
else:
    for stream in streams:
        print("--------------------")
        print("Name:", stream.name())
        print("Type:", stream.type())
        print("Channels:", stream.channel_count())
        print("Sample Rate:", stream.nominal_srate())