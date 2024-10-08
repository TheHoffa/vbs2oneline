import sys

def convert_to_oneliner(input_file, output_file):
    # Open the input file and read its contents
    with open(input_file, "rt") as file:
        # Read the content and perform replacements
        one_liner = (
            file.read()
            .replace("\r", "")
            .replace("\n", ":")
            .replace("\t", " ")
            .replace("& _ :", "& ")
            .replace("& _:", "& ")
        )

    # Write the result to the output file
    with open(output_file, "wt") as file:
        file.write(one_liner)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert_vbscript.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    convert_to_oneliner(input_file, output_file)
