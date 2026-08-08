# Convert bytes into KB, MB, and GB.

def convert_bytes(byts):

    kb = byts / 1000
    mb = byts / 1000000
    gb = byts / 1000000000

    return (kb, mb, gb)

def main():

    byts = int(input("Enter the bytes : "))

    k_b, m_b, g_b = convert_bytes(byts)
    print(f"{byts} bytes means {k_b} KB , {m_b} MB & {g_b} GB")

if __name__ == "__main__":
    main()