# GITHUB ACTIONS
Istraziti koncept Github Action-a. Napraviti Github action koji se pokrece za svaki pull request. 
Za ovo je potrebno kreirati docker image i pushati ga na Github registry da bi se mogao koristiti u test koraku.
Testovi se mogu pokrenuti sa `bazel test //test:test_dummy_logger`

```
on:
    pull_request:
        branches: ["main"]
jobs:
    build_container:
        runs-on: self-hosted
            ...
            run: |
                docker build ...
                docker push ... ghcr.io/...
    run_tests:
        runs-on: self-hosted
            ...
            run: |
                bazel test //test:test_dummy_logger