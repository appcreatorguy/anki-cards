import os
import re
import sys

walk_dir = sys.argv[1]

print("walk_dir = " + walk_dir)

# If your current working directory may change during script execution, it's recommended to
# immediately convert program arguments to an absolute path. Then the variable root below will
# be an absolute path as well. Example:
# walk_dir = os.path.abspath(walk_dir)
print("walk_dir (absolute) = " + os.path.abspath(walk_dir))

for root, subdirs, files in os.walk(walk_dir):
    print("--\nroot = " + root)
    list_file_path = os.path.join(root, "my-directory-list.txt")

    for subdir in subdirs:
        print("\t- subdirectory " + subdir)

    for filename in files:
        file_path = os.path.join(root, filename)
        converted_file_path = os.path.join(root, (filename + "_converted.txt"))

        print("\t- file %s (full path: %s)" % (filename, file_path))
        print(
            "\t- converted file %s (full path: %s)"
            % ((filename + "_converted.txt"), converted_file_path)
        )

        with open(converted_file_path, "wt") as conv_file:
            with open(file_path, "rt") as f:
                content = f.readlines()
                f_content = f.read()
                new_f_content = []
                new_new_f_content = []
                print(f_content)
                for line in content:
                    if not line.startswith("#"):
                        new_f_content.append(line)
                i = 0
                for line in new_f_content:
                    if not i == 0:
                        new_new_f_content.append(line)
                    i += 1
                for i in range(0, len(new_new_f_content)):
                    line = new_new_f_content[i]
                    x = new_f_content[0][:1]
                    new_line = line.replace("x", ";")
                    new_line = new_line.replace("\n", "\n\n")
                    new_new_f_content[i] = new_line
                print(new_new_f_content)
            for line in new_new_f_content:
                conv_file.write(line)
