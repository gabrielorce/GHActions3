import sys

def increment_version(version):
    """
    Increments the version if it contains a '-', otherwise appends '-1'.
    """
    if '-' in version:
        print(f"{version} already contains a '-', incrementing version")
        version_split = version.rsplit('-', 1)  # Split from the right to avoid breaking versions with multiple '-'
        try:
            version_int = int(version_split[1]) + 1
            version = f"{version_split[0]}-{version_int}"
        except ValueError:
            print("ERROR: The version suffix after '-' is not a number.")
            sys.exit(1)
    else:
        print(f"{version} is missing a '-', adding '-1' to the version")
        version = f"{version}-1"
    
    return version

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("ERROR: No version provided.")
        sys.exit(1)

    new_version = increment_version(sys.argv[1])
    print(new_version)  # Print the version so it can be captured in GitHub Actions
