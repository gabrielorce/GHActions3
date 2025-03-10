
def call(String version) {
    if (version.contains('-')) {
        echo "$version already contains a -, incrementing version"
        VERSION_SPLIT = version.split('-')
        int VERSION_INT = VERSION_SPLIT[1] as int
        VERSION_INT++;
        version = VERSION_SPLIT[0] + "-" + VERSION_INT
    } else {
        echo "$version is missing a -. adding -1 to the version"
        version = version + "-1"
    }
    return version
}


// Read command-line arguments and execute
def providedData = [filePath: args[0]]
def result = call(providedData)
println result  // This output will be captured by GitHub Actions
