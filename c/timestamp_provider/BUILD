load("@rules_cc//cc:defs.bzl", "cc_binary", "cc_library")
cc_binary(
    name = "timestamp_provider",
    srcs = ["main.c"],
    deps = [
        "//c/timestamp_provider/timestamp_provider_lib:timestamp_provider_lib",
    ],
)