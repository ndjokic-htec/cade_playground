load("@rules_python//python:defs.bzl", "py_binary", "py_test")

py_binary(
    name = "dummy_logger",
    srcs = ["dummy_logger.py"],
    main = "dummy_logger.py",
    deps = [
        "//python/random_print_library:random_print_library",
    ],
    visibility = ["//visibility:public"], 
)

py_test(
    name = "dummy_logger_test",
    srcs = ["dummy_logger_test.py"],
    deps = [
        ":dummy_logger",
    ],
)
