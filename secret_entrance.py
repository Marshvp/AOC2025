import sys

def secret_entrance(sequence):
    dial = 50
    password = 0
    with open(sequence) as seq:
        for line in seq:
            print(line.split())
            line.strip()
            direction = line[0]
            amount = int(line[1:])
            print(f"direction {direction}")
            print(f"amount {amount}")
            
            if direction.lower() == "l":
                dial = (dial - amount) % 100
            elif direction.lower() == "r":
                dial = (dial + amount) % 100

            if dial == 0:
                password += 1

            print(dial)
            print(f"Password: {password}")
            

    return password
if __name__ == "__main__":
    sequence = sys.argv[1]
    secret_entrance(sequence)
    pass
# Return The number of 0 in the sequence.

# Have an array of 1-99 when hitting an end loop the the other side.
# Testing Params
# L68
# L30
# R48
# L5
# R60
# L55
# L1
# L99
# R14
# L82
